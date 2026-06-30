# Real Trace Evaluation of Structured Tool-Call Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evaluation-of-structured-tool-call-evidence-led-21caf06d0e`
Run ID: `real-trace-evaluation-of-structured-tool-call-evidence-led-21caf06d0e-20260525T151901057231+0000`

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

- Parent run decision: Structured Evidence Ledger for Tool-Call Verification: enoch://control-plane/projects/structured-evidence-ledger-for-tool-call-verification-ff7d3bdd026a/runs/structured-evidence-ledger-for-tool-call-verification-ff7d3bdd026a-20260525T135741103565+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aea5c8197654

## What looked useful

Structured verification matched 25/25 real agent-message metric claims and rejected 24/24 counterfactual swaps, while raw substring matching false-accepted 24/24 counterfactuals.

## Boundaries and scale limits

Tested on 40 local ledger/trace/tool-related Codex logs with 25 extracted natural metric claims and 24 controlled counterfactual swaps; regex claim extraction and numeric/tool-output facts only.

## Claim scope

A structured key/value ledger built from real Codex tool-call traces can verify agent-written numeric metric claims and reject same-output numeric counterfactual swaps in a small local real-trace sample.

## Why it stopped

Tier 1 real-trace evidence supports the mechanism for numeric tool-output claims, but it is not broad or natural enough for paper-positive closure.

## Recommended next action

Run a bounded labeled natural-unsupported-claim benchmark using the same real-trace ledger, with richer claim extraction and blind/deterministic labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Labeled Natural Unsupported-Claim Audit for Real Tool-Call Evidence Ledgers
- Success threshold: At least 100 labeled natural claims, structured-ledger false-accept rate at least 50% lower than substring matching, supported-claim precision at or above 0.90, and no unhandled parser crashes.
- Stop condition: Stop as negative if fewer than 50 labelable natural claims are found in the frozen corpus or if structured verification does not reduce false accepts versus substring matching.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evaluation-of-structured-tool-call-evidence-led-21caf06d0e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
