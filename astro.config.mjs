import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import {
  remarkMermaid,
  remarkAbsoluteImages,
  rehypeAdmonitions,
  rehypeRewriteLinks,
} from "./src/plugins/markdown.ts";

export default defineConfig({
  site: "https://MrHaper.github.io/CANFD_Library",
  base: "/CANFD_Library",
  trailingSlash: "always",
  viewTransitions: true,
  build: {
    format: "directory",
  },
  markdown: {
    remarkPlugins: [remarkMermaid, [remarkAbsoluteImages, { base: "/CANFD_Library" }]],
    rehypePlugins: [rehypeAdmonitions, [rehypeRewriteLinks, { base: "/CANFD_Library" }]],
    shikiConfig: {
      theme: "github-light",
      wrap: true,
    },
  },
  integrations: [sitemap()],
  vite: {
    ssr: {
      noExternal: ["motion"],
    },
  },
});
