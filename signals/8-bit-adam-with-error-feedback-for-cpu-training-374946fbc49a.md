# 8-bit Adam with Error Feedback for CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-with-error-feedback-for-cpu-training-374946fbc49a`
Run ID: `8-bit-adam-with-error-feedback-for-cpu-training-374946fbc49a-20260629T185155049826+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4a5ef7e4f0eb

## What looked useful

Default eps=1e-8 failed numerically for both 8-bit variants across all seeds. With eps=1e-4, error feedback nearly recovered FP32 validation loss but ran at 0.632x FP32 throughput and used 1.250x FP32 Adam effective optimizer-state memory because residuals were float32.

## Boundaries and scale limits

Not tested on transformers, language modeling, large models, fused CPU kernels, block-wise quantization, or compressed residuals. The result is a small direct CPU optimizer mechanism test, not broad training validation.

## Claim scope

Bounded NumPy CPU synthetic MLP evidence: tensor-wise 8-bit Adam moment quantization with float32 error-feedback residuals was tested against FP32 Adam over 5 seeds.

## Why it stopped

Proxy-sized direct CPU test falsified the simple memory-saving version: error feedback repaired convergence only after eps stabilization, but erased memory savings and slowed CPU training.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replace float32 residuals with compressed or block-local residuals and add a stable second-moment floor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed-residual 8-bit Adam with stable second-moment floor
- Success threshold: No numerical failures; mean validation loss within 0.02 of FP32 Adam; effective optimizer-state memory at or below 0.40x FP32 Adam; throughput at least 0.80x FP32 Adam in the same NumPy CPU setting or with a justified fused/vectorized implementation.
- Stop condition: Stop if residual compression pushes effective state above 0.50x FP32 Adam, if any 8-bit variant still fails numerically across multiple seeds, or if throughput remains below 0.70x FP32 Adam after vectorized implementation.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-with-error-feedback-for-cpu-training-374946fbc49a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
