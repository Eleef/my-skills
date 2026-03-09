# 结构化模板：平台与索引 (Structural Templates: Platform and Index)

当结构化编辑的目标是项目入口文档或共享平台文档时，使用这些更完整的草案骨架。仅选择其中一个家族。

## PROJECT_INDEX
**建议路径：** `docs/00_project_index.md`

```markdown
# [项目名称] 上下文地图 (Context Map)
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

## 1. 项目概览
- 此仓库的用途
- 服务对象
- 文档集的涵盖范围

## 2. 架构一览
- 文档模型：
- 应用/平台拆分：
- SSOT 所在地：

## 3. 文档导航
### 平台 (Platform)
- 前端：
- 后端：
- 运维 (Ops)：
- 标准 (Standards)：

### 应用 (Apps)
- <app>：

### 架构决策记录 (ADR)
- `docs/adr/`

### 开发状态 (Dev Status)
- `docs/dev_status/active_task.md`
- `docs/dev_status/todo.md`
- `docs/dev_status/history_log.md`

### 问题记录 (Issues)
- `docs/issues/`

## 4. 关键环境变量
| 变量名 | 必填 | 描述 | 示例 |
|---|---|---|---|

## 5. 新文档存放位置
- 平台共享指南：
- 应用特定行为：
- 架构决策：
- 排障或事件复盘：
- 实时迭代上下文：
```

## PLATFORM_*
**建议路径：** `docs/platform/<区域>/README.md` 或 `docs/platform/<组件>/specs/<主题>.md`

```markdown
# 平台：<区域或组件>
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

## 1. 目的
- 此文档涵盖了哪些共享能力
- 为什么它属于平台层

## 2. 范围
- 适用于：
- 不适用于：

## 3. 结构
- 共享架构或行为：
- 关键模块或界面：
- 约束或假设：

## 4. 规则或契约
- 如果这是指南：共享规则
- 如果这是规范 (Spec)：权威契约和稳定标题

## 5. 运维与验证
- 如何使用或验证它
- 命令、冒烟测试或评审检查

## 6. 参考资料
- 相关标准：
- 相关 ADR：
- 相关应用文档：
```

## PLATFORM_STANDARDS
**建议路径：** `docs/platform/standards/<主题>.md`

```markdown
# 标准：<主题>
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])
> 状态：草稿 / 活跃 / 稳定 (Draft / Active / Stable)

## 1. 目的
- 此标准解决什么问题
- 为什么它应该跨应用或团队共享

## 2. 范围
- 适用于：
- 不适用于：

## 3. 规则
- 规则 1：
- 规则 2：
- 规则 3：

## 4. 要求的实现预期
- 代码或文档必须如何操作以符合规范
- 采用此标准时预期会发生变更的产物

## 5. 验证
- 如何验证合规性
- 冒烟测试 / 评审检查 / 命令

## 6. 示例
- 正确示例：
- 错误示例：

## 7. 参考资料
- 相关 ADR：
- 相关词典/规范文档：
- 相关应用文档：
```
