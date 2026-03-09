---
name: doc-template-router
description: 将仓库文档任务路由到正确的编辑模式和模板形态。每当用户想要创建文档、重写或重构现有文档、在功能/词典/标准/开发状态/问题/ADR 格式之间进行选择、决定编辑是微型还是结构化、或应用基于检查清单的文档质量控制而非自由写作时，使用此技能。当任务主要关于在起草前选择正确的文档格式、标准 vs ADR vs 词典存放位置、模板家族或编辑路径时，首选此技能。
---

# 文档模板路由器 (Doc Template Router)

当任务涉及选择正确的文档模式而非运行完整的 DocOps 工作流时，使用此技能。

## 目标
将文档请求转化为最小的正确编辑路径：
- 仅使用检查清单的微型编辑 (Micro-edit)
- 使用单一模板家族的结构化编辑 (Structural edit)

此技能是模板路由层。它应与常驻规则保持分离。

## 决策流

### 1. 确定编辑规模 (Edit size)
如果满足以下任一条件，将请求视为**微型编辑 (Micro-edit)**：
- 仅更改一个小的章节
- 总变更量大约在 30 行以内
- 未创建新文档
- 不需要重排主要章节
- 不涉及系统性的词典/Schema 重新设计

对于微型编辑：
- 不要加载完整的模板正文
- 仅使用适当的检查清单 (Checklist)
- 保留现有结构

如果满足以下任一条件，将请求视为**结构化编辑 (Structural edit)**：
- 正在创建新文档
- 添加或重组了多个章节
- 将多个来源合并到一个新结构中
- 词典内容需要大规模重做

对于结构化编辑：
- 仅选择一个模板家族
- 除非用户明确要求，否则不要混用多个顶层模板结构

### 2. 路由到模板家族
使用以下映射关系：
- 项目入口 / 导航 → `PROJECT_INDEX`
- 平台共享文档或平台拥有的规范 → `PLATFORM_*`
- 平台可重用的标准 / 约定 / 政策 → `PLATFORM_STANDARDS`
- 应用概览 → `APP_README`
- 功能叙事 / 验收 / 流程 → `FEATURE_SPEC`
- API 契约 → `DICTIONARY_API_SCHEMA`
- 数据 / 数据库契约 → `DICTIONARY_DATA_SCHEMA`
- UI 契约 → `DICTIONARY_UI_SCHEMA`
- 开发状态更新 → `DEV_STATUS_*`
- 错误报告 / 事件复盘 → `ISSUE`
- 架构决策 → `ADR_*`

### 3. 保持 SSOT 边界清晰
- 应用词典 (Dictionary) 文档是应用作用域 Schema 和契约的权威。
- 平台拥有的共享契约可能存在于 `docs/platform/<component>/specs/**` 中。
- 功能文档应链接到权威文档，而非复制完整的表格。
- 运维 (Ops) 文档应描述操作和部署行为，不要重复 Schema。

### 4. 应用正确的检查清单 (Checklist)
对于以下常见的微型编辑情况，恰好使用一个相关的检查清单家族：
- `FEATURE`
- `DICTIONARY`
- `ISSUE`
- `DEV_STATUS`

对于其他小型文档类型，如项目索引、应用概览、平台文档或 ADR：
- 保留现有结构
- 使用 `references/template_notes.md` 了解章节预期
- 除非编辑变为结构化，否则不要加载完整的骨架

检查清单的目的：
- 在需要时更新时间戳
- 保留稳定的锚点 (Anchors)
- 链接保持可用
- 无重复的 Schema 偏移 (Drift)
- 行为变更时包含验证和回滚

### 5. 输出格式
在路由请求时，简要报告：
1. 编辑类型：微型或结构化
2. 选择的模板家族或检查清单家族
3. 为什么选择这条路由
4. 任何缺失的输入
5. 最可能受影响的文档路径

## 参考文件
仅读取你需要的内容：
- `references/routing_table.md` 用于路由映射
- `references/checklists.md` 用于微型编辑质量检查
- `references/template_notes.md` 用于最小化的结构化模板指南
- `references/structural_templates_platform.md` 用于 `PROJECT_INDEX`, `PLATFORM_*`, 和 `PLATFORM_STANDARDS`
- `references/structural_templates_app_core.md` 用于 `APP_README` 和 `FEATURE_SPEC`
- `references/structural_templates_app_contracts.md` 用于 `DICTIONARY_*`
- `references/structural_templates_status_and_records.md` 用于 `DEV_STATUS_*`, `ISSUE`, 和 `ADR_*`

## 编写指南
- 优先选择最小的符合规范的结构。
- 当基于检查清单的补丁足够时，不要强加完整的模板。
- 如果用户要求草案但原始材料不完整，创建一个带有明确假设的草案，而非虚构细节。
- 如果任务实际上关于仓库范围内的工作流、开发状态协调或多步骤 DocOps 执行，请将其交回给 `docops-mode`，而不是吸收整个过程。

## 示例触发场景
- "我要新建一个 feature 文档，你先帮我判断该走哪个模板。"
- "这个 API schema 文档要重构，帮我判断是微调还是结构性改写。"
- "我要补一个 issue 复盘，但不想自由发挥，你按模板路由来。"
- "先别写内容，先告诉我这次 dev_status 更新该用哪种结构。"
- "这个规则以后多个 app 都要复用，你判断该写 standards、ADR 还是 dictionary。"
