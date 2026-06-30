# Pretrained Small-Transformer Challenge Attestation Under Production Quantization and Sparse Distillation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-small-transformer-challenge-attestation-under-p-e336434188`
Run ID: `pretrained-small-transformer-challenge-attestation-under-p-e336434188-20260520T061606776824+0000`

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

- Parent run decision: Transformer Challenge-Response Attestation Under Quantization and Distillation: enoch://control-plane/projects/transformer-challenge-response-attestation-under-quantizat-bf667d6806/runs/transformer-challenge-response-attestation-under-quantizat-bf667d6806-20260520T060547829665+0000
- Parent run decision: Challenge-Response Forward-Pass Attestation: enoch://control-plane/projects/challenge-response-forward-pass-attestation-8b72fe142b3d/runs/challenge-response-forward-pass-attestation-8b72fe142b3d-20260520T055710672234+0000

## What looked useful

Dense owner and int8 quantized owner achieved 1.000 mean challenge accuracy and 1.0 pass rate; non-attested baseline was near chance at 0.2375. Dense public-only distillation and 50/80/90% sparse distillation were near chance on challenge accuracy (0.2375-0.2521) with public accuracy drops of 0.077-0.139, so the combined quantization-plus-sparse-distillation robustness claim is unsupported.

## Boundaries and scale limits

No real pretrained transformer, real text dataset, production quantization runtime, or trained sparse transformer body was used. Sparse distillation was a classifier-head distillation proxy and also failed the public-utility drop bound.

## Claim scope

In a controlled NumPy small-transformer-style random-feature classifier with an explicit secret challenge-prototype verifier, challenge attestation survived full encoder/head/prototype int8 dequantized inference across five fixed seeds, but public-only dense and sparse distillation did not inherit the challenge signal.

## Why it stopped

Tier-2 fixed-seed proxy evidence supports quantization robustness but falsifies automatic sparse-distillation survival under the tested threshold; this is not full-scale validation and not paper-ready.

## Recommended next action

Stop this follow-up as no-paper useful signal; the next bounded test should use a real pretrained small transformer and compare public-only sparse distillation against a verifier-preserving sidecar or replay strategy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-Preserving Sparse Distillation for Small Pretrained Transformers
- Success threshold: Across at least three fixed seeds, verifier-preserving sparse distillation must achieve challenge accuracy >= 0.90, false accept <= 0.35, and public utility drop <= 0.03 versus the dense attested owner, while public-only sparse distillation remains below threshold.
- Stop condition: Stop if public-only and verifier-preserving sparse students both fail challenge accuracy >= 0.90 or if all sparse students exceed the 0.03 public-utility drop bound.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-small-transformer-challenge-attestation-under-p-e336434188`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
