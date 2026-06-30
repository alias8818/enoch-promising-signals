# CPU n-gram speculative decoding for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-gpt-2-small-1b8a81884701`
Run ID: `cpu-n-gram-speculative-decoding-for-gpt-2-small-1b8a81884701-20260526T003731051693+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/03f9b4ed37ec

## What looked useful

The mechanism is real but not sufficient in this bounded CPU implementation: n=1 drafts accepted 173-184 tokens across 10 prompts, yet mean throughput fell from about 15.2 tokens/s baseline to about 8.5-8.6 tokens/s speculative.

## Boundaries and scale limits

Small prompt set, greedy decoding only, Python implementation, no batch serving, no optimized KV-preserving rejection path, no long-context corpus evaluation.

## Claim scope

For a Python/Hugging Face exact greedy GPT-2-small CPU implementation on 10 fixed prompts with 64 generated tokens each, unigram n-gram speculation accepted some draft tokens but reduced wall-clock throughput to about 0.57-0.58x of the KV-cache greedy baseline.

## Why it stopped

Bounded direct GPT-2-small CPU tests showed exact n-gram speculation was slower than baseline despite nonzero acceptance; this is an early falsification of the naive speedup hypothesis, not a full validation across optimized implementations.

## Recommended next action

Stop this run as a no-paper useful negative; only revisit with a KV-preserving rejection implementation and adaptive proposal gating benchmarked on at least 50 prompts x 128 new tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-preserving adaptive n-gram speculation for GPT-2-small CPU decoding
- Success threshold: Mean tokens/s at least 1.10x baseline and median speedup at least 1.05x with exact token equality on all prompts.
- Stop condition: Stop as negative if adaptive KV-preserving speculation remains below 1.00x mean speedup or exactness fails on any prompt.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-gpt-2-small-1b8a81884701`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
