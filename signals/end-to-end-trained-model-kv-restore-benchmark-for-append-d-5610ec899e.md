# End-to-end trained-model KV restore benchmark for append-delta anchor checkpoints

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-trained-model-kv-restore-benchmark-for-append-d-5610ec899e`
Run ID: `end-to-end-trained-model-kv-restore-benchmark-for-append-d-5610ec899e-20260603T213424020853+0000`

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

- Parent run decision: Delta-Encoded Anchor State Checkpoints for Context Recomputation: enoch://control-plane/projects/delta-encoded-anchor-state-checkpoints-for-context-recomputation-9f8fe29d4613/runs/delta-encoded-anchor-state-checkpoints-for-context-recomputation-9f8fe29d4613-20260602T225752720661+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93566c73e35a

## What looked useful

The mechanism works correctly within tight tolerances: max KV absolute difference was 0.000366032 and max next-logit absolute difference was 0.000000238. The latency result was negative at this scale: direct prefill averaged 0.513844 ms while restore from disk plus concat plus GPU transfer averaged 0.964861 ms, a 0.532558x speedup ratio.

## Boundaries and scale limits

This did not test GPT-2-small-class or larger models, pretrained language models, long-context prompts, production serialization, memory-mapped caches, persistent GPU-resident caches, batching, concurrency, or serving-system contention.

## Claim scope

In a controlled Tier 1 test with an end-to-end trained 875k-parameter causal transformer, 256-token prefixes, 192-token KV anchors, and 64 appended delta tokens, append-delta anchor restore preserved KV/logit numerical equivalence but was slower than direct GPU prefill when restore included disk load, concatenation, and device transfer.

## Why it stopped

No-paper Tier 1 direct test: correctness was supported, but the tested append-delta restore path was slower than direct prefill, so the latency hypothesis is not paper-positive.

## Recommended next action

Run a bounded deepen follow-up on a larger transformer and longer prefixes with a production-like restore path to locate the context/model-size crossover, or stop if the target claim is only small-model latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crossover benchmark for append-delta KV restore on larger models and longer prefixes
- Success threshold: At one or more realistic prefix lengths, restore from a persisted append-delta anchor must be at least 1.25x faster than direct prefill while keeping max next-logit absolute difference <= 0.00001.
- Stop condition: Stop if all tested larger/longer configurations remain slower than direct prefill or if memory/runtime exceeds the calibrated local budget before reaching a plausible crossover.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-trained-model-kv-restore-benchmark-for-append-d-5610ec899e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
