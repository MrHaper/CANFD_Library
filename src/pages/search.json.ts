import type { APIRoute } from "astro";
import { getCollection } from "astro:content";
import { withBase } from "../lib/base";

function stripMd(src: string, max = 900): string {
  return src
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/!\[[^\]]*\]\([^)]*\)/g, " ")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/[#>*_`~|-]/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, max);
}

function urlFor(collection: string, id: string): string {
  if (collection === "docs") {
    if (id === "sic") return "/sic/";
    if (id === "about") return "/about/";
    if (id === "contribute") return "/contribute/";
    return `/${id}/`;
  }
  let slug = id.replace(/\.md$/, "").replace(/\/index$/, "");
  if (collection === "resources") {
    return slug === "index" ? "/resources/" : `/resources/${slug}/`;
  }
  if (slug === "index") return `/${collection}/`;
  return `/${collection}/${slug}/`;
}

export const GET: APIRoute = async () => {
  const collections = ["design", "knowledge", "tutorials", "glossary", "learn", "resources", "docs"] as const;
  const items: any[] = [];
  for (const name of collections) {
    const entries = await getCollection(name);
    for (const e of entries) {
      if (e.id.includes("_template")) continue;
      const path = urlFor(name, e.id);
      items.push({
        title: e.data.title || e.id,
        description: e.data.description || "",
        tags: e.data.tags || [],
        url: withBase(path),
        path: withBase(path),
        text: stripMd((e as any).body || ""),
      });
    }
  }
  return new Response(JSON.stringify(items), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
