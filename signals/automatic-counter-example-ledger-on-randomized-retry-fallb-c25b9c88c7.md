# Automatic counter-example ledger on randomized retry/fallback tool tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `automatic-counter-example-ledger-on-randomized-retry-fallb-c25b9c88c7`
Run ID: `automatic-counter-example-ledger-on-randomized-retry-fallb-c25b9c88c7-20260611T213845263711+0000`

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

- Parent run decision: Real-agent counter-example ledger on repeated tool-use failures: enoch://control-plane/projects/real-agent-counter-example-ledger-on-repeated-tool-use-fai-796c9749e3/runs/real-agent-counter-example-ledger-on-repeated-tool-use-fai-796c9749e3-20260611T204151375882+0000
- Parent run decision: Counter-Example Ledger: Negative-Memory Layer Reduces Repeated Failures: enoch://control-plane/projects/counter-example-ledger-negative-memory-layer-reduces-repeated-failures-48876d31d9e2/runs/counter-example-ledger-negative-memory-layer-reduces-repeated-failures-48876d31d9e2-20260611T184359910258+0000

## What looked useful

Contextual ledger duplicate counter-example task rate was 0.0 versus 0.0568125 for randomized retry/fallback, a 100% reduction. Success rate improved by 0.0041823 absolute versus baseline and by 0.0145677 absolute versus global blacklist. Exact memory only partially reduced recurrence, while coarse/global memory overblocked and reduced success.

## Boundaries and scale limits

The validation used simulated tasks and deterministic structural failure rules, not live LLM tool calls, real API failures, production traces, or multi-session stale-ledger drift. It covered 64 seeds and 192000 tasks per policy on local CPU.

## Claim scope

In a fixed-seed synthetic randomized retry/fallback tool-task simulator, a contextual automatic counter-example ledger keyed by tool, intent, data type, and constraint eliminated repeated structural counter-example attempts while preserving task success relative to a no-memory randomized retry/fallback baseline.

## Why it stopped

Tier 2 synthetic validation supports the mechanism but does not provide direct real-agent evidence needed for a paper.

## Recommended next action

Stop this run as no-paper useful signal; next, run the same ledger policies on real or recorded LLM tool-call traces with structural versus transient failure labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based counter-example ledger validation for LLM tool retries
- Success threshold: Contextual ledger reduces duplicate structural failure recurrence by at least 40% versus the strongest retry/fallback baseline, success rate drops by no more than 1 percentage point, and false skips remain below the coarse/global ablations.
- Stop condition: Stop as negative if contextual ledger fails the recurrence reduction threshold, loses more than 1 percentage point success, or cannot beat a learned-prior/best-of-N retry baseline on direct trace metrics.

## Evidence references

- Artifact root: `<local-path>/projects/automatic-counter-example-ledger-on-randomized-retry-fallb-c25b9c88c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
