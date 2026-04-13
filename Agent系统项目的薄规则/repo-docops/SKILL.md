---
name: repo-docops
description: Use when working on this repository's code, docs, architecture, troubleshooting, or iteration tasks that need the local DocOps workflow, docs map, template loading policy, or dev_status maintenance rules
---

# Repo DocOps

This skill is the detailed workflow for repo-scoped DocOps tasks in `feat-langchain`.
The always-on subset lives in `/home/jack/agent-project/agent-middleware-space/feat-langchain/AGENTS.md`.
The preserved source document lives in `/home/jack/agent-project/agent-middleware-space/feat-langchain/.agents/AGENTS.md`.

## When To Use

Use this skill when the task touches repository code or docs and any of the following apply:

- More than one file will change
- The task involves architecture, troubleshooting, or iteration history
- You need project context from `docs/**`
- You need to update `docs/dev_status/**`
- You need to edit docs using `docs/_meta/templates.md`

Do not load this skill for unrelated general questions.

## Core Rules

- Never fabricate repository state, outputs, configs, or prior history.
- If a required file or output is unavailable, explicitly enter degraded mode: say what is missing, request the minimum missing inputs, and mark assumptions and risks.
- Every verification statement must be labeled `VERIFIED`, `BROKEN`, or `UNVERIFIED`.
- Any `docs/dev_status/**` update must include an explicit Track tag. If the user did not provide one, confirm first; if that is not possible, proceed only with `PLATFORM-GENERAL` as an assumption.
- App-specific material belongs in `docs/apps/<app>/**`; cross-app guidance belongs in `docs/platform/**`.
- If code changes affect API, data, workflow, or deployment, update the corresponding docs in the same task.

## Bootstrap Order

For non-trivial repo tasks, read only what is needed in this order:

1. `docs/00_project_index.md`
2. `docs/dev_status/active_task.md`
3. If an app is involved: `docs/apps/<app>/00_readme.md`
4. If contracts, fields, or schemas are involved: `docs/apps/<app>/dictionary/*.md`
5. If deployment, domains, routing, or ops are involved: app ops first, then `docs/platform/ops/**`
6. If writing or restructuring docs: `docs/_meta/templates.md` using the template loading rule below

## Template Loading Rule

Never import all of `docs/_meta/templates.md`.

- Read its Routing Table first
- Then load only the needed template block marked by `<!-- TEMPLATE:XXX:BEGIN -->`
- For micro-edits that only change a small passage and do not change structure, use only the Checklist section as a quality gate

## Working States

Keep the task in one of these states:

- `PLANNING`: requirements unclear, ask one batch of key questions and mark assumptions
- `DESIGN`: compare approaches, define interfaces/data/risk/acceptance
- `IMPLEMENTING`: list code and doc changes plus compatibility and rollback notes
- `VERIFYING`: run checks and report labeled outcomes
- `DONE`: archive progress, reset active status for the current Track, and identify the next target if needed

## Idea Parking

When the user says an idea is for later:

- Simple idea: add it to the top of `docs/dev_status/todo.md` with `**<TRACK> / <AREA>**`
- Multi-step or architecture-heavy idea: create a draft design doc in the right docs area and add a todo summary linking to it

## dev_status Update Rule

When editing `docs/dev_status/**`:

- Only update the current Track block in `active_task.md` and its overview row
- Never rewrite unrelated Track blocks
- In `history_log.md`, each entry may contain exactly one Track
- If the conversation pauses before completion, update `active_task.md` for the current Track with objective, context, focus, and next actions
- If the task is complete and user-confirmed, write a top-entry summary into `history_log.md` and reset or update the current Track status

## Delivery Format

For design, implementation, or verification outputs, include:

1. Summary: why and what
2. Docs changes: paths and key points
3. Code changes: paths and key points
4. Verification: commands, expected result, and `VERIFIED` / `BROKEN` / `UNVERIFIED`
5. Risks and rollback: compatibility risk, follow-up risk, and rollback path
