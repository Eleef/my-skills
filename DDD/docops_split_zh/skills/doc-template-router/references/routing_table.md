# 路由表 (Routing Table)

## 模板家族映射 (Template family map)
- 项目全局入口或导航变更 → `PROJECT_INDEX`
- 共享的平台文档或平台拥有的规范 → `PLATFORM_*`
- 平台可重用的约定、政策或工程规则 → `PLATFORM_STANDARDS`
- 应用概览 / 应用首页 → `APP_README`
- 功能描述 / 用户流程 / 验收标准 → `FEATURE_SPEC`
- API 契约 / Endpoint 行为 → `DICTIONARY_API_SCHEMA`
- 数据库 / 表 / 数据契约 → `DICTIONARY_DATA_SCHEMA`
- UI 路由 / 状态 / 埋点契约 → `DICTIONARY_UI_SCHEMA`
- 活动任务 / Todo / 历史更新 → `DEV_STATUS_*`
- 错误报告 / 事件记录 → `ISSUE`
- 架构决策 → `ADR_*`

## 何时选择标准 (Standards) 而非其他文档
- 当指南旨在供多个应用或功能复用时，使用 `PLATFORM_STANDARDS`。
- 当输出是位于 `docs/platform/<component>/specs/**` 下的平台拥有规范或契约时，使用 `PLATFORM_*`。
- 当主要输出是一个决策及其后果时，使用 `ADR_*`。
- 当输出是一个应用作用域的契约或 Schema 权威时，使用 `DICTIONARY_*`。
- 当输出是一个单一功能叙事和验收定义时，使用 `FEATURE_SPEC`。

## 微型编辑的默认路由 (Micro-edit default routing)
- 这些是最常见的微小编辑中由检查清单支持的默认路由。
- 小的功能补丁 → 检查清单 `FEATURE`
- 小的词典补丁 → 检查清单 `DICTIONARY`
- 小的问题更新 → 检查清单 `ISSUE`
- 小的开发状态更新 → 检查清单 `DEV_STATUS`
