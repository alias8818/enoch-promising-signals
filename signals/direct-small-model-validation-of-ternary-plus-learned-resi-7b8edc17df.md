# Direct Small-Model Validation of Ternary Plus Learned Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-small-model-validation-of-ternary-plus-learned-resi-7b8edc17df`
Run ID: `direct-small-model-validation-of-ternary-plus-learned-resi-7b8edc17df-20260520T163542372725+0000`

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

- Parent run decision: Learned Residual Channels for Ternary-Plus-Correction Quantization: enoch://control-plane/projects/learned-residual-channels-for-ternary-plus-correction-quantization-329e57a71a01/runs/learned-residual-channels-for-ternary-plus-correction-quantization-329e57a71a01-20260520T145805882509+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97eb668fc02a

## What looked useful

Rank-8 residual channels improved validation loss versus ternary-only in all three 5000-step confirmation seeds by 0.0799 to 0.1041 nats, with mean improvement 0.0926 nats. Mean dense, ternary, and rank-8 validation losses were 1.9901, 2.2498, and 2.1572; rank 8 closed 35.8% of the dense-vs-ternary gap, below the 50% success threshold.

## Boundaries and scale limits

This run did not test transformers, GPT-2-small-class models, hardware-efficient ternary kernels, long pretraining, downstream transfer, or broad multi-dataset robustness. Evidence is limited to a compact MLP next-character model and three confirmation seeds.

## Claim scope

In a small NumPy character-level MLP language model on Tiny Shakespeare, learned low-rank residual channels added to straight-through ternary linear layers consistently improved validation loss versus ternary-only controls, but did not close the predeclared 50% dense-vs-ternary gap.

## Why it stopped

No-paper useful signal: direct small-model evidence supports a residual-channel mechanism but misses the predeclared 50% gap-closure threshold and is not transformer-scale or publication-grade.

## Recommended next action

Run a bounded deepen follow-up using a small transformer language model with dense, ternary-only, and ternary-plus-residual rank sweep controls; stop if rank-limited residuals again fail to close at least 50% of the validation-loss gap across seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Rank Sweep for Ternary Plus Learned Residual Channels
- Success threshold: A rank-limited residual transformer closes at least 50% of the dense-vs-ternary validation-loss gap in mean final validation loss across at least three seeds and improves ternary-only by at least 0.05 nats in every seed.
- Stop condition: Stop as negative if no tested residual rank closes at least 50% of the validation-loss gap in a controlled small transformer run, or if the only successful ranks erase the intended full-precision parameter advantage.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-model-validation-of-ternary-plus-learned-resi-7b8edc17df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
