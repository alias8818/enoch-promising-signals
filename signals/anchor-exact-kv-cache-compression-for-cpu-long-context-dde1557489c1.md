# Anchor-Exact KV Cache Compression for CPU Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-exact-kv-cache-compression-for-cpu-long-context-dde1557489c1`
Run ID: `anchor-exact-kv-cache-compression-for-cpu-long-context-dde1557489c1-20260610T010134488202+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb42f9c0ae34

## What looked useful

The mechanism is conditionally promising when attention mass aligns with exact anchors or locally coherent blocks, but the iid control shows high relative L2 error around 0.74-0.78 at 32k context, falsifying a broad general-accuracy claim.

## Boundaries and scale limits

No real transformer KV traces, no end-to-end inference engine integration, no perplexity or generation-quality measurement, one CPU host, sequence length capped at 32768, dimension capped at 128.

## Claim scope

Synthetic NumPy CPU proxy for single-step decode attention: periodic anchor KV entries plus count-weighted block summaries can reduce attention slots by 21-32x and preserve outputs on smooth block-structured or anchor-retrieval traces, but not on iid diffuse-attention traces.

## Why it stopped

Proxy evidence produced a useful mechanism signal and a clear failure mode, but it is not full validation and does not support a paper now.

## Recommended next action

Run a bounded deepen test on real long-context transformer KV traces, measuring per-layer/head attention-output error and task quality before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-exact compression on real transformer KV traces
- Success threshold: At least 8x effective slot reduction with median per-layer/head relative L2 <= 0.02, p95 <= 0.05, and task accuracy or quality drop <= 1 percentage point on the tested workload.
- Stop condition: Stop if real KV traces show median relative L2 > 0.10 at 4x slot reduction or task quality drops by more than 3 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-cache-compression-for-cpu-long-context-dde1557489c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
