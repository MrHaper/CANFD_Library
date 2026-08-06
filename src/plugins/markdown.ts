import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import remarkRehype from "remark-rehype";
import rehypeStringify from "rehype-stringify";
import { visit } from "unist-util-visit";
import { fromHtml } from "hast-util-from-html";
import type { Root } from "mdast";
import type { Root as HastRoot } from "hast";

const TYPE_LABELS: Record<string, string> = {
  tip: "提示",
  note: "注意",
  warning: "警告",
  abstract: "摘要",
  info: "信息",
  success: "成功",
  danger: "危险",
};

function renderInnerMd(source: string): string {
  const file = unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkRehype)
    .use(rehypeStringify)
    .processSync(source);
  return String(file);
}

/** 在 rehype 层把 pymdownx 风格的 `!!! type "标题"` 段落转换为告警块。 */
export function rehypeAdmonitions() {
  return (tree: HastRoot) => {
    visit(tree, "element", (node: any, index: number | null, parent: any) => {
      if (index === null || !parent || node.tagName !== "p") return;
      const text = (node.children || [])
        .map((c: any) => (c.type === "text" ? c.value : ""))
        .join("");
      const m = text.match(/^!!!\s+([a-z]+)\s*(?:["“]([^"”]*)["”])?\s*([\s\S]*)$/i);
      if (!m) return;
      const type = m[1].toLowerCase();
      const title = m[2] || TYPE_LABELS[type] || type;
      const rest = m[3]?.trim() || "";
      const bodyHtml = rest ? renderInnerMd(rest) : "";
      const asideHtml =
        `<aside class="admonition admonition-${type}">` +
        `<p class="admonition-title">${title}</p>` +
        `<div class="admonition-body">${bodyHtml}</div></aside>`;
      const nodes = fromHtml(asideHtml, { fragment: true }).children;
      parent.children.splice(index, 1, ...nodes);
    });
  };
}

/** 把 mermaid 代码块提取为 <pre class="mermaid">,由前端渲染。 */
export function remarkMermaid() {
  return (tree: Root) => {
    visit(tree, "code", (node: any, index: number | null, parent: any) => {
      if (index === null || !parent) return;
      if (node.lang !== "mermaid") return;
      const value = String(node.value ?? "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
      parent.children[index] = { type: "html", value: `<pre class="mermaid">${value}</pre>` } as any;
    });
  };
}

/** 把相对图片路径解析为绝对站点路径,避免 Astro 把它们当模块资源处理。 */
export function remarkAbsoluteImages() {
  return (tree: Root, file: any) => {
    const filePath: string = file.history?.[0] ?? "";
    const sep = filePath.includes("\\") ? "\\" : "/";
    const marker = `${sep}src${sep}content`;
    const idx = filePath.indexOf(marker);
    let basePath = "/";
    if (idx !== -1) {
      basePath = filePath.slice(idx + marker.length).replace(/\\/g, "/");
    }
    if (basePath.startsWith("/pages/")) {
      const name = basePath.split("/").pop() || "";
      basePath = "/" + name;
    }
    // 资源条目源文件在 _entries 下,按旧层级解析相对链接
    if (/^\/resources\/[^/]+\/[^/]+\.md$/.test(basePath) && !basePath.includes("standards-text") && !basePath.includes("full-text")) {
      basePath = basePath.replace(/^\/resources\//, "/resources/_entries/");
    }
    const baseUrl = new URL(basePath, "https://canfd.local");
    visit(tree, "image", (node: any) => {
      const src = node.url || "";
      if (/^(https?:|data:|#)/i.test(src) || src.startsWith("/")) return;
      try {
        const url = new URL(src, baseUrl);
        node.url = url.pathname + (url.hash || "");
      } catch {
        // ignore
      }
    });
  };
}

/** 把旧的相对 .md 链接重写为新的站点路由。 */
export function rehypeRewriteLinks() {
  return (tree: any, file: any) => {
    const filePath: string = file.history?.[0] ?? "";
    const marker = `${filePath.includes("\\") ? "\\" : "/"}src${filePath.includes("\\") ? "\\" : "/"}content`;
    const idx = filePath.indexOf(marker);
    let basePath = "/";
    if (idx !== -1) {
      basePath = filePath.slice(idx + marker.length).replace(/\\/g, "/");
    }
    // pages 集合渲染在站点根级(/about/、/contribute/),按文件名解析链接
    if (basePath.startsWith("/pages/")) {
      const name = basePath.split("/").pop() || "";
      basePath = "/" + name;
    }
    // 资源条目源文件在 _entries 下,按旧层级解析相对链接
    if (/^\/resources\/[^/]+\/[^/]+\.md$/.test(basePath) && !basePath.includes("standards-text") && !basePath.includes("full-text")) {
      basePath = basePath.replace(/^\/resources\//, "/resources/_entries/");
    }
    const baseUrl = new URL(basePath, "https://canfd.local");
    visit(tree, "element", (node: any) => {
      if (node.tagName !== "a") return;
      const href = node.properties?.href;
      if (typeof href !== "string" || href === "") return;
      if (/^(https?:|mailto:|tel:|data:|javascript:)/i.test(href)) return;
      if (href.startsWith("/") || href.startsWith("#")) return;
      let url: URL;
      try {
        url = new URL(href, baseUrl);
      } catch {
        return;
      }
      let out = url.pathname;
      if (out.endsWith(".md")) {
        out = out.slice(0, -3);
        if (out.endsWith("/index")) out = out.slice(0, -6);
        if (out === "/index") out = "/";
        // 旧资源条目路径 -> 新路由
        out = out.replace(/^\/resources\/_entries\//, "/resources/");
      } else if (out.endsWith(".pdf") || out.endsWith(".svg") || out.endsWith(".png") || out.endsWith(".jpg")) {
        node.properties.href = out + (url.hash || "");
        return;
      } else if (out.endsWith(".html")) {
        node.properties.href = out + (url.hash || "");
        return;
      }
      if (!out.endsWith("/") && out !== "/") out += "/";
      node.properties.href = out + (url.hash || "");
    });
  };
}
