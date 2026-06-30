# Asymmetric Quantization for Anchor KV States

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `asymmetric-quantization-for-anchor-kv-states-a3f55a63c9c5`
Run ID: `asymmetric-quantization-for-anchor-kv-states-a3f55a63c9c5-20260525T151901478158+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccacb4f92101

## What looked useful

Across 80 synthetic workloads, anchor K6/V2 improved base top-1 preservation over uniform 4/4 (0.996948 vs 0.995386) but worsened output MSE (8.756e-06 vs 4.998e-06). Anchor K2/V6 failed routing badly (0.947778 base top-1 preserved), while K4/V8 had the best output MSE among practical policies (4.869e-06) without routing gains.

## Boundaries and scale limits

Attention-level proxy only: no trained transformer, no natural-language long-context benchmark, no packed low-bit KV-cache kernel, no latency or end-to-end decoding quality validation.

## Claim scope

Synthetic anchor-retrieval attention on GB10 shows anchor key precision improves argmax routing preservation under hard distractors, but key-heavy asymmetric anchor KV allocation does not improve overall output fidelity under the tested local bit budgets.

## Why it stopped

No-paper useful signal: this proxy supports routing sensitivity of anchor keys but early-falsifies the broader key-heavy asymmetric anchor KV claim for output fidelity under the tested bit budgets.

## Recommended next action

Run a bounded tiny-transformer cached-decoding retrieval benchmark before any larger scale-up; stop if key-heavy anchor quantization still fails to beat uniform/value-heavy policies on both retrieval and output/logit fidelity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Cached-Decoding Test for Anchor KV Bit Allocation
- Success threshold: Key-heavy anchor quantization must improve retrieval by at least 0.5 percentage points over uniform 4/4 while keeping logit KL/cross-entropy delta no worse than the best uniform or value-heavy policy within 5%.
- Stop condition: Stop as negative if key-heavy policies improve routing but again lose on output/logit fidelity, or if they fail to improve retrieval by at least 0.5 percentage points over uniform 4/4.

## Evidence references

- Artifact root: `<local-path>/projects/asymmetric-quantization-for-anchor-kv-states-a3f55a63c9c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
