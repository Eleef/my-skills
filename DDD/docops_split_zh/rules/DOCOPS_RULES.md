# DocOps 规则核心 (Core)

> 目的：从 `doc-ops-prompt.md` 中提取的轻量级常驻规则。
> 将其作为持久化的规则层。保持简短且稳定。

## 范围门控 (Scope gate)
- 仅在用户请求涉及本仓库的代码、文档、架构、调试或迭代工作流时应用这些规则。
- 如果请求明显与本项目无关，请勿强制执行 DocOps 工作流或更新 `dev_status`。

## 真实性与验证 (Reality and verification)
- 请勿虚构仓库文件、输出、配置、历史记录或运行时行为。
- 如果某个文件或输出不可用，请明确说明并请求提供最少量的缺失输入。
- 在交付中使用明确的验证标签：
  - `VERIFIED`（已验证）：实际运行并通过，附带命令和简短的输出摘要。
  - `BROKEN`（损坏）：实际运行并失败，附带复现步骤、错误摘要和下一步修复方向。
  - `UNVERIFIED`（未验证）：未运行或无可用证明。

## 工作状态 vs 验证 (Working state vs verification)
- `Working state`（工作状态）说明任务在工作流中所处的位置。
- `Verification labels`（验证标签）说明特定结果的证据状态。
- 它们是相互独立的：一个任务应当有一个主工作状态，而一次回复可能包含多个验证标签。

## 开发状态的轨迹标记 (Track tagging)
- 任何涉及 `docs/dev_status/**` 的更新都必须指定一条轨迹 (Track)。
- 如果用户未指定，请先询问。
- 如果需要临时假设，请使用 `PLATFORM-GENERAL` 并将其标注为假设。

## SSOT 与原子更新 (SSOT and atomic updates)
- App 作用域的字段、契约、Schema、表结构和 API 行为仅在 `docs/apps/<app>/dictionary/**` 中具有权威性。
- 平台共享的契约或规范在所有者为可重用的平台组件或服务时，可能在 `docs/platform/<component>/specs/**` 中具有权威性。
- `features/**` 可以引用权威文档，但不得维护第二个 Schema 副本。
- 如果代码变更影响了 API、数据、工作流或部署行为，请在同一任务中更新相应的文档。

## 交付格式 (Delivery format)
在提供 DESIGN（设计）/ IMPLEMENTING（实施）/ VERIFYING（验证）风格的结果时，请包含：
1. 当前工作状态 (Current Working State)
2. 摘要 (Summary)（原因 / 内容）
3. 文档变更 (Docs changes)（路径 + 关键点）
4. 代码变更 (Code changes)（路径 + 关键点）
5. 验证 (Verification)（命令 + 预期 + VERIFIED/BROKEN/UNVERIFIED）
6. 风险与回滚 (Risks and rollback)

**简短示例：**
- 当前工作状态：`IMPLEMENTING`
- 验证：
  - 单元测试：`VERIFIED`
  - 端到端流程：`UNVERIFIED`

## 完结纪律 (Completion discipline)
- 如果工作在完成前暂停，请仅更新相关轨迹的活动任务上下文。
- 不要覆盖 `active_task.md` 中的其他轨迹。
- `history_log.md` 条目必须是单轨迹条目。
- 当用户确认完成时，添加一条简洁的顶部历史记录，并重置或更新相关的活动状态。

## 技能交付 (Skill handoff)
- 对于较重的文档工作，请使用专门的 DocOps 工作流技能，而不是扩展这些规则。
- 对于模板选择、路由和检查清单驱动的起草，请使用专门的模板技能，而不是在常驻规则中保留模板详情。
