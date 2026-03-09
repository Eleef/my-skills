# Micro-edit Checklists

## FEATURE
- Update the last-updated timestamp if the doc format uses one.
- Do not copy SSOT field tables into the feature doc.
- Keep purpose, key flow, acceptance points, and relevant links accurate.
- If behavior changes, note risks or rollback guidance.

## DICTIONARY
- Update the last-updated timestamp if the doc format uses one.
- Preserve stable endpoint/table heading conventions.
- Keep types, optionality, defaults, and errors aligned with implementation.
- If there is a breaking change, mention affected areas and downstream docs to sync.

## ISSUE
- Update the last-updated timestamp if the doc format uses one.
- Keep symptom, impact, repro, expected vs actual, root cause, fix, verification, and rollback present.
- Ensure logs and examples are redacted.
- Link to dictionary sections instead of duplicating contract tables.

## DEV_STATUS
- Keep newest items first in todo/history files.
- Keep active task content focused on current objective, focus, and next actions.
- Preserve track isolation when multiple tracks coexist.
- Include traceable references such as doc paths, commands, PRs, or commits when available.
