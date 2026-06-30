# Live-model suffix-anchor speculative decoding latency test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-model-suffix-anchor-speculative-decoding-latency-test-3feba8fc19`
Run ID: `live-model-suffix-anchor-speculative-decoding-latency-test-3feba8fc19-20260629T041024161631+0000`

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

- Parent run decision: Suffix-anchor speculative decoding: an n-gram draft anchored at exact suffix positions: enoch://control-plane/projects/suffix-anchor-speculative-decoding-an-n-gram-draft-anchored-at-exact-suffix-positions-6b48beadbf8f/runs/suffix-anchor-speculative-decoding-an-n-gram-draft-anchored-at-exact-suffix-positions-6b48beadbf8f-20260629T035021972181+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a06f4725978c

## What looked useful

Cached suffix-anchor chunk verification produced conditional latency gains, while naive uncached verification mostly lost. Acceptance rate and draft length are the controlling factors.

## Boundaries and scale limits

One small model, three synthetic repeated prompts, greedy decoding only, one local GPU host, Python harness rather than production serving engine; not validated on large models, real traces, sampling, request batching, or engine-native cache APIs.

## Claim scope

On distilgpt2 running on GB10 CUDA, a KV-cache-aware suffix-anchor verifier can beat cached greedy decoding on synthetic repeated-span prompts when draft acceptance is high; best measured case was 2.08x mean throughput with anchor length 2 and draft length 8.

## Why it stopped

No-paper closure: the bounded live-model result is useful but too narrow and synthetic for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up using real repeated-context prompts and an engine-integrated cache verifier on a larger local model before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Engine-integrated suffix-anchor speculative decoding on real repeated-context traces
- Success threshold: Median tokens/s speedup >= 1.25x over cached greedy on at least 100 prompts, with no output divergence from greedy and acceptance rate >= 0.60 in the winning subset.
- Stop condition: Stop if median speedup is < 1.10x or if acceptance falls below 0.40 on the trace-derived prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/live-model-suffix-anchor-speculative-decoding-latency-test-3feba8fc19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
