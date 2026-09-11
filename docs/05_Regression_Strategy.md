# Regression Strategy

Regression is organized by risk rather than by executing every test blindly.

## Tier 0 — Smoke

- application starts
- API health endpoint responds
- basic UI loads

## Tier 1 — Critical regression

- authentication
- transaction creation
- idempotency
- amount validation
- transaction status

## Tier 2 — Extended regression

- transaction history
- error responses
- UI refresh behavior
- supporting workflows

## Automation strategy

Automate tests that are:

- deterministic
- repeated frequently
- business-critical
- expensive to execute manually
- valuable as release gates

Keep exploratory and highly visual checks available for human validation.

## Change-based selection

When a transaction service changes, execute Tier 0 + Tier 1 automatically and prioritize transaction-related Tier 2 tests.

When UI-only changes occur, execute Tier 0 + affected UI paths plus the API contract smoke suite.
