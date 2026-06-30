# N-gram draft speculative decoding for GPT-2-small inference speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-for-gpt-2-small-inference-speedup-617db0b6bf7b`
Run ID: `n-gram-draft-speculative-decoding-for-gpt-2-small-inference-speedup-617db0b6bf7b-20260604T215015184113+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/33ebd991a77f

## What looked useful

N-gram prompt/history drafting can reduce GPT-2-small target model calls on repetitive greedy outputs, but production-relevant fp16 exactness failed on several repetitive prompts; the result is useful for designing a stricter follow-up, not enough for a paper.

## Boundaries and scale limits

Single model size, one GPU host, fixed small prompt suite, greedy decoding only, no batching, no sampling, no long-context corpus, Python prototype cache handling, and fp16 validation did not exactly match cached greedy outputs.

## Claim scope

On a bounded 16-prompt GPT-2-small greedy decoding benchmark with 64 new tokens per prompt on GB10/CUDA, exact float32 n-gram draft validation produced mean speedups of 1.151x for 2-gram and 1.176x for 3-gram prompt/history lookup versus a KV-cache greedy baseline.

## Why it stopped

No-paper closure: bounded direct GPT-2-small evidence supports the mechanism in exact float32, but the practical fp16 path is not exact and the prompt suite is too small for publication-grade validation.

## Recommended next action

Run a bounded deepen test with bf16/fp16 exactness controls, tie-margin diagnostics, and an optimized non-mutating cache branch before considering any larger serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact low-precision n-gram speculative decoding controls for GPT-2-small
- Success threshold: Exact low-precision output match on all prompts and at least 1.10x mean speedup with p50 speedup above 1.05x for the best setting.
- Stop condition: Stop if low-precision exactness still fails after tie-margin controls, or if exact implementation overhead keeps mean speedup at or below 1.05x.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-gpt-2-small-inference-speedup-617db0b6bf7b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
