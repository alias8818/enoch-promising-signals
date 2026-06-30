# Ternary draft with FP8 residual for CPU spec decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-draft-with-fp8-residual-for-cpu-spec-decoding-f3f73cba610f`
Run ID: `ternary-draft-with-fp8-residual-for-cpu-spec-decoding-f3f73cba610f-20260628T210717455746+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ba6eef76f325

## What looked useful

At temperature 1.0, a 20% sparse FP8 residual improved acceptance surrogate over ternary-only by +0.0639 to +0.0825 across tested ternary densities. Best practical under-8-bit case reached 0.8989 mean acceptance surrogate, 0.8945 p05, KL 0.0323, top-1 agreement 0.5684, and 6.80 bits/weight with 16-bit sparse indexes.

## Boundaries and scale limits

No real transformer weights, token traces, packed CPU ternary kernel, sparse FP8 residual kernel, KV-cache interaction, or end-to-end speculative decoding throughput was tested. Dense NumPy timings are not CPU speedup evidence.

## Claim scope

Synthetic LM-head-like projection proxy shows sparse FP8 residuals can materially improve distribution match and speculative acceptance surrogate over ternary-only weights while staying below an 8-bit dense storage budget under simple sparse-index accounting.

## Why it stopped

Proxy evidence supports the residual-correction mechanism but does not validate real CPU speculative decoding speedup or model behavior, so publication-grade closure is not available from this run.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded direct follow-up using real small transformer weights, token traces, and a faithful packed/sparse CPU cost model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-transformer CPU speculative decoding with ternary draft and sparse FP8 residual
- Success threshold: At least 1.15x CPU tokens/s versus the best dense-small or ternary-only draft baseline at matched output quality, with mean speculative acceptance at least 0.85 and no worse than 1% relative quality drift on the chosen held-out corpus.
- Stop condition: Stop if the sparse residual path fails to exceed ternary-only acceptance by 0.03 absolute on real model traces, or if measured residual overhead removes any projected tokens/s gain.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-draft-with-fp8-residual-for-cpu-spec-decoding-f3f73cba610f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
