# Real-corpus suffix-array candidate verification with tuned CPU and length-bucketed GPU baselines

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `real-corpus-suffix-array-candidate-verification-with-tuned-b49520209a`
Run ID: `real-corpus-suffix-array-candidate-verification-with-tuned-b49520209a-20260609T084535331953+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Medium-scale GPU candidate-buffer verification with variable-length suffix-array oracle: enoch://control-plane/projects/medium-scale-gpu-candidate-buffer-verification-with-variab-85b5349876/runs/medium-scale-gpu-candidate-buffer-verification-with-variab-85b5349876-20260609T044808730164+0000
- Parent run decision: GPU Candidate Buffer Verification With Independent Suffix-Array Cross-Check: enoch://control-plane/projects/gpu-candidate-buffer-verification-with-independent-suffix-1956faed0c/runs/gpu-candidate-buffer-verification-with-independent-suffix-1956faed0c-20260609T021442066517+0000

## What looked useful

Large resident GPU batches reached about 2.78B candidates/s versus 0.70B candidates/s for the tuned CPU baseline, but length bucketing was tied with or slower than the unbucketed GPU control across smoke, medium, large, and length-specific controls.

## Boundaries and scale limits

One corpus, one GB10 host, isolated candidate verification stage only; suffix-array construction/search and end-to-end application latency were not measured.

## Claim scope

On enwik8 candidate verification batches up to 32M candidates on one NVIDIA GB10, GPU-resident verification is faster than a 20-thread OpenMP CPU memcmp baseline, but length-bucketed fixed-length CUDA kernels do not materially improve over a simpler unbucketed CUDA kernel.

## Why it stopped

Bounded direct validation supported GPU offload but failed to show a meaningful length-bucketing advantage over a real unbucketed GPU control.

## Recommended next action

Stop this follow-up as no-paper useful evidence; use the unbucketed GPU baseline for future integrated suffix-array experiments unless a new kernel design offers a clear mechanism beyond length bucketing.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-suffix-array-candidate-verification-with-tuned-b49520209a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
