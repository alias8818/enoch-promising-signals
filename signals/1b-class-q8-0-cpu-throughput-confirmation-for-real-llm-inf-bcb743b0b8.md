# 1B-class Q8_0 CPU throughput confirmation for real LLM inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1b-class-q8-0-cpu-throughput-confirmation-for-real-llm-inf-bcb743b0b8`
Run ID: `1b-class-q8-0-cpu-throughput-confirmation-for-real-llm-inf-bcb743b0b8-20260611T013629185509+0000`

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

- Parent run decision: INT8 Quantization for Home CPU Inference: enoch://control-plane/projects/int8-quantization-for-home-cpu-inference-15fec1bafda7/runs/int8-quantization-for-home-cpu-inference-15fec1bafda7-20260611T003731870951+0000
- Parent run decision: Real-model CPU tokens/sec validation for int8 quantized LLM inference: enoch://control-plane/projects/real-model-cpu-tokens-sec-validation-for-int8-quantized-ll-05aa242988/runs/real-model-cpu-tokens-sec-validation-for-int8-quantized-ll-05aa242988-20260611T005438176976+0000

## What looked useful

Direct real-model CPU benchmarks show Q8_0 is viable but slower than same-model Q4_K_M: best Q8_0 generation was 6.47 tok/s versus Q4_K_M 8.50 tok/s, and best Q8_0 prompt processing was 77.23 tok/s versus Q4_K_M 101.39 tok/s. Thread scaling was non-monotonic, with generation peaking at 10 threads and degrading at 20/40 threads; explicit NUMA distribute/isolate modes were slower than default at the Q8_0 10-thread point.

## Boundaries and scale limits

Single host, one 1.5B model family, one benchmark harness, one prompt/generation length pair, no quality evaluation, and no newer CPU or production serving validation. The Q4_K_M control was faster across measured cells, so this is not a paper-positive throughput claim for Q8_0.

## Claim scope

On an Intel Xeon Silver 4114 dual-socket CPU worker, Qwen2.5-1.5B-Instruct Q8_0 GGUF runs real CPU-only llama.cpp inference with best observed throughput of 77.23 prompt tok/s at 20 threads and 6.47 generation tok/s at 10 threads for 512-token prompt and 128-token generation benchmarks.

## Why it stopped

Medium direct evidence supports practical viability of 1.5B Q8_0 CPU inference on this host but does not support a paper-positive throughput advantage because the real Q4_K_M baseline is consistently faster.

## Recommended next action

Stop this run as a no-paper useful signal; only deepen if the next bounded test compares default scheduling against explicit CPU affinity/NUMA pinning on a newer CPU under the same Q8_0 versus Q4_K_M harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU affinity and newer-CPU check for 1.5B Q8_0 generation throughput
- Success threshold: A useful deepen result requires Q8_0 generation at least 20% faster than this run's 6.47 tok/s default best on comparable hardware settings, or a clear falsification showing no affinity/NUMA setting beats default by more than 5%; paper-positive would additionally require Q8_0 to match or exceed Q4_K_M throughput under a quality-justified setting, which this run did not show.
- Stop condition: Stop if all tested affinity/NUMA settings keep Q8_0 generation within 5% of or below the current 6.47 tok/s default best, or if Q4_K_M remains at least 15% faster at every tuned setting.

## Evidence references

- Artifact root: `<local-path>/projects/1b-class-q8-0-cpu-throughput-confirmation-for-real-llm-inf-bcb743b0b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
