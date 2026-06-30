# 1-Bit Optimizer States with Error Feedback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-optimizer-states-with-error-feedback-6345b089174d`
Run ID: `1-bit-optimizer-states-with-error-feedback-6345b089174d-20260628T050852174614+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/3ae7c4efc8f7

## What looked useful

Error feedback is not sufficient by itself for a practical 1-bit optimizer-state claim: the tested EF variant had mean quadratic final loss 199.558 versus 7.14e-16 for fp32 momentum, and its full-precision residual makes total optimizer state about 1.035x fp32 momentum despite a 0.035x persistent sign state.

## Boundaries and scale limits

Five seeds, 256-parameter quadratic and 128-parameter logistic classifier only; no Adam second moment state, no transformer training, no large model, no hardware bandwidth measurement, and no compressed-residual variant.

## Claim scope

Small CPU-only NumPy objectives show that sign+scale momentum with full-precision error feedback can train an easy logistic classifier to comparable accuracy, but fails an ill-conditioned quadratic and does not preserve total optimizer-state memory savings when the residual is counted.

## Why it stopped

Proxy/local early falsification: the tested full-precision-residual EF implementation fails the hard toy objective and does not achieve total 1-bit optimizer-state memory savings; this is not full validation of all possible 1-bit optimizer designs.

## Recommended next action

Stop this implementation as no-paper evidence; if continuing, run a bounded follow-up that compresses or removes the EF residual and tests anisotropic stability before any model-scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed-residual 1-bit momentum stability probe
- Success threshold: Compressed-residual variant keeps total optimizer state below 0.25x fp32 momentum and reaches within 2x fp32 momentum final loss on the quadratic plus within 1 percentage point accuracy on the small neural-network task.
- Stop condition: Stop if no compressed-residual variant beats naive sign+scale on the quadratic while preserving at least 4x optimizer-state memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-optimizer-states-with-error-feedback-6345b089174d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
