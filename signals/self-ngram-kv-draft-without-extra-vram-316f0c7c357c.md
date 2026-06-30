# Self-ngram KV draft without extra VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `self-ngram-kv-draft-without-extra-vram-316f0c7c357c`
Run ID: `self-ngram-kv-draft-without-extra-vram-316f0c7c357c-20260604T043212540828+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c9e6c312f6e1

## What looked useful

Float32 exact runs showed 3.10x speedup and 68.38% fewer forwards on repetitive prompts, and 1.97x speedup with 45.88% fewer forwards on lower-repetition control prompts. Peak CUDA allocation increased by about 2.0-2.2 MB and no draft model or persistent second KV cache was used.

## Boundaries and scale limits

Only GPT-2-small, greedy decoding, 6 repetitive prompts and 6 control prompts, 96 generated tokens per prompt, local GB10 PyTorch/Transformers harness. No 7B+ model, no production serving engine, no real benchmark corpus, no sampling correction, and fp16 exactness failed in this implementation.

## Claim scope

On GPT-2-small greedy decoding over two six-prompt local suites, self-ngram batched verification using the same target KV cache reduced forward calls and improved wall-clock throughput with only a small temporary CUDA memory increase, while preserving exact greedy output in float32.

## Why it stopped

No-paper closure: the local GPT-2-small evidence supports the mechanism, but the result is too small and synthetic for a paper and fp16 exactness failed.

## Recommended next action

Run a bounded direct follow-up in a production-style inference engine on a 1B-7B model with long-context benchmark prompts, exactness checks under the intended serving dtype, and latency/memory telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact low-precision self-ngram KV drafting on realistic long-context inference
- Success threshold: At least 1.3x median decode speedup on repeated long-context workloads with no persistent extra model/cache VRAM, no exactness failures under the intended dtype, and no more than 5% slowdown on low-repetition controls.
- Stop condition: Stop if exactness cannot be preserved under the serving dtype, if median speedup is below 1.1x after overheads, or if low-repetition controls regress by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/self-ngram-kv-draft-without-extra-vram-316f0c7c357c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
