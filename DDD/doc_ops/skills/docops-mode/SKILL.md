---
name: docops-mode
description: Enter a structured DocOps workflow for repository-related documentation, architecture, debugging, and implementation-tracking tasks. Use this whenever the user asks to plan, audit, reorganize, or update project docs; keep `docs/dev_status/**` in sync; clarify documentation scope; separate app docs from platform docs; move from clarified requirement/spec into implementation planning; run a documentation bootstrap; or follow a multi-step repo documentation process instead of giving a one-off answer. Prefer this skill for non-trivial doc work, doc-driven debugging, architecture-note updates, spec-to-implementation bridging, and tasks that require state, handoff, or verification discipline.
---

# DocOps Mode

Use this skill for heavier repository documentation work. This skill is the workflow layer, not the always-on rules layer.

## What this skill does
- Determines whether the request belongs to DocOps scope.
- Runs a compact bootstrap over relevant project docs.
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

### 3. Run compact bootstrap
For non-trivial tasks, read only the minimum relevant files in this order when available:
1. `docs/00_project_index.md`
2. `docs/dev_status/active_task.md`
3. `docs/apps/<app>/00_readme.md` if an app is involved
4. `docs/apps/<app>/dictionary/*.md` if contracts/schema are involved
5. `docs/apps/<app>/ops/**` first, then `docs/platform/ops/**`, if deployment or routing is involved

If files are unavailable, enter degraded mode instead of guessing.

### 4. Use degraded mode honestly
If you cannot access the relevant files or outputs:
- Explicitly state what is unavailable.
- Request the smallest missing set.
- Offer an MVP answer with assumptions and risks clearly labeled.
- Never invent repository facts.

### 5. Batch unclear questions
If the task is unclear, ask a single grouped clarification set rather than many small back-and-forth questions.

Focus on:
- objective
- scope boundaries
- target app or platform area
- acceptance criteria
- required track for `docs/dev_status/**`

Before answers arrive, you may give a draft only if assumptions are marked.

### 6. Respect app/platform separation
- App-specific content belongs in `docs/apps/<app>/**`.
- Shared, cross-app guidance belongs in `docs/platform/**`.
- Keep platform docs generic and link to app docs instead of absorbing app-specific behavior.

### 7. Enforce SSOT behavior
- App dictionary files are the contract authority for app-scoped behavior.
- Platform-owned shared contracts may live in `docs/platform/<component>/specs/**`.
- Feature docs tell the story and link to the relevant authority docs instead of restating them.
- Do not maintain duplicate schemas in feature or ops docs.
- If the task changes behavior, update both implementation and affected docs together.

### 8. Delegate template work when needed
If the task requires template routing, structural doc generation, or checklist-driven drafting, use the sibling skill `doc-template-router`.

Use it especially when:
- creating a new document
- heavily restructuring an existing doc
- choosing among feature / dictionary / standards / dev_status / issue / ADR formats
- deciding micro-edit vs structural-edit flow

### 9. Bridge spec to implementation explicitly
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
  - platform-owned shared contract changes -> `docs/platform/<component>/specs/**`
- If the change creates reusable cross-app guidance, route it into `platform/standards/**` instead of hiding it inside a feature doc.
- Treat acceptance criteria as the source for verification, not as decorative prose.
- If implementation reveals a spec gap, patch the spec before claiming completion.

### 10. Park ideas that are not ready to implement
If the user says "not now", "later", or shares a rough idea without wanting execution yet:
- add a concise item to `docs/dev_status/todo.md` for simple future work
- create a draft design or standards note for larger ideas, then link it from todo
- keep the note small, explicit, and track-tagged

### 11. Delivery format
For DESIGN / IMPLEMENTING / VERIFYING outputs, use this structure:
1. Current Working State
2. Summary
3. Docs changes
4. Code changes
5. Verification
6. Risks and rollback

Use explicit `VERIFIED`, `BROKEN`, or `UNVERIFIED` labels.

**Short example:**
- Current Working State: `VERIFYING`
- Verification:
  - smoke test: `VERIFIED`
  - production parity check: `UNVERIFIED`

### 12. Completion and pause handling
If pausing mid-task:
- update only the relevant track block in `active_task.md`
- do not overwrite unrelated tracks
- preserve objective, current focus, and next actions
- if you are preserving a stable handoff checkpoint with git, sync the relevant dev-status update before or together with that commit
- if dev status is updated without a commit, state why the work is still WIP or why no clean commit boundary exists yet

If the task is completed and confirmed:
- add a concise top-entry summary to `history_log.md`
- reset or update the active state for that track
- keep each history entry single-track
- if the result should be preserved as a completion or stage-complete commit, make sure the dev-status updates land before or together with that commit
## Practical heuristics
- Prefer the minimum doc surface needed for the task.
- Keep process visible, but keep output lean.
- Treat DocOps as a workflow harness, not a reason to over-document.
- If the task is a tiny one-section update, skip heavy workflow and do the minimal compliant edit.
- If the user's main need is template choice, structural routing, or checklist-based drafting, hand off to `doc-template-router` early instead of duplicating its job.

## Example trigger scenarios
- "帮我梳理这个仓库的 docs 结构，然后给我一个落地改造方案。"
- "把这个功能的文档、dev_status、history 一起理顺。"
- "这个排障过程需要补到 docs 里，你按规范带我走完整流程。"
- "我不确定这块应该写到 platform 还是 app 文档，你来判断并落地。"
- "这个需求已经有 spec 了，我现在要开始改代码，你先帮我做实现前桥接和验证计划。"

## Companion files
- Use `references/bootstrap_and_states.md` for the compact state/bootstrap cheat sheet if you need a quick refresher.
- Use `references/implementation_bridge.md` when the task is moving from requirement/spec into code and verification.
