# Confidence-Gated Cascade with KV-Prefix Reuse for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-cascade-with-kv-prefix-reuse-for-local-serving-abc42e4dcc77`
Run ID: `confidence-gated-cascade-with-kv-prefix-reuse-for-local-serving-abc42e4dcc77-20260516T192914547611+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9734c9277505

## What looked useful

KV-prefix reuse is not a universal win: it was slower at tiny prefixes, nearly neutral at 512+96 tokens, and useful at 1536+96 tokens; the cascade's advantage depends more on gate escalation rate and a strong baseline comparison than on prefix reuse alone.

## Boundaries and scale limits

No pretrained model quality, confidence calibration, production serving backend, batching, concurrency, decode-token latency, cache eviction, or 7B+ model validation was measured.

## Claim scope

On a GB10 PyTorch proxy with randomly initialized causal transformers, reusable large-model prefix KV gives a clear prefill benefit for long shared prefixes and a confidence-gated cascade beats large-only prefix-cache serving only when escalation remains below roughly 65-70%.

## Why it stopped

No-paper closure: this is a proxy systems result with mixed evidence, useful thresholds, and no direct task-quality validation.

## Recommended next action

Run a bounded direct follow-up with real pretrained small/large local models, calibrated confidence thresholds, and an end-to-end large-only prefix-cache serving baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct confidence-quality cascade test with real local models
- Success threshold: At equal accepted answer quality, p50 or mean end-to-end latency improves by at least 15% versus large-only prefix-cache serving while escalation is no more than 65%.
- Stop condition: Stop negative if calibrated escalation exceeds 70% at the quality target or if end-to-end speedup versus the large-only prefix-cache baseline is below 10%.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cascade-with-kv-prefix-reuse-for-local-serving-abc42e4dcc77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
