# Speculative decoding with 2-bit residual-channel draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-2-bit-residual-channel-draft-model-8d7c28ac0887`
Run ID: `speculative-decoding-with-2-bit-residual-channel-draft-model-8d7c28ac0887-20260602T112004389363+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ab396c8efbc2

## What looked useful

The bottleneck itself did not immediately fail: 2-bit residual/logit quantization over candidate sets of 32, 64, 128, and 256 retained high acceptance relative to exact top-k logits and strongly beat uniform top-k controls. This supports testing a real cheap draft, but does not justify a paper or deployed-speed claim.

## Boundaries and scale limits

No trained draft model, no non-oracle candidate predictor, no end-to-end speculative decoding wall-clock benchmark, and no large-model or production-serving validation were run. The speed result is an analytical proxy using assumed draft/verifier cost ratios.

## Claim scope

On a distilgpt2 verifier mechanism probe over 128-context samples, an oracle top-k candidate set with 2-bit quantized centered residual logits preserved most exact top-k speculative acceptance: 0.7467 mean acceptance at top-k 128 versus 0.8357 exact top-k and 0.2813 uniform top-k.

## Why it stopped

No-paper closure: this run produced a useful mechanism signal but only with oracle candidate sets and verifier-derived residual logits, so it is not direct validation of a deployable 2-bit residual-channel draft model.

## Recommended next action

Run a bounded deepen follow-up that trains a small non-oracle candidate/residual draft against distilgpt2 logits and measures actual speculative decoding acceptance and latency against a parameter-matched dense draft control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a non-oracle 2-bit residual-channel draft for distilgpt2 speculative decoding
- Success threshold: Mean acceptance at gamma 4 >= 0.70, measured tokens/sec at least 1.3x greedy verifier decoding, and better tokens/sec than a parameter-matched dense draft under identical batch and sequence settings.
- Stop condition: Stop if the non-oracle draft cannot achieve mean acceptance >= 0.55 or if measured draft/verifier latency ratio exceeds 0.20, because the mechanism signal would not translate into practical speculative speedup at this scale.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-2-bit-residual-channel-draft-model-8d7c28ac0887`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
