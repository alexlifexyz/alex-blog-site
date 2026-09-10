#!/usr/bin/env python3
"""
WeChat Content Workspace -> Astro Blog Sync Script (Production Grade)
Extracts high-quality canonical articles from wechat-content-workspace,
deduplicates drafts vs published versions, cleans editorial scratchpads,
assigns 4 core categories and tags, and syncs into src/content/posts/.
"""

import os
import re
from pathlib import Path

SOURCE_DIR = Path("/Users/mac/studio/20-content/wechat-content-workspace")
TARGET_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "posts"

EMOJI_PATTERN = re.compile(
    r"[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf\u2300-\u23ff\u2b50\ufe0f\u200d]",
    flags=re.UNICODE
)

def strip_emojis(text: str) -> str:
    if not text:
        return ""
    cleaned = EMOJI_PATTERN.sub("", text)
    return re.sub(r"[ \t]+", " ", cleaned).strip()

ORIGINALS = {
    "2026-03-23-old-java-keeps-reading-stacktraces.md",
    "2026-03-24-thinking-programmer-will-be-out-first.md",
    "2026-03-25-layoff-to-outsourcing-and-more-anxious.md",
    "2026-03-26-demo-anxiety-after-three-days.md",
    "2026-03-27-why-a-35-year-old-java-engineer-is-thinking-about-ai-apps.md",
    "2026-09-08-java21-enterprise-hybrid-rag-in-practice.md"
}

def determine_category(title, body):
    text = (title + " " + body[:400]).lower()
    if any(w in text for w in ["rag", "deepseek", "agent", "prompt", "claude code", "cursor", "mcp", "工具包", "向量", "代码", "llm", "接口适配", "模型接口"]):
        return "ai-engineering"
    if any(w in text for w in ["java", "微服务", "高并发", "架构", "性能", "堆栈", "分布式", "系统设计", "中间件"]):
        return "architecture"
    if any(w in text for w in ["openai", "anthropic", "sora", "黄仁勋", "马斯克", "a16z", "copilot", "token", "算力", "商业", "实施", "315", "投毒", "行业", "榜单", "agi"]):
        return "insights"
    return "essays"

def extract_tags(title, body, category):
    tags = []
    text = title + " " + body[:500]
    
    tag_rules = [
        ("DeepSeek", ["DeepSeek", "deepseek"]),
        ("RAG", ["RAG", "rag", "检索增强"]),
        ("Agent", ["Agent", "智能体", "agent", "OpenClaw"]),
        ("Claude", ["Claude", "claude"]),
        ("Cursor", ["Cursor", "cursor"]),
        ("MCP", ["MCP", "mcp"]),
        ("Java", ["Java", "java", "Spring"]),
        ("微服务", ["微服务", "分布式"]),
        ("高并发", ["高并发", "QPS", "性能"]),
        ("OpenAI", ["OpenAI", "openai", "Sora"]),
        ("Anthropic", ["Anthropic", "anthropic"]),
        ("行业观察", ["行业", "商业", "趋势", "落地", "实施", "Token"]),
        ("工程思考", ["思考", "判断", "经验", "决策", "代码"]),
        ("35岁", ["35岁", "35+", "中年", "养家"]),
        ("职场人生", ["职场", "程序员", "裁员", "外包", "失业", "焦虑"]),
    ]
    
    for tag_name, keywords in tag_rules:
        if any(k in text for k in keywords):
            tags.append(tag_name)
            
    if not tags:
        tags = ["随笔思考"]
    return tags[:4]

def score_file(p):
    name = p.name.lower()
    score = 0
    if "published" in str(p): score += 100
    if "已发布" in name: score += 50
    if "发布版" in name: score += 40
    if "终稿" in name: score += 30
    if "正文" in name: score += 20
    if "初稿" in name: score -= 20
    return score

