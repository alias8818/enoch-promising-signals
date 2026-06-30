# AVX2 INT2 residual-channel kernel for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `avx2-int2-residual-channel-kernel-for-cpu-inference-fcd791b80a6e`
Run ID: `avx2-int2-residual-channel-kernel-for-cpu-inference-fcd791b80a6e-20260629T081412515513+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/2449eeb394cd

## What looked useful

Full 1024+tail dot products showed only mixed small effects, with residual AVX2 winning 12/31 tail cases versus scalar and 12/31 versus padded. Tail-only diagnostics were negative: residual AVX2 won 0/31 cases versus scalar and only 2/31 versus padded.

## Boundaries and scale limits

Microbenchmark only; no full inference runtime integration, no multi-layer model traces, no cross-CPU replication, and no optimized shuffle/BMI2 decoder variant.

## Claim scope

On this AVX2 Xeon host, a straightforward packed-INT2 residual-channel cleanup path that decodes the tail into a zero-padded 32-byte temporary and runs one AVX2 dot block is not faster than scalar cleanup, and is usually slower than padding to a full block when tail work is isolated.

## Why it stopped

The result is a bounded microbenchmark early falsification of the simple residual AVX2 temporary-buffer design, not a full inference-stack validation.

## Recommended next action

Stop this run; if continuing locally, implement a shuffle-LUT or BMI2-assisted packed INT2 residual decoder and require at least 1.10x median tail-only speedup over both scalar and padded baselines on 20/31 tail widths.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shuffle-LUT packed INT2 residual decoder for AVX2 tail cleanup
- Success threshold: At least 1.10x median tail-only speedup over both scalar and padded baselines on 20/31 tail widths, with no more than 5% regression in the 1024+tail full-dot benchmark.
- Stop condition: Stop if the optimized decoder still loses to scalar on more than 11/31 tail widths or cannot beat padded full-block handling by at least 1.05x on 16/31 tail widths.

## Evidence references

- Artifact root: `<local-path>/projects/avx2-int2-residual-channel-kernel-for-cpu-inference-fcd791b80a6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
