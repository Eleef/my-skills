# Documentation Templates Library (v2: Platform + Apps + SSOT)

> Last Updated: 2026-01-07 16:00 (America/Los_Angeles)

此文件包含两类内容：

1. RULES（规则/约束）：只在你需要“校验文档质量/规范”时读取
2. TEMPLATES（模板正文）：只在“新建文档 / 结构性改写”时读取

为降低 Token 与注意力成本，本文件提供“按需加载策略（Loader Policy）”与“路由表（Routing Table）”，确保 Agent **只加载必要片段**。

---

## 0) Loader Policy（强制：如何读取本文件）

### 0.1 禁止整文件导入

当需要参考模板时，**禁止**一次性导入整个 templates.md。 必须遵循：

1. 先读本文件的 **Routing Table（第 1 节）**
2. 判断任务属于哪类模板
3. 只加载对应的一个模板块（通过 `<!-- TEMPLATE:XXX:BEGIN -->` 定位）
4. 微改动优先只看 **Checklist（第 2 节）**，不要读模板正文

### 0.2 Micro-edit vs Structural-edit 判定（D 方案轻约束）

**Micro-edit（微改动）**：满足任一条件 → 不读模板正文，仅用 Checklist 校验

* 只改 1 个小节或 ≤ 30 行
* 不新增文档、不重排章节层级、不大幅改结构
* 不涉及 dictionary（契约/字段/表结构）的大改

**Structural-edit（结构性改写）**：满足任一条件 → 读 1 个模板块（仅一个）

* 新建文档
* 新增多个章节 / 重排结构
* 把多个来源内容合并成新结构
* dictionary 需要系统性调整（如新加大量 endpoint/table、改锚点规范）

> 备注：RULES（第 3 节）仅在需要校验规范、或涉及 SSOT/dictionary 时读取。

---

## 1) Routing Table（关键词路由：读哪个模板块）

### 1.1 常见任务 → 模板块

* 改项目全局入口/导航：`TEMPLATE:PROJECT_INDEX`
* 改 Platform 通用文档（frontend/backend/ops）：`TEMPLATE:PLATFORM_*`
* 改某 App 总览入口：`TEMPLATE:APP_README`
* 改 Feature（需求/流程/UI状态/验收）：`TEMPLATE:FEATURE_SPEC`
* 改 API 契约（endpoint/字段/错误码/行为）：`TEMPLATE:DICTIONARY_API_SCHEMA`
* 改 Data/DB 契约（表结构/约束/迁移说明）：`TEMPLATE:DICTIONARY_DATA_SCHEMA`
* 改 UI 契约（路由/状态机/埋点字典/错误映射）：`TEMPLATE:DICTIONARY_UI_SCHEMA`
* 更新 dev_status（active_task/todo/history）：`TEMPLATE:DEV_STATUS_*`
* 新建/复盘 bug：`TEMPLATE:ISSUE`
* 记录架构决策：`TEMPLATE:ADR_*`

### 1.2 Micro-edit 默认策略

* 微改 Feature：只用 `CHECKLIST:FEATURE`
* 微改 Dictionary：只用 `CHECKLIST:DICTIONARY`
* 微改 Issue：只用 `CHECKLIST:ISSUE`
* 微改 dev_status：只用 `CHECKLIST:DEV_STATUS`

---

## 2) CHECKLISTS（微改动默认只读这里）

### CHECKLIST:FEATURE（Feature 文档微改动校验）

- [ ] 文档头部包含 `> Last Updated: YYYY-MM-DD HH:MM (TZ)`（本次修改后需更新）
- [ ] “故事/流程”描述不复制 SSOT 字段表（如需示例仅 3–8 字段，并注明“示例非权威，以 dictionary 为准”）
- [ ] 引用 API/Table 时使用稳定锚点（Endpoint: `## <METHOD> <PATH> - ...`；Table: `## 表: upwork.<table>`）
- [ ] 变更包含：目的/范围、关键流程、验收点（至少 3 条）、风险/回滚（如涉及行为变化）
- [ ] 相关文档链接（dictionary / guides / adr / ops）可点击且不失效

### CHECKLIST:DICTIONARY（Dictionary 微改动校验）

