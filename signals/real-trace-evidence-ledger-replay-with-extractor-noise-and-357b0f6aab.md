# Real-trace evidence ledger replay with extractor noise and downstream QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-evidence-ledger-replay-with-extractor-noise-and-357b0f6aab`
Run ID: `real-trace-evidence-ledger-replay-with-extractor-noise-and-357b0f6aab-20260525T110510919670+0000`

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

- Parent run decision: Evidence Ledger Compression for Long Agent Runs on Memory-Constrained CPU: enoch://control-plane/projects/evidence-ledger-compression-for-long-agent-runs-on-memory-constrained-cpu-bd136dad7647/runs/evidence-ledger-compression-for-long-agent-runs-on-memory-constrained-cpu-bd136dad7647-20260525T101421030788+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/74ba39470e6c

## What looked useful

At 20% drop, 20% flip, and 20% spurious noise, confidence-weighted replay reached 0.772 mean exact QA versus 0.430 for latest-write replay. Redundant facts with at least three clean records reached about 0.960 exact QA, while single-record facts reached about 0.634, showing that replay robustness depends on evidence redundancy.

## Boundaries and scale limits

Single project trace bundle; 15 deterministic QA facts; 35 clean evidence records; synthetic extractor noise; exact lookup QA rather than open-ended QA; CPU-only Tier 1 controlled small direct test.

## Claim scope

On one real local Enoch/Codex trace bundle with synthetic extractor drop/flip/spurious noise, confidence/consensus evidence-ledger replay improves downstream exact QA over latest-write replay, but only reaches high reliability for facts with redundant evidence.

## Why it stopped

Tier 1 direct test produced a useful but no-paper mixed result: replay policies improve robustness, but overall QA reliability under 20% matched noise is too low because many facts have only singleton evidence.

## Recommended next action

Run a bounded deepen test on 20-50 real agent trace bundles using real extractor outputs and a redundancy-aware abstention policy; stop if redundant facts do not maintain at least 0.93 exact QA at 20% observed extractor error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Redundancy-aware evidence ledger replay on multi-trace real extractor outputs
- Success threshold: At observed extractor error near or above 20%, redundant facts must reach >=0.93 exact QA, false answers must drop >=30% versus latest-write replay, and abstention must be concentrated on singleton or contradictory evidence.
- Stop condition: Stop as negative if redundant facts fall below 0.90 exact QA or if false-answer reduction versus latest-write replay is below 15% on the multi-trace real-extractor corpus.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-replay-with-extractor-noise-and-357b0f6aab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
