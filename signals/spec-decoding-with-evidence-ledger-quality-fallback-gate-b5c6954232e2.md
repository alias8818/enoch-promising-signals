# Spec Decoding with Evidence-Ledger Quality Fallback Gate

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spec-decoding-with-evidence-ledger-quality-fallback-gate-b5c6954232e2`
Run ID: `spec-decoding-with-evidence-ledger-quality-fallback-gate-b5c6954232e2-20260629T111656161482+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/44e2a0250434

## What looked useful

Across 1,200 synthetic sequences per condition, ledger gating improved draft-only exact match from 0.8557 to 0.9691 at 14.7% target calls for high-quality draft settings, but confidence-only gating was competitive and beat ledger gating at the low-quality <=45% target-call point.

## Boundaries and scale limits

No real LLMs, no real speculative-decoding acceptance kernel, no benchmark text, no wall-clock serving latency, and no GPU inference. Target-call fraction is a proxy for cost.

## Claim scope

Synthetic deterministic decoding probe only: an evidence-ledger fallback gate can recover much of target-token quality at reduced target-call fraction when draft evidence is informative, especially at medium/high draft quality.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and mixed against a simpler confidence-gate baseline, not a full validation.

## Recommended next action

Run a bounded real-model deepen test comparing ledger gating against confidence-only gating and exact speculative decoding on a small fixed text benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-model ledger-gated speculative decoding benchmark
- Success threshold: Ledger gating must beat confidence-only gating by at least 2% relative target-call reduction at matched target NLL, or at least 2% relative target NLL reduction at matched latency, across most tested seeds.
- Stop condition: Stop if ledger gating fails to beat confidence-only gating on both quality and cost/latency at the small-model scale.

## Evidence references

- Artifact root: `<local-path>/projects/spec-decoding-with-evidence-ledger-quality-fallback-gate-b5c6954232e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
