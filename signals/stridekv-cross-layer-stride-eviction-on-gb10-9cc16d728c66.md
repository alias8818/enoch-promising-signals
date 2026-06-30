# StrideKV: Cross-Layer Stride Eviction on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stridekv-cross-layer-stride-eviction-on-gb10-9cc16d728c66`
Run ID: `stridekv-cross-layer-stride-eviction-on-gb10-9cc16d728c66-20260630T050115730179+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc6ddb85ba8b

## What looked useful

Cross-layer stride retained about 0.031 more full-attention mass and reduced mean relative L2 error by about 0.045 versus a global stride phase in the layer-phased synthetic scenario across 10/10 seeds, but lost to the matching global stride phase in the global-phase scenario across 10/10 seeds.

## Boundaries and scale limits

No real transformer weights, no perplexity or task evaluation, no autoregressive serving loop, no allocator integration, and no long-context production traces were tested.

## Claim scope

Synthetic GB10 CUDA attention-output proxy at sequence length 8192, 12 layers, 8 heads, head dimension 64, and 12.5% retained KV tokens shows cross-layer stride eviction helps when distant attention-relevant tokens are layer-phase shifted, but not when phases are globally aligned, random, or recent.

## Why it stopped

Proxy evidence is mixed: it supports the conditional mechanism but early-falsifies a generic cross-layer stride eviction advantage and is not direct/full validation.

## Recommended next action

Stop this run as no-paper proxy evidence; next, test the same policies inside a small real transformer decode/perplexity harness with diagnosed layer-wise attention phases before considering any larger GB10 serving experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model decode test for layer-phased StrideKV eviction
- Success threshold: At the same retained KV budget, cross-layer stride improves next-token loss or perplexity by at least 2% relative to both sliding-window and global-stride baselines on at least 3 seeds or prompt shards, without reducing decode throughput by more than 5%.
- Stop condition: Stop if real-model layer-wise attention is not phase-diverse, or if cross-layer stride fails to beat both equal-budget baselines on loss/perplexity in the first bounded decode replay.

## Evidence references

- Artifact root: `<local-path>/projects/stridekv-cross-layer-stride-eviction-on-gb10-9cc16d728c66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
