export const RESOURCE_LABELS: Record<string, string> = {
  standards: "标准规范",
  patents: "专利",
  papers: "论文",
  journals: "期刊",
  books: "教材书籍",
  vendors: "厂商资料",
  "tools-community": "工具与社区",
  "sic-design": "SIC 设计专题",
  "standards-text": "标准全文",
  "full-text": "资料全文",
};

export function resourceLabel(cat: string): string {
  return RESOURCE_LABELS[cat] || cat;
}

export function routeSlug(id: string): string {
  return id.replace(/\.md$/, "").replace(/\/index$/, "");
}

export function accessLabel(access?: string): string {
  switch (access) {
    case "free":
      return "免费";
    case "paid":
      return "付费";
    case "member":
      return "会员";
    default:
      return access || "—";
  }
}

export function statusLabel(status?: string): string {
  switch (status) {
    case "withdrawn":
      return "已撤销";
    case "verified":
      return "已验证";
    case "unverified":
      return "待核验";
    default:
      return status || "—";
  }
}

export function priorityStars(priority?: number): string {
  const p = priority || 0;
  return "★".repeat(p) + "☆".repeat(Math.max(0, 3 - p));
}
