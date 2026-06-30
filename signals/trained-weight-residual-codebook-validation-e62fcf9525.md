# Trained-weight residual codebook validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trained-weight-residual-codebook-validation-e62fcf9525`
Run ID: `trained-weight-residual-codebook-validation-e62fcf9525-20260526T161151232056+0000`

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

- Parent run decision: Block-wise residual codebooks for 1-bit inference: enoch://control-plane/projects/block-wise-residual-codebooks-for-1-bit-inference-2a440fb9b3eb/runs/block-wise-residual-codebooks-for-1-bit-inference-2a440fb9b3eb-20260525T222531346967+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/85f01aa3b2bb

## What looked useful

Learned residual VQ beat both controls on normalized weight MSE in 5/5 seeds, preserved at least 98% of dense accuracy in 4/5 seeds, and had median accuracy drop 0.003662 versus 0.104492 for 2-bit scalar quantization.

## Boundaries and scale limits

Tiny MLP only; synthetic task; nominal 2 index bits per weight; codebook overhead is large relative to the toy model; no transformer, language-model perplexity, deployment packing, entropy coding, post-quantization fine-tuning, kernel speed, or large-scale robustness evidence.

## Claim scope

In a five-seed synthetic two-moons MLP test with 4,482 trained weights, a learned residual vector codebook over 8-weight blocks preserved function and reconstructed trained weights better than same-index-bit scalar quantization and random residual-codebook controls.

## Why it stopped

Tier 1 controlled small direct test met the useful-signal threshold, but paper readiness requires larger architecture/task evidence and full compression accounting.

## Recommended next action

Run a bounded direct follow-up on a small transformer or GPT-2-small-class model with matched net bit budget including codebook overhead, reporting validation loss/perplexity and weight reconstruction controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer trained-weight residual codebook validation
- Success threshold: Learned residual VQ must beat matched-net-bit scalar/groupwise controls on validation loss delta and weight NMSE in at least 3/3 seeds or checkpoints while preserving at least 98% of dense-task performance.
- Stop condition: Stop if learned residual VQ fails to beat the matched-net-bit control on validation loss or weight NMSE in two seeds/checkpoints, or if codebook overhead eliminates the nominal compression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/trained-weight-residual-codebook-validation-e62fcf9525`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
