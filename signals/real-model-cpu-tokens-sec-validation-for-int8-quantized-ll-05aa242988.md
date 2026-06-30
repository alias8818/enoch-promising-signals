# Real-model CPU tokens/sec validation for int8 quantized LLM inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-cpu-tokens-sec-validation-for-int8-quantized-ll-05aa242988`
Run ID: `real-model-cpu-tokens-sec-validation-for-int8-quantized-ll-05aa242988-20260611T005438176976+0000`

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

- Parent run decision: INT8 Quantization for Home CPU Inference: enoch://control-plane/projects/int8-quantization-for-home-cpu-inference-15fec1bafda7/runs/int8-quantization-for-home-cpu-inference-15fec1bafda7-20260611T003731870951+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1c2cf98124c5

## What looked useful

A real quantized LLM ran successfully on CPU with direct generated-token measurements: 4 threads averaged 17.50 tok/s in the 128-token sweep and 19.24 tok/s in a 256-token confirmation; 8 threads was unstable and slower on average.

## Boundaries and scale limits

Single CPU host, one 0.5B-class Q8_0 GGUF model, one prompt shape, no batching, no long-context test, no larger-model validation, and no fp16/fp32 or other-quantization baseline. The controller prompt did not provide a numeric throughput threshold.

## Claim scope

On cpu-worker with 8 online logical CPUs, llama-cpp-python CPU-only inference for Qwen2.5 0.5B Instruct GGUF Q8_0 achieved about 18-20 generated tokens/sec at the best tested 4-thread setting for 128-256 token generations.

## Why it stopped

No-paper Tier 1 direct measurement completed; evidence is useful but too narrow for publication and lacks the numeric threshold referenced by the controller prompt.

## Recommended next action

Run the same harness on a 1B-1.5B Q8_0 model with a predeclared throughput threshold, then compare against this 0.5B result before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 1B-class Q8_0 CPU throughput confirmation for real LLM inference
- Success threshold: Best thread count mean >= 10 generated tokens/sec over at least two 256-token generations, min run >= 8 generated tokens/sec, and max RSS <= 2 GiB.
- Stop condition: Stop as unsupported if all tested thread counts average below 10 generated tokens/sec or any valid run exceeds 2 GiB RSS on the CPU worker.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-cpu-tokens-sec-validation-for-int8-quantized-ll-05aa242988`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
