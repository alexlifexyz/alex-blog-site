import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const posts = (await getCollection("posts", ({ data }) => !data.draft))
    .sort((a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime());

  return rss({
    title: "何占伟 / Alex · 技术专栏 & 数字花园",
    description: "11 年 Java 后端架构，专注企业级 RAG 与大模型应用工程化落地、全栈架构与长期主义技术思考。",
    site: context.site || "https://blog.alexai.top",
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      link: `/posts/${post.slug}/`,
      categories: [post.data.category, ...(post.data.tags || [])],
    })),
    customData: `<language>zh-CN</language>`,
  });
}
