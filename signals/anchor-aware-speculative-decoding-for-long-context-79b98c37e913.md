# Anchor-Aware Speculative Decoding for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-aware-speculative-decoding-for-long-context-79b98c37e913`
Run ID: `anchor-aware-speculative-decoding-for-long-context-79b98c37e913-20260620T035417565254+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a49c4c28f6c4

## What looked useful

Unique anchor-aware draft retrieval reduced verifier calls by 16.7% versus prompt lookup in the synthetic anchor-gap condition, matched baseline on direct-copy and corrupt-anchor controls, and required a uniqueness guard to avoid severe regressions with duplicate anchors.

## Boundaries and scale limits

No real LLM inference, tokenizer, KV-cache, GPU latency, batching, or natural long-context corpus was tested. Proxy speedup is based on verifier-call count rather than wall-clock serving latency.

## Claim scope

Synthetic lossless speculative-decoding simulator with paired trials over anchor-gap, direct-copy, corrupt-anchor, and duplicate-anchor conditions. A unique-anchor guard reduced verifier calls in the intended anchor-gap mechanism case and avoided duplicate-anchor regressions.

## Why it stopped

Proxy-only synthetic mechanism evidence is useful but insufficient for paper-positive validation of long-context LLM serving.

## Recommended next action

Stop this run as a synthetic useful signal; next run should implement the guarded policy in a real small-model speculative decoding stack and measure wall-clock latency plus verifier calls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Guarded anchor-aware drafting in real small-model speculative decoding
- Success threshold: At least 10% wall-clock latency reduction and at least 10% target-forward-pass reduction versus prompt lookup on unique-anchor tasks, with no statistically meaningful regression on corrupt or duplicate-anchor controls.
- Stop condition: Stop if guarded anchor-aware drafting fails to reduce wall-clock latency by 5% versus prompt lookup or if draft overhead erases verifier-call savings on the small-model benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-aware-speculative-decoding-for-long-context-79b98c37e913`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
