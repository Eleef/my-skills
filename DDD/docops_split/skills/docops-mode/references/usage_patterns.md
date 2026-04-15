---
name: docops-usage-patterns
description: Low-frequency heuristics and trigger examples for deciding when to use docops-mode.
---

## Practical heuristics
- Prefer the minimum doc surface needed for the task.
- Keep process visible, but keep output lean.
- Treat DocOps as a workflow harness, not a reason to over-document.
- If the task is a tiny one-section update, skip heavy workflow and do the minimal compliant edit.
- If the user's main need is template choice, structural routing, or checklist-based drafting, hand off to `doc-template-router` early instead of duplicating its job.

## Example trigger scenarios
- "帮我梳理这个仓库的 docs 结构，然后给我一个落地改造方案。"
- "把这个功能的文档、dev_status、history 一起理顺。"
- "这个排障过程需要补到 docs 里，你按规范带我走完整流程。"
- "我不确定这块应该写到 platform 还是 app 文档，你来判断并落地。"
- "这个需求已经有 spec 了，我现在要开始改代码，你先帮我做实现前桥接和验证计划。"
