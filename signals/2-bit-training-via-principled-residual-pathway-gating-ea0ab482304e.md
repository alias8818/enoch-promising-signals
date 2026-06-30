# 2-bit training via principled residual pathway gating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-training-via-principled-residual-pathway-gating-ea0ab482304e`
Run ID: `2-bit-training-via-principled-residual-pathway-gating-ea0ab482304e-20260602T171020632108+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/50c77ab4cb0d

## What looked useful

Residual attenuation is the supported mechanism: fixed-scale 2-bit residual branches catastrophically failed, while small residual gates trained near the full-precision controls. The learnable ReZero-style gate did not beat a fixed 0.1 gate, so the stronger principled/learnable gating claim is not supported by this run.

## Boundaries and scale limits

CPU-only NumPy toy regression; no transformer language modeling, no real dataset, no PyTorch/GPU training, no kernel efficiency measurement, and only 3 seeds at width 64/depth 6/800 steps.

## Claim scope

Toy-scale NumPy teacher-student residual MLP regression shows that small residual-path gates stabilize 2-bit quantized residual-branch training, reducing validation NMSE from 131.812816 for fixed scale 1.0 to about 0.175 for small-gate variants across 3 seeds.

## Why it stopped

Toy-scale evidence supports residual attenuation but not the stronger learnable/principled gate mechanism; this is insufficient for a paper-positive decision.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should be a small transformer language-model experiment comparing fixed small residual scaling against learnable/principled gates under 2-bit residual-branch quantization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small transformer test of fixed versus learnable gates for 2-bit residual branches
- Success threshold: Learnable/principled gated 2-bit training reaches validation loss within 20% of the full-precision control and improves by at least 10% over fixed small residual scaling across seeds.
- Stop condition: Stop if fixed small residual scaling matches or beats learnable gates, or if all 2-bit variants remain more than 50% worse than full precision after the bounded training budget.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-training-via-principled-residual-pathway-gating-ea0ab482304e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
