# Factored Adam: Low-Rank Optimizer State Decomposition

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `factored-adam-low-rank-optimizer-state-decomposition-f8bd170c9602`
Run ID: `factored-adam-low-rank-optimizer-state-decomposition-f8bd170c9602-20260528T200844674402+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5ca0ea14d489

## What looked useful

Adam second moments were highly low-rank in the proxy, but first moments were less compressible: dense AdamW rank-16 captured about 84% of exp_avg energy with about 0.35 relative error, and about 99.5-99.7% of exp_avg_sq energy with about 0.06-0.07 clamped relative error. This supports testing adaptive or sufficiently large-rank momentum factorization rather than very small fixed ranks.

## Boundaries and scale limits

This is not full validation: the task is synthetic and small, the optimizer reconstructs dense buffers and recomputes full SVDs, measured wall-clock and allocator memory are not representative of true factor storage, and no Transformer/GPT-2-scale language-modeling baseline was run.

## Claim scope

On a small CUDA-backed teacher-student MLP classification proxy, per-step rank-16 SVD compression of AdamW matrix moment buffers preserved or improved test loss versus AdamW across 3 seeds while using a theoretical 10.7% of dense Adam optimizer-state bytes for factorized matrix states; ranks 4 and 8 degraded training quality.

## Why it stopped

Proxy evidence is mixed and useful but not publication-grade: aggressive ranks failed, rank 16 looked promising, and prior art plus lack of true memory/runtime measurement prevent a paper-ready positive claim.

## Recommended next action

Stop this worker run as a no-paper useful signal; next, implement true factor-storage updates and benchmark rank-adaptive Factored Adam against AdamW, Adafactor, and GaLore/Adapprox-style baselines on a small Transformer language-modeling task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True Factor-Storage Factored Adam on Small Transformer Language Modeling
- Success threshold: Within 0.05 validation-loss or perplexity-equivalent delta of AdamW across 3 seeds, at least 40% measured optimizer-state memory reduction, and no more than 20% throughput slowdown versus AdamW on the bounded Transformer benchmark.
- Stop condition: Stop as negative if true factor storage cannot beat Adafactor/GaLore-style baselines on memory-quality tradeoff or if matching AdamW requires ranks that save less than 25% measured optimizer-state memory.

## Evidence references

- Artifact root: `<local-path>/projects/factored-adam-low-rank-optimizer-state-decomposition-f8bd170c9602`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
