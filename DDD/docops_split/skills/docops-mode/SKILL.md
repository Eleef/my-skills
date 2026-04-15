---
name: docops-mode
description: Coordinate multi-step DocOps workflow for repository-related documentation, architecture, debugging, and implementation-tracking tasks. Use this when the work spans planning, active `spec/**` workspace management, `docs/dev_status/**` sync, state or handoff updates, repo-wide documentation reorganization, or explicit spec-to-implementation bridging. Prefer this skill for non-trivial doc work, doc-driven debugging, architecture-note coordination, and tasks that require workflow state or verification discipline. Do not use this for isolated template choice, simple published-doc routing, or micro-vs-structural edit classification; use `doc-template-router` for those.
---

# DocOps Mode

Use this skill for heavier repository documentation work. This skill is the workflow layer, not the always-on rules layer.

## What this skill does
- Determines whether the request belongs to DocOps scope.
- Runs a compact bootstrap over relevant project docs.
- Uses an active `spec/**` workspace when the material is still evolving.
- Reads managed doc metadata before expanding into full body content.
- Makes staged document access observable when metadata-first triage matters.
- Switches into the correct working state.
- Clarifies missing requirements in one batch when the task is unclear.
- Decides whether the task needs a template-routing skill.
- Produces structured delivery and clean handoff notes.

## Workflow

### 1. Apply scope gate
Use DocOps mode only when the user request is related to the current repository's code, docs, architecture, debugging, deployment notes, or iteration workflow.

If the request is clearly outside the project, answer normally and do not force DocOps conventions.

### 2. Pick the working state
Choose one state and say it implicitly through behavior:
- `PLANNING`: request is still unclear or incomplete.
- `DESIGN`: comparing approaches, contracts, risks, or acceptance boundaries.
- `IMPLEMENTING`: making concrete doc/code changes.
- `VERIFYING`: running checks or summarizing verification status.
- `DONE`: wrapping up and updating status/history.

Do not pretend to be in multiple states at once. Progress cleanly.

`Working state` tracks workflow stage. It is different from `VERIFIED` / `BROKEN` / `UNVERIFIED`, which track the evidence status of specific results.
It applies only to the current task or track and its in-scope artifacts, not to the whole `docs/**` tree.

### 3. Run compact bootstrap
For non-trivial tasks, read only the minimum relevant files in this order when available:
1. `docs/00_project_index.md`
2. `docs/dev_status/active_task.md`
3. the current `spec/**` work area if the task is still in flight, under clarification, or under design
4. `docs/apps/<app>/00_readme.md` if an app is involved
5. `docs/apps/<app>/dictionary/*.md` if contracts/schema are involved
6. `docs/platform/<component>/specs/api_schema.md`, `data_schema.md`, or `ui_schema.md` if a platform-owned contract is involved
7. `docs/apps/<app>/ops/**` first, then `docs/platform/ops/**`, if deployment or routing is involved

For managed markdown in `docs/**` or `spec/**`:
- read YAML front matter first
- use `kind`, `scope`, `lifecycle`, `authority`, and `summary` to decide if the file is in scope
- then read only the body sections allowed by the document access rules
- if several managed docs are candidates or a target doc is large, make the staged access path visible through a metadata scan, bounded window read, or stable-anchor read before expanding
- do not describe the workflow as progressive loading unless the actual reads followed that sequence
- if a full-file read is needed, state the reason instead of implying the load stayed bounded

If files are unavailable, enter degraded mode instead of guessing.

### 4. Use active workspace vs published docs
- Use `spec/**` for evolving stage material such as requirements drafts, acceptance notes, open questions, implementation notes, and verification plans.
- Use `docs/**` for published knowledge and authority docs that other work should reference.
- Keep `docs/dev_status/**` as the lightweight index that points to the current `spec/**` work area, relevant published docs, and key code areas.
- Do not treat the whole `docs/**` tree as being in the current working state; only current-task artifacts are active.
- Publish material from `spec/**` into `docs/**` once it becomes authority or durable shared knowledge.

