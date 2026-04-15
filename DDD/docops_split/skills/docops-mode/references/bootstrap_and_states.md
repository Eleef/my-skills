---
name: bootstrap-and-states
description: Bootstrap sequence and state model for running the core DocOps workflow.
---

## Compact bootstrap order
1. `docs/00_project_index.md`
2. `docs/dev_status/active_task.md`
3. the current `spec/**` work area when the task is still under clarification, design, or active implementation
4. `docs/apps/<app>/00_readme.md` when an app is involved
5. `docs/apps/<app>/dictionary/*.md` when contracts or schema matter
6. `docs/platform/<component>/specs/api_schema.md`, `data_schema.md`, or `ui_schema.md` when a platform-owned contract matters
7. `docs/apps/<app>/ops/**` first, then `docs/platform/ops/**`, when deployment/ops/routing matter

If any critical file is unavailable, switch to degraded mode and say exactly what is missing.

For managed markdown under `docs/**` and `spec/**`:
- read YAML front matter first
- use `kind` and related metadata to decide whether the file is in scope
- then read only the body sections allowed by the document access rules

## Scope of working state
- Working state applies to the current task or track, not to the whole `docs/**` tree.
- Historical records under `docs/**` are reference material unless the task explicitly includes updating them.
- `docs/dev_status/**` should point to the active `spec/**` work area and relevant published docs instead of duplicating full draft content.

## Working states
### PLANNING
Use when the user goal, scope, or acceptance criteria are unclear.
- Ask one grouped clarification set.
- Provide only an assumption-labeled draft.

### DESIGN
Use when comparing structures, contracts, risks, or documentation placement.
- Make tradeoffs explicit.
- Keep app/platform boundaries clear.

### IMPLEMENTING
Use when editing docs or code.
- Keep changes atomic with related docs.
- Keep active drafts in `spec/**` until they become published docs.
- Avoid duplicate schema content outside dictionary files.

### VERIFYING
Use when commands were run or validation was attempted.
- Label as `VERIFIED`, `BROKEN`, or `UNVERIFIED`.
- Include command and short result summary.

### DONE
Use when the task is finished and confirmed.
- Update relevant dev status files if applicable.
- Publish, archive, or retire stage-only `spec/**` material as needed.
- Leave a concise trail for the next session.
