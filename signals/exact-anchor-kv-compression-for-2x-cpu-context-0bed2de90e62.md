# Exact-anchor KV compression for 2x CPU context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-2x-cpu-context-0bed2de90e62`
Run ID: `exact-anchor-kv-compression-for-2x-cpu-context-0bed2de90e62-20260527T204050968381+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71f9eafbd9e9

## What looked useful

At 2048->1024 slots, smooth-segment K/V achieved mean relative L2 around 0.04 with simple periodic/recent anchors, while IID and sparse-spike cases failed with simple anchors around 0.24-0.27 relative L2. Oracle/hybrid anchor selection reduced error to 0.01-0.10. At 8192->4096 slots, compressed attention alone showed about 1.8-4.0x speedup, but rebuilding summaries cost roughly 87-102 ms versus 2-4 ms for full attention.

## Boundaries and scale limits

No real transformer, perplexity, generation, multi-query serving, or online cache-maintenance evaluation was run. Oracle-assisted strategies are upper bounds, and the naive per-query compression rebuild is slower than full attention end to end.

## Claim scope

Synthetic single-query attention proxy for 2:1 KV slot compression: exact anchors plus count-weighted contiguous summaries can approximate full 2x-context attention when KV states are locally redundant or when high-logit anchors are selected by an oracle.

## Why it stopped

Synthetic proxy supports the mechanism conditionally but does not validate the practical CPU 2x-context claim; simple anchor policies fail important cases and per-query compression rebuild is too slow.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should use real transformer KV traces with an implementable online anchor policy and incremental summary maintenance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV trace test for online exact-anchor compression
- Success threshold: Across at least 100 real prompt/query samples, mean relative attention-output error <= 0.15, mean cosine >= 0.98, token-logit/perplexity degradation small enough to be practically negligible, and end-to-end CPU latency at least 1.3x faster than full 2x-context attention.
- Stop condition: Stop if non-oracle anchor policies exceed 0.20 mean relative error or if incremental cache maintenance removes the latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-2x-cpu-context-0bed2de90e62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
