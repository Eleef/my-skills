# Routing Table

If an existing managed doc already has YAML front matter, use its `kind` as the primary routing signal before relying on path or heading heuristics.

## Template family map
- Project global entry or navigation changes → `PROJECT_INDEX`
- Shared platform docs or platform-owned specs → `PLATFORM_*`
- Platform reusable conventions, policies, or engineering rules → `PLATFORM_STANDARDS`
- App overview / app home → `APP_README`
- Feature description / user flow / acceptance criteria → `FEATURE_SPEC`
- API contract / endpoint behavior → `DICTIONARY_API_SCHEMA`
- Database / table / data contract → `DICTIONARY_DATA_SCHEMA`
- UI route / state / tracking contract → `DICTIONARY_UI_SCHEMA`
- Active task / todo / history updates → `DEV_STATUS_*`
- Bug report / incident write-up → `ISSUE`
- Architecture decision → `ADR_*`

## When to choose standards instead of other docs
- Use `PLATFORM_STANDARDS` when the guidance is meant to be reused across multiple apps or features.
- Use `PLATFORM_*` when the output is a platform-owned spec or contract under `docs/platform/<component>/specs/**`.
- Use `ADR_*` when the key output is a decision and its consequences.
- Use `DICTIONARY_*` when the output is an app-scoped contract or schema authority.
- Use `FEATURE_SPEC` when the output is a single feature story and acceptance definition.

## Micro-edit default routing
- These are the default checklist-backed routes for the most common small edits.
- Small feature patch → checklist `FEATURE`
- Small dictionary patch → checklist `DICTIONARY`
- Small issue update → checklist `ISSUE`
- Small dev status update → checklist `DEV_STATUS`
