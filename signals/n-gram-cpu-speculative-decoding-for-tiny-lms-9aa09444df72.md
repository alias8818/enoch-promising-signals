# N-gram CPU Speculative Decoding for Tiny LMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-speculative-decoding-for-tiny-lms-9aa09444df72`
Run ID: `n-gram-cpu-speculative-decoding-for-tiny-lms-9aa09444df72-20260528T200854046143+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57b4ce2850fe

## What looked useful

The mechanism works and was exact in corrected final runs: tiny-gpt2 had 2.26x-2.76x mean speedups by suite/config with 0 incorrect records; DistilGPT-2 natural prompts had 1.02x-1.14x mean speedups with low 0.20-0.33 acceptance, while repetitive prompts had 1.11x-1.33x mean speedups with 0.49-0.68 acceptance. This suggests prompt-local n-gram speculative decoding is useful mainly when local repetition makes draft acceptance likely.

## Boundaries and scale limits

Tested only Hugging Face PyTorch CPU inference, greedy decoding, 1-thread final runs plus a small 8-thread sensitivity check, 8 total tiny-gpt2 prompts at 32 new tokens, and 4 DistilGPT-2 prompts at 16 new tokens. No long-context corpus benchmark, production runtime, quantized runtime, batching, broad model family, or paper-grade prompt distribution was tested.

## Claim scope

Local CPU-only greedy decoding benchmarks show that prompt/history n-gram drafting can exactly preserve target-model greedy output and reduce wall-clock time for tiny/small GPT-style LMs, with strong gains on a pathological tiny GPT-2 checkpoint and modest to moderate gains on bounded DistilGPT-2 prompts.

## Why it stopped

Bounded direct CPU evidence supports the mechanism but is too small and distribution-dependent for a publication-grade positive result.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test adaptive gating and corpus-augmented n-gram drafting on a small public text benchmark before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive n-gram speculative decoding on a public small-LM text benchmark
- Success threshold: At least 1.15x geometric-mean wall-clock speedup over cached greedy decoding with zero token mismatches and no prompt suite below 1.00x.
- Stop condition: Stop if exactness fails after repair fixes, or if geometric-mean speedup is below 1.05x or any major natural-text prompt suite is slower than cached greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-speculative-decoding-for-tiny-lms-9aa09444df72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
