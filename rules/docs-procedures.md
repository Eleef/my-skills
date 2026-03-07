---
trigger: model_decision
description: 触发 docs 文档时, 提供细节流程与模板规则.
---

# 细节流程与模板规则

## 模板引用与草案规则
- 重点覆盖模板核心要素，标题可灵活调整。
- 所有日期记录统一格式：`YYYY-MM-DD HH:MM`。
- 必须引用的核心文档缺失（如 `docs/guide/testing.md`）：
  1) 先从现有仓库/索引/指南推断技术栈与结构；
  2) 若仍不确定，创建 `> Status: Draft` 的通用骨架，标注 `TODO(需确认)`；
  3) 同时在 `docs/dev_status/active_task.md` 记录待确认项。
- 发现目录或关键文件缺失时，可主动提议初始化或补齐；不确定之处必须标注 `TODO(需确认)`。

## 模板库披露（核心要素速查）

### 1. Project Index (`docs/00_project_index.md`)
项目入口，必须包含：
- **Project Overview**: 只有一句话的介绍。
- **Quick Nav**: 指向 active_task, roadmap, architecture 等核心文档的链接。
- **Environment**: 关键的 env var 示例（脱敏）。
- **Key Resources**: 仓库地址、设计稿链接、Jira/飞书链接。

### 2. Active Task Context (`docs/dev_status/active_task.md`)
当前上下文，相当于“保存点”，必须包含：
- **Objective**: 当前正在攻克的一级目标。
- **Context Dump**: 任何接手人需要立即知道的信息（报错堆栈、已验证的假设、临时文件位置）。
- **Todo List**:
  - [x] 已完成
  - [/] 进行中
  - [ ] 待办
- **Blockers**: 阻碍进度的问题。

### 3. Technical Design (`docs/tech/designs/*.md`)
技术方案，必须包含：
- **Context**: 为什么要做这个？
- **Architecture**: 核心图表 (Mermaid)。
- **Data Model**: Schema changes。
- **API Spec**: 关键接口定义。
- **Migration**: 如何迁移这一步至关重要。

### 4. ADR (Architecture Decision Record) (`docs/adr/001-title.md`)
架构决策记录，必须包含：
- **Status**: Proposed / Accepted / Deprecated
- **Context**: 面临什么问题？有哪些选项？
- **Decision**: 选择了什么？
- **Consequences**: 带来了什么好处？引入了什么坏处（成本/风险）？

### 5. Issue / Bug Report (`docs/issues/YYYY-MM-DD-name.md`)
问题追踪，必须包含：
- **Observed**: 现象、报错日志。
- **Expected**: 预期行为。
- **Reproduction**: 复现步骤。
- **Analysis**: 根因分析 (RCA)。
- **Resolution**: 修复方案及验证结果。

## 归档规则（spec -> docs）
- **触发时机**：由 `my-skill-plan` 技能完成开发并通过验证后。
- **映射关系**：
  - `spec/features/xxx/requirements.md` -> `docs/product/features/xxx.md`
  - `spec/features/xxx/design.md` -> `docs/tech/designs/xxx.md`
  - 测试用例/脚本 -> `tests/` 或 `docs/guide/testing.md` 补充。
- **清理**：归档后，可清理 `spec/` 下的过程文件，或将其移动到 `spec/archived/` 以保持工作区整洁。

## Idea Parking 协议
- 触发：用户表示“现在不做/先记下来”。
- Type A（简单想法）：写入 `docs/dev_status/todo.md` 顶部（倒序）。
- Type B（详细方案）：
  1) 详细内容沉淀到知识库（如 `docs/tech/designs/xxx_plan.md` / `docs/product/xxx_plan.md` / `docs/adr/xxx_plan.md`），文档开头标 `> Status: Draft`；
  2) 在 `docs/dev_status/todo.md` 顶部创建摘要条目并附相对路径与章节定位。

## 任务生命周期协议 (Lifecycle Protocols)

### Exit Protocol（任务未完成但用户暂停/切换）
更新 `docs/dev_status/active_task.md`，确保下一次回来能无缝接续：
1. **Context Dump**: 甚至包括当前打开的文件、光标位置思考、剪贴板里的临时代码。
2. **Next Action**: 下一步具体执行那个命令、修改哪个函数。
3. **WIP Patch**: 如果有未提交代码，生成 patch 或建议 stash。

### Completion Protocol（目标完成）
1. 读取 `active_task.md`，提取核心成果写入 `docs/dev_status/history_log.md` 顶部（倒序）。
2. 查看 `docs/dev_status/todo.md`，询问是否将其中某项提升为下一个 Objective。
3. 将 `active_task.md` 重置为初始状态（清空 WIP 信息，保留骨架）。