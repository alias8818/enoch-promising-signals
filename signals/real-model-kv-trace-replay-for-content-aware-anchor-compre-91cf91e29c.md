# Real-model KV trace replay for content-aware anchor compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-kv-trace-replay-for-content-aware-anchor-compre-91cf91e29c`
Run ID: `real-model-kv-trace-replay-for-content-aware-anchor-compre-91cf91e29c-20260516T062012655924+0000`

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

- Internal Enoch project: Real-model KV trace replay for content-aware anchor compression: internal_generated:real-model-kv-trace-replay-for-content-aware-anchor-compre-91cf91e29c

## What looked useful

Exact content anchor rows are strong retrieval handles, but naive anchor-plus-recent cache replay is brittle in noisy long prefixes and can be much worse than target-anchor-only or full replay.

## Boundaries and scale limits

Single 3B-class model, synthetic forced-choice retrieval prompts, oracle span selector, Hugging Face cache-pruning replay rather than a production serving kernel, no learned selector, no organic traces, and no end-to-end latency benchmark.

## Claim scope

On a 48-example fixed-seed synthetic multi-record retrieval task with Qwen/Qwen2.5-3B-Instruct and real Hugging Face KV trace replay, oracle target-record-only retention preserved 41/48 answers with a median of 41 retained prefix tokens, but the intended content-anchor-plus-recent policy achieved only 13/48 to 20/48 across 256-1024 retained-token budgets.

## Why it stopped

Tier 2 real-model replay did not support the intended content-anchor-plus-recent compression policy: full cache reached 45/48, target-anchor-only reached 41/48, but content-anchor-plus-recent reached only 20/48, 15/48, and 13/48 at 256, 512, and 1024 retained tokens.

## Recommended next action

Stop this paper claim; if continuing, run a bounded mechanism test that isolates why retained recent distractor KV suppresses the selected anchor and whether segment-aware masking fixes it.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Segment-aware masking for content-anchor KV replay
- Success threshold: Segment-aware or distractor-suppressed content-anchor-plus-recent reaches at least 38/48 accuracy at 512 retained tokens, beats recent-only and uniform by paired sign test p < 0.05, and loses no more than 5 examples relative to target-anchor-only.
- Stop condition: Stop if the modified policy remains below 32/48 accuracy at 512 retained tokens or still performs significantly worse than target-anchor-only, because the problem is then not just recent distractor interference.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-kv-trace-replay-for-content-aware-anchor-compre-91cf91e29c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
