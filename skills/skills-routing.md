## Skill 路由规则

在决定是否触发 `my-skill-specify`、`my-skill-plan` 或 `my-skill-docs` 时，按任务阶段路由，而不是按关键词路由。

- 当请求存在歧义、信息不完整、缺少范围/输入输出/验收标准，或存在多种合理解释时，使用 `my-skill-specify`。
- 当需求已基本清晰，但任务需要实现规划、方案权衡、多文件改动分析、接口/数据设计，或测试/回滚规划时，使用 `my-skill-plan`。
- 当已经有稳定结果或阶段产出，需要同步到项目文档、从 `spec/` 归档到 `docs/`、记录到状态/历史文件，或作为验收证据留痕时，使用 `my-skill-docs`。
- `my-skill-docs` 支持动作：过程中的状态同步，以及阶段稳定后的成果归档。前者可用于更新 active task、history、todo、blocker、next action；后者才涉及 `spec/` 到 `docs/` 的长期沉淀。
- 如果任务在 planning 或 documentation 过程中重新变得不清晰，切回 `my-skill-specify`。
- 如果任务在澄清后已经具备实施条件，从 `my-skill-specify` 切换到 `my-skill-plan`。
- 如果实现或验证完成后需要更新文档，从 `my-skill-plan` 切换到 `my-skill-docs`。
- 对于可以直接完成的单步小任务，不要触发这些 skills；这类任务无需澄清、规划或文档处理即可直接完成。
- 优先触发“最小且足够”的 skill；除非确实需要明确交接，否则不要同时触发多个 skill。
