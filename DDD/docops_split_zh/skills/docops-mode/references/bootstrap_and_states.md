# DocOps 引导与状态 (Bootstrap and States)

## 精简引导顺序 (Compact bootstrap order)
1. `docs/00_project_index.md`
2. `docs/dev_status/active_task.md`
3. 涉及应用时，读取 `docs/apps/<app>/00_readme.md`
4. 涉及契约或 Schema 时，读取 `docs/apps/<app>/dictionary/*.md`
5. 涉及部署/运维/路由时，先读取 `docs/apps/<app>/ops/**`，然后是 `docs/platform/ops/**`

如果任何关键文件不可用，切换到降级模式并明确指出缺失的内容。

## 工作状态 (Working states)
### PLANNING (规划中)
在用户目标、范围或验收标准不明确时使用。
- 提出一组集中的澄清问题。
- 仅提供标注有假设的草案。

### DESIGN (设计中)
在对比结构、契约、风险或文档存放位置时使用。
- 使权衡过程显性化。
- 保持应用/平台边界清晰。

### IMPLEMENTING (实施中)
在编辑文档或代码时使用。
- 保持变更与相关文档的原子性。
- 避免在词典 (dictionary) 文件之外出现重复的 Schema 内容。

### VERIFYING (验证中)
在运行命令或尝试验证时使用。
- 标注为 `VERIFIED`、`BROKEN` 或 `UNVERIFIED`。
- 包含命令和简短的结果摘要。

### DONE (完成)
在任务结束并确认后使用。
- 如果适用，更新相关的开发状态文件。
- 为下一次会话留下简洁的痕迹。
