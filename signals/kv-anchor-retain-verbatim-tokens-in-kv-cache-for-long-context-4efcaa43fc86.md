# KV-Anchor: Retain Verbatim Tokens in KV Cache for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-anchor-retain-verbatim-tokens-in-kv-cache-for-long-context-4efcaa43fc86`
Run ID: `kv-anchor-retain-verbatim-tokens-in-kv-cache-for-long-context-4efcaa43fc86-20260628T060334735884+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c40863a826e

## What looked useful

At 16k context and 512-token budget, heuristic KV-anchor retention kept the exact target span in 88.3% of trials versus 1.7% for both sliding-window and sink-plus-window baselines; at 1024 and 2048 budgets it reached 100%. Oracle anchor retention was 100% in every group. Heuristic failures were caused by distractor anchors consuming the reserved anchor budget.

## Boundaries and scale limits

Proxy-only cache-token retention simulation; no transformer inference, real KV-cache kernel, model logits, real tokenization, natural corpus, or latency measurement. Contexts were 4096-16384 synthetic tokens with 60 trials per length.

## Claim scope

Deterministic simulator evidence shows that retaining detected verbatim anchor spans in a bounded KV-token cache preserves answer-critical spans much better than sliding-window or sink-plus-window retention on synthetic long-context streams, when the correct span is detected and the anchor budget is not exhausted by distractors.

## Why it stopped

Proxy simulation supports the mechanism but is not direct model evidence and cannot justify a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the retention policy into a small causal LM inference cache and measure answer exact match, memory, and latency against sliding-window and sink-token baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-Anchor in a Small Transformer Inference Cache
- Success threshold: At least 20 percentage points higher exact-match accuracy than the best recency baseline at equal KV-token budget on two context lengths, with less than 25% latency overhead and documented distractor failure cases.
- Stop condition: Stop if non-contiguous/block KV retention cannot be implemented locally, or if accuracy gain is below 5 percentage points at equal budget on the first two evaluated context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/kv-anchor-retain-verbatim-tokens-in-kv-cache-for-long-context-4efcaa43fc86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
