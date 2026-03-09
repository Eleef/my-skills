# 结构化模板：状态与记录 (Structural Templates: Status and Records)

当结构化编辑的目标是开发状态文档或持久的决策/事件记录时，使用这些更完整的草案骨架。仅选择其中一个家族。

## DEV_STATUS_*
**建议路径：** `docs/dev_status/active_task.md`, `docs/dev_status/todo.md`, `docs/dev_status/history_log.md`

```markdown
# 活动任务上下文 (Active Task Context)
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

## <轨迹 (TRACK)>
### 当前目标
- ...

### 当前焦点
- [ ] ...

### 后续行动
1. ...
2. ...
```

```markdown
# 待办事项 / 积压工作 (Todo / Backlog)
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

> 最新项在前。

- [YYYY-MM-DD] **<轨迹> / <区域>** <简短项> - <链接或笔记>
```

```markdown
# 历史记录 (History Log)
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

> 最新条目在前。每个条目为单一轨迹。

## [YYYY-MM-DD] **<轨迹>** <目标摘要>
- 已交付或已变更内容：
- 已变更文档：
- 验证情况：
- 后续跟进：
```

## 问题 (ISSUE)
**建议路径：** `docs/issues/YYYY-MM-DD-<问题名称>.md`

```markdown
# 问题：<简短标题>
> 日期：[YYYY-MM-DD] ([时区])
> 严重程度：P0 / P1 / P2

## 环境 (Environment)
- 版本/分支：
- 环境变量（已脱敏）：
- 步骤上下文：

## 症状 vs 预期 (Symptom vs Expected)
- 症状：
- 预期：

## 复现步骤
1. ...
2. ...

## 根本原因分析 (Root Cause Analysis)
- 发生原因：
- 促成因素：

## 解决方案
- 已做的变更：
- 已更新的文档：

## 验证 (Verification)
- 命令：
- 状态：VERIFIED / BROKEN / UNVERIFIED

## 回滚 (Rollback)
- ...
```

## ADR_*
**建议路径：** `docs/adr/ADR-<范围>-###-标题.md`

```markdown
# ADR：<标题>
> 日期：[YYYY-MM-DD] ([时区])
> 状态：草稿 / 已接受 / 已废弃 (Draft / Accepted / Deprecated)
> 范围：PLATFORM / <APP>

## 上下文 (Context)
- 正在解决什么问题？
- 约束：
- 考虑过的选项：

## 决策 (Decision)
- 我们决定...

## 后果 (Consequences)
- 正面影响：
- 负面影响：
- 后续跟进：

## 参考资料
- 相关文档：
- 相关问题：
- 相关代码区域：
```
