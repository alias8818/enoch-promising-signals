# Segment-level recurrence for long-context CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `segment-level-recurrence-for-long-context-cpu-inference-2ff336750287`
Run ID: `segment-level-recurrence-for-long-context-cpu-inference-2ff336750287-20260522T115616996362+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c1981d2fd8ee

## What looked useful

Fixed segment summaries produced large state and latency reductions on CPU, but naive mean/sub-block recurrent summaries lost sparse old-token retrieval almost completely. Recent-window retrieval remained intact because recent tokens were kept exact.

## Boundaries and scale limits

No trained language model, no perplexity/task evaluation, no quantized production kernels, no batching, and no learned or query-conditioned memory. Runtime evidence is CPU-worker microbenchmark evidence only.

## Claim scope

Synthetic CPU single-token attention proxy comparing exact KV-cache attention with fixed segment recurrent summaries up to 65,536 tokens, d_key=128, d_value=64, 512-token exact recent window, and 1 or 4 mean summaries per 256-token old segment.

## Why it stopped

Proxy evidence is useful but not paper-ready: naive fixed segment recurrence is fast and memory-efficient, but it fails old-token retrieval in the synthetic mechanism test rather than validating general long-context CPU inference.

## Recommended next action

Stop this no-paper run; run a bounded follow-up that adds query-conditioned sparse segment retrieval or learned summaries and requires old-token target cosine >= 0.8 while retaining at least 10x state reduction at 65,536 tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Query-conditioned segment memory for sparse old-token retrieval
- Success threshold: At 65,536 tokens, old-token recurrent target cosine >= 0.8, local target cosine >= 0.98, and retained state reduction >= 10x with CPU per-query speedup >= 5x versus exact attention.
- Stop condition: Stop if old-token target cosine remains below 0.5 at >= 10x state reduction, or if the method requires retaining so many exact old tokens that speedup falls below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/segment-level-recurrence-for-long-context-cpu-inference-2ff336750287`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
