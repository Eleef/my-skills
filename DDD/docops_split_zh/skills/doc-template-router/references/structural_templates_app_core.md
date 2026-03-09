# 结构化模板：应用概览与功能 (Structural Templates: App Overview and Features)

当结构化编辑的目标是应用级概览或功能叙事文档时，使用这些更完整的草案骨架。仅选择其中一个家族。

## APP_README
**建议路径：** `docs/apps/<app>/00_readme.md`

```markdown
# 应用：<app>
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

## 1. 这是一个什么应用？
- 目标用户：
- 核心流程：
- 超出范围：

## 2. 快速链接
### 词典 (Dictionary)
- `dictionary/api_schema.md`
- `dictionary/data_schema.md`
- `dictionary/ui_schema.md`

### 功能 (Features)
- `features/<feature>.md`

### 指南 (Guides)
- `guides/local_setup.md`
- `guides/troubleshooting.md`

## 3. 领域术语 (Domain Terms)
- 术语：
- 术语：

## 4. 高层流程
- 入口点：
- 主要交互：
- 外部依赖：

## 5. 当前状态
- 已上线：
- 进行中：
- 风险：
```

## FEATURE_SPEC
**建议路径：** `docs/apps/<app>/features/<feature>.md`

```markdown
# 功能：<feature>
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])
> 状态：草稿 / 活跃 / 稳定 (Draft / Active / Stable)

## 1. 目标与非目标
- 目标：
- 非目标：

## 2. 用户故事与价值
- 作为一名 ...
- 我想要 ...
- 以便 ...

## 3. 范围
- 范围内：
- 范围外：

## 4. UX / UI 行为
- 入口：
- 加载中：
- 空状态：
- 错误：
- 权限：

## 5. 端到端流程
1. ...
2. ...
3. ...

## 6. 契约引用 (Contract References)
- API：`../dictionary/api_schema.md#...`
- 数据：`../dictionary/data_schema.md#...`
- UI：`../dictionary/ui_schema.md#...`（如果有）

## 7. 验收标准 (Acceptance Criteria)
- [ ] ...
- [ ] ...
- [ ] ...

## 8. 实现影响 (Implementation Impact)
- 预期变更的代码区域：
- 预期更新的文档：
- 约束此工作的标准或 ADR：

## 9. 验证计划 (Verification Plan)
- 命令：
- 冒烟测试：
- 预期结果：

## 10. 发布 / 回滚 (Rollout / Rollback)
- 发布说明：
- 回滚说明：
```
