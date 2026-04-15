---
name: handoff-and-delivery
description: Low-frequency boundary guidance for pause, completion, and structured delivery handling.
---

## 1. Park ideas that are not ready to implement
If the user says "not now", "later", or shares a rough idea without wanting execution yet:
- add a concise item to `docs/dev_status/todo.md` for simple future work
- create a draft design or standards note for larger ideas, then link it from todo
- keep the note small, explicit, and track-tagged

## 2. Structured delivery format
For DESIGN / IMPLEMENTING / VERIFYING outputs, use this structure:
1. Current Working State
2. Summary
3. Doc Access Notes (for doc-heavy or repo-wide tasks)
4. Spec workspace changes
5. Docs changes
6. Code changes
7. Verification
8. Risks and rollback

Use explicit `VERIFIED`, `BROKEN`, or `UNVERIFIED` labels.

Short example:
- Current Working State: `VERIFYING`
- Verification:
  - smoke test: `VERIFIED`
  - production parity check: `UNVERIFIED`

## 3. Pause and completion handling
If pausing mid-task:
- update only the relevant track block in `active_task.md`
- do not overwrite unrelated tracks
- preserve objective, current focus, and next actions
- point to the active `spec/**` work area and relevant published docs instead of copying large draft content into `active_task.md`
- if you are preserving a stable handoff checkpoint with git, sync the relevant dev-status update before or together with that commit
- if dev status is updated without a commit, state why the work is still WIP or why no clean commit boundary exists yet

If the task is completed and confirmed:
- add a concise top-entry summary to `history_log.md`
- reset or update the active state for that track
- keep each history entry single-track
- if the result should be preserved as a completion or stage-complete commit, make sure the dev-status updates land before or together with that commit
- publish stable outputs from `spec/**` into `docs/**` and archive, summarize, or retire remaining stage-only drafts

## 4. Git and dev-status checkpoint sync
- Treat a stable git commit and `docs/dev_status/**` update as the same handoff checkpoint when work reaches a meaningful boundary, such as feature completion, stage completion, pause handoff, or a stable intermediate milestone worth preserving.
- If that checkpoint needs a git commit, update the relevant dev-status files before or together with the commit.
- If dev status is updated without a commit, state why, such as pending verification, WIP-only state, or no clean commit boundary yet.
- Do not force this on every tiny edit or exploratory commit.
