# Structural Templates: Platform and Index

Use these as fuller drafting skeletons when a structural edit targets project entry docs, shared platform docs, or platform-owned contract docs. Pick one family only.

## PROJECT_INDEX
**Suggested path:** `docs/00_project_index.md`

```markdown
---
kind: project_index
scope: repo
lifecycle: active
authority: published_reference
summary: Repository context map and docs navigation.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# [Project Name] Context Map

## 1. Project Overview
- What this repository is for
- Who it serves
- What belongs in this docs set

## 2. Architecture at a Glance
- Docs model:
- App/platform split:
- Where SSOT lives:

## 3. Documentation Navigation
### Platform
- Frontend:
- Backend:
- Ops:
- Standards:

### Apps
- <app>:

### ADR
- `docs/adr/`

### Dev Status
- `docs/dev_status/active_task.md`
- `docs/dev_status/todo.md`
- `docs/dev_status/history_log.md`

### Issues
- `docs/issues/`

## 4. Key Environment Variables
| Variable | Required | Description | Example |
|---|---|---|---|

## 5. Where to Put New Docs
- Platform shared guidance:
- App-specific behavior:
- Architecture decisions:
- Troubleshooting or incident reviews:
- Live iteration context:
```

## PLATFORM_DOC
**Suggested paths:** `docs/platform/<area>/README.md` or `docs/platform/<area>/<topic>.md`

```markdown
---
kind: platform_doc
scope: platform:<area_or_component>
lifecycle: draft
authority: published_reference
summary: Shared platform guidance or overview for <area_or_component>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# Platform: <area_or_component>

## 1. Purpose
- What shared capability this doc covers
- Why it belongs at the platform layer

## 2. Scope
- Applies to:
- Does not apply to:

## 3. Structure
- Shared architecture or behavior:
- Key modules or surfaces:
- Constraints or assumptions:

## 4. Rules or Contract
- Shared rules, architecture notes, or reusable operating guidance
- Stable terminology and links to any contract docs that this guidance depends on

## 5. Operations and Verification
- How to use or verify it
- Commands, smoke checks, or review checks

## 6. References
- Related standards:
- Related ADRs:
- Related app docs:
```

## PLATFORM_API_SCHEMA
**Suggested path:** `docs/platform/<component>/specs/api_schema.md`

```markdown
---
kind: platform_api_schema
scope: platform:<component>
lifecycle: stable
authority: platform_contract
summary: Platform API contract authority for <component>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# Platform API Schema: <component>

## <METHOD> <PATH> - <short name>
### Purpose
- ...

### Auth
- Required:
- Roles/Scopes:

### Request
#### Query
| name | type | required | description |
|---|---|---:|---|

#### Body
| field | type | required | description |
|---|---|---:|---|

### Response
#### 200
| field | type | description |
|---|---|---|

### Errors
- 400:
- 401:
- 403:
- 500:

### Notes
- Consumers:
- Versioning:
- Backward compatibility:
```

## PLATFORM_DATA_SCHEMA
**Suggested path:** `docs/platform/<component>/specs/data_schema.md`

```markdown
---
kind: platform_data_schema
scope: platform:<component>
lifecycle: stable
authority: platform_contract
summary: Platform data contract authority for <component>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# Platform Data Schema: <component>

## Entity: <entity_name>
### Purpose
- ...

### Fields
| field | type | nullable | description |
|---|---|---:|---|

### Constraints
- Unique:
- FK:
- Check:

### Indexes
- ...

### Notes
- Upstream producers:
- Downstream consumers:
- Migration or rollback notes:
```

## PLATFORM_UI_SCHEMA
**Suggested path:** `docs/platform/<component>/specs/ui_schema.md`

```markdown
---
kind: platform_ui_schema
scope: platform:<component>
lifecycle: stable
authority: platform_contract
summary: Platform UI or interaction contract authority for <component>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# Platform UI Schema: <component>

## 1. Routes or Surfaces
| surface | auth | description |
|---|---|---|

## 2. States
- <surface_or_flow>: Idle -> Loading -> Loaded -> Error

## 3. Events
| event | trigger | payload |
|---|---|---|

## 4. Error Mapping
| source_error | ui_message | action |
|---|---|---|

## 5. Notes
- Consuming apps:
- Stability expectations:
- Related platform docs:
```

## PLATFORM_STANDARDS
**Suggested path:** `docs/platform/standards/<topic>.md`

```markdown
---
kind: platform_standard
scope: platform:<topic_area>
lifecycle: draft
authority: published_reference
summary: Shared engineering standard for <topic>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# Standard: <topic>

## 1. Purpose
- What problem this standard solves
- Why it should be shared across apps or teams

## 2. Scope
- Applies to:
- Does not apply to:

## 3. Rules
- Rule 1:
- Rule 2:
- Rule 3:

## 4. Required Implementation Expectations
- What code or docs must do to comply
- Which artifacts are expected to change when adopting this standard

## 5. Verification
- How to verify compliance
- Smoke checks / review checks / commands

## 6. Examples
- Good example:
- Bad example:

## 7. References
- Related ADRs:
- Related dictionary/spec docs:
- Related app docs:
```
