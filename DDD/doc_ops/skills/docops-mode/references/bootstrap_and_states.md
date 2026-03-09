# DocOps Bootstrap and States

## Compact bootstrap order
1. `docs/00_project_index.md`
2. `docs/dev_status/active_task.md`
3. `docs/apps/<app>/00_readme.md` when an app is involved
4. `docs/apps/<app>/dictionary/*.md` when contracts or schema matter
5. `docs/apps/<app>/ops/**` first, then `docs/platform/ops/**`, when deployment/ops/routing matter

If any critical file is unavailable, switch to degraded mode and say exactly what is missing.

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
- Avoid duplicate schema content outside dictionary files.

### VERIFYING
Use when commands were run or validation was attempted.
- Label as `VERIFIED`, `BROKEN`, or `UNVERIFIED`.
- Include command and short result summary.

### DONE
Use when the task is finished and confirmed.
- Update relevant dev status files if applicable.
- Leave a concise trail for the next session.
