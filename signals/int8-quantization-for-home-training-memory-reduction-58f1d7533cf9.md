# INT8 Quantization for Home Training Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-quantization-for-home-training-memory-reduction-58f1d7533cf9`
Run ID: `int8-quantization-for-home-training-memory-reduction-58f1d7533cf9-20260608T070351308838+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f79dba4e738d

## What looked useful

The mechanism gives the expected optimizer-state memory reduction, but the naive INT8 Adam variant diverged badly across block sizes and parameter counts while running slower than FP32 in this NumPy implementation.

## Boundaries and scale limits

Tested only synthetic dense quadratic optimization at 50k, 200k, and 1M parameters for up to 40 steps on a CPU worker. Did not test transformer training, real datasets, activation memory, checkpointing, GPU kernels, or 7B+ scale.

## Claim scope

Naive blockwise INT8 quantization of both Adam first- and second-moment optimizer states reduces state bytes by about 75% but is not a viable drop-in training-memory reduction method on the tested dense quadratic CPU proxy.

## Why it stopped

Proxy early falsification: direct optimizer-state memory was favorable, but convergence failed catastrophically on small and medium synthetic tests, so scaling this exact design is not justified.

## Recommended next action

Stop this naive variant; run a bounded follow-up that stabilizes second-moment quantization before considering any larger training benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized INT8 Adam second-moment quantization for home-training memory
- Success threshold: At least 70% optimizer-state memory reduction and final loss within 1.2x FP32 Adam on both proxy and small-network tasks, with no catastrophic divergence.
- Stop condition: Stop if stabilized INT8 second-moment variants either diverge or exceed 2x FP32 final loss on the proxy after two reasonable quantization designs.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-for-home-training-memory-reduction-58f1d7533cf9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
