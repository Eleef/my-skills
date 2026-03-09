# DocOps Skill Test Prompts

Use these prompts for lightweight manual trigger testing. They are written to help you judge whether `docops-mode` or `doc-template-router` should be chosen.

## Prompts expected to trigger `docops-mode`

### 1. Repo docs restructure
帮我梳理这个仓库现有文档的组织方式。我想把平台通用文档和某个 app 的业务文档彻底拆开，同时把 `dev_status` 的维护方式一起定下来。先不要直接写大段正文，先按流程给我方案。

### 2. Debugging + docs sync
我刚解决了一个部署问题，现在需要把排障过程、相关风险、以及后续要跟进的事项补到仓库文档里。顺便帮我判断这次是不是还要更新 `active_task` 或 `history_log`。

### 3. Multi-step feature documentation
我要推进一个新功能，涉及 API、数据字段、验收说明和当前迭代状态。你不要只回答建议，直接按完整 DocOps 工作流带我走。

### 4. Spec to implementation bridge
这个需求已经聊清楚了，也有 feature 草案和 API 约束。现在我要开始改代码，你先帮我把 implementation checklist、受影响代码面、验证计划和要同步的文档列出来。

## Prompts expected to trigger `doc-template-router`

### 5. Choose template family first
我要新增一篇文档，但我还没决定它应该是 feature、issue、还是 ADR。你先别写内容，先帮我路由到正确模板。

### 6. Micro-edit vs structural-edit
这个 `api_schema.md` 我只想补两个 endpoint 的说明，但也可能顺手重排目录。你先帮我判断这次到底算微改还是结构改。

### 7. Checklist-driven status update
我准备更新 `docs/dev_status/history_log.md`，但只想确认这次需要遵守哪些最小 checklist，不需要你先写正文。

### 8. Standards routing
我们最近在几个 app 里都遇到了同样的接口命名和错误返回风格不一致的问题。我不想把这事写进单个 feature 文档，你先帮我判断这应该落到 standards、ADR、还是 dictionary。

## Near-miss prompts that should usually NOT trigger these skills

### 9. Pure code change
帮我把这个 TypeScript 函数改成更简洁的写法，不需要动文档。

### 10. Generic explanation
解释一下什么是 SSOT，用中文简单说明就行，不结合当前仓库。

## Quick evaluation guide
- If the prompt is about repository documentation workflow, state tracking, or coordinated doc changes, prefer `docops-mode`.
- If the prompt is mainly about choosing format, edit path, checklist, template family, or standards-vs-ADR-vs-dictionary routing, prefer `doc-template-router`.
- If the prompt is just coding or general explanation, neither skill should be necessary.
