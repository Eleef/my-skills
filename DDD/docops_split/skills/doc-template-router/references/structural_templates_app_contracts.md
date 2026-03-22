# Structural Templates: App Contracts

Use these as fuller drafting skeletons when a structural edit targets app-owned contract authority docs. Pick one family only.

## DICTIONARY_API_SCHEMA
**Suggested path:** `docs/apps/<app>/dictionary/api_schema.md`

```markdown
---
kind: dictionary_api_schema
scope: app:<app>
lifecycle: stable
authority: app_contract
summary: API contract authority for <app>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# <app> API Schema (SSOT)

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
- Pagination:
- Rate limit:
- Idempotency:
```

## DICTIONARY_DATA_SCHEMA
**Suggested path:** `docs/apps/<app>/dictionary/data_schema.md`

```markdown
---
kind: dictionary_data_schema
scope: app:<app>
lifecycle: stable
authority: app_contract
summary: Data contract authority for <app>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# <app> Data Schema (SSOT)

## Table: <table_name>
### Purpose
- ...

### Columns
| column | type | nullable | index | description |
|---|---|---:|---:|---|

### Constraints
- Unique:
- FK:
- Check:

### Indexes
- ...

### Migrations
- files:
- rollback notes:
```

## DICTIONARY_UI_SCHEMA
**Suggested path:** `docs/apps/<app>/dictionary/ui_schema.md`

```markdown
---
kind: dictionary_ui_schema
scope: app:<app>
lifecycle: stable
authority: app_contract
summary: UI contract authority for <app>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# <app> UI Schema (SSOT)

## 1. Routes
| route | page | auth | description |
|---|---|---|---|

## 2. State Machines
- <page_or_flow>: Idle -> Loading -> Loaded -> Error

## 3. Tracking Events
| event | trigger | payload |
|---|---|---|

## 4. Error Mapping
| api_error | ui_message | action |
|---|---|---|

## 5. Notes
- Links to related feature specs:
- Links to API/data contracts:
```
