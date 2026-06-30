# Real Pretrained Small-Transformer Verifier-Preserving Sparse KD

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `real-pretrained-small-transformer-verifier-preserving-spar-a537583ea7`
Run ID: `real-pretrained-small-transformer-verifier-preserving-spar-a537583ea7-20260520T064222773559+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Pretrained Small-Transformer Challenge Attestation Under Production Quantization and Sparse Distillation: enoch://control-plane/projects/pretrained-small-transformer-challenge-attestation-under-p-e336434188/runs/pretrained-small-transformer-challenge-attestation-under-p-e336434188-20260520T061606776824+0000
- Parent run decision: Verifier-Preserving Sparse Distillation for Small Pretrained Transformers: enoch://control-plane/projects/verifier-preserving-sparse-distillation-for-small-pretrain-75bbf6c990/runs/verifier-preserving-sparse-distillation-for-small-pretrain-75bbf6c990-20260520T062706525601+0000

## What looked useful

Sparse KD recovered mean teacher decision agreement from 0.78096 to 0.84136 at 70% sparsity and from 0.78670 to 0.81269 at 80% sparsity across 3 seeds, but sparse supervised recovery was effectively tied at 70% and slightly higher at 80%.

## Boundaries and scale limits

Single verifier architecture, single SST-2 task, 3 seeds, 1024 recovery examples per seed, 3 epochs, unstructured global magnitude masks only, and no downstream generation/verifier-loop evaluation. This is not broad Tier-4 paper-readiness evidence.

## Claim scope

On a real pretrained DistilBERT SST-2 verifier with global unstructured transformer-weight sparsity, short sparse KD recovery improves dense-verifier decision agreement over matched prune-only baselines at 70% and 80% sparsity, but it does not outperform a matched sparse supervised recovery control.

## Why it stopped

Tier 4 paper-readiness threshold was not met: the primary mechanism improves over prune-only but fails to beat a real matched supervised control and remains far below dense verifier preservation.

## Recommended next action

Stop this depth-4 follow-up without paper writing; preserve the useful negative/control evidence that KD helps versus prune-only but is not uniquely better than supervised sparse recovery.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-pretrained-small-transformer-verifier-preserving-spar-a537583ea7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
