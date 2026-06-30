# 1-layer draft plus n-gram cache for GPT-2 speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-layer-draft-plus-n-gram-cache-for-gpt-2-speculative-decoding-6aeac9324898`
Run ID: `1-layer-draft-plus-n-gram-cache-for-gpt-2-speculative-decoding-6aeac9324898-20260601T091001416697+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/720c4f3d6b32

## What looked useful

N-gram cache raised acceptance from 7.3% to 25.6% at gamma=4 and from 12.1% to 36.3% at gamma=2, but target-only greedy remained faster: 221 tok/s versus 133 tok/s at gamma=4 and 213 tok/s versus 145 tok/s at gamma=2.

## Boundaries and scale limits

Small prompt set, 384 generated tokens per valid run, bfloat16 CUDA on GB10, full-context exact verification rather than optimized KV-cache speculative serving, no trained/distilled draft, no batch-serving or larger-model validation.

## Claim scope

On 8 short prompts with GPT-2-small greedy decoding, a one-layer GPT-2 draft initialized from target weights is a weak proposer; adding an online n-gram cache improves acceptance and reduces draft calls but does not beat target-only full-context greedy throughput in the exact benchmark.

## Why it stopped

Bounded exact GPT-2-small evidence shows a mechanism improvement from the n-gram cache but not a practical speedup; the result is an early local falsification of the simple speed claim, not a full-scale validation.

## Recommended next action

Stop this run as no-paper evidence; a bounded follow-up should test an exact optimized KV-cache verifier against a cached target-only baseline before any larger scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact KV-cache speculative decoding benchmark for GPT-2 one-layer draft plus n-gram cache
- Success threshold: At least 1.15x wall-time speedup over cached target-only greedy with 100% exact-match outputs and target calls/token below 0.9 on the selected prompt suite.
- Stop condition: Stop if exactness fails after cache rollback fixes, or if acceptance remains below 40% and throughput remains below target-only greedy on the 100-prompt suite.

## Evidence references

- Artifact root: `<local-path>/projects/1-layer-draft-plus-n-gram-cache-for-gpt-2-speculative-decoding-6aeac9324898`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
