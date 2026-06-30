# INT2 Weight-Only Quantization with Learned Residual Scales

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weight-only-quantization-with-learned-residual-scales-f2a605341018`
Run ID: `int2-weight-only-quantization-with-learned-residual-scales-f2a605341018-20260523T150534470262+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/94b8eb508186

## What looked useful

INT2 LRS reduced mean relative layer-output MSE from 0.177196 to 0.136698 across 24 synthetic layer probes, a 22.85% reduction, with largest gains on heavy-tailed Student-t weights. It worsened synthetic task accuracy drop from 2.67 percentage points to 3.52 percentage points, so reconstruction-only LRS is not sufficient evidence for a positive quantization claim.

## Boundaries and scale limits

No real pretrained transformer, no real language-model perplexity, no downstream dataset, no fused INT2 kernel, and no serving throughput measurement. Task evidence is a single synthetic teacher/student MLP run.

## Claim scope

Bounded synthetic PTQ evidence for 2-bit groupwise weight-only quantization: one extra learned residual scale per group reduces reconstruction and layer-output MSE versus one-scale INT2, but did not improve a small synthetic quantized inference task.

## Why it stopped

No-paper useful signal: proxy layer metrics improved, but the bounded task-level quantized inference test regressed versus one-scale INT2, so this is not a positive result or full validation.

## Recommended next action

Stop the paper path for reconstruction-only LRS; the concrete next bounded test is activation-aware LRS fitting on pretrained GPT-2-small-class layers with calibration activations and perplexity measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware INT2 learned residual scales on GPT-2-small-class layers
- Success threshold: Activation-aware LRS must reduce held-out perplexity degradation by at least 20% relative to one-scale INT2 while staying within 10% of the 4-level learned-codebook control and documenting overhead.
- Stop condition: Stop if activation-aware LRS fails to improve held-out perplexity or accuracy over one-scale INT2 on two independently seeded calibration/evaluation splits.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weight-only-quantization-with-learned-residual-scales-f2a605341018`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
