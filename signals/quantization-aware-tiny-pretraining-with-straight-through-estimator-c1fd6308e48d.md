# Quantization-Aware Tiny Pretraining with Straight-Through Estimator

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-aware-tiny-pretraining-with-straight-through-estimator-c1fd6308e48d`
Run ID: `quantization-aware-tiny-pretraining-with-straight-through-estimator-c1fd6308e48d-20260528T025217074126+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58cdd723e86b

## What looked useful

Naive STE QAT is locally viable for 8-bit and plausibly useful at 4-bit tiny pretraining, but 2-bit STE is an early negative in this setup with final validation loss 5.594 versus dense 3.808 and mean weight SQNR about 0.60 dB.

## Boundaries and scale limits

Proxy synthetic data only; tiny model only; two seeds; MLP/head quantization plus activation fake quantization, not every attention projection; no calibrated integer kernels, real language corpus, GPT-2-small-class baseline, downstream evaluation, or long-run robustness.

## Claim scope

On a deterministic synthetic next-token pretraining task with an 867k-parameter tiny decoder, STE fake-quantized QAT matched dense training at 8 bits, learned with a small validation-loss penalty at 4 bits, and failed to learn competitively at 2 bits under the same 800-step, two-seed budget.

## Why it stopped

Proxy-only useful signal: sufficient to reject naive 2-bit STE for this tiny setup and prioritize 4-bit follow-up, but insufficient for paper-positive claims about language pretraining.

## Recommended next action

Run a bounded natural-language confirmation with a GPT-2-small-class or parameter-matched small transformer, quantizing attention projections as well as MLP/head layers and comparing dense, PTQ, QAT-4, and QAT-2 controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Natural-Language Confirmation for 4-bit STE QAT Tiny Pretraining
- Success threshold: QAT-4 final validation loss within 0.10 nats/token or 3 percent perplexity of dense while QAT-2 remains at least 0.50 nats/token worse or shows reproducible instability.
- Stop condition: Stop if QAT-4 is more than 0.25 nats/token worse than dense on two consecutive seeds, if QAT-2 matches 4-bit after stabilization indicating this run's 2-bit failure was synthetic-task-specific, or if the run exceeds the bounded local compute budget without checkpointed evidence.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-tiny-pretraining-with-straight-through-estimator-c1fd6308e48d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
