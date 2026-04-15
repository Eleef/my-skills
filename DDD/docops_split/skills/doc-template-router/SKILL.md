---
name: doc-template-router
description: Route published repository documentation tasks to the right editing pattern and template shape. Use this whenever the user wants to create a doc, rewrite or restructure an existing published doc, choose between feature/app-contract/platform-contract/standards/dev-status/issue/ADR formats, decide whether an edit is micro or structural, or apply checklist-based documentation quality control instead of freeform writing. Prefer this skill whenever the task is mainly about selecting the correct published doc format, platform-contract-vs-standard-vs-ADR-vs-dictionary placement, template family, or edit path before drafting. Do not use this as a substitute for repo-wide DocOps workflow or `dev_status` coordination across a larger task.
---

# Doc Template Router

Use this skill when the task is about selecting the right documentation pattern rather than running the full DocOps workflow.

## Goal
Turn a document request into the smallest correct editing path:
- micro-edit with checklist only
- structural edit with a single template family

This skill is the template-routing layer. It should stay separate from always-on rules.

## Decision flow

### 1. Inspect metadata first
If the target doc already exists and is a managed markdown file:
- read YAML front matter before reading body content
- use `kind`, `scope`, `lifecycle`, `authority`, and `summary` to confirm the route
- if front matter is missing, treat it as metadata debt and infer the route carefully from path plus headings

### 2. Determine edit size
Classify in this order.

Treat the request as a **structural edit** first if any of these are true:
- a new document is being created
- multiple sections are added or reorganized
- several sources are being merged into a new structure
- dictionary or contract content needs broad rework

For structural edits:
- choose one template family only
- do not mix multiple top-level template structures unless the user explicitly asks

If no structural condition matched, treat the request as a **micro-edit** only when all of these are true:
- only one small section changes
- total change is roughly within 30 lines
- the existing document remains in place
- no major section reordering is needed
- no systematic dictionary or contract redesign is involved
- the template family does not change

For micro-edits:
- do not load full template bodies
- use the appropriate checklist only
- preserve the existing structure

### 3. Route to a template family
Use this mapping:
- Project entry / navigation → `PROJECT_INDEX`
- Platform shared guidance or overview → `PLATFORM_DOC`
- Platform-owned API contract → `PLATFORM_API_SCHEMA`
- Platform-owned data / DB contract → `PLATFORM_DATA_SCHEMA`
- Platform-owned UI / route / event contract → `PLATFORM_UI_SCHEMA`
- Platform reusable standards / conventions / policies → `PLATFORM_STANDARDS`
- App overview → `APP_README`
- Feature story / acceptance / flow → `FEATURE_SPEC`
- API contract → `DICTIONARY_API_SCHEMA`
- Data / DB contract → `DICTIONARY_DATA_SCHEMA`
- UI contract → `DICTIONARY_UI_SCHEMA`
- Dev status update → `DEV_STATUS_*`
- Bug report / incident review → `ISSUE`
- Architecture decision → `ADR_*`

### 4. Keep SSOT boundaries clean
- App dictionary docs are authoritative for app-scoped schema and contracts.
- Platform-owned shared contracts may live in `docs/platform/<component>/specs/**`.
- Feature docs should link to authority docs instead of copying full tables.
- Ops docs should describe operation and deployment behavior, not duplicate schemas.

### 5. Apply the right checklist
For the common micro-edit cases below, use exactly one relevant checklist family:
- `FEATURE`
- `DICTIONARY`
- `PLATFORM_CONTRACT`
- `ISSUE`
- `DEV_STATUS`

For other small doc types such as project index, app overview, platform guidance docs, platform contract docs, or ADRs:
- preserve the existing structure
- use `references/template_notes.md` for section expectations
- do not load a fuller skeleton unless the edit becomes structural

Checklist intent:
- timestamp updated when needed
- stable anchors preserved
- links remain usable
- no duplicate schema drift
- verification and rollback included when behavior changes

### 6. Output format
When routing a request, report briefly:
1. Edit type: micro or structural
2. Chosen template family or checklist family
3. Why this route fits
4. Any missing inputs
5. The doc path(s) most likely affected

For lower-frequency writing and example guidance, load the relevant reference file only when needed.

## Reference files
Read only what you need:
- `references/routing_table.md` for the route map
- `references/checklists.md` for micro-edit quality checks
- `../docops-mode/references/document_metadata_and_access.md` for the front matter standard and kind-based body access rules
- `references/template_notes.md` for minimal structural template guidance
- `references/structural_templates_platform.md` for `PROJECT_INDEX`, `PLATFORM_DOC`, `PLATFORM_*_SCHEMA`, and `PLATFORM_STANDARDS`
- `references/structural_templates_app_core.md` for `APP_README` and `FEATURE_SPEC`
- `references/structural_templates_app_contracts.md` for `DICTIONARY_*`
- `references/structural_templates_status_and_records.md` for `DEV_STATUS_*`, `ISSUE`, and `ADR_*`
- `references/usage_patterns.md` for writing guidance and example trigger scenarios

Default behavior:
- prefer the smallest compliant structure
- hand back to `docops-mode` when the request becomes repo-wide workflow, active-stage drafting, or broader dev-status coordination
