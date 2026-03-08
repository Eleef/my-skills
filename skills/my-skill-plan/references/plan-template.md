# 计划模板（Plan Template）

在需要输出可执行实施计划时，可参考以下骨架并按需裁剪。

## 适用场景
- 需求已清晰，需要拆解实施步骤
- 涉及多文件改动、测试策略或迁移安排
- 需要把方案沉淀到 `spec/features/<feature-key>/05_plan.md`

## 推荐结构
```md
# [Feature Name] Implementation Plan
> Status: Draft | Date: YYYY-MM-DD

## 1. 背景与目标
- Why
- What
- 不做什么（Out of Scope）

## 2. 变更范围
### 2.1 文档变更
- `docs/...`：...

### 2.2 代码变更
- `src/...`：...
- `tests/...`：...

## 3. 实施步骤
1. ...
2. ...
3. ...

## 4. 验证方式
- 命令：`...`
- 预期：...
- 状态：UNVERIFIED | BROKEN | VERIFIED

## 5. 风险与回滚
- 风险：...
- 兼容性：...
- 回滚方式：...
```

## 使用提示
- 小任务不必强行写完整计划文档。
- 若更偏设计而不是实施步骤，改用 `04_design.md` 并参考 `design-doc-template.md`。
