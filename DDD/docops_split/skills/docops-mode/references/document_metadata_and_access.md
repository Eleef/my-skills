---
name: document-metadata-and-access
description: Metadata-first rules for keeping document routing and reads or writes bounded as the repository grows.
---

## 1. Required front matter for managed markdown
Managed markdown under `docs/**` and `spec/**` should start with YAML front matter unless the file is generated, exported, or an explicitly temporary scratch note.

Minimum keys:

```yaml
---
kind: feature_spec
scope: app:<app>
lifecycle: draft
authority: published_reference
summary: One-line description of what this doc is for.
updated_at: "YYYY-MM-DD HH:MM (TZ)"
---
```

### Key meaning
- `kind`: document family used for routing and body access rules
- `scope`: repo / platform / app / track scope, such as `repo`, `platform:auth`, `app:upwork`, `track:APP-UPWORK`
- `lifecycle`: document lifecycle such as `draft`, `active`, `stable`, `deprecated`, or `archived`
- `authority`: how strongly other work should rely on this doc, such as `workspace`, `published_reference`, `app_contract`, `platform_contract`, `workflow_record`, `incident_record`, or `decision_record`
- `summary`: one short sentence for quick triage
- `updated_at`: last meaningful content change in the repository timestamp format

### Track scope for shared `dev_status` files
- Shared files such as `docs/dev_status/active_task.md`, `docs/dev_status/todo.md`, and `docs/dev_status/history_log.md` are usually multi-track documents.
- For shared files, use a shared file scope such as `repo` and keep track identity in section headings, checklist items, or history entry titles.
- Use file-level `scope: track:<TRACK>` and an optional `track` key only when the repository intentionally stores one file per track.

## 1.5 Lightweight front matter for skill references
Files under `skills/**/references/**` may also start with YAML front matter so they can follow the same metadata-first triage pattern.

Minimum keys:

```yaml
---
name: handoff-and-delivery
description: Low-frequency boundary guidance for pause, completion, and delivery handling.
---
```

Guidelines:
- keep reference metadata to `name` and `description` only
- prefer short stable names that are easy to scan in batch output
- keep `description` to one sentence focused on what the note is for
- do not copy the full managed-doc schema into skill references unless a real routing need appears

## 2. Read protocol
For managed docs, use this default read order:
1. Read YAML front matter
2. Decide whether the doc is in scope from `kind`, `scope`, `lifecycle`, `authority`, and `summary`
3. Read only the body sections allowed by the kind-specific rules below
4. Expand to more sections only when the current task truly requires it

Optional helper for larger doc trees:
- Use `skills/docops-mode/scripts/metadata_index.py` when you need a bounded batch scan of front matter before deciding which files to open deeply.
- Treat the helper as a triage accelerator, not as a replacement for reading the relevant target body sections before editing.
- For `skills/**/references/**`, `name` and `description` are usually enough for batch triage.

### Progressive loading must be operational
- Prompt wording alone does not prove that staged loading happened.
- Only describe the read path as metadata-first or progressive when the actual access sequence followed it.
- Preferred observable access modes:
  1. bounded metadata scan via `skills/docops-mode/scripts/metadata_index.py`
  2. bounded head/window read for log-like or status docs
  3. stable-anchor or target-section read for contract and structured docs
  4. full-file read only with an explicit reason
- If tooling forces a broader read than desired, state the limitation instead of claiming bounded access.
- For repo-wide or doc-heavy tasks, record a short `Doc Access Notes` summary in the delivery so reviewers can verify the access pattern.

If front matter is missing:
- note the metadata debt
- infer the likely `kind` and `scope` from path and headings
- avoid broad reads until the file is repaired

## 3. Kind-specific body access rules
### `requirements_draft`
- Typical path: `spec/features/<feature-key>/01_requirements.md`
- Read: front matter, summary paragraph, open sections being discussed
- Write: patch by heading
- Notes: do not publish as final authority

### `acceptance_note`
- Typical path: `spec/features/<feature-key>/02_acceptance.md`
- Read: front matter, acceptance checklist, unresolved items
- Write: patch checklist items or acceptance headings
- Notes: treat as working acceptance source until promoted

