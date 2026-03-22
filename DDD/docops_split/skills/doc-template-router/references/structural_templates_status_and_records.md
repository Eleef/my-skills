# Structural Templates: Status and Records

Use these as fuller drafting skeletons when a structural edit targets dev-status docs or durable decision/incident records. Pick one family only.

## DEV_STATUS_*
**Suggested paths:** `docs/dev_status/active_task.md`, `docs/dev_status/todo.md`, `docs/dev_status/history_log.md`

```markdown
---
kind: dev_status_active_task
scope: track:<TRACK>
lifecycle: active
authority: workflow_record
summary: Live task state for <TRACK>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
track: <TRACK>
---

# Active Task Context

## <TRACK>
### Current Objective
- ...

### Relevant Paths
- Active spec workspace:
- Published docs:
- Key code areas:

### Current Focus
- [ ] ...

### Next Actions
1. ...
2. ...
```

```markdown
---
kind: dev_status_todo
scope: track:<TRACK>
lifecycle: active
authority: workflow_record
summary: Backlog items for <TRACK> or related work areas.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
track: <TRACK>
---

# Todo / Backlog

- [YYYY-MM-DD] **<TRACK> / <AREA>** <short item> - <link or note>
```

```markdown
---
kind: dev_status_history
scope: track:<TRACK>
lifecycle: stable
authority: workflow_record
summary: Completed history entries for <TRACK>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
track: <TRACK>
---

# History Log

## [YYYY-MM-DD] **<TRACK>** <objective summary>
- What shipped or changed:
- Changed docs:
- Verification:
- Follow-ups:
```

## ISSUE
**Suggested path:** `docs/issues/YYYY-MM-DD-<issue_name>.md`

```markdown
---
kind: issue
scope: app:<app_or_area>
lifecycle: active
authority: incident_record
summary: Incident or bug record for <short issue title>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
severity: P0 / P1 / P2
---

# Issue: <short issue title>

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
---
kind: adr
scope: platform:<area_or_app>
lifecycle: stable
authority: decision_record
summary: Architecture decision record for <title>.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
decision_status: draft / accepted / deprecated
---

# ADR: <title>

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
