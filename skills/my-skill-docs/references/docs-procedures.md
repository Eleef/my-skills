# 文档流程与模板规则

在需要更新项目文档、同步验收记录、归档 `spec/` 成果或维护状态文档时，按需读取本文件。

## 使用原则
- 优先遵循仓库已有文档结构；不要因为技能规范强行重构目录。
- 默认只更新当前任务所需的最少文档。
- 发现目录或关键文件缺失时，可以建议初始化或补齐；只有在当前任务确有必要且用户同意时再创建。
- 所有日期记录统一格式：`YYYY-MM-DD HH:MM`。
- 不记录真实密钥、Token、私钥或生产数据；示例使用占位符。

## 模板引用与草案规则
- 创建新文档或重构旧文档时，优先参考 `docs/_meta/templates.md` 的结构建议（若存在）。
- 重点覆盖模板核心要素，标题可按当前项目实际情况调整。
- 必须引用的核心文档缺失（如 `docs/guide/testing.md`）时：
  1. 先从现有仓库结构、索引或指南推断技术栈与流程；
  2. 若仍不确定，只输出通用骨架，并明确标注 `TODO(需确认)`；
  3. 如需留痕，可在 `docs/dev_status/active_task.md` 记录待确认项。

## 核心文档速查

### 1. Project Index (`docs/00_project_index.md`)
项目入口，建议包含：
- **Project Overview**：一句话项目说明。
- **Quick Nav**：指向 active_task、roadmap、architecture 等核心文档。
- **Environment**：关键 env var 示例（脱敏）。
- **Key Resources**：仓库、设计稿、任务系统等入口链接。

### 2. Active Task Context (`docs/dev_status/active_task.md`)
当前上下文，建议包含：
- **Objective**：当前一级目标。
- **Context Dump**：任何接手人需要立即知道的高价值上下文。
- **Todo List**：
  - [x] 已完成
  - [/] 进行中
  - [ ] 待办
- **Blockers**：当前阻塞项。
- **Next Action**：下一个明确动作。

### 3. Technical Design (`docs/tech/designs/*.md`)
技术方案，建议包含：
- **Context**：为什么要做。
- **Architecture**：核心图表或流程说明。
- **Data Model**：Schema changes。
- **API Spec**：关键接口定义。
- **Migration**：迁移或兼容说明。

### 4. ADR (`docs/adr/001-title.md`)
架构决策记录，建议包含：
- **Status**：Proposed / Accepted / Deprecated。
- **Context**：面临的问题与候选方案。
- **Decision**：最终选择。
- **Consequences**：收益、成本与风险。

### 5. Issue / Bug Report (`docs/issues/YYYY-MM-DD-name.md`)
问题追踪，建议包含：
- **Observed**：现象、报错日志。
- **Expected**：预期行为。
- **Reproduction**：复现步骤。
- **Analysis**：根因分析。
- **Resolution**：修复方案与验证结果。

## `spec/` 命名建议
若项目采用本套 `spec/` 结构，推荐统一为：
```text
spec/features/<feature-key>/
├── 01_requirements.md
├── 02_acceptance.md
├── 03_open_questions.md
├── 04_design.md
└── 05_plan.md
```

## 归档规则（spec -> docs）
- **触发时机**：需求或方案已稳定，且需要归档到长期文档。
- **推荐映射**：
  - `01_requirements.md` -> `docs/product/features/<feature-key>.md`
  - `04_design.md` -> `docs/tech/designs/<feature-key>.md`
  - `05_plan.md` -> 按需合并到设计文档、运行指南或阶段记录，不要求一对一长期保留
  - 验证方式与测试结论 -> `docs/guide/testing.md` 或对应功能文档中的验证章节
- **索引维护**：若新增长期文档，更新 `docs/00_project_index.md` 中的入口。
- **过程文件处理**：归档后是否保留 `spec/` 过程文件，应遵循项目习惯；不要默认清理或移动。

## 验证状态记录
- `UNVERIFIED`：未运行测试或未完成验证。
- `BROKEN`：已验证失败，需附修复方向或阻塞说明。
- `VERIFIED`：已验证通过，附命令与关键结果摘要。

## Idea Parking 协议
- 触发：用户表示“现在不做”“先记下来”或“后面再说”。
- Type A（简单想法）：写入 `docs/dev_status/todo.md` 顶部（倒序）。
- Type B（详细方案）：
  1. 详细内容沉淀到知识库（如 `docs/tech/designs/<name>_plan.md` / `docs/product/<name>_plan.md` / `docs/adr/<name>_plan.md`），文档开头标 `> Status: Draft`；
  2. 在 `docs/dev_status/todo.md` 顶部创建摘要条目并附相对路径。

## 生命周期记录

### 暂停记录
当任务未完成但用户暂停或切换时，至少记录：
1. 当前目标
2. 已完成内容
3. 未完成内容
4. 阻塞项
5. 下一步动作

### 结项记录
当阶段目标完成时，至少记录：
1. 本阶段完成内容
2. 验证状态与关键结果
3. 相关文档入口
4. 后续可选事项
