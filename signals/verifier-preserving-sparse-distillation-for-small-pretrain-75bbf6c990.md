# Verifier-Preserving Sparse Distillation for Small Pretrained Transformers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `verifier-preserving-sparse-distillation-for-small-pretrain-75bbf6c990`
Run ID: `verifier-preserving-sparse-distillation-for-small-pretrain-75bbf6c990-20260520T062706525601+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Transformer Challenge-Response Attestation Under Quantization and Distillation: enoch://control-plane/projects/transformer-challenge-response-attestation-under-quantizat-bf667d6806/runs/transformer-challenge-response-attestation-under-quantizat-bf667d6806-20260520T060547829665+0000
- Parent run decision: Pretrained Small-Transformer Challenge Attestation Under Production Quantization and Sparse Distillation: enoch://control-plane/projects/pretrained-small-transformer-challenge-attestation-under-p-e336434188/runs/pretrained-small-transformer-challenge-attestation-under-p-e336434188-20260520T061606776824+0000

## What looked useful

At 80% realized sparsity over 5 fixed seeds, verifier-preserving sparse KD improved easy verifier accuracy over LM-only sparse KD by +0.1383 and hard verifier accuracy by +0.1452, reduced verifier BCE by about 0.18, and changed LM loss by less than 0.00004. The effect was positive for verifier accuracy and BCE in every seed.

## Boundaries and scale limits

The validation used a from-scratch compact transformer and synthetic checksum verifier, not a real pretrained GPT-2-small-class model or natural-language verifier benchmark. It ran 5 seeds on GB10 CUDA with 1200 teacher steps and 600 student steps per variant.

## Claim scope

In a controlled synthetic small causal-transformer certificate task, adding verifier-logit plus verifier-label preservation during 80% sparse distillation restored verifier accuracy lost by LM-only sparse KD while preserving LM loss.

## Why it stopped

Mechanism supported in a bounded synthetic validation, but the original small-pretrained-transformer claim remains unclosed because no real pretrained model or natural-language verifier benchmark was tested.

## Recommended next action

Stop this run as no-paper useful evidence; the next concrete step is a depth-4 validation on a real pretrained small transformer with a real verifier target and the same sparse KD ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Pretrained Small-Transformer Verifier-Preserving Sparse KD
- Success threshold: Across at least 3 fixed seeds, verifier-preserving sparse KD improves verifier AUC or accuracy by at least 5 points over LM-only sparse KD at matched sparsity, with perplexity no worse than 1% relative to LM-only sparse KD.
- Stop condition: Stop as negative if verifier-preserving sparse KD fails to improve verifier metrics by 2 points or more in at least 2 of 3 seeds, or if perplexity degradation exceeds 3% relative to LM-only sparse KD.

## Evidence references

- Artifact root: `<local-path>/projects/verifier-preserving-sparse-distillation-for-small-pretrain-75bbf6c990`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
