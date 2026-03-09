# Spec-to-Implementation Bridge

Use this note when a task is moving from clarified requirement into actual implementation.

## Implementation entry checklist
Before coding, make these explicit:
- Requirement being solved
- Primary spec docs
- Applicable standards / ADRs / platform constraints
- Expected code areas to change
- Expected doc areas to change
- Acceptance criteria to verify
- Verification plan

## Mapping rules
### If the change is feature-level
- Feature doc carries goal, scope, UX, and acceptance criteria.
- Dictionary docs carry API/data/UI contracts.
- Code implements the behavior defined there.

### If the change is contract-level
- Update the authority spec first or atomically with code.
- Use `docs/apps/<app>/dictionary/**` for app-owned contracts.
- Use `docs/platform/<component>/specs/**` for platform-owned shared contracts.
- Feature docs should reference the changed contract, not restate it.

### If the change is reusable across apps
- Add or update a standards doc under `docs/platform/standards/**`.
- Link the standard from feature, ADR, or implementation notes as needed.

### If the change is architectural
- Record the decision in ADR when the tradeoff matters beyond one local patch.

## Verification mapping
- Every meaningful acceptance criterion should have a verification step.
- If no runnable command exists, define a smoke check or observable outcome.
- If verification fails, do not claim completion; mark `BROKEN` and capture the gap.

## Closure mapping
At completion, make sure the final state is reflected in:
- implementation or code summary
- changed docs
- verification status
- relevant `dev_status/**` files
- issue/troubleshooting/ADR entries if the work produced lasting operational knowledge
