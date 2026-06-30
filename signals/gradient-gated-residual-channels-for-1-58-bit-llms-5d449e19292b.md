# Gradient-Gated Residual Channels for 1.58-bit LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-gated-residual-channels-for-1-58-bit-llms-5d449e19292b`
Run ID: `gradient-gated-residual-channels-for-1-58-bit-llms-5d449e19292b-20260531T142231592660+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58a9b8942e46

## What looked useful

Sparse residual channel capacity helped the ternary proxy when assigned randomly, but the tested dynamic gradient-gated channel refresh policy failed to capture that benefit. This cautions against scaling the dynamic gradient-EMA gating policy without first resolving mask stability and selection quality.

## Boundaries and scale limits

Toy synthetic task only; two seeds; 435k-845k parameter models; no real text corpus, GPT-2-small-class baseline, BitNet kernel stack, or 7B+ validation.

## Claim scope

In a tiny 2-layer ternary STE causal Transformer on a deterministic synthetic LM task, dynamic gradient-EMA selection of sparse full-precision residual output channels did not improve over same-budget random residual channels and was worse than plain ternary after 1000 steps.

## Why it stopped

Bounded proxy/early falsification: dynamic gradient-gated residual channels failed against same-budget random residual controls and did not justify scale-up as implemented.

## Recommended next action

Stop this implementation as no-paper evidence; if continuing locally, run a bounded frozen-gradient-mask ablation with mask-churn diagnostics before any larger model training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen Gradient-Selected Residual Channels with Mask-Churn Diagnostics
- Success threshold: Static-gradient residual mask beats random-static residual and plain ternary by at least 3% mean eval loss over three seeds, while dynamic-gradient does not regain parity through longer training.
- Stop condition: Stop if static-gradient selection is not better than random-static residual channels or if benefits disappear on a real text corpus proxy.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-gated-residual-channels-for-1-58-bit-llms-5d449e19292b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
