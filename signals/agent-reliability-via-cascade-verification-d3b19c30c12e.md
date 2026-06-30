# Agent Reliability via Cascade Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-via-cascade-verification-d3b19c30c12e`
Run ID: `agent-reliability-via-cascade-verification-d3b19c30c12e-20260523T154635161596+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72c532193db4

## What looked useful

Cascade verification is promising as a reliability mechanism when the target metric is accepted-error rate, but this run falsifies the stronger cost-efficiency version under the tested assumptions. Correlated verifier failures and repair cost are the critical risks to measure next.

## Boundaries and scale limits

100,000 synthetic trials per policy per scenario; no real LLM agents, no real verifier models, no executable or human-labeled benchmark, no latency or token accounting beyond synthetic cost units.

## Claim scope

Synthetic mechanism test of cascade verification policies over simulated agent answers, verifier errors, repair, confidence, and task ambiguity. Cascade reduced accepted wrong-answer rate versus no verification and slightly versus strong verification on every initial answer, but did not reduce cost versus strong verification and lost utility to a confidence gate under correlated/adversarial verifier failures.

## Why it stopped

Proxy-only synthetic result produced a useful mixed signal, but not direct evidence for deployed agent reliability or a paper-ready claim.

## Recommended next action

Run the same policy comparison on a small real-agent trace benchmark with executable or human ground truth before any larger scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace cascade verification with executable ground truth
- Success threshold: Cascade accepted-error rate is at least 25% lower than no verification and not worse than strong-all by more than 2 percentage points, while average cost is no more than 1.10x strong-all.
- Stop condition: Stop if cascade fails to beat no verification on accepted-error rate by 10% relative or if cost exceeds 1.25x strong-all without a compensating accepted-error improvement.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-cascade-verification-d3b19c30c12e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
