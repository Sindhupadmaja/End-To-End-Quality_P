# Risk-Based Test Plan

## Objective

Determine whether the release is safe enough to move toward production based on business risk and measurable evidence.

## Test scope

### Functional
- authentication
- transaction creation
- idempotency
- amount validation
- transaction status
- transaction history

### Non-functional focus
- API response correctness
- validation quality
- basic UI reliability
- release readiness
- rollback readiness

## Priority matrix

| Priority | Meaning | Execution |
|---|---|---|
| P0 | Release blocker | Every release |
| P1 | Critical business path | Every release |
| P2 | Important supporting behavior | Regression cycle |
| P3 | Low-risk/cosmetic | As capacity permits |

## Negative testing

Negative cases intentionally validate:

- invalid credentials
- zero amount
- negative amount
- duplicate requests
- malformed payloads
- missing required fields

## Defect severity

**Critical:** financial/security integrity or release-blocking failure.

**High:** major business path failure without an acceptable workaround.

**Medium:** degraded functionality with workaround.

**Low:** cosmetic or low-impact issue.
