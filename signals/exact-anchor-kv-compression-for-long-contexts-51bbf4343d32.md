# Exact-Anchor KV Compression for Long Contexts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-long-contexts-51bbf4343d32`
Run ID: `exact-anchor-kv-compression-for-long-contexts-51bbf4343d32-20260608T202802260948+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/43da9b60f994

## What looked useful

At a mean 3.49% KV slot ratio, exact-anchor compression beat random and recent-window controls in all 81 anchor-retrieval trials, but passed a relative-L2 <0.5 at <=10% slots threshold only in 31/243 trials, all from the anchor-retrieval regime. Mixed attention had median relative L2 10.86 and lost to recent-window in 81/81 trials. Anchor attention mass strongly predicted error (Pearson correlation -0.807 with log error).

## Boundaries and scale limits

Tested synthetic K/V tensors only, one attention head, sequence lengths up to 16384, d_head 64, 64 queries, 243 sweep trials on one NVIDIA GB10. Did not test real LLM layers, generation quality, perplexity, multi-layer accumulation, positional effects, batching overhead, or established KV compression baselines beyond random and recent-window controls.

## Claim scope

Synthetic single-head attention probes show exact-anchor KV compression is useful only when full attention mass is concentrated on preserved anchors; it is not a generally reliable long-context KV compression method under mixed or diffuse attention.

## Why it stopped

Closed as no-paper useful signal: bounded synthetic evidence supports the high-anchor-mass mechanism but shows a clear failure mode for mixed and diffuse attention, so the broad idea is not validated.

## Recommended next action

Do one bounded deepen test on a small real transformer retrieval workload: measure whether a practical anchor-selection rule can keep accuracy or perplexity within 5% of full KV at <=10% KV slots while beating recent-window and random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model exact-anchor KV compression on a small retrieval benchmark
- Success threshold: At <=10% KV slots, exact-anchor compression is within 5% relative task accuracy or perplexity of full KV and beats recent-window/random controls in at least 80% of evaluated settings.
- Stop condition: Stop if selected-anchor attention mass stays below 0.2 on most examples or if task degradation exceeds 10% relative at every tested KV budget.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-contexts-51bbf4343d32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
