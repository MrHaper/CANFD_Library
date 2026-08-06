# CAN FD 知识库

面向 **模拟 IC 设计工程师**(嵌入式工程师为辅助读者)的中文 **CAN FD / CAN SIC** 学习资料库,沉淀「协议 → 物理层 → 收发器设计 → 测试认证」全流程知识。

> 建站背景:团队已流片一颗 CAN FD (SIC) 收发器芯片,本站把这套过程中的标准、专利、论文、厂商资料与工程经验整理成可公开访问的知识体系。

## 站点内容

| 板块 | 内容 | 入口 |
| --- | --- | --- |
| 学习路线 | 模拟 IC / 嵌入式两条分角色路线,按阶段给出目标、必读与动手任务 | [学习路线](https://MrHaper.github.io/CANFD_Library/learn/) |
| 设计参考 | **收发器模块参数设计要点**(模拟 IC 主线):规格基线、时序链路预算、输出级、接收比较器、SIC 控制、振铃抑制、ESD/总线保护、电源唤醒与自查总表 | [设计参考](https://MrHaper.github.io/CANFD_Library/design/) |
| 知识库 | 8 大子域:协议、位定时、物理层与 SIC、收发器设计、控制器、工具测试、项目实践笔记、SIC 设计专题 | [知识库](https://MrHaper.github.io/CANFD_Library/knowledge/) |
| 教程 | 12 篇原创图文教程(帧结构、位定时、TDC、SocketCAN、示波器抓帧、plugfest 等) | [教程](https://MrHaper.github.io/CANFD_Library/tutorials/) |
| 资源库 | 115 条分类索引:标准 / 专利 / 论文 / 期刊 / 教材 / 厂商资料 / 工具社区 / SIC 专题,45 份公开 PDF 直接下载 | [资源库](https://MrHaper.github.io/CANFD_Library/resources/) |
| 标准全文 | Bosch CAN FD 规范等公开标准全文站内查阅,关键标准参数速查 | [标准查阅](https://MrHaper.github.io/CANFD_Library/resources/standards-text/) |
| 术语表 | 51 个中英对照词条,A-Z 即时查漏 | [术语表](https://MrHaper.github.io/CANFD_Library/glossary/) |
| SIC 学习笔记 | 原理 → 设计 → 测试三章单文件网页,含 22 张原创技术图,可打印 | [SIC 学习笔记](https://MrHaper.github.io/CANFD_Library/files/sic-design/SIC%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.html) |

## 技术栈

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)(Python)静态文档站
- 中文搜索:jieba 分词 + 自定义词典
- 图表:Mermaid 全站 100+ 张(本地托管 JS)+ 22 张原创 SVG 技术图
- 部署:GitHub Actions 自动构建并发布到 GitHub Pages

## 本地开发

```bash
python -m venv .venv
source .venv/Scripts/activate        # Windows
pip install -r requirements.txt

mkdocs serve                         # 本地预览
mkdocs build --strict                # 严格构建(零警告门禁)
python scripts/validate_resources.py docs/   # 资源数据校验(ERROR=0)
```

## 维护与贡献

**仓库运营规则、内容更新流程、部署方式与已知限制请先阅读 [OPERATIONS.md](OPERATIONS.md)。**

- 勘误记录与贡献指南:https://MrHaper.github.io/CANFD_Library/contribute/
- 发现错误或想补充资料:在 [Issues](https://github.com/MrHaper/CANFD_Library/issues) 提交,或直接发起 Pull Request
- 发布方式:推送 `main` 分支,GitHub Actions 自动构建部署

## 许可说明

仓库内 **PDF 与标准全文归原作者/组织所有**,本站仅托管可免费公开获取的资料;站点原创内容(教程、知识库、术语释义等)以仓库声明为准,引用请注明出处。
