# Principled Residual Channel Pruning for VRAM-Constrained Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `principled-residual-channel-pruning-for-vram-constrained-inference-2e118fb2fe1e`
Run ID: `principled-residual-channel-pruning-for-vram-constrained-inference-2e118fb2fe1e-20260610T203341908675+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fb7c04855f43

## What looked useful

Activation RMS was the best immediate post-training pruning score at all tested channel budgets; random and all other methods recovered dense accuracy after 3 fine-tuning epochs; residual-width slicing reduced parameters by up to 92.3% and estimated residual activations by 75.0% at 25% kept channels, but latency remained about 0.89x of dense rather than faster.

## Boundaries and scale limits

Not tested on transformers, real language-model datasets, KV-cache pressure, production kernels, large batch/token shapes, or peak VRAM allocation. Synthetic data and one full seed limit generality.

## Claim scope

Bounded proxy result on a synthetic teacher-labeled residual MLP: physical residual-channel slicing can greatly reduce parameters and estimated residual activation bytes, but the tested gradient-weighted saliency rule did not outperform activation RMS and did not improve measured small-model GPU latency.

## Why it stopped

Proxy evidence is mixed and early: it supports residual-channel pruning mechanics but falsifies the stronger claim that the tested principled gradient-weighted score is better than simple controls in this setting.

## Recommended next action

Stop this as a no-paper useful signal; a bounded follow-up should test activation RMS versus gradient-weighted saliency on a GPT-2-small-class transformer with real validation loss and peak VRAM/tokens-per-second metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer residual-width pruning with activation RMS control
- Success threshold: A pruning rule is useful only if it keeps validation loss within 5% relative of dense at at least 50% residual-width reduction and shows either lower peak VRAM or higher throughput than dense; gradient-weighted saliency must beat activation RMS by at least 1% absolute retained-loss margin to justify its extra complexity.
- Stop condition: Stop if activation RMS or random matches gradient-weighted saliency within measurement noise across two pruning budgets, or if pruned transformer runs do not reduce peak allocated VRAM or improve throughput.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channel-pruning-for-vram-constrained-inference-2e118fb2fe1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
