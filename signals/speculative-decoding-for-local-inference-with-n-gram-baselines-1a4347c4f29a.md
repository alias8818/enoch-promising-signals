# Speculative Decoding for Local Inference with N-gram Baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-for-local-inference-with-n-gram-baselines-1a4347c4f29a`
Run ID: `speculative-decoding-for-local-inference-with-n-gram-baselines-1a4347c4f29a-20260608T084611991991+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/19c7a26103ad

## What looked useful

Unigram prompt/history lookup with max draft 8 reduced target forwards from 384 to 219 on GPT-2 repeated prompts and from 384 to 179 on DistilGPT-2 repeated prompts, with observed tokens/s speedups of 1.55x and 1.73x versus no-draft greedy. Non-repetitive prompts were weak: GPT-2 n=1 reached 1.27x ideal and 1.22x observed speedup, while DistilGPT-2 reached only 1.05x ideal and 1.04x observed speedup. Exactness checks matched greedy decoding.

## Boundaries and scale limits

Tested only cached gpt2 and distilgpt2 models, 12 hand-authored repeated prompts and 12 hand-authored non-repetitive prompts, 32 generated tokens per prompt, Python/Hugging Face implementation, greedy decoding only. No optimized serving engine, production traces, larger instruction models, batching, quantization, or latency percentile study.

## Claim scope

Small local CUDA experiments with exact greedy speculative decoding show that prompt/history n-gram lookup can reduce target forwards for GPT-2-class models on repetition-heavy prompts, but benefits are much weaker on non-repetitive prompts.

## Why it stopped

Evidence is bounded and useful but too small and hand-authored for a paper; it supports n-gram speculative decoding as a repetition-sensitive baseline rather than a broadly validated local inference method.

## Recommended next action

Stop this run as a no-paper useful signal; deepen only with a real trace or benchmark corpus stratified by prompt repetition and an optimized local inference runtime.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-stratified n-gram speculative decoding benchmark for local inference
- Success threshold: Show at least 1.25x median tokens/s or latency improvement over no-draft on the high-repetition split without regression greater than 5% on low-repetition prompts, with exact output equivalence under deterministic decoding.
- Stop condition: Stop if high-repetition prompts fail to reach 1.15x observed speedup in an optimized runtime or if low-repetition routing cannot avoid measurable regressions.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-for-local-inference-with-n-gram-baselines-1a4347c4f29a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
