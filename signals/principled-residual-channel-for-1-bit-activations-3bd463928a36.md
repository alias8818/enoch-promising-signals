# Principled Residual Channel for 1-bit Activations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `principled-residual-channel-for-1-bit-activations-3bd463928a36`
Run ID: `principled-residual-channel-for-1-bit-activations-3bd463928a36-20260528T142813393915+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9eafc81d5e7c

## What looked useful

Residual-r32 reduced reconstruction MSE by 24.9% versus sign-only and improved synthetic classification by +1.85 percentage points over binary_h130 and +1.27 points over binary_h132, with lower test loss in both controls.

## Boundaries and scale limits

No real dataset, transformer, language-model, large-scale, kernel-efficiency, or long-training evidence was produced. The result is limited to small CUDA MLP probes with 5 seeds.

## Claim scope

On a synthetic teacher-student MLP task and a linear reconstruction probe, adding a narrow real-valued projection of the quantization residual to 1-bit sign activations improves information recovery and modestly improves classification versus same-width and wider binary controls.

## Why it stopped

Worker run produced a useful synthetic mechanism signal but not direct publication-grade evidence; stop as no-paper evidence rather than claiming full validation.

## Recommended next action

Run one bounded real-data follow-up comparing residual-channel binary activations against parameter-matched binary controls on a small vision or character-language task before considering larger model validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data residual-channel binary activation confirmation
- Success threshold: Residual-channel model beats the best parameter-matched binary control by at least 1% relative validation loss or 0.5 percentage points accuracy on mean across seeds without increasing parameters by more than 5%.
- Stop condition: Stop if the residual-channel model fails to beat the best parameter-matched binary control on mean validation loss or accuracy across 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channel-for-1-bit-activations-3bd463928a36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
