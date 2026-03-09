# DocOps Rules Core

> Purpose: lightweight always-on rules extracted from `doc-ops-prompt.md`.
> Use this as the persistent rules layer. Keep it short and stable.

## Scope gate
- Only apply these rules when the user request is related to this repository's code, docs, architecture, debugging, or iteration workflow.
- If the request is explicitly unrelated to this project, do not force DocOps workflow or `dev_status` updates.

## Reality and verification
- Do not invent repository files, outputs, config, history, or runtime behavior.
- If a file or output is unavailable, say so explicitly and ask for the minimum missing inputs.
- Use explicit verification labels in delivery:
  - `VERIFIED`: actually run and passed, with command and short output summary.
  - `BROKEN`: actually run and failed, with repro steps, error summary, and next fix direction.
  - `UNVERIFIED`: not run or no proof available.

## Working state vs verification
- `Working state` tells where the task is in the workflow.
- `Verification labels` tell the evidence status of a specific result.
- They are independent: one task should have one main working state, while a response may include multiple verification labels.

## Track tagging for dev status
- Any update involving `docs/dev_status/**` must specify a track.
- If the user did not specify one, ask first.
- If a temporary assumption is required, use `PLATFORM-GENERAL` and label it as an assumption.

## SSOT and atomic updates
- App-scoped fields, contracts, schema, table structures, and API behavior are authoritative only in `docs/apps/<app>/dictionary/**`.
- Platform-shared contracts or specs may be authoritative in `docs/platform/<component>/specs/**` when the owner is a reusable platform component or service.
- `features/**` may reference authority docs but must not maintain a second schema copy.
- If code changes affect API, data, workflow, or deployment behavior, update the corresponding docs in the same task.

## Delivery format
When providing DESIGN / IMPLEMENTING / VERIFYING style results, include:
1. Current Working State
2. Summary (why / what)
3. Docs changes (paths + key points)
4. Code changes (paths + key points)
5. Verification (commands + expectation + VERIFIED/BROKEN/UNVERIFIED)
6. Risks and rollback

**Short example:**
- Current Working State: `IMPLEMENTING`
- Verification:
  - unit tests: `VERIFIED`
  - end-to-end flow: `UNVERIFIED`

## Completion discipline
- If work pauses before completion, update the active task context for the relevant track only.
- Do not overwrite other tracks in `active_task.md`.
- `history_log.md` entries must be single-track entries.
- When the user confirms completion, add a concise top-entry history record and reset or update the relevant active state.

## Git and dev-status checkpoint sync
- Treat a stable git commit and `docs/dev_status/**` update as the same handoff checkpoint when work reaches a meaningful boundary, such as feature completion, stage completion, pause handoff, or a stable intermediate milestone worth preserving.
- If that checkpoint needs a git commit, update the relevant dev-status files before or together with the commit.
- If dev status is updated without a commit, state why, such as pending verification, WIP-only state, or no clean commit boundary yet.
- Do not force this on every tiny edit or exploratory commit.

## Skill handoff
- For heavier document work, use a dedicated DocOps workflow skill instead of expanding these rules.
- For template selection, routing, and checklist-driven drafting, use a dedicated template skill instead of keeping template details in always-on rules.
