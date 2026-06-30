# INT4 weight-only quantization with calibration for CPU LM inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-weight-only-quantization-with-calibration-for-cpu-lm-inference-037d38acc6c0`
Run ID: `int4-weight-only-quantization-with-calibration-for-cpu-lm-inference-037d38acc6c0-20260613T090952186759+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/032f66016b8b

## What looked useful

Calibration is useful for reducing grouped INT4 output error in a bounded LM-linear proxy, but naive dequantize-each-call CPU inference was only 0.212x FP32 speed. A real CPU INT4 kernel and real-model perplexity test are required before any paper claim.

## Boundaries and scale limits

One NumPy CPU worker run, synthetic heavy-tailed weights and activations, three GPT-2-small-shape linear projections, no real pretrained model, no tokenizer/corpus, no native INT4 GEMM. Runtime was 3.58 seconds for the main proxy.

## Claim scope

Synthetic GPT-2-small-shaped linear-layer proxy: calibration-selected clipping for grouped signed INT4 weight-only quantization reduced held-out output relative MSE by 13.67% versus max-absolute INT4, and reduced shifted-activation relative MSE by 13.10%. The result does not cover real LM perplexity or optimized packed INT4 CPU kernels.

## Why it stopped

Proxy-only useful signal: calibration reduced output error, but no real LM quality evidence was produced and the naive CPU implementation was not speed-viable.

## Recommended next action

Run a bounded direct-evidence follow-up on a real small LM using corpus perplexity and a native packed INT4 CPU kernel; do not write a paper from this proxy-only run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LM INT4 calibration perplexity and native CPU kernel test
- Success threshold: Calibrated INT4 must reduce perplexity degradation by at least 10% relative to max-absolute INT4 at the same group size and achieve at least 1.2x single-thread or bounded-thread latency speedup versus FP32 on the tested CPU kernel.
- Stop condition: Stop if calibrated INT4 does not improve held-out perplexity over max-absolute INT4, or if the native packed INT4 kernel is not faster than FP32 under the same thread and batch settings.

## Evidence references

- Artifact root: `<local-path>/projects/int4-weight-only-quantization-with-calibration-for-cpu-lm-inference-037d38acc6c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
