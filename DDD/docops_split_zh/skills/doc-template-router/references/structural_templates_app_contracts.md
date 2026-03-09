# 结构化模板：应用契约 (Structural Templates: App Contracts)

当结构化编辑的目标是应用拥有的契约权威文档时，使用这些更完整的草案骨架。仅选择其中一个家族。

## DICTIONARY_API_SCHEMA
**建议路径：** `docs/apps/<app>/dictionary/api_schema.md`

```markdown
# <app> API Schema (SSOT)
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

## <方法> <路径> - <简称>
### 目的
- ...

### 认证 (Auth)
- 必需：
- 角色/范围：

### 请求
#### 查询参数 (Query)
| 名称 | 类型 | 必填 | 描述 |
|---|---|---:|---|

#### 请求体 (Body)
| 字段 | 类型 | 必填 | 描述 |
|---|---|---:|---|

### 响应
#### 200
| 字段 | 类型 | 描述 |
|---|---|---|

### 错误 (Errors)
- 400：
- 401：
- 403：
- 500：

### 注意事项
- 分页：
- 速率限制：
- 幂等性：
```

## DICTIONARY_DATA_SCHEMA
**建议路径：** `docs/apps/<app>/dictionary/data_schema.md`

```markdown
# <app> 数据 Schema (SSOT)
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

## 表：<表名>
### 目的
- ...

### 列 (Columns)
| 列名 | 类型 | 可为空 | 索引 | 描述 |
|---|---|---:|---:|---|

### 约束 (Constraints)
- 唯一性：
- 外键 (FK)：
- 检查 (Check)：

### 索引 (Indexes)
- ...

### 迁移 (Migrations)
- 文件：
- 回滚说明：
```

## DICTIONARY_UI_SCHEMA
**建议路径：** `docs/apps/<app>/dictionary/ui_schema.md`

```markdown
# <app> UI Schema (SSOT)
> 最后更新：[YYYY-MM-DD HH:MM] ([时区])

## 1. 路由
| 路由 | 页面 | 认证 | 描述 |
|---|---|---|---|

## 2. 状态机
- <页面或流程>：Idle -> Loading -> Loaded -> Error

## 3. 埋点事件 (Tracking Events)
| 事件 | 触发器 | 负载 (Payload) |
|---|---|---|

## 4. 错误映射
| API 错误 | UI 消息 | 操作 |
|---|---|---|

## 5. 注意事项
- 链接到相关功能规范：
- 链接到 API/数据契约：
```
