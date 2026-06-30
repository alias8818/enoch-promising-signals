# Principled Residual Channels: Which Layers Actually Need Full Precision

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `principled-residual-channels-which-layers-actually-need-full-precision-07ee886af520`
Run ID: `principled-residual-channels-which-layers-actually-need-full-precision-07ee886af520-20260610T084651969946+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ef360c99b240

## What looked useful

All-3-bit residual quantization increased validation loss by 0.2355 mean and dropped accuracy by 0.0650 mean over three seeds. Sensitivity-ranked full-precision layer/channel exceptions beat random masks on loss in 3/3 seeds at budgets 6, 12, 24, and 48, with mean loss advantages of 0.0210, 0.0312, 0.0492, and 0.0552 respectively. The best single full-precision layer by loss recovery was layer 0 in all three seeds.

## Boundaries and scale limits

Synthetic nonlinear classification only; no transformer attention, layer norm, token sequence data, pretrained LLMs, GPT-2-small-class baseline, hardware quantization kernels, or large-scale training/inference validation were tested.

## Claim scope

In a 6-block NumPy residual-MLP proxy with 3-bit residual activation quantization, residual precision sensitivity is nonuniform by layer/channel; sensitivity-ranked full-precision exceptions recover more validation loss than random exceptions at matched budgets across three seeds.

## Why it stopped

The result is a three-seed synthetic residual-MLP proxy, not direct transformer evidence; it supports the mechanism but cannot justify a paper about which transformer layers need full precision.

## Recommended next action

Stop this run as no-paper useful proxy evidence; the concrete next action is a bounded GPT-2-small-class confirmation using calibration-set residual sensitivity to choose full-precision activation exceptions and held-out perplexity to compare against random and layerwise heuristics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small residual activation precision sensitivity confirmation
- Success threshold: At two or more precision budgets, sensitivity-ranked exceptions recover at least 25% more perplexity degradation than random masks and outperform a same-budget layerwise heuristic on held-out data in at least 3 independent splits/seeds.
- Stop condition: Stop if all tested budgets fail to beat random and layerwise controls on held-out perplexity, or if calibration-selected exceptions do not transfer beyond the calibration split.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channels-which-layers-actually-need-full-precision-07ee886af520`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
