export interface CategoryMeta {
  slug: string;
  name: string;
  description: string;
  icon: string;
  color: string;
}

export const CATEGORIES: Record<string, CategoryMeta> = {
  "ai-engineering": {
    slug: "ai-engineering",
    name: "AI 工业落地",
    description: "企业级 RAG、DeepSeek 实战、Agent 工具调用与落地工程实践",
    icon: "",
    color: "#0f766e",
  },
  "architecture": {
    slug: "architecture",
    name: "Java 架构底座",
    description: "20万 QPS 统一认证、微服务脚手架、高并发与生产可用性实录",
    icon: "",
    color: "#2563eb",
  },
  "insights": {
    slug: "insights",
    name: "行业观察与思考",
    description: "AI 商业化落地、Token 经济、大模型时代技术演进与行业观察",
    icon: "",
    color: "#d97706",
  },
  "essays": {
    slug: "essays",
    name: "工程随笔与生活",
    description: "35 岁老 Java 的转型思考、职场见闻、慢学沉淀与生活琐记",
    icon: "",
    color: "#7c3aed",
  },
};

/**
 * 规范化分类标识（兼容历史命名）
 */
export function normalizeCategory(raw?: string): string {
  if (!raw) return "essays";
  const lower = raw.toLowerCase().trim();
  if (lower === "ai" || lower === "rag" || lower === "ai-engineering") {
    return "ai-engineering";
  }
  if (lower === "architecture" || lower === "java" || lower === "backend") {
    return "architecture";
  }
  if (lower === "insights" || lower === "industry" || lower === "tech") {
    return "insights";
  }
  if (lower === "survival" || lower === "career" || lower === "writing" || lower === "essays") {
    return "essays";
  }
  return CATEGORIES[lower] ? lower : "essays";
}

export function getCategoryMeta(raw?: string): CategoryMeta {
  const key = normalizeCategory(raw);
  return CATEGORIES[key] || CATEGORIES["essays"];
}
