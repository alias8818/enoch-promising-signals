# Parameter-matched tokenized LM check for ternary plus learned residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `parameter-matched-tokenized-lm-check-for-ternary-plus-lear-180afa3479`
Run ID: `parameter-matched-tokenized-lm-check-for-ternary-plus-lear-180afa3479-20260520T183003305997+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Small Transformer Rank Sweep for Ternary Plus Learned Residual Channels: enoch://control-plane/projects/small-transformer-rank-sweep-for-ternary-plus-learned-resi-c580ac1277/runs/small-transformer-rank-sweep-for-ternary-plus-learned-resi-c580ac1277-20260520T181412380935+0000
- Parent run decision: Direct Small-Model Validation of Ternary Plus Learned Residual Channels: enoch://control-plane/projects/direct-small-model-validation-of-ternary-plus-learned-resi-7b8edc17df/runs/direct-small-model-validation-of-ternary-plus-learned-resi-7b8edc17df-20260520T163542372725+0000

## What looked useful

Mean deterministic validation loss over seeds 1,2,3: dense 1.59841, ternary 1.58223, ternary_residual 1.57882. Ternary_residual beat dense by -0.01959 loss consistently across seeds, but beat ternary-only by only -0.00342 mean loss with mixed per-seed deltas [0.00345, -0.00036, -0.01333].

## Boundaries and scale limits

Small corpus, byte tokenizer, small 2M-parameter transformer, 5,000-step runs only. Training used floating latent weights with ternary forward STE, so this does not validate ternary inference kernels, storage efficiency, GPT-2-small scale, standard web/text corpora, longer schedules, or broad generation quality.

## Claim scope

On a 3-seed, 2M-parameter, byte-tokenized Tiny Shakespeare causal LM benchmark, STE ternary transformer linear layers and ternary-plus-rank-16 residual linear layers both beat a parameter-matched dense transformer on deterministic held-out validation loss after 5,000 GPU training steps. The residual-channel variant had the best mean validation loss but did not robustly beat the ternary-only ablation across every seed.

## Why it stopped

Bounded direct validation found a useful ternary-vs-dense signal but mixed evidence for the learned residual-channel advantage over ternary-only; this is insufficient for publication-grade support of the stated mechanism.

## Recommended next action

Stop this follow-up as no-paper useful evidence; the only worthwhile deepen test would be a residual-rank and width ablation at the same scale or a larger standard-corpus validation, but this depth-3 branch should not claim paper readiness from the current mixed residual ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-rank sweep for parameter-matched ternary token LMs
- Success threshold: Residual variants must beat ternary-only in every seed with mean validation-loss improvement >= 0.01 and no parameter-count advantage over 3%.
- Stop condition: Stop if no residual rank beats ternary-only by >= 0.01 mean validation loss across three seeds, or if the best rank wins only through a parameter-count or width mismatch.

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-tokenized-lm-check-for-ternary-plus-lear-180afa3479`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