- [ ] 文档头部包含 `> Last Updated: YYYY-MM-DD HH:MM (TZ)`（本次修改后需更新）
- [ ] 该文件是 SSOT：不要在 features/ops 里维护第二份字段/契约（features 只引用）
- [ ] Endpoint 标题遵循：`## <METHOD> <PATH> - <short name>`（保证锚点稳定）
- [ ] 表标题遵循：`## 表: <schema>.<table_name>`（保证锚点稳定）
- [ ] 字段/类型/可选性/默认值/错误码与实际实现一致（必要时附验证命令或代码位置）
- [ ] 如有 breaking change：在字典内标注影响面，并在相关 feature/ops 中同步更新

### CHECKLIST:ISSUE（Issue 微改动校验）

- [ ] 文档头部包含 `> Last Updated: YYYY-MM-DD HH:MM (TZ)`（本次修改后需更新）
- [ ] 包含：现象、影响范围、复现步骤（最小）、期望/实际、根因、修复、验证、回滚方案
- [ ] 日志/截图/数据已脱敏（token/密码/生产数据必须打码或用占位符）
- [ ] 如涉及契约变化：链接到 dictionary 的具体段落（而不是复制字段表）

### CHECKLIST:DEV_STATUS（状态文档微改动校验）

- [ ] `todo.md` / `history_log.md` 使用倒序（最新在最上）
- [ ] `active_task.md` 只保留当前上下文：Objective / Current Focus / Next Actions
- [ ] 记录条目包含日期时间与可追溯线索（相关 PR/commit/文档路径/命令）

---

## 3) RULES & CONSTRAINTS（规则与约束：按需读取）

### 3.1 v2 信息架构（权威目录树）

```text
docs/
├── 00_project_index.md                 # 全局入口：项目地图/导航
├── _meta/
│   └── templates.md                    # 模板库 + 规则 + 路由（按块加载）
├── platform/                           # 平台通用能力（跨 App 复用）
│   ├── frontend/                       # 通用前端架构/UI Kit/状态管理
│   ├── backend/                        # 通用后端架构/Auth/DB 规范
│   ├── ops/                            # 运维/部署/环境/可观测性
│   └── standards/                      # （可选）统一规范集中区
├── apps/                               # 业务应用（按 App 隔离）
│   └── <app>/
│       ├── 00_readme.md                # App 全景图入口（导航 + 领域说明）
│       ├── dictionary/                 # SSOT：契约/字典（唯一真相）
│       │   ├── api_schema.md           # API 契约（endpoint/字段/错误码/行为）
│       │   ├── data_schema.md          # 数据/DB 契约（表结构/约束/索引/迁移说明）
│       │   └── ui_schema.md            # （可选）前端契约（路由/状态机/埋点/错误映射）
│       ├── features/                   # Story：一个功能一篇（端到端，但不复制 schema）
│       ├── guides/                     # How-to：怎么跑/怎么验收/怎么排障
│       └── adr/                        # App 级架构决策
├── adr/                                # Platform 级架构决策
├── dev_status/                         # 工作状态：active_task/todo/history
└── issues/                             # 复杂问题复盘/根因/验证记录
```

### 3.2 时间戳格式（强制）

所有文档头部更新时间统一使用：

* `> Last Updated: YYYY-MM-DD HH:MM (TZ)`
* 示例：`> Last Updated: 2026-01-07 16:00 (America/Los_Angeles)`

### 3.3 文件名规范（建议强制）

* 统一使用 `snake_case.md`
* 除 ADR 外不使用编号前缀（避免频繁重排）
* 文件名表达语义：✅ `job_search.md` ❌ `001_job_search.md`

### 3.4 倒序规则（强制）

* `docs/dev_status/todo.md`：倒序（最新在最上）
* `docs/dev_status/history_log.md`：倒序（最新在文件顶部）

### 3.5 Doc Ownership（建议）

* `docs/platform/**`：平台通用能力负责人
* `docs/apps/<app>/**`：该 App Owner
* `docs/adr/**`：Platform 架构师
* `docs/apps/<app>/adr/**`：App 架构师
* `docs/dev_status/**`：当前执行者
* `docs/issues/**`：问题负责人

### 3.6 SSOT（强制禁令）

* 字段/契约/Schema/表结构/API 行为的**权威定义**只能在（按归属选择其一）：

  * **App 级契约（业务域）**：`apps/<app>/dictionary/**`
  * **Platform 级契约（共享能力）**：`platform/<component>/specs/**`（例如 `platform/agent/specs/`）
* `apps/<app>/features/**` **不得**复制字段表、不得维护第二份 schema
* Feature 可以给“最小示例”（3~8 字段）但必须标注：

  * “示例非权威，以 dictionary 为准”

### 3.7 Dictionary 命名（推荐最小集合）

