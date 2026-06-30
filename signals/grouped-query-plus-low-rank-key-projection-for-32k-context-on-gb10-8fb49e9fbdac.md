# Grouped-Query Plus Low-Rank Key Projection for 32k Context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `grouped-query-plus-low-rank-key-projection-for-32k-context-on-gb10-8fb49e9fbdac`
Run ID: `grouped-query-plus-low-rank-key-projection-for-32k-context-on-gb10-8fb49e9fbdac-20260619T184557894584+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fbfae992bbdc

## What looked useful

At 32k context with 32 query heads and head dim 64, 4-KV-head GQA reduced baseline logical KV cache from 256 MiB to 32 MiB and decode time from about 1.24 ms to 0.316 ms. Adding rank-16 key projection reduced the 4-KV-head cache to 20 MiB and decode time to about 0.249 ms, but relative L2 error rose to roughly 0.66-0.75 when activations were high-rank/noisy.

## Boundaries and scale limits

No trained model, no perplexity or downstream task evaluation, no fused production attention kernel, batch size 1 only, synthetic activations only, and no end-to-end generation benchmark.

## Claim scope

Synthetic single-token decode microbenchmark on NVIDIA GB10: GQA plus rank-16 or rank-32 key projection reduces logical KV-cache bytes and can improve unfused PyTorch attention latency at 32k context when query/key activations are low-intrinsic-rank or near the retained subspace.

## Why it stopped

The result is a synthetic proxy useful signal, not full validation: it supports the memory/latency mechanism under low-rank assumptions but shows large attention-output error when activations are not low-rank and provides no trained-model quality evidence.

## Recommended next action

Run a parameter-matched GPT-2-small-class follow-up comparing MHA, GQA, and GQA plus low-rank key projection on perplexity plus 32k decode throughput; stop this run as no-paper microbenchmark evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched GPT-2-small test of GQA plus low-rank key projection
- Success threshold: GQA plus low-rank keys achieves validation perplexity within 2 percent of the matched GQA control while reducing logical KV-cache bytes by at least 25 percent and improving 32k decode latency by at least 10 percent on GB10.
- Stop condition: Stop if perplexity worsens by more than 5 percent versus the GQA control at equal training budget, or if 32k decode latency improves by less than 5 percent after cache projection overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/grouped-query-plus-low-rank-key-projection-for-32k-context-on-gb10-8fb49e9fbdac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