### 5. Use degraded mode honestly
If you cannot access the relevant files or outputs:
- Explicitly state what is unavailable.
- Request the smallest missing set.
- Offer an MVP answer with assumptions and risks clearly labeled.
- Never invent repository facts.

### 6. Batch unclear questions
If the task is unclear, ask a single grouped clarification set rather than many small back-and-forth questions.

Focus on:
- objective
- scope boundaries
- target app or platform area
- acceptance criteria
- required track for `docs/dev_status/**`

Before answers arrive, you may give a draft only if assumptions are marked.

### 7. Respect app/platform separation
- App-specific content belongs in `docs/apps/<app>/**`.
- Shared, cross-app guidance belongs in `docs/platform/**`.
- Keep platform docs generic and link to app docs instead of absorbing app-specific behavior.

### 8. Enforce SSOT behavior
- App dictionary files are the contract authority for app-scoped behavior.
- Platform-owned shared API, data, UI, or similar contracts may live in `docs/platform/<component>/specs/**`.
- Feature docs tell the story and link to the relevant authority docs instead of restating them.
- Do not maintain duplicate schemas in feature or ops docs.
- If the task changes behavior, update both implementation and affected docs together.

### 9. Delegate template work when needed
If the task requires template routing, structural doc generation, or checklist-driven drafting, use the sibling skill `doc-template-router`.

Use it especially when:
- creating a new document
- heavily restructuring an existing doc
- choosing among feature / app contract / platform contract / standards / dev_status / issue / ADR formats
- deciding micro-edit vs structural-edit flow

### 10. Bridge spec to implementation explicitly
Before code changes begin, make the bridge visible.

Capture these items as a compact implementation entry checklist:
- the requirement or user objective being solved
- the primary spec document(s) that define the change
- the standards, ADRs, or platform constraints that apply
- the code areas expected to change
- the docs that must be updated atomically
- the acceptance criteria that must be verified
- the verification plan: commands, smoke checks, or observable outcomes

Use these bridging rules:
- If behavior, API, or data contracts change, update the relevant authority spec before or together with code changes:
  - app-owned contract changes -> `docs/apps/<app>/dictionary/**`
  - platform-owned API contract changes -> `docs/platform/<component>/specs/api_schema.md`
  - platform-owned data contract changes -> `docs/platform/<component>/specs/data_schema.md`
  - platform-owned UI, route, state, or event contract changes -> `docs/platform/<component>/specs/ui_schema.md`
- If the change creates reusable cross-app guidance, route it into `platform/standards/**` instead of hiding it inside a feature doc.
- Treat acceptance criteria as the source for verification, not as decorative prose.
- If implementation reveals a spec gap, patch the spec before claiming completion.

### 11. Load boundary-action guidance only when needed
For lower-frequency boundary actions, use `references/handoff_and_delivery.md` instead of keeping the full procedure in active context.

Load it when the task needs any of these:
- parking ideas that are not ready to implement
- structured DESIGN / IMPLEMENTING / VERIFYING delivery
- pause handoff or confirmed completion handling
- git and `docs/dev_status/**` checkpoint sync

For lower-frequency heuristics and trigger examples, load `references/usage_patterns.md` only when the task needs that extra guidance.

## Companion files
- Use `references/bootstrap_and_states.md` for the compact state/bootstrap cheat sheet if you need a quick refresher.
- Use `references/active_workspace_model.md` when you need the preferred `spec/**` vs `docs/**` split.
- Use `references/document_metadata_and_access.md` when you need the front matter standard or kind-specific read/write rules.
- Use `references/implementation_bridge.md` when the task is moving from requirement/spec into code and verification.
- Use `references/handoff_and_delivery.md` for low-frequency boundary actions such as parking ideas, structured delivery, pause/completion handling, and checkpoint sync.
- Use `references/usage_patterns.md` for lower-frequency heuristics and concrete trigger examples.
