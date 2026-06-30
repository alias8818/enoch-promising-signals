# Random Subspace Gradient Descent for Memory-Efficient Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `random-subspace-gradient-descent-for-memory-efficient-training-ae2ba3e78d5a`
Run ID: `random-subspace-gradient-descent-for-memory-efficient-training-ae2ba3e78d5a-20260527T231320920382+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03cd32ce872a

## What looked useful

Naive random subspace SGD implemented by masking gradients after backward fails the memory-efficiency goal while preserving some optimizer-dependent learning signal; memory savings require avoiding full-gradient creation, not post-hoc masking.

## Boundaries and scale limits

Synthetic MLP only; no real language/vision dataset, no large model, no distributed run, and no custom low-memory autograd or fused sparse backward implementation.

## Claim scope

Bounded local PyTorch MLP probes show that post-backward random coordinate masking is not memory-efficient because full gradients and AdamW state are still materialized; short-run AdamW learning signal can survive 10% gradient masking on a synthetic teacher task.

## Why it stopped

Proxy/local evidence, not full-scale validation, shows the simple post-backward random subspace approach does not reduce target training memory.

## Recommended next action

Stop this implementation path as an early proxy falsification; the only worthwhile next local test is a custom block-sparse/custom-autograd variant that never materializes full gradients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-sparse autograd random subspace training without full gradient materialization
- Success threshold: At least 25% lower CUDA peak allocation than dense AdamW and at least 90% of dense AdamW validation-loss improvement over the same step budget.
- Stop condition: Stop if active-block backward still materializes full gradients or if validation-loss improvement is below 70% of dense AdamW at the measured memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/random-subspace-gradient-descent-for-memory-efficient-training-ae2ba3e78d5a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
