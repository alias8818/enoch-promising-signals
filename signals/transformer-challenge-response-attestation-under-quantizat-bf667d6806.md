# Transformer Challenge-Response Attestation Under Quantization and Distillation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `transformer-challenge-response-attestation-under-quantizat-bf667d6806`
Run ID: `transformer-challenge-response-attestation-under-quantizat-bf667d6806-20260520T060547829665+0000`

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

- Parent run decision: Challenge-Response Forward-Pass Attestation: enoch://control-plane/projects/challenge-response-forward-pass-attestation-8b72fe142b3d/runs/challenge-response-forward-pass-attestation-8b72fe142b3d-20260520T055710672234+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/080b78960275

## What looked useful

The mechanism appears viable locally but conditional: quantization-style weight rounding did not erase the trained challenge map, while distillation only retained it when the challenge distribution was represented in the distillation data.

## Boundaries and scale limits

Toy synthetic data, tiny randomly initialized transformers, enrolled exact prompts only, no natural-language paraphrases, no adversarial removal, no GPT-2-small-class/pretrained model, and no production dynamic quantized kernels because the local ARM PyTorch build rejected eager dynamic quantization.

## Claim scope

In a three-seed synthetic tiny causal-transformer test with 32 enrolled challenge IDs, challenge-response attestation reached 100% exact accuracy, survived explicit symmetric int8 weight quantize/dequant simulation, was lost under distillation when challenge prompts were absent, and was preserved when challenge prompts were included at a 10% mixture.

## Why it stopped

Tier 1 direct toy evidence produced a useful mechanism signal, but the result is not paper-positive because it is synthetic and small-scale.

## Recommended next action

Run a bounded deepen test on a small pretrained transformer or GPT-2-small-class model with natural-language challenge prompts, production quantization paths, and distillation mixtures that include 0%, 1%, and 10% challenge prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Small-Transformer Challenge Attestation Under Production Quantization and Sparse Distillation
- Success threshold: Quantized model retains at least 95% enrolled challenge accuracy with less than 5% relative utility loss, 0% challenge distillation falls near chance, and at least one sparse challenge mixture recovers at least 80% challenge accuracy across seeds.
- Stop condition: Stop if quantization drops challenge accuracy below 80% while normal utility is preserved, or if all sparse distillation mixtures remain near chance despite teacher challenge accuracy above 95%.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-challenge-response-attestation-under-quantizat-bf667d6806`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
