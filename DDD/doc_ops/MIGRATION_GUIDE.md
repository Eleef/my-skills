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

## 4. First prompts to test after migration
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

## 5. What not to test first
Avoid starting with tiny one-step prompts like:
- simple file reads
- generic concept explanations
- pure code changes with no docs impact

Those often should not trigger either skill.

## 6. Success criteria for the migration
The migration is in good shape when:
- rules stay lightweight
- `docops-mode` handles workflow and spec-to-implementation bridge
- `doc-template-router` handles placement and template routing
- standards no longer get confused with ADR or dictionary docs
- acceptance criteria influence verification instead of staying as prose only

## 7. Suggested next step
After moving the files, run the manual prompts in `test_prompts.md` and note:
- which skill triggers
- whether any prompt under-triggers or over-triggers
- whether the chosen route feels natural

Then do one final round of description tuning only if the trigger behavior feels off.

## 8. Possible future evolution
Do not split the skills further yet.

If future use shows trigger overlap or context pressure, prefer splitting by workflow frequency:
- keep high-frequency middle-loop work in `docops-mode`
- move low-frequency boundary work into separate helpers only when needed

Suggested future candidates:
- start-of-stage work: kickoff, plan framing, initial clarification
- end-of-stage work: pause handoff, completion update, history/archive handling
