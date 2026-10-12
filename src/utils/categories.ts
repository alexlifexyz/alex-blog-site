export interface CategoryMeta {
  slug: string;
  name: string;
  description: string;
}

export const CATEGORIES: Record<string, CategoryMeta> = {
  "ai-engineering": {
    slug: "ai-engineering",
    name: "AI 工程",
    description: "RAG、Agent 与工具调用的落地实践",
  },
  architecture: {
    slug: "architecture",
    name: "Java 架构",
    description: "高并发、微服务与生产可用性",
  },
  insights: {
    slug: "insights",
    name: "行业观察",
    description: "AI 行业动态与商业化",
  },
  essays: {
    slug: "essays",
    name: "随笔",
    description: "职业转型、学习方法与生活",
  },
};

/** Normalise legacy category names used in older front matter. */
export function normalizeCategory(raw?: string): string {
  if (!raw) return "essays";
  const lower = raw.toLowerCase().trim();
  if (["ai", "rag", "ai-engineering"].includes(lower)) return "ai-engineering";
  if (["architecture", "java", "backend"].includes(lower)) return "architecture";
  if (["insights", "industry", "tech"].includes(lower)) return "insights";
  if (["survival", "career", "writing", "essays"].includes(lower)) return "essays";
  return CATEGORIES[lower] ? lower : "essays";
}

export function getCategoryMeta(raw?: string): CategoryMeta {
  return CATEGORIES[normalizeCategory(raw)] || CATEGORIES.essays;
}
