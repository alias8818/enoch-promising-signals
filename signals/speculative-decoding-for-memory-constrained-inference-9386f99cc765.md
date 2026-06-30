# Speculative Decoding for Memory-Constrained Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-for-memory-constrained-inference-9386f99cc765`
Run ID: `speculative-decoding-for-memory-constrained-inference-9386f99cc765-20260611T033747533784+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a1a3c6f35e71

## What looked useful

A GPU-resident draft broke memory fit in 108 of 864 target-fitting modeled cases. Offloaded drafting produced 54 high-acceptance opportunity cases where GPU fit was preserved and expected target calls dropped by at least 35%. The microbenchmark confirmed the mechanism: 100% acceptance reduced target forwards from 65 to 9 at lookahead 8, while 0% acceptance increased target forwards to 129 and slowed decoding.

## Boundaries and scale limits

Direct runtime evidence used a tiny random GPT-2-style model with synthetic acceptance controls on GB10. The 7B/13B results are formula-based fp16 memory and target-call projections, not measured full-model serving runs.

## Claim scope

Local proxy evidence shows that speculative decoding under tight accelerator memory is only attractive when draft memory is offloaded or very small and draft acceptance is high; ordinary GPU-resident drafting can break target-only memory fit.

## Why it stopped

This is proxy/early evidence, not full validation: it narrows the viable claim and rejects the broad memory-constrained inference claim as stated, but real-model offloaded drafting must be measured before any paper-positive decision.

## Recommended next action

Run a bounded deepen test with real small target/draft models under an enforced accelerator memory cap, comparing GPU-resident draft, CPU/offloaded draft, and target-only baseline on real prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Offloaded Drafting Under Accelerator Memory Cap
- Success threshold: Offloaded draft preserves target-only memory fit and improves tokens/s by at least 15% at acceptance >= 0.7 in a case where GPU-resident draft exceeds the memory cap or reduces feasible context/batch.
- Stop condition: Stop if measured acceptance is below 0.5 across real prompts, CPU/offloaded draft latency erases target-call savings, or no tested configuration creates a target-fits/gpu-draft-does-not-fit memory boundary.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-for-memory-constrained-inference-9386f99cc765`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
