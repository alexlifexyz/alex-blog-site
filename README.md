# alex-blog-site

何占伟的博客。Astro 静态站，Pagefind 全文搜索。

## 写文章

文章放在 `src/content/posts/`，文件名即链接（小写）。Front matter：

```yaml
title: "标题"
description: "一两句摘要，显示在列表和分享卡片上"
pubDate: 2026-10-12
category: ai-engineering   # ai-engineering / architecture / insights / essays
tags: ["RAG", "Java"]
featured: false            # true 会进入首页「精选」（最多 3 篇）
draft: false               # true 不发布
```

## 本地运行

```bash
npm install
npm run dev        # 开发预览（搜索在构建后才可用）
npm run build      # 构建 + 生成搜索索引
```

## 字体

标题用 Noto Serif SC。`public/fonts/noto-serif-sc-subset.woff2` 是按全站标题用字裁出的子集，新文章里没覆盖到的字会回退到按 unicode-range 切片的完整字体，显示不受影响。标题用字变化较多时重新生成：

```bash
npm run build
python3 scripts/subset-serif-font.py /path/to/NotoSerifSC-SemiBold.otf
```

## 主题

浅色 / 深色的选择写在 `.alexai.top` 域的 `alexai-theme` cookie 里，与主站和其他子站共用。
