import { getCollection, type CollectionEntry } from "astro:content";

export type Post = CollectionEntry<"posts">;

export async function getPublishedPosts(): Promise<Post[]> {
  const posts = await getCollection("posts", ({ data }) => !data.draft);
  return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

const pad = (n: number) => String(n).padStart(2, "0");

/** Dates in front matter are calendar dates; read them in UTC so the build machine's zone never shifts the day. */
export function ymd(date: Date): string {
  return `${date.getUTCFullYear()}-${pad(date.getUTCMonth() + 1)}-${pad(date.getUTCDate())}`;
}

export function md(date: Date): string {
  return `${pad(date.getUTCMonth() + 1)}-${pad(date.getUTCDate())}`;
}

export function year(date: Date): number {
  return date.getUTCFullYear();
}

export function readingStats(body = "") {
  const text = body.replace(/```[\s\S]*?```/g, " ").replace(/<[^>]+>/g, " ");
  const cjk = (text.match(/[㐀-鿿]/g) || []).length;
  const words = (text.match(/[A-Za-z0-9_]+/g) || []).length;
  const total = cjk + words;
  return { words: total, minutes: Math.max(1, Math.round(total / 400)) };
}

export function groupByYear(posts: Post[]) {
  const groups = new Map<number, Post[]>();
  for (const p of posts) {
    const y = year(p.data.pubDate);
    if (!groups.has(y)) groups.set(y, []);
    groups.get(y)!.push(p);
  }
  return [...groups.entries()].sort((a, b) => b[0] - a[0]);
}

export function tagCounts(posts: Post[]) {
  const counts = new Map<string, number>();
  for (const p of posts) for (const t of p.data.tags) counts.set(t, (counts.get(t) || 0) + 1);
  return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], "zh-CN"));
}

/** Posts sharing the most tags with `post`, newest first on ties. */
export function relatedPosts(post: Post, all: Post[], limit = 3): Post[] {
  const tags = new Set(post.data.tags);
  return all
    .filter((p) => p.id !== post.id)
    .map((p) => ({ p, score: p.data.tags.filter((t) => tags.has(t)).length }))
    .filter((x) => x.score > 0)
    .sort((a, b) => b.score - a.score || b.p.data.pubDate.valueOf() - a.p.data.pubDate.valueOf())
    .slice(0, limit)
    .map((x) => x.p);
}

export const postUrl = (p: Post) => `/posts/${p.slug}/`;

/** Front-matter descriptions sometimes carry inline markdown; show them as plain text. */
export const plain = (s = "") => s.replace(/`([^`]*)`/g, "$1").replace(/\*\*([^*]*)\*\*/g, "$1");
