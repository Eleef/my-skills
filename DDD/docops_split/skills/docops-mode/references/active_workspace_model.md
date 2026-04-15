---
name: active-workspace-model
description: Working model for keeping active stage material in spec and durable knowledge in docs.
---

## Default split
- `spec/**` is the preferred active workspace for in-flight stage material.
- `docs/**` is the published knowledge base and authority surface.
- `docs/dev_status/**` is the lightweight state index that points to active work and published outputs.

## Typical `spec/**` contents
- `spec/00_index.md` for a small workspace index when needed
- `spec/features/<feature-key>/01_requirements.md`
- `spec/features/<feature-key>/02_acceptance.md`
- `spec/features/<feature-key>/03_open_questions.md`
- `spec/features/<feature-key>/04_implementation_notes.md`
- `spec/features/<feature-key>/05_verification_plan.md`

Use the smallest subset needed. Do not create every file by default.
Use the same minimal YAML front matter standard as managed docs under `docs/**`.

## What belongs in `docs/**`
- app-owned authority docs such as `docs/apps/<app>/dictionary/**`
- published feature specs that other work should reference
- platform standards and platform-owned shared specs
- issue write-ups, ADRs, and durable troubleshooting knowledge
- dev-status summaries and history records

## Publishing rules
- Keep unstable drafts, unresolved questions, and stage-specific working notes in `spec/**`.
- Publish to `docs/**` once the content becomes implementation authority, cross-session reference material, or durable operational knowledge.
- Do not leave the only authoritative contract in `spec/**`.
- When publishing, prefer linking from `spec/**` drafts to the final `docs/**` target instead of duplicating long sections.

## Dev-status role
- `active_task.md` should point to the current `spec/**` work area and relevant published docs when they exist.
- `todo.md` can point to either a future `spec/**` work area or a published design/doc path.
- `history_log.md` should summarize completed outcomes and point to the published docs or commits, not preserve the whole draft workspace.

## Closure
- At stage completion, publish stable outputs into `docs/**`.
- Archive, summarize, or retire remaining stage-only `spec/**` notes according to repository convention.
- Avoid leaving `spec/**` as an unbounded second docs tree.
