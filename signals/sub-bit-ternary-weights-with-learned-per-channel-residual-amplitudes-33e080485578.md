# Sub-bit ternary weights with learned per-channel residual amplitudes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-bit-ternary-weights-with-learned-per-channel-residual-amplitudes-33e080485578`
Run ID: `sub-bit-ternary-weights-with-learned-per-channel-residual-amplitudes-33e080485578-20260619T224623291416+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ebfb3f457883

## What looked useful

Residual amplitudes are conditionally useful when the first ternary pass leaves sparse large residual errors. They are not a general equal-budget improvement over plain sparse ternary; density allocation can be better spent on a single ternary code for Gaussian-like weights.

## Boundaries and scale limits

Synthetic matrix and linear teacher-label probe only; no trained network checkpoint, real data activations, end-task accuracy/perplexity, packed kernel benchmark, or true entropy-coded implementation was tested.

## Claim scope

On synthetic 16x512 weight matrices at an estimated 0.706 bits/weight, a two-stage sparse ternary representation with learned per-channel residual amplitudes improves reconstruction and teacher-label preservation for Student-t and channel-outlier weights, but not for Gaussian or the tested low-rank-heavy-tail proxy.

## Why it stopped

No-paper closure: bounded synthetic evidence is mixed and conditional, so it is useful for scoping the next test but does not validate the sub-bit ternary residual-amplitude idea on real models.

## Recommended next action

Run a bounded real-layer follow-up on trained small-model weights: quantize layers only after measuring sparse heavy-tailed residual structure, then compare reconstruction, activation error, and task metrics at matched storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-layer residual-amplitude ternary quantization after residual sparsity screening
- Success threshold: On screened real layers, residual-amplitude ternary must reduce activation MSE by at least 5% versus equal-budget plain sparse ternary and preserve task metric within the same or better degradation band across at least 3 seeds or checkpoints.
- Stop condition: Stop if real layers do not show sparse heavy-tailed residuals after first-pass ternary quantization, or if residual-amplitude ternary fails to beat equal-budget plain ternary on activation error in two representative model families.

## Evidence references

- Artifact root: `<local-path>/projects/sub-bit-ternary-weights-with-learned-per-channel-residual-amplitudes-33e080485578`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
