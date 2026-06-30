# Exact-Anchor KV Compression for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-long-context-on-cpu-9464a846a971`
Run ID: `exact-anchor-kv-compression-for-long-context-on-cpu-9464a846a971-20260607T224002967116+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd8255f1ed89

## What looked useful

At length 32768, exact-anchor centroid compression reduced the estimated KV cache from 16.00 MiB to 0.28 MiB and accelerated single-query attention by 141x-309x, but relative L2 error was near zero only for anchor-heavy attention mass (0.000018 error, 0.999982 anchor mass) and was large when non-anchor tokens mattered (1.048-2.494 error).

## Boundaries and scale limits

No real transformer perplexity, generation quality, learned anchor selection, multi-layer effects, multi-head effects, batching, or production CPU serving stack was tested. The benchmark is synthetic and proxy-scale despite using long sequence lengths.

## Claim scope

Synthetic single-query CPU decode attention with 64 exact anchors and 64-token centroid compression over lengths 4096, 16384, and 32768 at dimension 64. The method is accurate only when full attention mass is already concentrated on preserved anchors.

## Why it stopped

Proxy/synthetic evidence shows exact anchor preservation alone is not generally accurate; it only works when attention mass is already anchor-dominant, so this is not full validation and not paper-ready.

## Recommended next action

Stop this run as a proxy early falsification of the broad exactness claim; only pursue a bounded deepen test if reframed as approximate anchor-biased KV compression with local-window preservation and real small-model perplexity controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Approximate anchor-plus-local KV compression on a small real transformer
- Success threshold: At least 4x KV memory reduction, at least 1.5x CPU decode speedup, and less than 2% relative perplexity degradation versus full KV on the selected public validation slice.
- Stop condition: Stop if anchors-plus-local exceeds 5% perplexity degradation at 4x compression or fails to beat full KV CPU decode throughput by 1.2x.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-context-on-cpu-9464a846a971`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
