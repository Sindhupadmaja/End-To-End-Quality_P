# Risk Register

| Risk | Impact | Likelihood | Change Surface | Score | Level | Mitigation |
|---|---:|---:|---:|---:|---|---|
| Duplicate transaction | 5 | 4 | 5 | 100 | Critical | Idempotency API tests + regression |
| Incorrect transaction amount | 5 | 3 | 4 | 60 | High | Boundary and negative tests |
| UI state not refreshed | 4 | 3 | 4 | 48 | High | Critical-path UI automation |
| Authentication failure | 5 | 2 | 3 | 30 | High | API negative testing |
| Error response mismatch | 3 | 3 | 2 | 18 | Medium | Contract validation |
| Rollback failure | 5 | 2 | 2 | 20 | Medium | Deployment rehearsal |

## Prioritization

The highest-risk behavior receives:

1. deeper test design
2. automation
3. regression protection
4. explicit release-gate visibility
