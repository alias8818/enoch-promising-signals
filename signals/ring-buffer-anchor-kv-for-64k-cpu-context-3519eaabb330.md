# Ring-Buffer Anchor KV for 64K CPU Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ring-buffer-anchor-kv-for-64k-cpu-context-3519eaabb330`
Run ID: `ring-buffer-anchor-kv-for-64k-cpu-context-3519eaabb330-20260529T220610883374+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9cb0c1dbbdea

## What looked useful

Ring plus anchors recovered salient old anchor queries at Hit@1 1.0000 versus 0.0000 for sliding-window-only, matched recent-query Hit@1 1.0000, reduced projected KV memory from 32.0 GiB to 4.234 GiB for a representative 32-layer fp16 KV cache, and improved CPU attention-score latency by about 5.5x versus full 64K. Arbitrary old-query Hit@1 was only 0.0039, matching the tiny retained fraction.

## Boundaries and scale limits

The run used synthetic normalized vectors and CPU matrix-multiplication latency proxies only. It did not implement a real transformer KV-cache path, learned anchor selection, perplexity evaluation, downstream generation tests, batching, NUMA tuning, or production serving overheads.

## Claim scope

Synthetic 65,536-token key/query retrieval shows that a recent-token ring plus sparse anchors can preserve explicitly anchored old facts and recent facts while retaining 13.23% of KV tokens, but it does not preserve arbitrary old-token recall.

## Why it stopped

This run is a synthetic/proxy useful signal, not a full validation; it supports anchored retrieval but early-falsifies any broad arbitrary-old-context preservation claim.

## Recommended next action

Run a bounded real-model follow-up that implements ring-plus-anchor KV in an inference cache and compares against full KV and sliding-window baselines on a small long-context retrieval/perplexity benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Ring-Anchor KV on Small Long-Context Retrieval
- Success threshold: At a KV token budget no more than 15% of full 64K, ring-plus-anchor should recover at least 90% of full-KV anchored retrieval accuracy, beat sliding-window anchored retrieval by at least 30 percentage points, keep arbitrary-fact limitations explicit, and show at least 3x attention-score latency improvement versus full KV.
- Stop condition: Stop if a real-model implementation cannot exceed sliding-window anchored retrieval by 10 percentage points at comparable KV budget, or if perplexity/quality degradation makes the cache unusable despite anchored recall gains.

## Evidence references

- Artifact root: `<local-path>/projects/ring-buffer-anchor-kv-for-64k-cpu-context-3519eaabb330`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
