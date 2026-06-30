# Suffix-Cache SpecDec for Local Draft-Target Pairs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `suffix-cache-specdec-for-local-draft-target-pairs-720991cffe69`
Run ID: `suffix-cache-specdec-for-local-draft-target-pairs-720991cffe69-20260531T233121878478+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4b1cd1e04538

## What looked useful

Naive suffix-only target cache reuse produced mean target total variation 0.232 on natural prefixes and 0.207 on equal-length prefixes; GPT-2 target / distilgpt2 draft acceptance probability changed by 0.207 mean and up to 0.452 for draft top tokens, while identical full-context repeat controls had zero drift.

## Boundaries and scale limits

Tested on small GPT-2/distilgpt2 and distilgpt2-only probes with 12 natural-prefix contexts plus a 4-context equal-prefix-token-length control. Did not test optimized serving throughput, larger 1B/7B pairs, multi-token draft blocks, or quality under approximate reuse.

## Claim scope

For GPT-2-class decoder-only local draft-target speculative decoding, a target verification cache keyed only by a shared prompt suffix is not exact across different prefixes; it changes target distributions and draft-token acceptance probabilities.

## Why it stopped

Bounded direct/proxy falsification: the run directly showed cross-prefix target distribution drift and SpecDec acceptance-ratio errors, so suffix-only reuse is not a correct exact target verification cache.

## Recommended next action

Stop this naive suffix-only exact-cache line; a follow-up should test a complete-history trie/KV cache or an explicitly approximate suffix reuse method with quality and acceptance-error bounds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Complete-History Trie Cache for Local SpecDec Prefill Reuse
- Success threshold: Zero distribution/decision mismatch against uncached verification for identical complete histories, plus at least 10% end-to-end latency reduction on a repeated-prompt trace.
- Stop condition: Stop if correctness requires keys as large as the full uncached KV state with no measurable latency or memory benefit on repeated traces.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-cache-specdec-for-local-draft-target-pairs-720991cffe69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
