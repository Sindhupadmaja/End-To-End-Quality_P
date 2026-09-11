# Requirements Traceability Matrix

Traceability connects business intent to executable validation.

| Requirement | Risk | Tests | Coverage |
|---|---|---|---|
| REQ-001 Authentication | Critical | TC-001, TC-002 | Covered |
| REQ-002 Transaction creation | Critical | TC-003, TC-004 | Covered |
| REQ-003 Idempotency | Critical | TC-005 | Covered |
| REQ-004 Amount validation | High | TC-006, TC-007 | Covered |
| REQ-005 Status query | High | TC-008 | Covered |
| REQ-006 Transaction history | High | TC-009, TC-010 | Covered |
| REQ-007 API errors | Medium | TC-011 | Covered |
| REQ-008 Rollback | Medium | TC-012 | Partial |

## Coverage rule

A requirement is considered covered when at least one executable test exists and its expected behavior is explicit.

Critical requirements require positive and negative validation where applicable.
