# Micro-edit Checklists

## FEATURE
- Ensure required YAML front matter is present and update `summary`, `lifecycle`, and `updated_at` when meaning changes.
- Do not copy SSOT field tables into the feature doc.
- Keep purpose, key flow, acceptance points, and relevant links accurate.
- If behavior changes, note risks or rollback guidance.

## DICTIONARY
- Ensure required YAML front matter is present and update `summary`, `lifecycle`, and `updated_at` when meaning changes.
- Preserve stable endpoint/table heading conventions.
- Keep types, optionality, defaults, and errors aligned with implementation.
- If there is a breaking change, mention affected areas and downstream docs to sync.

## PLATFORM_CONTRACT
- Ensure required YAML front matter is present and update `summary`, `lifecycle`, and `updated_at` when meaning changes.
- Preserve stable endpoint, entity, route, state, and event anchors used by downstream apps or platform docs.
- Keep compatibility notes, ownership boundaries, and downstream references accurate for the affected contract surface.
- If there is a breaking or cross-app change, mention consumers, rollout constraints, and which related docs must be synced atomically.

## ISSUE
- Ensure required YAML front matter is present and update `summary`, `lifecycle`, and `updated_at` when meaning changes.
- Keep symptom, impact, repro, expected vs actual, root cause, fix, verification, and rollback present.
- Ensure logs and examples are redacted.
- Link to dictionary sections instead of duplicating contract tables.

## DEV_STATUS
- Ensure required YAML front matter is present and update `summary`, `lifecycle`, and `updated_at` when meaning changes.
- Keep newest items first in todo/history files.
- Keep active task content focused on current objective, focus, and next actions.
- Link to the active `spec/**` work area and relevant published docs when they exist instead of duplicating long draft content.
- Preserve track isolation when multiple tracks coexist.
- Include traceable references such as doc paths, commands, PRs, or commits when available.
