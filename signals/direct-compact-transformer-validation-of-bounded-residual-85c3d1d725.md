# Direct compact-transformer validation of bounded residual-channel QAT

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-compact-transformer-validation-of-bounded-residual-85c3d1d725`
Run ID: `direct-compact-transformer-validation-of-bounded-residual-85c3d1d725-20260609T144815968434+0000`

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

- Parent run decision: Bounded Quantization-Aware Training Run for Residual Channel Quantizer: enoch://control-plane/projects/bounded-quantization-aware-training-run-for-residual-channel-quantizer-f96c1cfa416b/runs/bounded-quantization-aware-training-run-for-residual-channel-quantizer-f96c1cfa416b-20260609T095315235216+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b4f39773704c

## What looked useful

Bounded residual-channel QAT improved mechanism diagnostics at both 8-bit and 4-bit: mean saturation fell by 0.44 percentage points at 8-bit and 0.53 percentage points at 4-bit, while quantization MSE fell by 0.00776 and 0.00681 respectively. Mean validation loss improved only 0.00076 CE at 8-bit and 0.00122 CE at 4-bit with 2/3 seed wins, so the accuracy threshold is not robustly supported.

## Boundaries and scale limits

Small character-level dataset, compact transformer only, three seeds, 800 training steps, fake quantization rather than integer deployment kernels; no GPT-2-small-class, subword, larger-corpus, long-training, or serving validation.

## Claim scope

In a 421,697-parameter 2-layer character-level causal transformer trained for 800 steps on Tiny Shakespeare, bounded per-channel residual fake quantization consistently reduced residual saturation and quantization MSE versus a matched per-tensor residual fake-quantization control, but validation-loss gains were tiny and seed-dependent.

## Why it stopped

Tier 1 direct compact-transformer evidence produced a useful mechanism signal but not robust accuracy support; this should not proceed to paper writing from the current evidence.

## Recommended next action

Run a bounded deepen test on a GPT-2-small-class or at least 10M-parameter subword LM with real activation calibration and a predeclared >=0.01 validation CE improvement threshold over per-tensor residual QAT; stop if the effect remains below seed noise.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium subword-LM validation of bounded residual-channel QAT under stronger quantization pressure
- Success threshold: Bounded per-channel residual QAT must beat per-tensor residual QAT by >=0.01 mean validation CE, win at least 4/5 seeds, reduce mean saturation and quantization MSE, and not increase the FP degradation gap by more than 10% relative to the control.
- Stop condition: Stop as no-paper if mean validation CE improvement is <0.005, fewer than 4/5 seeds improve, or diagnostics improve without a measurable validation-loss benefit.

## Evidence references

- Artifact root: `<local-path>/projects/direct-compact-transformer-validation-of-bounded-residual-85c3d1d725`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
