export const BASE = import.meta.env.BASE_URL;

export function withBase(path: string): string {
  if (!path) return BASE || "/";
  if (/^(https?:|mailto:|tel:|data:|javascript:|#)/i.test(path)) return path;
  const prefix = BASE.endsWith("/") ? BASE.slice(0, -1) : BASE;
  if (path.startsWith(prefix + "/") || path === prefix) return path;
  return prefix + (path.startsWith("/") ? path : "/" + path);
}
