# CAN FD 知识库

面向 **模拟 IC 设计工程师**(嵌入式工程师为辅助读者)的中文 **CAN FD / CAN SIC** 知识库:协议、位定时、物理层、收发器模块设计、测试认证与资源索引。

## 技术栈

- [Astro](https://astro.build) 5(Content Collections + View Transitions)
- [Motion](https://motion.dev) 弹簧动效
- Mermaid(本地托管 JS,客户端渲染)
- 部署:GitHub Actions → GitHub Pages(`actions/deploy-pages`)

## 本地开发

```bash
# 使用 pnpm 9(package.json 已声明 packageManager,corepack 会自动选择)
corepack enable
pnpm install
pnpm dev        # http://localhost:4321
pnpm build      # 输出 dist/
pnpm preview
```

验证命令:

```bash
pnpm exec astro check   # 类型检查(0 错误)
pnpm audit --prod       # 依赖安全审计
```

## 目录结构

```text
src/
├── content/            # Markdown 内容集合
│   ├── design/         # 设计参考(模块参数设计要点)
│   ├── knowledge/      # 知识库
│   ├── tutorials/      # 教程
│   ├── glossary/       # 术语表
│   ├── learn/          # 学习路线
│   ├── resources/      # 资源条目(含 standards-text / full-text)
│   └── pages/          # about / contribute / sic(SIC 专题站内页)
├── components/         # 毛玻璃头部、搜索、主题切换、动效组件
├── layouts/            # Base / Doc
├── pages/              # 路由(含动态集合路由)
├── plugins/            # Markdown 插件(告警块/Mermaid/链接重写)
└── styles/             # Apple 风格设计系统
public/
├── files/              # PDF 与 SIC 专题图(静态资源)
└── js/mermaid.min.js   # 本地托管的 Mermaid
```

## 内容维护

- 知识/教程/术语:直接编辑 `src/content/**/*.md`,frontmatter 含 `title/description/tags`;
- SIC 专题:站内单页 `src/content/pages/sic.md`(路由 `/sic/`),图片位于 `public/files/sic-design/images/`;旧的独立 HTML 笔记已移除,不要再引用;
- TX 模块:设计要点见 `src/content/design/tx-module.md`;模拟 IC 教材知识总结见 `src/content/knowledge/transceiver-design/analog-ic-textbooks.md`;
- 资源条目:编辑 `src/content/resources/<分类>/<slug>.md`,分类页自动生成,无需手维护汇总表;
- 新资源 PDF:放入 `public/files/<分类>/`,并在条目 frontmatter 写 `local_file: files/<分类>/<文件名>.pdf`;
- 重新生成 PDF 以外的静态资源后运行 `pnpm build` 验证。

## 部署

推送 `main` 分支,`.github/workflows/pages.yml` 自动构建并发布到 GitHub Pages。
