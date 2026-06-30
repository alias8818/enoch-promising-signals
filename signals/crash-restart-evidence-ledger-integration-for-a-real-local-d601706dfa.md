# Crash-restart evidence ledger integration for a real local agent loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-restart-evidence-ledger-integration-for-a-real-local-d601706dfa`
Run ID: `crash-restart-evidence-ledger-integration-for-a-real-local-d601706dfa-20260523T075504346532+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence ledger for small local agents with hash rollback: enoch://control-plane/projects/evidence-ledger-for-small-local-agents-with-hash-rollback-285fb95e160d/runs/evidence-ledger-for-small-local-agents-with-hash-rollback-285fb95e160d-20260523T060034565690+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c8b93e0fc7

## What looked useful

Ledger-backed restart completed 20/20 trials after 108 hard exits with 0 duplicate side effects, 0 missing side effects, 0 missing completion events, and 20/20 valid hash chains; the volatile control completed only 9/20 trials and produced 16163 duplicate side effects under the same restart bound.

## Boundaries and scale limits

Small single-host Tier 1 run only: 20 trials, 30 items per trial, one worker at a time, filesystem side effects, no real LangGraph/Enoch controller integration, no real LLM calls, no host reboot, no concurrent writers, and no crash injection between external side effect and durable completion event.

## Claim scope

In a controlled local subprocess agent-loop harness, a SQLite evidence ledger used as the restart source of truth recovered completed work across injected hard process exits and prevented duplicate filesystem side effects for ledgered completed items.

## Why it stopped

Tier 1 direct harness supports the restart-ledger mechanism but is not full validation or paper-ready because it omits production loop integration, concurrent writers, reboot/power-loss behavior, and the hardest side-effect crash windows.

## Recommended next action

Run a deepen follow-up that injects crashes before and after non-idempotent side effects in an actual LangGraph or Enoch local loop, using idempotency keys or a two-phase effect protocol as the success criterion.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-window evidence ledger test inside a real LangGraph local loop
- Success threshold: Across at least 50 injected-crash trials and all crash windows, the integrated loop completes every planned item with zero duplicate committed side effects, zero missing committed side effects, all orphan intents either recovered or explicitly marked abandoned, and valid ledger integrity checks.
- Stop condition: Stop as unsupported if any crash window produces unrecoverable duplicate committed side effects or ledger divergence under the idempotency/two-phase protocol.

## Evidence references

- Artifact root: `<local-path>/projects/crash-restart-evidence-ledger-integration-for-a-real-local-d601706dfa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
