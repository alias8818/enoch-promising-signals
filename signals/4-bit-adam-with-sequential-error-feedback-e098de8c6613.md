# 4-bit Adam with Sequential Error Feedback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-adam-with-sequential-error-feedback-e098de8c6613`
Run ID: `4-bit-adam-with-sequential-error-feedback-e098de8c6613-20260525T192241905289+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/830068e89f03

## What looked useful

Positive log-domain 4-bit second-moment quantization made plain 4-bit Adam-state simulation stable. Adding residual feedback to both m and v produced quadratic loss around 1.30e9 versus 1.47e-9 for plain 4-bit and 6.15e-11 for FP32. Restricting feedback to m recovered quadratic convergence but did not improve the MLP validation loss over plain 4-bit.

## Boundaries and scale limits

No packed int4 kernel, no real memory-pressure benchmark, no GPT-2-small or larger training, no distributed training, and only 5 seeds on synthetic/proxy tasks.

## Claim scope

Bounded CUDA behavioral simulation of 4-bit Adam optimizer-state quantization on an ill-conditioned quadratic and synthetic teacher-student MLP. Full m+v step-to-step error feedback is not supported because it catastrophically failed the quadratic; m-only feedback is a plausible mechanism signal but not validated on real language-model training.

## Why it stopped

Proxy evidence is mixed: full sequential error feedback on both Adam states is unstable on a direct optimizer stress test, while m-only feedback needs direct model-training evidence before any paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded small language-model experiment comparing packed q4_plain against q4_ef_m_only with explicit residual memory accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small language-model validation of m-only error feedback for 4-bit Adam states
- Success threshold: q4_ef_m_only reaches validation loss no worse than q4_plain and within 1% of FP32 Adam while preserving at least 25% optimizer-state memory reduction after residual accounting.
- Stop condition: Stop if q4_ef_m_only is worse than q4_plain by more than 1% validation loss, loses the memory advantage after residual accounting, or reproduces second-moment-like instability.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-adam-with-sequential-error-feedback-e098de8c6613`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
