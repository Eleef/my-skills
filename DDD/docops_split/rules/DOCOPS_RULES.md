# DocOps Rules Core
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
- `Working state` applies only to the current task or track and its in-scope artifacts, not to the whole `docs/**` tree.
- `Verification labels` tell the evidence status of a specific result.
- They are independent: one task should have one main working state, while a response may include multiple verification labels.

## Track tagging for dev status
- Any update involving `docs/dev_status/**` must specify a track in the edited block, entry, or handoff note.
- Shared `docs/dev_status/**` files may carry multiple tracks at once; keep track identity in section headings or log entries instead of forcing a single file-level track in front matter.
- If the repository intentionally uses one file per track, file-level `scope: track:<TRACK>` is still valid.
- If the user did not specify one, ask first.
- If a temporary assumption is required, use `PLATFORM-GENERAL` and label it as an assumption.

## Active workspace vs published docs
- Prefer `spec/**` as the active workspace for in-flight stage material such as requirements drafts, acceptance notes, open questions, implementation notes, and verification plans.
- Treat `docs/**` as the published knowledge base and authority surface rather than the default place for every evolving draft.
- `docs/dev_status/**` should stay small and act as an index to the current `spec/**` work area, relevant published docs, and key code paths when available.
- Do not treat the whole `docs/**` tree as being in the current working state; only files directly in scope for the current task are active.
- When a draft becomes an authority or durable project reference, publish it into the appropriate `docs/**` location.
- At stage completion, archive, summarize, or retire stage-only `spec/**` notes so they do not become hidden long-term state.

## Managed markdown metadata and access
- Managed markdown docs under `docs/**` and `spec/**` should start with YAML front matter unless the file is generated, exported, or an explicitly temporary scratch note.
- Minimum front matter keys:
  - `kind`
  - `scope`
  - `lifecycle`
  - `authority`
  - `summary`
  - `updated_at`
- Read front matter first before reading the body of a managed doc.
- Let `kind` drive body access rules such as read window, stable anchors, append-vs-patch behavior, and ordering expectations.
- If a managed doc is missing front matter, treat it as metadata debt: infer the route carefully for the current task and add or repair metadata when touching the file.
- For body access rules, prefer kind-specific partial reads and targeted writes instead of loading full files by default.
- Do not claim metadata-first or progressive loading unless the actual access path followed it.
- When bounded access matters, make the read path observable through a metadata scan, bounded window read, or explicit stable-anchor read before expanding further.
- If the task or available tooling forces a full-file read, say so explicitly and state why the broader read was necessary.

## SSOT and atomic updates
- App-scoped fields, contracts, schema, table structures, and API behavior are authoritative only in `docs/apps/<app>/dictionary/**`.
- Platform-shared API, data, UI, or other reusable contracts may be authoritative in `docs/platform/<component>/specs/**` when the owner is a reusable platform component or service.
- `features/**` may reference authority docs but must not maintain a second schema copy.
- If code changes affect API, data, workflow, or deployment behavior, update the corresponding docs in the same task.

## Skill handoff
- For heavier document work, use a dedicated DocOps workflow skill instead of expanding these rules.
- For template selection, routing, and checklist-driven drafting, use a dedicated template skill instead of keeping template details in always-on rules.
- Keep always-on rules focused on scope, metadata, SSOT, and truthfulness; leave low-frequency delivery, handoff, and checkpoint procedures to the DocOps workflow skill.
