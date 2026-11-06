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
const writing = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/writing" }),
  schema: z
    .object({
      title: z.string(),
      summary: z.string(),
      topic: z.enum([
        "Architecture",
        "Operations & FinOps",
        "Technical leadership",
      ]),
      takeaway: z.string(),
      draft: z.boolean().default(true),
      publicationMonth: z
        .string()
        .regex(/^\d{4}-(0[1-9]|1[0-2])$/)
        .optional(),
      experiencePeriod: z.string().optional(),
      order: z.number().default(0),
      sketch: z.enum([
        "handover",
        "recovery",
        "tenancy",
        "completion",
        "feedback",
        "provider",
      ]),
    })
    .superRefine((article, context) => {
      if (!article.draft && !article.publicationMonth) {
        context.addIssue({
          code: "custom",
          message: "Published articles require a publication month.",
          path: ["publicationMonth"],
        });
      }
    }),
});
export const collections = { work, writing };
