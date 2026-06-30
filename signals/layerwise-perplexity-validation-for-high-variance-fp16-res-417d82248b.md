# Layerwise perplexity validation for high-variance FP16 residual activation channels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layerwise-perplexity-validation-for-high-variance-fp16-res-417d82248b`
Run ID: `layerwise-perplexity-validation-for-high-variance-fp16-res-417d82248b-20260528T141243989736+0000`

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

- Parent run decision: Outlier-Channel Residual: FP16 for High-Variance Activation Channels at 2-bit: enoch://control-plane/projects/outlier-channel-residual-fp16-for-high-variance-activation-channels-at-2-bit-023d78bcac1a/runs/outlier-channel-residual-fp16-for-high-variance-activation-channels-at-2-bit-023d78bcac1a-20260528T102153376612+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b81ac000324e

## What looked useful

High-variance FP16 residual channel ablation increased validation PPL in all 12 layers, with mean delta +2088.31 versus +0.29 for low-variance controls and +0.45 for random controls; baseline PPL was 50.5982.

## Boundaries and scale limits

One pretrained model, one dataset, 32 calibration sequences, 64 validation sequences, 128-token windows, one channel fraction, one zero-ablation intervention, and no FP32 matched comparison or larger-model replication.

## Claim scope

In GPT-2-small FP16 CUDA inference on Wikitext-2, the top 1% residual block-output channels by calibration activation variance are disproportionately important for validation perplexity under layerwise zero-ablation compared with same-cardinality low-variance and random controls.

## Why it stopped

Tier 1 direct small test produced mechanism support but not publication-grade breadth; stopping as no-paper useful signal rather than claiming full validation.

## Recommended next action

Run a bounded deepen follow-up that repeats the layerwise test with FP16-vs-FP32 matched channel selection, multiple calibration seeds, and perturbation/noise interventions that mimic realistic precision error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: FP16-specific residual channel sensitivity with matched FP32 and perturbation controls
- Success threshold: Across at least three seeds, high-variance FP16 perturbations exceed same-cardinality random controls in at least 9/12 layers and show at least 5x mean delta PPL versus random controls without relying solely on zero-ablation.
- Stop condition: Stop if high-variance perturbations fail to exceed random controls in at least 9/12 layers for two independent seeds, or if FP16 and FP32 matched runs show no meaningful difference and only zero-ablation produces an effect.

## Evidence references

- Artifact root: `<local-path>/projects/layerwise-perplexity-validation-for-high-variance-fp16-res-417d82248b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
