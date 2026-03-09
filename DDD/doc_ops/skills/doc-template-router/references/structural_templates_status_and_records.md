# Structural Templates: Status and Records

Use these as fuller drafting skeletons when a structural edit targets dev-status docs or durable decision/incident records. Pick one family only.

## DEV_STATUS_*
**Suggested paths:** `docs/dev_status/active_task.md`, `docs/dev_status/todo.md`, `docs/dev_status/history_log.md`

```markdown
# Active Task Context
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

## <TRACK>
### Current Objective
- ...

### Current Focus
- [ ] ...

### Next Actions
1. ...
2. ...
```

```markdown
# Todo / Backlog
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

> Newest items first.

- [YYYY-MM-DD] **<TRACK> / <AREA>** <short item> - <link or note>
```

```markdown
# History Log
> Last Updated: [YYYY-MM-DD HH:MM] ([TZ])

> Newest entries first. Each entry is single-track.

## [YYYY-MM-DD] **<TRACK>** <objective summary>
- What shipped or changed:
- Changed docs:
- Verification:
- Follow-ups:
```

## ISSUE
**Suggested path:** `docs/issues/YYYY-MM-DD-<issue_name>.md`

```markdown
# Issue: <short issue title>
> Date: [YYYY-MM-DD] ([TZ])
> Severity: P0 / P1 / P2

## Environment
- version/branch:
- env vars (redacted):
- steps context:

## Symptom vs Expected
- Symptom:
- Expected:

## Reproduction Steps
1. ...
2. ...

## Root Cause Analysis
- why it happened:
- contributing factors:

## Resolution
- changes made:
- docs updated:

## Verification
- Commands:
- Status: VERIFIED / BROKEN / UNVERIFIED

## Rollback
- ...
```

## ADR_*
**Suggested path:** `docs/adr/ADR-<SCOPE>-###-title.md`

```markdown
# ADR: <title>
> Date: [YYYY-MM-DD] ([TZ])
> Status: Draft / Accepted / Deprecated
> Scope: PLATFORM / <APP>

## Context
- What problem is being solved?
- Constraints:
- Options considered:

## Decision
- We decided to...

## Consequences
- Positive:
- Negative:
- Follow-ups:

## References
- Related docs:
- Related issues:
- Related code areas:
```
