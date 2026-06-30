# Direct small-transformer validation of learned 1.5-bit residual channel selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-small-transformer-validation-of-learned-1-5-bit-res-a37c7fe71e`
Run ID: `direct-small-transformer-validation-of-learned-1-5-bit-res-a37c7fe71e-20260629T200642892832+0000`

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

- Parent run decision: 1.5-bit Weight Quantization with Learned Residual Channel Selection: enoch://control-plane/projects/1-5-bit-weight-quantization-with-learned-residual-channel-selection-a821d3a65335/runs/1-5-bit-weight-quantization-with-learned-residual-channel-selection-a821d3a65335-20260629T191212885661+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9402cc56d81

## What looked useful

Learned selection gave consistent teacher-KL improvements over the best non-learned control: 3.7% at 2.0 estimated bits, 6.8% at 2.5 estimated bits, and 9.4% at 3.5 estimated bits. This supports the channel-selection mechanism locally but does not validate a deployable or paper-ready 1.5-bit transformer quantization result.

## Boundaries and scale limits

Synthetic randomly initialized model and synthetic token streams only; no pretrained or trained small transformer, no real-corpus perplexity, no packed 1.5-bit kernel, no end-to-end speed or memory measurement, and effective residual formats above the pure 1.5-bit base when dense residual rows are included.

## Claim scope

In a NumPy 4-layer 96-dim synthetic decoder-transformer forward-pass probe, activation-weighted learned residual input-channel selection reduced dense-teacher KL and logit MSE versus random, weight-magnitude, and quantization-error controls at residual fractions 3.125%, 6.25%, and 12.5%.

## Why it stopped

Closed as no-paper useful signal because this run directly tested a small-transformer quantization mechanism but only on synthetic random-weight evidence, not the trained/pretrained transformer validation required for the original claim.

## Recommended next action

Run the same learned/random/magnitude/error control suite on a trained small transformer or pretrained GPT-2-small-class checkpoint with real held-out corpus loss before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained small-transformer residual channel selection control suite
- Success threshold: Learned selection should improve held-out loss or teacher KL by at least 5% relative to the best non-learned residual-channel control at a matched effective bit budget across at least three seeds or calibration splits.
- Stop condition: Stop as negative if learned selection fails to beat the best non-learned control by 5% on both held-out loss and teacher KL, or if the effect appears only on synthetic/random-weight models.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-transformer-validation-of-learned-1-5-bit-res-a37c7fe71e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
