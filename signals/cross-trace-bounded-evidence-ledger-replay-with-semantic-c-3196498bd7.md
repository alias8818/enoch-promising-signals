# Cross-Trace Bounded Evidence Ledger Replay with Semantic Claim Checks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-trace-bounded-evidence-ledger-replay-with-semantic-c-3196498bd7`
Run ID: `cross-trace-bounded-evidence-ledger-replay-with-semantic-c-3196498bd7-20260607T085302671711+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Bounded Evidence Ledger for Agent Reliability: enoch://control-plane/projects/bounded-evidence-ledger-for-agent-reliability-94bd73bc056a/runs/bounded-evidence-ledger-for-agent-reliability-94bd73bc056a-20260607T040905432796+0000
- Parent run decision: Replay Bounded Evidence Ledger on Real Agent Tool Traces: enoch://control-plane/projects/replay-bounded-evidence-ledger-on-real-agent-tool-traces-d3748df8ac/runs/replay-bounded-evidence-ledger-on-real-agent-tool-traces-d3748df8ac-20260607T062038975331+0000

## What looked useful

Cross-trace replay beat text search by +0.484 macro F1 at a 280-event bound and the structured no-semantic ablation reached 0.855 macro F1 with a 560-event bound, but the semantic target only reached 0.675 macro F1 at that bound and overmatched unknown or contradicted claims.

## Boundaries and scale limits

600 synthetic cases and 28,800 claims per variant; template paraphrases rather than human-written traces; CPU-only local benchmark; no production evidence logs, LLM embeddings, or human adjudication.

## Claim scope

On a fixed-seed synthetic multi-trace claim-status benchmark, cross-trace structured replay is useful versus text search, but the tested semantic claim-check fallback does not improve over structured replay and introduces false positives.

## Why it stopped

Tier 2 fixed-seed benchmark produced a mixed/negative result for the core semantic claim-check mechanism: it beats weak text search but loses to a real structured replay ablation.

## Recommended next action

Stop paper path for the tested method; run a bounded follow-up only if semantic checks are redesigned as calibrated abstaining contradiction checks and evaluated against the structured no-semantic replay baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Abstaining Semantic Checks for Cross-Trace Evidence Replay
- Success threshold: At least +0.03 macro F1 over structured no-semantic replay and no more than 2% absolute increase in unknown->supported false positives on a fixed validation split.
- Stop condition: Stop if semantic abstention cannot outperform structured no-semantic replay across at least 3 fixed seeds or if unknown->supported false positives increase materially at the best macro-F1 threshold.

## Evidence references

- Artifact root: `<local-path>/projects/cross-trace-bounded-evidence-ledger-replay-with-semantic-c-3196498bd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
