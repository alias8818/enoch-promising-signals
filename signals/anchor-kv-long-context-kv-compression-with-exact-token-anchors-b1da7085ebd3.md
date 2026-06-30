# Anchor-KV: Long-Context KV Compression with Exact Token Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-kv-long-context-kv-compression-with-exact-token-anchors-b1da7085ebd3`
Run ID: `anchor-kv-long-context-kv-compression-with-exact-token-anchors-b1da7085ebd3-20260628T023234878627+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9f1b28255977

## What looked useful

Anchor-KV reached 1.000 mean anchor hit rate across 40 synthetic 4096-token trials at 1%-8% cache budgets, while sliding-window and uniform exact-token baselines stayed around 0.033-0.110 anchor hit rate. Anchor output MSE versus full-cache attention was about 10x lower for Anchor-KV at 1% budget.

## Boundaries and scale limits

No real transformer LM, learned anchor selection, multi-layer cache interaction, GPU serving throughput, perplexity, or downstream long-context QA was tested. General non-anchor quality was not improved.

## Claim scope

In synthetic single-layer attention traces with oracle anchor positions, preserving exact K/V entries for marked anchors maintains anchor-directed recall under 1%-8% cache budgets when the anchor set fits in budget.

## Why it stopped

Closed as no-paper useful signal: this run provides a bounded synthetic mechanism test, not direct real-model evidence.

## Recommended next action

Implement Anchor-KV in a small transformer inference stack and run deterministic long-context retrieval plus perplexity/latency/memory comparisons against sliding-window and published KV-compression baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer Anchor-KV retrieval and perplexity confirmation
- Success threshold: At the same cache budget, Anchor-KV improves out-of-window retrieval accuracy by at least 20 percentage points over sliding-window and does not worsen perplexity by more than 5% relative to the strongest compressed baseline.
- Stop condition: Stop if Anchor-KV fails to beat sliding-window retrieval by at least 10 percentage points in the first real-model smoke, or if anchor preservation causes more than 10% perplexity degradation at the tested budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-kv-long-context-kv-compression-with-exact-token-anchors-b1da7085ebd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
