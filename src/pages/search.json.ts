import type { APIRoute } from "astro";
import { getCollection } from "astro:content";

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
  let slug = id.replace(/\.md$/, "").replace(/\/index$/, "");
  return `/${collection}/${slug}/`;
}

export const GET: APIRoute = async () => {
  const collections = ["design", "knowledge", "tutorials", "glossary", "learn", "resources"] as const;
  const items: any[] = [];
  for (const name of collections) {
    const entries = await getCollection(name);
    for (const e of entries) {
      if (e.id.includes("_template")) continue;
      const cat = name === "resources" ? e.id.split("/")[0] : name;
      const path = urlFor(cat, e.id);
      items.push({
        title: e.data.title || e.id,
        description: e.data.description || "",
        tags: e.data.tags || [],
        url: path,
        path,
        text: stripMd((e as any).body || ""),
      });
    }
  }
  return new Response(JSON.stringify(items), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
