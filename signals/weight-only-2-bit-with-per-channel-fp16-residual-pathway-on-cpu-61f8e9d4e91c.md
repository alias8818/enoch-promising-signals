# Weight-only 2-bit with per-channel FP16 residual pathway on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `weight-only-2-bit-with-per-channel-fp16-residual-pathway-on-cpu-61f8e9d4e91c`
Run ID: `weight-only-2-bit-with-per-channel-fp16-residual-pathway-on-cpu-61f8e9d4e91c-20260621T230038185505+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1bcbea3c9b85

## What looked useful

At residual_k=128, compression remained 9.12x versus FP32 but relative L2 error was still 0.6792 and speed was below dense FP32 in the primary sweep. At residual_k=2048, relative L2 improved to 0.2756 but compression fell to 1.23x and speed was 0.58x dense FP32.

## Boundaries and scale limits

Tested only synthetic normal weights/activations for m=256,n=4096 on one CPU worker using a scalar single-thread implementation. No real model, perplexity, downstream task, batched GEMM, learned/codebook quantizer, or SIMD-optimized kernel was evaluated.

## Claim scope

Synthetic single-layer CPU matvec shows that packed weight-only 2-bit weights with sparse per-channel FP16 residual corrections reduce output error monotonically, but not enough at useful compression ratios, and larger residual budgets lose speed and compression advantages.

## Why it stopped

Proxy early falsification: the directly tested CPU matvec mechanism did not provide a useful accuracy/speed/compression point, though full real-model validation was not attempted.

## Recommended next action

Stop this run as a proxy early falsification; the next bounded test, if pursued, should use an optimized SIMD decode path and real small-model quality metrics before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD and real-model check for 2-bit residual CPU inference
- Success threshold: At least 4x model compression versus FP32, relative output error below 0.20 on held-out real-model activations or no more than 5% degradation on a small downstream/perplexity metric, and latency no worse than dense FP32 for the same batch shape.
- Stop condition: Stop if SIMD decode remains slower than dense FP32 at 4x compression or if real-model quality remains outside the success threshold at residual budgets that preserve 4x compression.

## Evidence references

- Artifact root: `<local-path>/projects/weight-only-2-bit-with-per-channel-fp16-residual-pathway-on-cpu-61f8e9d4e91c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
