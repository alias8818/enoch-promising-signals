# CPU Sub-Byte Quantization with Vectorized Residual Encoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-sub-byte-quantization-with-vectorized-residual-encoding-d3cfc01554f5`
Run ID: `cpu-sub-byte-quantization-with-vectorized-residual-encoding-d3cfc01554f5-20260621T233435589459+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/78415dbfa451

## What looked useful

q4 storage/throughput is promising for bandwidth-bound CPU matvecs, with up to 2.06x q4-vs-int8 speedup in the larger run, but q4 relative RMSE is about 1.39 versus about 0.0055 for int8. Adding 64 residuals per row changes q4 relative RMSE only from 1.393154 to 1.393120 while increasing latency versus q4 alone.

## Boundaries and scale limits

Synthetic random dense matvec only; single-process CPU benchmark; fp32 activations; per-row symmetric weight quantization; no grouped quantization, production inference stack, downstream model quality, or multi-seed statistical study.

## Claim scope

On this AVX-512 Xeon CPU, a simple packed signed 4-bit dense matvec can reduce weight storage to about half of int8 and improve throughput on medium/larger synthetic matrices, but the tested sparse int8 residual correction does not materially recover numerical accuracy.

## Why it stopped

Bounded local proxy/early mechanism test found that the residual encoding path adds overhead and does not materially improve q4 error, so scaling this exact design is not justified.

## Recommended next action

Stop this implementation as no-paper evidence; if continuing, test grouped q4 or activation-calibrated residual selection against int8 with a success threshold of at least 10x RMSE reduction over plain q4 while retaining at least 1.2x int8 speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Grouped q4 with calibration-aware residual selection for CPU matvec
- Success threshold: Relative RMSE at least 10x lower than plain q4 and q4+residual latency at least 1.2x faster than int8, with storage no more than 0.75x int8 on both tested matrix sizes.
- Stop condition: Stop if grouped/calibrated residuals fail to achieve at least 3x q4 RMSE reduction on the first medium-size matrix or if residual latency is slower than int8.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-sub-byte-quantization-with-vectorized-residual-encoding-d3cfc01554f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
