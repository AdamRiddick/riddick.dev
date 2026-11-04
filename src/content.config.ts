import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { glob } from "astro/loaders";
const work = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/work" }),
  schema: z.object({
    number: z.string(),
    title: z.string(),
    summary: z.string(),
    category: z.string(),
    outcome: z.string(),
    tags: z.array(z.string()),
    period: z.string(),
    role: z.string(),
    continuity: z.string(),
  }),
});
export const collections = { work };
