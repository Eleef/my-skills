---
name: structural-template-notes
description: Shared notes for applying one template family at a time while preserving minimal managed metadata.
---

## Managed metadata
All managed markdown docs should start with the minimal YAML front matter:
- `kind`
- `scope`
- `lifecycle`
- `authority`
- `summary`
- `updated_at`

Use front matter for routing and quick triage before reading the body.

## PROJECT_INDEX
Use for the global docs entry point and navigation map.
Include:
- project overview
- architecture-at-a-glance
- documentation navigation
- where to place new docs

## PLATFORM_DOC
Use for shared frontend/backend/ops documentation and platform guidance that is not itself a stable contract table.
Keep platform docs generic and reusable across apps.
Do not absorb app-specific details.

## PLATFORM_API_SCHEMA
Use for platform-owned API contracts under `docs/platform/<component>/specs/**`.
Keep endpoint headings stable and make request/response/errors explicit.

## PLATFORM_DATA_SCHEMA
Use for platform-owned data and entity contracts under `docs/platform/<component>/specs/**`.
Keep table or entity headings stable and document constraints and migration notes when relevant.

## PLATFORM_UI_SCHEMA
Use for platform-owned UI, route, state, or event contracts under `docs/platform/<component>/specs/**`.
Keep reusable platform behavior separate from app-local adaptations.

## PLATFORM_STANDARDS
Use for reusable engineering rules, conventions, checklists, or policies that should apply across apps.
Include:
- scope
- rule set or standard
- when to apply it
- examples or counterexamples if helpful
- links to ADRs, specs, or app docs that implement the rule

## APP_README
Use for an app home page.
Include:
- what the app is
- quick links to dictionary/features/guides
- optional domain terms and high-level flow
- optional current status

## FEATURE_SPEC
Use for story-like feature docs.
Include:
- goal and non-goal
- user story and value
- UX/UI behavior
- end-to-end flow
- dictionary references instead of copied schema
- acceptance criteria
- edge cases and rollout notes as needed

## DICTIONARY_API_SCHEMA
Use for API contracts.
Keep endpoint headings stable and make request/response/errors explicit.

## DICTIONARY_DATA_SCHEMA
Use for data and table contracts.
Keep table headings stable and document purpose, columns, constraints, indexes, and migration notes.

## DICTIONARY_UI_SCHEMA
Use for UI contract docs such as routes, state machines, tracking events, and error mapping.

## DEV_STATUS_*
Use for active task, todo, and history log updates.
Prefer tiny edits and preserve ordering/track isolation.
Shared `docs/dev_status/**` files usually keep track identity in section headings or entry prefixes rather than file-level front matter.

## ISSUE
Use for bug reports and incident write-ups.
Keep repro, root cause, resolution, verification, and rollback easy to scan.

## ADR_*
Use for architecture decisions.
Make context, decision, consequences, and references explicit.
