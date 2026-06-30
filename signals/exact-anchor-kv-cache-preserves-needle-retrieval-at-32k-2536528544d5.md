# Exact-anchor KV cache preserves needle retrieval at 32K

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-kv-cache-preserves-needle-retrieval-at-32k-2536528544d5`
Run ID: `exact-anchor-kv-cache-preserves-needle-retrieval-at-32k-2536528544d5-20260621T014822139274+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/736bfc6bce23

## What looked useful

Across 12,960 trials, exact-anchor-plus-window cache achieved 100% hit rate for anchor-aligned old needles at query noise 0.0, 0.05, and 0.1 across d_model 32/64/128 and anchor strides 256/512/1024, while sliding-window cache achieved 0% because the needles were outside the final 2,048 rows. Off-anchor old needles also had 0% hit rate under exact-anchor caching, bounding the mechanism to explicitly preserved rows.

## Boundaries and scale limits

No real language model, learned representation, RoPE/position interaction, multi-head attention behavior, tokenizer placement, generation loop, or serving implementation was tested. Off-anchor old needles were not preserved, and high query noise degraded retrieval.

## Claim scope

At 32,768 synthetic normalized KV rows, preserving exact anchor rows plus a 2,048-row sliding window preserved retrieval of old anchor-aligned needles that pure sliding-window eviction lost. This claim applies only to exact preserved anchor positions in an associative-memory cache-policy probe.

## Why it stopped

The local run produced a useful synthetic mechanism signal but not direct publication-grade evidence for a real long-context model or serving system.

## Recommended next action

Run a bounded direct model follow-up that implements exact-anchor KV retention in a small 32K-capable transformer inference path and compares anchor-aligned and off-anchor needle retrieval against full-cache and sliding-window baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct 32K model needle retrieval with exact-anchor KV retention
- Success threshold: Exact-anchor-plus-window retrieval should be within 5 percentage points of full-cache accuracy on anchor-aligned old needles and at least 30 percentage points above sliding-window-only, without falsely preserving off-anchor old needles.
- Stop condition: Stop if exact-anchor-plus-window accuracy is not materially above sliding-window-only on anchor-aligned old needles, or if implementation overhead erases the intended memory/latency advantage versus full cache.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-cache-preserves-needle-retrieval-at-32k-2536528544d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
