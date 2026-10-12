import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const posts = (await getCollection("posts", ({ data }) => !data.draft))
    .sort((a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime());

  return rss({
    title: "何占伟的博客",
    description: "Java 后端、Agent 与 RAG 落地，以及一个老程序员对这一轮 AI 的观察。",
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
