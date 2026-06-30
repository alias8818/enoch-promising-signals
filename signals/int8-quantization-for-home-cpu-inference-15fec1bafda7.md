# INT8 Quantization for Home CPU Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int8-quantization-for-home-cpu-inference-15fec1bafda7`
Run ID: `int8-quantization-for-home-cpu-inference-15fec1bafda7-20260611T003731870951+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1c2cf98124c5

## What looked useful

Across 2048x2048, 4096x4096, and 11008x4096 matvecs at 1/4/8 threads, int8 weights cut storage from fp32 by 4x. Confirmation medians showed weight-only int8 speedups from 1.15x to 9.10x and int8-activation speedups from 1.53x to 8.68x, with relative RMSE about 0.0038-0.0040 for w8a32 and 0.0054-0.0057 for w8a8.

## Boundaries and scale limits

No real LLM runtime, tokenizer, KV cache, sampling loop, mmap behavior, power measurement, or perplexity/quality evaluation was tested. The host is a virtualized Xeon Silver 4114 CPU worker with only CPUs 0-7 online and no AVX-512 VNNI, so results should not be generalized to all home CPUs.

## Claim scope

On this CPU worker, synthetic batch-1 transformer-like matrix-vector layers using symmetric per-row int8 weights reduced weight memory 4x and usually improved latency versus fp32, with low relative RMSE. This supports int8 as a practical mechanism for home CPU inference kernels, not full LLM serving.

## Why it stopped

Synthetic kernel evidence supports the mechanism but is insufficient for full home CPU inference validation or a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded real-model llama.cpp follow-up on the same CPU class with tokens/sec, RSS, quality/perplexity, and affinity-controlled repetitions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU tokens/sec validation for int8 quantized LLM inference
- Success threshold: Int8 quantized model achieves at least 1.3x median tokens/sec improvement or at least 35% peak RSS reduction versus the closest higher-precision baseline, while maintaining a bounded quality/perplexity delta judged acceptable for the selected model.
- Stop condition: Stop if int8 is slower than baseline in median tokens/sec at matched thread counts and quality/perplexity is worse beyond the predefined threshold, or if no comparable higher-precision baseline can be run within local memory.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-for-home-cpu-inference-15fec1bafda7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
