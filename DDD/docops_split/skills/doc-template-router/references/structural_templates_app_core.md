# Structural Templates: App Overview and Features

Use these as fuller drafting skeletons when a structural edit targets app-level overview or feature story docs. Pick one family only.

## APP_README
**Suggested path:** `docs/apps/<app>/00_readme.md`

```markdown
---
kind: app_readme
scope: app:<app>
lifecycle: active
authority: published_reference
summary: Entry point and navigation for the <app> app docs.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# App: <app>

## 1. What Is This App?
- Target users:
- Core loop:
- Out of scope:

## 2. Quick Links
### Dictionary
- `dictionary/api_schema.md`
- `dictionary/data_schema.md`
- `dictionary/ui_schema.md`

### Features
- `features/<feature>.md`

### Guides
- `guides/local_setup.md`
- `guides/troubleshooting.md`

## 3. Domain Terms
- Term:
- Term:

## 4. High-Level Flow
- Entry points:
- Main interactions:
- External dependencies:

## 5. Current Status
- Live:
- In progress:
- Risks:
```

## FEATURE_SPEC
**Suggested path:** `docs/apps/<app>/features/<feature>.md`

```markdown
---
kind: feature_spec
scope: app:<app>
lifecycle: draft
authority: published_reference
summary: Feature specification for <feature>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---

# Feature: <feature>

## 1. Goal & Non-Goal
- Goal:
- Non-Goal:

## 2. User Story & Value
- As a ...
- I want ...
- So that ...

## 3. Scope
- In scope:
- Out of scope:

## 4. UX / UI Behavior
- Entry:
- Loading:
- Empty:
- Error:
- Permissions:

## 5. End-to-End Flow
1. ...
2. ...
3. ...

## 6. Contract References
- API: `../dictionary/api_schema.md#...`
- Data: `../dictionary/data_schema.md#...`
- UI: `../dictionary/ui_schema.md#...` (if any)

## 7. Acceptance Criteria
- [ ] ...
- [ ] ...
- [ ] ...

## 8. Implementation Impact
- Expected code areas:
- Expected docs to update:
- Standards or ADRs that constrain this work:

## 9. Verification Plan
- Commands:
- Smoke checks:
- Expected outcomes:

## 10. Rollout / Rollback
- Rollout notes:
- Rollback notes:
```
