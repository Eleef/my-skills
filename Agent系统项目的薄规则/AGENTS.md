# AGENTS.md

仓库内涉及代码、文档、架构、排障、迭代的任务，使用以下规则：
- Always-on 精简规则在本文件。
- 详细 DocOps 工作流已迁移到 `.agents/skills/repo-docops/SKILL.md`。
- 禁止编造文件内容、目录结构、配置、运行结果或历史；若读不到关键文件，必须声明降级状态，列出最小缺失输入，并显式标注假设与风险。
- 必须显式使用 `VERIFIED` / `BROKEN` / `UNVERIFIED` 标注验证状态。
- 只要更新 `docs/dev_status/**`，必须明确当前 Track；若未指定，应先确认，无法确认时只能以 `PLATFORM-GENERAL` 作为 assumption 继续。
- App-specific 内容只能落在 `docs/apps/<app>/**`；`docs/platform/**` 只放跨 App 通用内容。
- 影响 API、数据、流程、部署的代码变更，必须在同一任务里同步更新对应文档。
- 当任务稍复杂（多文件、架构、排障、需要上下文延续）时，必须转入 `.agents/skills/repo-docops/SKILL.md` 的详细流程。
- 涉及 `docs/_meta/templates.md` 时，禁止整文件导入；先读 Routing Table，再只读需要的模板块。若只是 micro-edit（不改结构且 ≤30 行），默认只用 Checklist 做校验。
- 并行任务下，只允许更新当前 Track 对应的 `active_task` 区块和 overview 行；不得覆盖其他 Track。
