# SpecDec Int3 Residual Draft CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `specdec-int3-residual-draft-cpu-3fa9f7d00818`
Run ID: `specdec-int3-residual-draft-cpu-3fa9f7d00818-20260604T021654002841+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d35ed7b1d326

## What looked useful

Packed int3 residual was slower than fp32 and int8 on the larger 4096x4096 projection, with only 0.33x to 0.56x speedup versus fp32 for residual variants and weak top-1 logit agreement around 0.42 to 0.47. Int8 had much stronger fidelity, around 7.5e-05 relative MSE and 0.95 to 1.0 top-1 agreement.

## Boundaries and scale limits

No real language model, tokenizer, autoregressive cache, or end-to-end speculative decoding acceptance loop was tested. The result covers synthetic projection-kernel behavior on this CPU worker with scalar packed-int3 unpacking, not optimized SIMD kernels or datacenter-scale serving.

## Claim scope

A straightforward OpenMP CPU implementation of packed int3 matvec plus sparse residual correction, tested on synthetic 2048x2048 and 4096x4096 projection workloads, is not a competitive speculative-decoding draft primitive versus fp32 or int8 baselines.

## Why it stopped

Early bounded kernel-level falsification: the tested int3 residual CPU path was slower than relevant baselines at 4096x4096 and had weak output-rank fidelity; this is not a full end-to-end speculative-decoding validation.

## Recommended next action

Stop this straightforward CPU int3 residual draft path as no-paper useful signal; only revisit with a hand-vectorized AVX2/AVX-512 int3 kernel and a tiny real-LM speculative decoding trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD int3 residual kernel plus tiny-LM speculative trace
- Success threshold: At 4096x4096 or larger, int3 residual must be at least 1.25x faster than int8 and 1.5x faster than fp32 while maintaining at least 0.85 top-1 agreement or an end-to-end speculative acceptance rate high enough to improve tokens/sec by at least 15% over an int8 draft.
- Stop condition: Stop if the optimized kernel remains slower than int8 at 4096x4096 or if tiny-LM speculative decoding fails to improve end-to-end tokens/sec by at least 15%.

## Evidence references

- Artifact root: `<local-path>/projects/specdec-int3-residual-draft-cpu-3fa9f7d00818`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
