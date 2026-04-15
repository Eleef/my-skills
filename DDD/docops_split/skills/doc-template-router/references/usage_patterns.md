# Usage Patterns

Load this note only when you need lower-frequency writing guidance or concrete trigger examples while using `doc-template-router`.

## Writing guidance
- Prefer the smallest compliant structure.
- Do not force a full template when a checklist-based patch is enough.
- If the user asks for a draft but the source material is incomplete, create a draft with explicit assumptions instead of fake details.
- If the request is still an in-flight stage draft rather than a published docs artifact, hand back to `docops-mode` and keep the evolving material in `spec/**` until it is ready to publish.
- If the task is really about repository-wide workflow, dev-status coordination, or multi-step DocOps execution, hand back to `docops-mode` instead of absorbing the whole process.

## Example trigger scenarios
- "我要新建一个 feature 文档，你先帮我判断该走哪个模板。"
- "这个 API schema 文档要重构，帮我判断是微调还是结构性改写。"
- "我要补一个 issue 复盘，但不想自由发挥，你按模板路由来。"
- "先别写内容，先告诉我这次 dev_status 更新该用哪种结构。"
- "这个规则以后多个 app 都要复用，你判断该写 standards、ADR 还是 dictionary。"
