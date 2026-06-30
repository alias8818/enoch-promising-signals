# Real-text GPT-2-small-class validation of INT2 residual-stream error feedback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-text-gpt-2-small-class-validation-of-int2-residual-st-dddac84349`
Run ID: `real-text-gpt-2-small-class-validation-of-int2-residual-st-dddac84349-20260619T200706310462+0000`

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

- Parent run decision: ActINT2-EF: Activation INT2 with error-feedback residual stream in transformers: enoch://control-plane/projects/actint2-ef-activation-int2-with-error-feedback-residual-stream-in-transformers-c4ea401e44a2/runs/actint2-ef-activation-int2-with-error-feedback-residual-stream-in-transformers-c4ea401e44a2-20260619T191623493939+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b31f7ad93d46

## What looked useful

Residual-stream error feedback produced a consistent mechanism-level improvement on real-text GPT-2-small-class inference, but absolute INT2 quality remained poor and the result is not paper-ready.

## Boundaries and scale limits

Inference-only fake activation quantization; full-precision weights; simple per-token absmax signed INT2 quantizer; WikiText-2 validation slices only; no trained INT2 model, no calibrated quantizer, no weight quantization, no generation-quality evaluation, and no deployment kernel measurement.

## Claim scope

On GPT-2 small inference over WikiText-2 validation slices, a simple layer-to-layer residual-stream error-feedback accumulator reduced fake INT2 activation-quantization logit MSE versus plain residual-stream INT2 by 37.98% on 64 sequences and 40.32% on 256 sequences, while also reducing cross-entropy degradation.

## Why it stopped

Tier 1 direct evidence supports the error-feedback mechanism, but this remains a small fake-quantization inference study with severe absolute quality degradation, so it should close as no-paper useful signal rather than paper-positive validation.

## Recommended next action

Run a bounded deepen test with calibrated INT2 activation scales and layer/bit ablations on a larger real-text validation set; stop paper escalation until absolute perplexity and robustness improve materially.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated GPT-2 small INT2 residual-stream error-feedback ablation
- Success threshold: INT2+error-feedback must reduce logit MSE by at least 25% versus calibrated plain INT2 and improve cross-entropy degradation by at least 0.5 nats/token without reducing top-1 agreement.
- Stop condition: Stop if calibrated INT2+error-feedback fails either the logit-MSE or cross-entropy threshold, or if absolute perplexity remains more than 20x the FP reference after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-gpt-2-small-class-validation-of-int2-residual-st-dddac84349`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
