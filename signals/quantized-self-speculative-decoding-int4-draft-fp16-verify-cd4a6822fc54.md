# Quantized-Self Speculative Decoding: INT4 Draft FP16 Verify

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-self-speculative-decoding-int4-draft-fp16-verify-cd4a6822fc54`
Run ID: `quantized-self-speculative-decoding-int4-draft-fp16-verify-cd4a6822fc54-20260529T233733620867+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aa1256092b70

## What looked useful

INT4 acceptance ranged from 0.947 at 11.28-bit mean target entropy to 0.780 at 1.56-bit entropy. Modeled gamma=8 speedup remained above baseline for draft cost ratios 0.2-0.3, but fell below baseline at cost ratio 0.5 in sharper regimes. At entropy 4.28 bits, 8/6/4/3-bit acceptance was 0.990/0.959/0.820/0.599.

## Boundaries and scale limits

CPU-only proxy; no real pretrained transformer, no FP16 verifier kernel, no packed INT4 kernel benchmark, no KV-cache or autoregressive wall-clock serving measurement.

## Claim scope

A deterministic synthetic next-token distribution probe found that an INT4 quantized draft of the same dense logit projection can preserve speculative acceptance in high-entropy regimes, but acceptance and modeled speedup degrade in sharper regimes and depend on the draft path being substantially cheaper than the verifier.

## Why it stopped

Proxy-only useful signal: the mechanism is conditionally plausible, but this run did not test real pretrained-model logits or real INT4/FP16 inference throughput, so it is not paper-ready.

## Recommended next action

Run a bounded direct validation on a real small causal LM with logged FP16 verifier logits, a packed INT4 draft path, real prompt batches, acceptance by entropy bucket, and wall-clock tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM INT4 self-speculation acceptance and throughput probe
- Success threshold: At least 1.25x wall-clock tokens/sec over verifier-only decoding on real prompts, mean acceptance >= 0.85, p05 acceptance >= 0.70 in low-entropy buckets, and measured draft cost <= 0.30x verifier cost.
- Stop condition: Stop if packed INT4 draft cost exceeds 0.50x verifier cost, mean acceptance is below 0.80, or any tested gamma fails to beat verifier-only throughput by at least 5%.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-self-speculative-decoding-int4-draft-fp16-verify-cd4a6822fc54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
