---
name: doc-template-router
description: Route published repository documentation tasks to the right editing pattern and template shape. Use this whenever the user wants to create a doc, rewrite or restructure an existing doc, choose between feature/dictionary/standards/dev-status/issue/ADR formats, decide whether an edit is micro or structural, or apply checklist-based documentation quality control instead of freeform writing. Prefer this skill whenever the task is mainly about selecting the correct published doc format, standards-vs-ADR-vs-dictionary placement, template family, or edit path before drafting.
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
Treat the request as a **micro-edit** if any of these are true:
- only one small section changes
- total change is roughly within 30 lines
- no new document is created
- no major section reordering is needed
- no systematic dictionary/schema redesign is involved

For micro-edits:
- do not load full template bodies
- use the appropriate checklist only
- preserve the existing structure

Treat the request as a **structural edit** if any of these are true:
- a new document is being created
- multiple sections are added or reorganized
- several sources are being merged into a new structure
- dictionary content needs broad rework

For structural edits:
- choose one template family only
- do not mix multiple top-level template structures unless the user explicitly asks

### 3. Route to a template family
Use this mapping:
- Project entry / navigation → `PROJECT_INDEX`
- Platform shared docs or platform-owned specs → `PLATFORM_*`
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
- `ISSUE`
- `DEV_STATUS`

For other small doc types such as project index, app overview, platform docs, or ADRs:
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

## Reference files
Read only what you need:
- `references/routing_table.md` for the route map
- `references/checklists.md` for micro-edit quality checks
- `../docops-mode/references/document_metadata_and_access.md` for the front matter standard and kind-based body access rules
- `references/template_notes.md` for minimal structural template guidance
- `references/structural_templates_platform.md` for `PROJECT_INDEX`, `PLATFORM_*`, and `PLATFORM_STANDARDS`
- `references/structural_templates_app_core.md` for `APP_README` and `FEATURE_SPEC`
- `references/structural_templates_app_contracts.md` for `DICTIONARY_*`
- `references/structural_templates_status_and_records.md` for `DEV_STATUS_*`, `ISSUE`, and `ADR_*`

## Writing guidance
- Prefer the smallest compliant structure.
- Do not force a full template when a checklist-based patch is enough.
- If the user asks for a draft but the source material is incomplete, create a draft with explicit assumptions instead of fake details.
- If the request is still an in-flight stage draft rather than a published docs artifact, hand back to `docops-mode` and keep the evolving material in `spec/**` until it is ready to publish.
- If the task is really about repository-wide workflow, dev-status coordination, or multi-step DocOps execution, hand back to `docops-mode` instead of absorbing the whole process.

## Example trigger scenarios
- "我要新建一个 feature 文档，你先帮我判断该走哪个模板。"
- "这个 API schema 文档要重构，帮我判断是微调还是结构性改写。"
- "我要补一个 issue 复盘，但不想自由发挥，你按模板路由来。"
- "先别写内容，先告诉我这次 dev_status 更新该用哪种结构。"
- "这个规则以后多个 app 都要复用，你判断该写 standards、ADR 还是 dictionary。"
