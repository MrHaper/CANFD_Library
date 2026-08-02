# CAN FD 知识库

面向 **模拟 IC 设计工程师、嵌入式工程师与学生** 的中文 CAN FD / CAN SIC 学习资料库,沉淀"协议 → 物理层 → 收发器设计 → 测试认证"全流程知识。

## 内容

- **资源库**:105 条分类索引(标准 / 专利 / 论文 / 期刊 / 教材 / 厂商资料 / 工具社区),35 份公开 PDF 可直接下载
- **原创教程**:12 篇图文教程(帧结构、位定时、TDC、SIC 振铃抑制、SocketCAN、示波器抓帧、一致性测试等)
- **学习路线**:模拟IC / 嵌入式 / 学生三条分阶段路径
- **知识库**:6 大子域 18 个知识点页 + 51 个术语词条

## 快速开始

```bash
pip install -r requirements.txt
mkdocs serve                 # 本地预览
mkdocs build --strict        # 严格构建(零警告门禁)
```

## 链接

- 线上站点:https://MrHaper.github.io/CANFD_Library/
- 学习路线:https://MrHaper.github.io/CANFD_Library/learn/
- 资源库:https://MrHaper.github.io/CANFD_Library/resources/
- 勘误与贡献:https://MrHaper.github.io/CANFD_Library/contribute/

## 维护与交接

**仓库运营规则、内容更新流程、部署方式、已知限制请阅读 [OPERATIONS.md](OPERATIONS.md)** —— 接手运营前必读。

- 内容更新流程(新增资料 / 勘误):见 OPERATIONS.md §4
- 维护纪律与红线(版权 / 元数据 / 链接层级):见 OPERATIONS.md §6、§8
- 发布:推送 `main` 分支,GitHub Actions 自动构建部署
