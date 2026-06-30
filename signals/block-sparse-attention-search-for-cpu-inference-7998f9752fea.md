# Block-Sparse Attention Search for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-sparse-attention-search-for-cpu-inference-7998f9752fea`
Run ID: `block-sparse-attention-search-for-cpu-inference-7998f9752fea-20260603T202221008914+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8eb4dc190ee9

## What looked useful

A radius-1 local block pattern met the <=0.10 relative L2 threshold on locality-biased inputs and accelerated CPU attention across all tested lengths; a random-input control showed sparse local attention fails badly without locality, bounding the mechanism claim.

## Boundaries and scale limits

Synthetic inputs only; no trained LLM traces, no perplexity or task-quality measurement, no production sparse kernel, one CPU host, one head dimension, and short bounded runs only.

## Claim scope

On a CPU worker using NumPy/OpenBLAS, searched local block-sparse causal attention over synthetic locality-biased Q/K/V can preserve output within 10% relative L2 error while improving prefill-style attention wall-clock latency by 3.9x to 15.2x for 512 to 2048 tokens.

## Why it stopped

Closed as no-paper useful signal because the positive mechanism evidence is synthetic/proxy and the control shows the claim depends on real attention locality.

## Recommended next action

Run a bounded deepen follow-up that replays block-pattern search on real small-LLM attention traces and measures next-token KL or perplexity impact against dense attention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay block-sparse CPU attention search on real small-LLM traces
- Success threshold: At least 2x median CPU attention speedup at 1024 or 2048 tokens with next-token KL <= 0.02 or layer-output relative L2 <= 0.10 on real prompts.
- Stop condition: Stop if no searched pattern reaches 1.5x speedup under the quality threshold on real traces, or if quality-preserving patterns require score density above 0.75.

## Evidence references

- Artifact root: `<local-path>/projects/block-sparse-attention-search-for-cpu-inference-7998f9752fea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
