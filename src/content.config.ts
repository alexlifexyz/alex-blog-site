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

const projectCollection = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    status: z.enum(["live", "building", "exploring"]).default("building"),
    stack: z.array(z.string()).default([]),
    year: z.string(),
    featured: z.boolean().default(false),
    links: z
      .object({
        repo: z.string().url().optional(),
        demo: z.string().url().optional(),
      })
      .optional(),
  }),
});

export const collections = {
  posts: postCollection,
  projects: projectCollection,
};
