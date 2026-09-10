import { defineCollection, z } from "astro:content";

const postCollection = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    description: z.string().default(""),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    featured: z.boolean().default(false),
    pinned: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    category: z.string().default("essays"),
    draft: z.boolean().default(false),
  }),
});

export const collections = {
  posts: postCollection,
};
