# KV-Cache Lookahead Speculation via Draft-then-Resample

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-lookahead-speculation-via-draft-then-resample-f7e86724c698`
Run ID: `kv-cache-lookahead-speculation-via-draft-then-resample-f7e86724c698-20260528T232151129392+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/792c980d2760

## What looked useful

At temperature 1.0, length-8 lookahead reused only 4.69% of prefetched KV tokens and had 0% full-prefix hits across 256 sampled continuations; length-4 reused 9.38%. Even at temperature 0.7, length-8 wasted 85.55% of prefetched KV. Greedy temperature 0 was a sanity check with 100% reuse.

## Boundaries and scale limits

This is not a production serving benchmark and does not test 7B+ models, asynchronous precompute, confidence-gated prefetch, or standard speculative decoding baselines. It directly measures exact prefix reuse on a small pretrained model.

## Claim scope

Bounded mechanism probe on distilgpt2 prompts: naive single-path KV-cache lookahead using the target model's own greedy continuation as an optimistic draft is not effective for stochastic draft-then-resample decoding because exact prefix reuse is too low.

## Why it stopped

Proxy/early falsification: under an optimistic draft-quality setup, stochastic resampling diverged too often for naive prefetched KV to be useful; full serving-scale validation was not run.

## Recommended next action

Stop this run as an early mechanism falsification for unconditional single-path lookahead; only pursue a bounded confidence-gated variant if a new run can test selection coverage and useful KV fraction directly.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Gated KV Lookahead Reuse
- Success threshold: For temperature 0.7 to 1.0 sampling, a gated policy must cover at least 30% of generated positions and achieve at least 65% mean useful KV fraction for L=2 or L=4; otherwise stop.
- Stop condition: Stop if coverage falls below 30%, useful KV fraction stays below 65%, or any measured end-to-end prototype shows no latency/throughput gain versus standard decoding.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-lookahead-speculation-via-draft-then-resample-f7e86724c698`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
