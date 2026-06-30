# Medium-scale GPU candidate-buffer verification with variable-length suffix-array oracle

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-scale-gpu-candidate-buffer-verification-with-variab-85b5349876`
Run ID: `medium-scale-gpu-candidate-buffer-verification-with-variab-85b5349876-20260609T044808730164+0000`

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

- Parent run decision: GPU Candidate Buffer Verification With Independent Suffix-Array Cross-Check: enoch://control-plane/projects/gpu-candidate-buffer-verification-with-independent-suffix-1956faed0c/runs/gpu-candidate-buffer-verification-with-independent-suffix-1956faed0c-20260609T021442066517+0000
- Parent run decision: CPU Suffix-Tree Draft for GPU Verification: enoch://control-plane/projects/cpu-suffix-tree-draft-for-gpu-verification-15fc2652ce5c/runs/cpu-suffix-tree-draft-for-gpu-verification-15fc2652ce5c-20260609T001642921234+0000

## What looked useful

Across three fixed seeds, variable-length GPU verification had zero CPU/GPU mismatches and averaged 8,855.9 Mcand/s in-kernel versus 200.7 Mcand/s for the CPU verifier. Shuffling candidates reduced GPU throughput to 2,436.0 Mcand/s, showing locality/order is an important mechanism.

## Boundaries and scale limits

Synthetic corpus only; scalar CPU baseline only; no real genome/log corpus; no tuned SIMD/OpenMP CPU baseline; no optimized length-bucketed GPU implementation; end-to-end suffix-array search is not accelerated by this claim.

## Claim scope

On deterministic synthetic DNA-like text of length 1,048,576 with suffix-array-oracle candidate buffers of about 17.1M candidates per seed, a simple GB10 CUDA verifier correctly validates variable-length candidates and materially outperforms a scalar CPU verifier on isolated verification throughput.

## Why it stopped

Medium synthetic direct verification supports the mechanism but is not publication-grade because corpus realism and tuned baselines are missing.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded deepening should repeat the protocol on a real corpus with tuned CPU SIMD/OpenMP and length-bucketed GPU baselines before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus suffix-array candidate verification with tuned CPU and length-bucketed GPU baselines
- Success threshold: Zero CPU/GPU mismatches and at least 10x isolated verification throughput for optimized GPU versus tuned CPU on real-corpus candidate buffers, with end-to-end overhead reported and no hidden candidate-generation advantage.
- Stop condition: Stop as negative if optimized GPU fails correctness, falls below 3x tuned CPU isolated verification throughput, or end-to-end oracle plus verification time is not competitive for any tested real-corpus workload.

## Evidence references

- Artifact root: `<local-path>/projects/medium-scale-gpu-candidate-buffer-verification-with-variab-85b5349876`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
