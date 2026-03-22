# Document Metadata and Access Rules

Use this note to keep document routing and reads/writes small as the repository grows.

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

## 2. Read protocol
For managed docs, use this default read order:
1. Read YAML front matter
2. Decide whether the doc is in scope from `kind`, `scope`, `lifecycle`, `authority`, and `summary`
3. Read only the body sections allowed by the kind-specific rules below
4. Expand to more sections only when the current task truly requires it

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
- Notes: do not rewrite unrelated tracks; keep large draft content out of this file

### `dev_status_todo`
- Read: front matter plus the first 30-60 body lines by default
- Write: prepend new items at the top
- Notes: newest first

### `dev_status_history`
- Read: front matter plus the first 40-80 body lines by default
- Write: prepend new single-track entries at the top
- Notes: newest first; usually no need to read deep history unless explicitly requested

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