* `dictionary/api_schema.md`：API 契约（SSOT）
* `dictionary/data_schema.md`：Data/DB 契约（SSOT）
* `dictionary/ui_schema.md`：前端契约（可选：路由/状态机/埋点字典/错误映射）

> 不要用 `backend_*.md` / `db_*.md` 这类重复表达。

### 3.8 Dictionary 体积控制（只在变大时使用）

默认一个文件够用；触发任一条件时允许拆分：

* `api_schema.md` > 25 endpoints 或 > 800 行 → 拆为 `api_<domain>_schema.md`
* `data_schema.md` > 20 tables → 拆为 `data_<domain>_schema.md` 拆分后仍遵守 SSOT：features 只引用，不复制字段细节。

### 3.9 锚点稳定性（强烈建议）

* Endpoint 标题统一：`## <METHOD> <PATH> - <short name>`
* Table 标题统一：`## Table: <table_name>`
* Feature 引用统一用这些标题锚点，避免断链

---

## 4) TEMPLATES（结构性改写才读；且只读一个块）

### Project Index（项目地图）

**文件路径**：`docs/00_project_index.md`
**用途**：全局入口，Agent 启动时必读。

```markdown
# [Project Name] Context Map
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## 1. Project Overview
> 一句话描述项目目标、用户与核心价值。

## 2. Architecture at a Glance
- Docs Model: Platform + Apps
- SSOT: 每个 App 的契约只在 apps/<app>/dictionary
- Feature Docs: apps/<app>/features 讲端到端 story，但不复制字段细节

## 3. Documentation Navigation

### 🧱 Platform (Shared)
- Frontend: [platform/frontend/README.md](platform/frontend/README.md)
- Backend: [platform/backend/README.md](platform/backend/README.md)
- Ops: [platform/ops/README.md](platform/ops/README.md)
- Standards (optional): [platform/standards/README.md](platform/standards/README.md)

### 🚀 Apps
- <app>: [apps/<app>/00_readme.md](apps/<app>/00_readme.md)

### 🏛️ ADR
- [adr/README.md](adr/README.md)

### 🚦 Dev Status
- [dev_status/active_task.md](dev_status/active_task.md)
- [dev_status/todo.md](dev_status/todo.md)
- [dev_status/history_log.md](dev_status/history_log.md)

### 🐛 Issues
- [issues/](issues/)

## 4. Key Environment Variables（禁止真密钥）
| Variable | Required | Description | Example |
|---|---|---|---|
| `ENV_TYPE` | Yes | dev/prod | `dev` |
| `BASE_URL` | Yes | API base | `http://localhost:8000` |

