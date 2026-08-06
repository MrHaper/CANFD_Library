import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const mdSchema = z
  .object({
    title: z.string(),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
    date: z.union([z.string(), z.date()]).optional(),
    authors: z.array(z.string()).optional(),
    type: z.string().optional(),
    organization: z.string().optional(),
    year: z.union([z.number(), z.string()]).optional(),
    version: z.string().optional(),
    access: z.string().optional(),
    status: z.string().optional(),
    download: z.string().optional(),
    priority: z.number().optional(),
    audience: z.array(z.string()).optional(),
    source: z.string().optional(),
    local_file: z.string().optional(),
    search: z.any().optional(),
  })
  .passthrough();

export const collections = {
  knowledge: defineCollection({
    loader: glob({ pattern: ["*.md", "**/*.md"], base: "./src/content/knowledge" }),
    schema: mdSchema,
  }),
  tutorials: defineCollection({
    loader: glob({ pattern: ["*.md", "**/*.md"], base: "./src/content/tutorials" }),
    schema: mdSchema,
  }),
  glossary: defineCollection({
    loader: glob({ pattern: ["*.md", "**/*.md"], base: "./src/content/glossary" }),
    schema: mdSchema,
  }),
  design: defineCollection({
    loader: glob({ pattern: ["*.md", "**/*.md"], base: "./src/content/design" }),
    schema: mdSchema,
  }),
  learn: defineCollection({
    loader: glob({ pattern: ["*.md", "**/*.md"], base: "./src/content/learn" }),
    schema: mdSchema,
  }),
  resources: defineCollection({
    loader: glob({ pattern: ["*.md", "**/*.md"], base: "./src/content/resources" }),
    schema: mdSchema,
  }),
  docs: defineCollection({
    loader: glob({ pattern: ["*.md", "**/*.md"], base: "./src/content/pages" }),
    schema: mdSchema,
  }),
};
