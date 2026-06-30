# End-to-end small-model test of outlier-conditioned residual channels for 1-bit activations

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `end-to-end-small-model-test-of-outlier-conditioned-residua-3b26596322`
Run ID: `end-to-end-small-model-test-of-outlier-conditioned-residua-3b26596322-20260522T025952855712+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Outlier-Conditioned Sparse Residual Channels for 1-bit Activations: enoch://control-plane/projects/outlier-conditioned-sparse-residual-channels-for-1-bit-activations-a8d68a94e5a7/runs/outlier-conditioned-sparse-residual-channels-for-1-bit-activations-a8d68a94e5a7-20260521T204102095214+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2a296f7a6b8d

## What looked useful

Outlier conditioning is mechanistically visible: OCR captured about 36.5-37.0% of quantization residual energy with a 6.25% channel budget, compared with about 6.2-6.3% for random residual channels. End-to-end validation loss improved only 0.34% over binary at 250 steps and 0.27% at 1000 steps, below the predefined 2% useful-support threshold.

## Boundaries and scale limits

CPU-only Tier 1 controlled small direct test; character-level Tiny Shakespeare; 2-layer 96-dim Transformer; MLP activation quantization only; dense PyTorch implementation; no GPT-2-small, large-corpus, attention-activation, serving-kernel, or multi-node validation.

## Claim scope

In a 242k-parameter Tiny Shakespeare character-level causal Transformer with 1-bit MLP hidden activations, selecting 6.25% sparse full-precision residual channels by activation outlier magnitude captures substantially more quantization residual energy than random selection but gives less than 0.4% validation-loss improvement over binary or same-budget random controls.

## Why it stopped

Controlled small direct tests showed only sub-threshold end-to-end gains despite strong residual-energy concentration, so the current method is not practically supported beyond a weak mechanism signal.

## Recommended next action

Stop this branch as no-paper useful evidence; do not escalate unless a separate bounded experiment changes the residual budget or quantization target and clears a 2% matched-control validation-loss threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-small-model-test-of-outlier-conditioned-residua-3b26596322`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
