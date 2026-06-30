# Queue-depth-driven KV compression with exact anchor tracking

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-depth-driven-kv-compression-with-exact-anchor-tracking-efdb9fe30216`
Run ID: `queue-depth-driven-kv-compression-with-exact-anchor-tracking-efdb9fe30216-20260608T021300124889+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/12924a52add1

## What looked useful

Queue-depth-adaptive exact-anchor compression preserved zero error at depth 1, reduced effective KV entries to 12.3% at depths 16/32, produced 14.48x and 7.51x decode-attention speedups versus full KV, and reduced anchor-seeking output error by about 5-8x compared with compressing old anchors.

## Boundaries and scale limits

No full LLM evaluation, no language-model loss or retrieval benchmark, no real serving traces, no continuous batching scheduler, no multi-layer cache interaction, and compression build was a Python prototype rather than an incremental production cache.

## Claim scope

Synthetic single-step CUDA attention benchmark at sequence length 4096, queue depths 1/4/16/32, float16 K/V, mean-pooled old non-anchor tokens, exact anchors plus recent window preserved.

## Why it stopped

No-paper useful signal: the mechanism is supported only by a synthetic GPU attention microbenchmark, not by direct LLM quality or real serving evidence.

## Recommended next action

Run a bounded direct-evidence follow-up with an incremental compressed KV cache inside a small decoder-only transformer and measure retrieval accuracy/perplexity under a continuous-batching simulator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incremental exact-anchor KV compression in a toy decoder serving simulator
- Success threshold: At high queue depth, adaptive exact-anchor compression should reduce decode latency or effective KV memory by at least 2x versus full KV while keeping retrieval accuracy within 2 percentage points and perplexity increase below 5%, and should outperform adaptive no-anchor compression on anchor-targeted probes.
- Stop condition: Stop if adaptive exact-anchor compression fails to beat full KV on latency/memory by 2x, loses more than 2 percentage points retrieval accuracy, raises perplexity by more than 5%, or anchor tracking no longer improves over the no-anchor ablation.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-driven-kv-compression-with-exact-anchor-tracking-efdb9fe30216`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