def extract_article(p):
    try:
        content = p.read_text(encoding="utf-8", errors="ignore").strip()
    except Exception:
        return None
        
    if len(content) < 150:
        return None
        
    lines = content.splitlines()
    
    # Extract date
    m_date = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
    if not m_date:
        m_folder = re.search(r"(\d{4})[/-](\d{2})[/-]?(\d{2})?", str(p))
        if m_folder:
            d = m_folder.group(3) or "15"
            date_str = f"{m_folder.group(1)}-{m_folder.group(2)}-{d}"
        else:
            date_str = "2026-03-20"
    else:
        date_str = m_date.group(1)
        
    # Extract Title
    title = ""
    for l in lines[:10]:
        s = l.strip()
        if s.startswith("# "):
            title = s.lstrip("# ").strip()
            break
            
    if not title:
        stem = p.stem
        stem = re.sub(r"^\d{4}-\d{2}-\d{2}-?", "", stem)
        stem = re.sub(r"^\d{2}-", "", stem)
        title = stem.split("-")[-1]
        
    title = re.sub(r"[\"']", "", title)
    title = re.sub(r"-(发布包|已发布|终稿.*|正文|发布版|初稿|增长版.*)$", "", title)
    title = re.sub(r"(发布包|已发布|终稿.*|正文|发布版|初稿|增长版.*)$", "", title).strip()
    title = strip_emojis(title)
    
    if not title or title.lower() in ["readme", "index", "drafts", "published"]:
        # Try finding in parent directory name e.g. 16-程序员自杀式职业
        parent_name = p.parent.name
        if parent_name and not parent_name.isdigit():
            clean_parent = re.sub(r"^\d{2}-", "", parent_name)
            clean_parent = strip_emojis(clean_parent)
            if len(clean_parent) > 2:
                title = clean_parent
        else:
            return None

    # Clean body
    cleaned_lines = []
    skip_mode = False
    in_real_content = False
    
    for l in lines:
        s = l.strip()
        if any(s.startswith(h) for h in ["## 类型判断", "## 备选标题", "## 建议发布时间", "## 封面文案", "## 朋友圈转发文案", "## 切口", "对应草稿："]):
            skip_mode = True
            continue
        if skip_mode and s.startswith("## 正文"):
            skip_mode = False
            in_real_content = True
            continue
        if skip_mode and s.startswith("#") and not any(s.startswith(h) for h in ["## 类型", "## 备选", "## 建议", "## 封面", "## 朋友圈"]):
            skip_mode = False
            
        if not skip_mode:
            if s.startswith("# ") and not in_real_content:
                in_real_content = True
                continue
            cleaned_lines.append(l)

    body = "\n".join(cleaned_lines).strip()
    body = strip_emojis(body)
    if len(body) < 180:
        return None
        
    # Extract Description
    desc_lines = [l.strip() for l in body.splitlines() if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("-") and not l.strip().startswith("`") and not l.strip().startswith("|")]
    description = ""
    for dl in desc_lines:
        if len(dl) >= 15:
            description = dl[:120].strip()
            break
    if not description:
        description = title
    description = strip_emojis(description)
    description = description.replace('"', '\\"')

    category = determine_category(title, body)
    tags = extract_tags(title, body, category)
    
    # Clean Slug
    slug_name = re.sub(r"[^\w\u4e00-\u9fa5\-]", "", title[:25]).strip("-")
    slug = f"{date_str}-{slug_name}"

    return {
        "slug": slug,
        "title": title,
        "description": description,
        "date": date_str,
        "category": category,
        "tags": tags,
        "body": body,
        "path": p,
        "score": score_file(p),
        "length": len(body)
    }

def main():
    print("Starting WeChat articles synchronization...")
    valid_folders = [
        SOURCE_DIR / "published",
        SOURCE_DIR / "drafts" / "2026",
        SOURCE_DIR / "drafts"
    ]
    
    candidates = []
    for vf in valid_folders:
        if not vf.exists(): continue
        for p in vf.glob("**/*.md"):
            if not p.is_file(): continue
            rel = str(p.relative_to(SOURCE_DIR))
            if any(x in rel.split("/") for x in ["README", "docs", "code", "context", "research", "analytics", "archive", "misc"]):
                continue
            candidates.append(p)

    articles = []
    for p in candidates:
        name = p.name.lower()
        if any(x in name for x in ["checklist", "prompt", "roadmap", "playbook", "plan-", "plan.", "brief", "log", "handoff", "template", "rule", "scorecard", "发布包", "选题卡", "预热包"]):
            continue
        art = extract_article(p)
        if art:
            articles.append(art)
            
    # Deduplicate by core title
    grouped = {}
    for a in articles:
        norm_key = re.sub(r"[^\w\u4e00-\u9fa5]", "", a["title"])[:10].lower()
        if not norm_key: continue
        if norm_key not in grouped:
            grouped[norm_key] = []
        grouped[norm_key].append(a)
        
    canonical = []
    for k, flist in grouped.items():
        flist.sort(key=lambda x: (x["score"], x["length"]), reverse=True)
        canonical.append(flist[0])
        
    print(f"Extracted {len(canonical)} unique canonical articles.")
    
    synced = 0
    for post in canonical:
        target_file = TARGET_DIR / f"{post['slug']}.md"
        if target_file.name in ORIGINALS:
            continue
            
        tags_str = "[" + ", ".join(f'"{t}"' for t in post['tags']) + "]"
        frontmatter = f"""---
title: "{post['title']}"
description: "{post['description']}"
pubDate: {post['date']}
category: "{post['category']}"
tags: {tags_str}
draft: false
---

"""
        full_content = frontmatter + post["body"] + "\n"
        target_file.write_text(full_content, encoding="utf-8")
        synced += 1
        
    print(f"Successfully synced {synced} new articles into {TARGET_DIR}.")

if __name__ == "__main__":
    main()
