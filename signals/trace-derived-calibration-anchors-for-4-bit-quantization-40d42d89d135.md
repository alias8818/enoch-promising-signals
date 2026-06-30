# Trace-Derived Calibration Anchors for 4-Bit Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-derived-calibration-anchors-for-4-bit-quantization-40d42d89d135`
Run ID: `trace-derived-calibration-anchors-for-4-bit-quantization-40d42d89d135-20260621T154112170104+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6efb0dc3fabc

## What looked useful

Trace anchors raised rare-subgroup accuracy by about 25.99 percentage points at budget 32 but reduced overall accuracy by about 7.23 percentage points; diverse trace anchors were near overall-neutral with a smaller rare gain of about 2.88 points.

## Boundaries and scale limits

Evidence is limited to a small synthetic MLP, simulated symmetric 4-bit quantization, 8 seeds, calibration budgets 16-128, and no real transformer/LLM or hardware int4 kernel validation.

## Claim scope

On a synthetic rare-outlier MLP task with simulated W4A4 post-training quantization, trace-derived calibration anchors identify rare activation regimes and reduce saturation, but naive top-outlier anchor calibration harms overall accuracy.

## Why it stopped

Proxy/local evidence supports the mechanism but early-falsifies the naive broad claim that top trace-derived anchors alone improve 4-bit quantization accuracy; this is not full validation.

## Recommended next action

Run a bounded deepen test of hybrid calibration that limits trace-anchor fraction and tunes clipping percentile on a small real transformer or GPT-2-small-class model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid trace-anchor calibration for small-transformer W4A4 PTQ
- Success threshold: Hybrid anchors improve tail/OOD metric by at least 3 percentage points or equivalent perplexity reduction while keeping overall accuracy/perplexity within 0.5 percentage points or 1 percent relative of the random-calibration baseline.
- Stop condition: Stop if hybrid policies repeat the top-anchor tradeoff by improving tail metrics only with more than 1 percentage point overall degradation, or if trace anchors do not improve tail metrics over random calibration.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-calibration-anchors-for-4-bit-quantization-40d42d89d135`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
