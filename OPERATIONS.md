# 运营说明(Astro 版)

## 结构要点

- **单一事实源**:资源分类页与条目页均由 `src/content/resources/**/*.md` 自动生成,不再维护 JSON/汇总表双份数据。
- **SIC 专题**:内容整合在 `src/content/pages/sic.md`(站内 `/sic/` 一页),22 张 SVG 位于 `public/files/sic-design/images/`;旧的独立 `SIC学习笔记.html` 已移除,不要再引用。
- **TX 模块与教材**:设计要点见 `src/content/design/tx-module.md`;模拟 IC 教材知识总结见 `src/content/knowledge/transceiver-design/analog-ic-textbooks.md`。
- **链接约定**:Markdown 内继续使用相对链接(`../glossary/x.md`、`../../files/xxx.pdf`),构建期由 `src/plugins/markdown.ts` 自动重写为最终路由;新增内容无需手算前缀。
- **图表**:Mermaid 代码块由前端渲染(本地 `public/js/mermaid.min.js`);SVG 技术图位于 `public/files/sic-design/images/`(由原 `scripts/generate_figures.py` 生成,保留在旧提交历史中,如需再生成可从历史恢复脚本)。

## 构建门禁

```bash
corepack enable          # 使用 pnpm 9(package.json packageManager)
pnpm install
pnpm build
pnpm exec astro check    # 类型检查(0 错误)
pnpm audit --prod        # 依赖安全审计
python3 ../tmp/check_dist.py   # 可选:内部链接完整性校验(需在项目外脚本目录)
```

## 部署

`main` 推送触发 `deploy-pages` 工作流:构建 `dist/` → 上传产物 → `actions/deploy-pages` 发布。Pages 设置需为 **GitHub Actions** 源(`build_type=workflow`)。

## 注意事项

- 不要提交 `node_modules/`、`dist/`、`.astro/`(已在 `.gitignore`);
- 新增 PDF 建议 ≤ 100MB(GitHub 单文件限制);
- 版权红线不变:只托管可免费公开获取的 PDF,付费标准只给官方链接。