## 5. “Where to Put New Docs”
- 平台通用 → platform/**
- 某 App 独有 → apps/<app>/**
- 影响架构的决策 → adr/**
- 复杂 bug 复盘 → issues/**
- 会话上下文 → dev_status/**
```

### Platform README（总入口，可选但强烈建议）

**文件路径**：`docs/platform/README.md`

```markdown
# Platform Docs
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## What belongs here?
- 跨 App 复用的架构、规范、运维与通用组件

## Navigation
- Frontend: ./frontend/README.md
- Backend: ./backend/README.md
- Ops: ./ops/README.md
- Standards (optional): ./standards/README.md
```

### Platform Frontend README

**文件路径**：`docs/platform/frontend/README.md`

```markdown
# Platform Frontend
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## Scope
- 通用 AppShell / UI Kit / 状态管理封装 / 前端目录规范

## Architecture
- Routing / Layout / Data Fetching
- Shared components policy

## UI Kit Rules
- 组件使用规范
- 表格/分页/空状态/错误态统一策略

## State Management Rules
- 缓存策略、请求封装、错误处理
```

### Platform Backend README

**文件路径**：`docs/platform/backend/README.md`

```markdown
# Platform Backend
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## Scope
- 通用 Auth / DB 规范 / 服务分层 / 错误码与日志规范

## Architecture
- Modules / Services / Repos 结构
- Dependency Injection / Config pattern

## Database Rules
- 迁移策略
- 索引/约束规范
- 事务边界建议
```

### Platform Ops README

**文件路径**：`docs/platform/ops/README.md`

```markdown
# Platform Ops
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## Dev Setup
- 环境搭建
- 常用命令
- 本地依赖服务

## Deployment
- 部署流程
- 环境变量
- 回滚策略

## Observability
- 日志/指标/告警规范
```

### App Readme（业务全景图）

**文件路径**：`docs/apps/<app>/00_readme.md`

````markdown
# App: <app>
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## 1. What is this App?
- 目标用户：
- 核心闭环：
- 不做什么（Out of scope）：

## 2. Quick Links
### Dictionary (SSOT)
- [dictionary/api_schema.md](dictionary/api_schema.md)
- [dictionary/data_schema.md](dictionary/data_schema.md)
- [dictionary/ui_schema.md](dictionary/ui_schema.md) (optional)

### Features (Story)
- [features/<feature>.md](features/<feature>.md)

### Guides (How-to)
- [guides/local_setup.md](guides/local_setup.md)
- [guides/troubleshooting.md](guides/troubleshooting.md)

## 3. Domain Terms（可选）
- Term A:
- Term B:

## 4. High-Level Flow（可选）
```mermaid
graph LR
  UI --> API --> DB
````

## 5. Current Status（可选）

* 已上线：
* 进行中：
* 风险点：

````
<!-- TEMPLATE:APP_README:END -->

<!-- TEMPLATE:DICTIONARY_API_SCHEMA:BEGIN -->
### API Schema（SSOT）
**文件路径**：`docs/apps/<app>/dictionary/api_schema.md`

```markdown
# <app> API Schema (SSOT)
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## Conventions
- Endpoint 标题：`## <METHOD> <PATH> - <short name>`
- 每个 Endpoint 必须包含：Purpose / Auth / Request / Response / Errors / Notes / Examples

---

## GET /api/v1/... - <short name>

### Purpose
- 这个接口解决什么问题？

### Auth
- Required: Yes/No
- Roles/Scopes: ...

### Request
#### Query
| name | type | required | description |
|---|---|---:|---|
| `q` | string | No | ... |

#### Body（如有）
| field | type | required | description |
|---|---|---:|---|
| `filters` | object | No | ... |

### Response
#### 200
| field | type | description |
|---|---|---|
| `items` | Item[] | ... |

### Errors
- 400: ...
- 401: ...
- 403: ...
- 500: ...

### Notes
- Pagination:
- Sorting:
- Rate limit:
- Idempotency:

### Examples
```bash
curl -X GET "<BASE_URL>/api/v1/..."
````

````
<!-- TEMPLATE:DICTIONARY_API_SCHEMA:END -->

<!-- TEMPLATE:DICTIONARY_DATA_SCHEMA:BEGIN -->
### Data Schema（SSOT）
**文件路径**：`docs/apps/<app>/dictionary/data_schema.md`

```markdown
# <app> Data Schema (SSOT)
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## Conventions
- Table 标题：`## Table: <table_name>`
- 每张表必须包含：Purpose / Columns / Constraints / Indexes / Migrations / Notes

---

## Table: <table_name>

### Purpose
- 存什么？
- 谁写谁读？
- 生命周期？

### Columns
| column | type | nullable | index | description |
|---|---|---:|---:|---|
| `id` | uuid | No | PK | ... |

### Constraints
- Unique:
- FK:
- Check:

### Indexes
- idx_xxx: (columns...) purpose...

### Migrations
- migration files:
- rollback notes:

### Notes
- computed/derived fields:
- data retention:
````

### UI Schema（可选 SSOT）

**文件路径**：`docs/apps/<app>/dictionary/ui_schema.md`

```markdown
# <app> UI Schema (optional SSOT)
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## 1. Routes
| route | page | auth | description |
|---|---|---|---|
| `/jobs` | JobsList | Yes | ... |

## 2. Page State Machines（可选）
- JobsList: Idle → Loading → Loaded → Error → Empty

## 3. Tracking Events（可选）
| event | trigger | payload |
|---|---|---|
| `jobs_filter_changed` | user changes filter | `{ key, value }` |

## 4. Error Mapping（可选）
| api_error | ui_message | action |
|---|---|---|
| `401` | "Please login" | redirect |
```

### Feature Spec（Story：端到端功能文档）

**文件路径**：`docs/apps/<app>/features/<feature>.md`

```markdown
# Feature: <feature>
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])
> Status: Draft / Active / Stable

## 1. Goal & Non-Goal
- Goal:
- Non-Goal:

## 2. User Story & Value
- As a ...
- I want ...
- So that ...

## 3. UX / UI Behavior（写交互与状态，不写字段细节）
- Entry:
- Empty state:
- Loading state:
- Error state:
- Permissions:

## 4. End-to-End Flow（纵切流程）
1) ...
2) ...
3) ...

## 5. API Usage（只引用，不复制字段）
- Use: `GET /api/v1/...`
  - Spec: ../dictionary/api_schema.md#<anchor>
- Use: `POST /api/v1/...`
  - Spec: ...

## 6. Data Touch Points（只引用，不复制字段）
- Table: `<table_name>`
  - Schema: ../dictionary/data_schema.md#table-<table_name>

## 7. Acceptance Criteria（可测试）
- [ ] 条件 A → 结果 ...
- [ ] 条件 B → 结果 ...

## 8. Non-Functional Requirements
- 性能/响应时间：
- 并发/容量：
- 安全/权限：

## 9. Edge Cases
- 网络异常：
- 数据为空：
- 重复提交：

## 10. Observability & Rollout（可选）
- logs/metrics:
- feature flag:
- rollback:
```

### App Guide: Local Setup

**文件路径**：`docs/apps/<app>/guides/local_setup.md`

```markdown
# <app> Local Setup
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## 1. Prerequisites
- runtime versions:
- dependencies:

## 2. Env Vars（占位符，禁止真密钥）
| Variable | Required | Description | Example |
|---|---|---|---|
| `DB_URL` | Yes | ... | `postgres://<REDACTED>` |

## 3. Commands
- Start:
- Test:
- Lint:

## 4. Smoke Check
- URL:
- Expected:
```

### App Guide: Troubleshooting

**文件路径**：`docs/apps/<app>/guides/troubleshooting.md`

```markdown
# <app> Troubleshooting
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## Common Issues
### Symptom
### Root Cause
### Fix Steps
### How to Verify
- Command:
- Status: VERIFIED / BROKEN / UNVERIFIED
```

### Dev Status: Active Task

**文件路径**：`docs/dev_status/active_task.md`

```markdown
# Active Task Context (Live State)
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## 🎯 Current Objective
> 一句话描述当前正在解决的核心问题。

## 🧩 Context Dump
- Relevant files:
- Key vars/flags:
- External deps:
- Assumptions:

## 🧠 Decisions
- 1~3 条关键取舍

## 🚧 Progress Checklist
- [ ] ...  <-- Current Focus

## 💥 Known Issues / Blockers
- Error / StackTrace（记得打码敏感信息）
- Attempted fixes:

## ⏭️ Next Actions
1. ...
2. ...
```

### Dev Status: Todo

**文件路径**：`docs/dev_status/todo.md`

```markdown
# Todo / Backlog
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

> 规则：倒序，最新条目写在最上面

- [YYYY-MM-DD] (P?) 简短描述 + 相关链接（可选）
- ...
```

### Dev Status: History Log

**文件路径**：`docs/dev_status/history_log.md`

```markdown
# History Log
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

> 规则：倒序，最新记录写在最上面

## [YYYY-MM-DD] <Objective Summary>
- What shipped / done:
- Key decisions:
- Changed docs:
- Verification:
- Follow-ups:
```

### Issue / Bug Report

**文件路径**：`docs/issues/YYYY-MM-DD-issue_name.md`

```markdown
# Issue: [简短描述现象]
> Date: [YYYY-MM-DD] ([TZ])
> Severity: P0/P1/P2

## Environment
- version/branch:
- env vars (redacted):
- steps context:

## Symptom vs Expected
- Symptom:
- Expected:

## Reproduction Steps
1) ...
2) ...

## Root Cause Analysis
- why it happened:
- contributing factors:

## Resolution
- changes made:
- docs updated:

## Verification
- Command:
- Status: VERIFIED / BROKEN / UNVERIFIED
```

### ADR Index

**文件路径**：`docs/adr/README.md`

```markdown
# ADR Index
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## What is ADR?
ADR = Architecture Decision Record。记录重要技术决策：背景、选择、结论与后果。

## ADR List
| ID | Scope | Title | Status | Date |
|---|---|---|---|---|
| ADR-PLATFORM-001 | PLATFORM | ... | Accepted | 2026-01-07 |
| ADR-UPWORK-001 | UPWORK | ... | Draft | 2026-01-07 |
```

### ADR Template

**文件路径**：`docs/adr/ADR-<SCOPE>-###-title.md`

```markdown
# ADR: [Title]
> Date: [YYYY-MM-DD] ([TZ])
> Status: Draft / Accepted / Deprecated
> Scope: PLATFORM / <APP>

## Context
- 我们在解决什么问题？
- 约束条件是什么？
- 有哪些选项？

## Decision
- 我们决定……

## Consequences
- Positive:
- Negative:
- Follow-ups:

## References
- Related docs/issues/PRs:
```
