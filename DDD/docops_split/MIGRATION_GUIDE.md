# Migration Guide

This guide tells you what to move where after reviewing the split output.

## 1. Move into your rules layer
Use this file as the lightweight persistent rules core:
- `rules/DOCOPS_RULES.md`

Recommended handling:
- merge the contents into your project-level always-on rules
- keep it short; do not merge the full workflow or template references into the rules layer

## 2. Move into your formal skills directory
Move these two folders as-is:
- `skills/docops-mode/`
- `skills/doc-template-router/`

Why:
- `docops-mode` is the workflow orchestrator
- `doc-template-router` is the routing / checklist / structural drafting tool

## 3. Keep these reference files bundled with the skills
### `docops-mode`
- `references/bootstrap_and_states.md`
- `references/active_workspace_model.md`
- `references/document_metadata_and_access.md`
- `references/implementation_bridge.md`

### `doc-template-router`
- `references/routing_table.md`
- `references/checklists.md`
- `references/template_notes.md`
- `references/structural_templates_platform.md`
- `references/structural_templates_app_core.md`
- `references/structural_templates_app_contracts.md`
- `references/structural_templates_status_and_records.md`

Do not flatten these into rules. They are skill resources.

## 4. Adopt the active workspace model
Use `spec/**` as the preferred working area for in-flight stage material:
- requirements drafts
- acceptance notes
- open questions
- implementation notes
- verification plans

Use `docs/**` for published authority and durable project knowledge.

Keep `docs/dev_status/**` small:
- point to the active `spec/**` work area
- point to relevant published docs
- avoid copying long draft content into status files

## 5. Adopt the metadata and access model
For managed markdown under `docs/**` and `spec/**`:
- add minimal YAML front matter
- read front matter first
- use `kind` to decide how much body content to read
- use kind-specific write rules instead of broad rewrites

High-value examples:
- `dev_status_history`: newest first, prepend updates, usually read only the first 40-80 body lines
- `dev_status_todo`: newest first, prepend updates, usually read only the first 30-60 body lines
- `dev_status_active_task`: read and patch only the current track block
- `dictionary_*`: read and patch by stable anchor instead of scanning the full file

## 6. First prompts to test after migration
Start with these from `test_prompts.md`:

### Test `docops-mode`
1. Repo docs restructure
2. Multi-step feature documentation
3. Spec to implementation bridge

Expected behavior:
- recognizes multi-step workflow
- clarifies scope if needed
- makes spec/docs/code/verification bridge visible
- mentions dev status or closure handling when relevant

### Test `doc-template-router`
1. Choose template family first
2. Standards routing
3. Micro-edit vs structural-edit

Expected behavior:
- chooses one route cleanly
- distinguishes standards vs ADR vs dictionary vs feature
- uses checklist for micro-edits
- uses fuller structural template skeleton only when needed

## 7. What not to test first
Avoid starting with tiny one-step prompts like:
- simple file reads
- generic concept explanations
- pure code changes with no docs impact

Those often should not trigger either skill.

## 8. Success criteria for the migration
The migration is in good shape when:
- rules stay lightweight
- `docops-mode` handles workflow and spec-to-implementation bridge
- `doc-template-router` handles placement and template routing
- `spec/**` is used for evolving stage work instead of turning `docs/**` into a mixed active/archive workspace
- managed docs can be triaged from YAML front matter before deep reads
- history/todo/status docs can be updated with local reads instead of whole-file scans
- standards no longer get confused with ADR or dictionary docs
- acceptance criteria influence verification instead of staying as prose only

## 9. Suggested next step
After moving the files, run the manual prompts in `test_prompts.md` and note:
- which skill triggers
- whether any prompt under-triggers or over-triggers
- whether the chosen route feels natural

Then do one final round of description tuning only if the trigger behavior feels off.

## 10. Possible future evolution
Do not split the skills further yet.

If future use shows trigger overlap or context pressure, prefer splitting by workflow frequency:
- keep high-frequency middle-loop work in `docops-mode`
- move low-frequency boundary work into separate helpers only when needed

Suggested future candidates:
- start-of-stage work: kickoff, plan framing, initial clarification
- end-of-stage work: pause handoff, completion update, history/archive handling
