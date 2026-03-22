# DocOps Split Output

This folder contains a practical split of the original workflow standard into:

- `rules/` → lightweight always-on guidance
- `skills/docops-mode/` → workflow skill for DocOps state/bootstrap/spec-to-implementation bridge/handoff
- `skills/doc-template-router/` → template routing, standards routing, checklist, and structural drafting skill

## Intended usage
- Put `rules/DOCOPS_RULES.md` into your persistent project rules layer after review.
- Keep the two skills as reusable, on-demand workflow components.
- Prefer `spec/**` as the active workspace for in-flight stage materials; publish stable authority or durable knowledge into `docs/**`.
- Use YAML front matter plus kind-based body access rules so agents can triage docs before reading full content.
- Evolve templates and routing in the skill references rather than bloating the rules layer.
- Use `test_prompts.md` for quick manual trigger checks before moving the skills into your main skills directory.
- Use `MIGRATION_GUIDE.md` for the move plan and first-test sequence.

## Why this split
- Stable constraints belong in rules.
- Multi-step workflow belongs in a workflow skill.
- Template routing and checklist logic belong in a template skill.

## Possible future evolution
- Keep the current skill split for now.
- If future trigger behavior or context pressure becomes an issue, prefer splitting `docops-mode` by workflow frequency rather than by doc type.
- Likely split direction:
  - high-frequency middle-loop work stays in `docops-mode` (docs sync, dev-status iteration, spec-to-implementation bridge, template delegation)
  - low-frequency boundary work can move later into separate start/close helpers (kickoff/planning start, pause/completion/archive)