### `open_questions`
- Typical path: `spec/features/<feature-key>/03_open_questions.md`
- Read: front matter and newest unresolved items first
- Write: prepend or patch the affected question block
- Notes: keep resolved items clearly marked or moved out

### `implementation_notes`
- Typical path: `spec/features/<feature-key>/04_implementation_notes.md`
- Read: front matter, current plan, touched code areas
- Write: patch by heading
- Notes: keep concise; promote durable knowledge elsewhere

### `verification_plan`
- Typical path: `spec/features/<feature-key>/05_verification_plan.md`
- Read: front matter, checklist, command blocks, expected outcomes
- Write: patch verification sections
- Notes: promote durable verification knowledge into published docs when needed

### `project_index`
- Read: front matter, top summary, navigation sections only
- Write: patch by section
- Notes: preserve navigation order and stable links

### `platform_doc`
- Read: front matter, purpose/scope, target section only
- Write: patch by section
- Notes: keep app-specific detail out

### `platform_api_schema`
- Typical path: `docs/platform/<component>/specs/api_schema.md`
- Read: front matter, then only the relevant endpoint anchor
- Write: patch by stable endpoint heading
- Notes: preserve stable heading format and downstream app references

### `platform_data_schema`
- Typical path: `docs/platform/<component>/specs/data_schema.md`
- Read: front matter, then only the relevant table or entity anchor
- Write: patch by stable table or entity heading
- Notes: preserve stable heading format and cross-app constraints

### `platform_ui_schema`
- Typical path: `docs/platform/<component>/specs/ui_schema.md`
- Read: front matter, then only the relevant route/state/event/error section
- Write: patch by stable section heading
- Notes: keep reusable platform behavior separate from app-local UI detail

### `platform_standard`
- Read: front matter, purpose, rule set, verification section
- Write: patch by heading
- Notes: preserve examples and rule numbering when present

### `app_readme`
- Read: front matter, summary, quick links, target section
- Write: patch by section
- Notes: avoid deep full-file reads unless restructuring

### `feature_spec`
- Read: front matter, goal/scope/acceptance, then only target sections
- Write: patch by stable section heading
- Notes: keep contract detail in authority docs, not copied into the feature doc

### `dictionary_api_schema`
- Read: front matter, then only the relevant endpoint anchor
- Write: patch by stable endpoint heading
- Notes: preserve stable heading format and avoid whole-file scans by default

### `dictionary_data_schema`
- Read: front matter, then only the relevant table anchor
- Write: patch by stable table heading
- Notes: preserve stable heading format and constraints structure

### `dictionary_ui_schema`
- Read: front matter, then only the relevant route/state/event/error section
- Write: patch by stable section heading
- Notes: avoid rereading unrelated pages or events

### `dev_status_active_task`
- Read: front matter, then current track block first
- Write: patch the current track block only
- Notes: shared files are usually multi-track, so track identity lives in the heading block; do not rewrite unrelated tracks; keep large draft content out of this file

### `dev_status_todo`
- Read: front matter plus the first 30-60 body lines by default
- Write: prepend new items at the top
- Notes: newest first; in shared files, keep track labels on each entry instead of in file-level front matter

### `dev_status_history`
- Read: front matter plus the first 40-80 body lines by default
- Write: prepend new single-track entries at the top
- Notes: newest first; in shared files, keep track labels in each entry heading; usually no need to read deep history unless explicitly requested

### `issue`
- Read: front matter, symptom/root-cause/resolution summary, latest verification
- Write: patch the affected sections or append the latest resolution details
- Notes: keep logs redacted

### `adr`
- Read: front matter, context, decision, consequences
- Write: patch consequences/follow-ups or append targeted clarifications
- Notes: do not disturb decision wording casually once accepted

## 4. Write protocol
- Prefer targeted writes over broad rewrites.
- Preserve stable headings and anchors used by other docs.
- Update front matter fields when the body meaning changes, especially `summary`, `lifecycle`, and `updated_at`.
- For ordered logs such as todo/history, preserve newest-first ordering.
- For authority docs, update only the affected anchors unless the task is explicitly structural.
- For shared `dev_status` files, keep track identity at the section or entry level unless the repository explicitly uses one-file-per-track.
