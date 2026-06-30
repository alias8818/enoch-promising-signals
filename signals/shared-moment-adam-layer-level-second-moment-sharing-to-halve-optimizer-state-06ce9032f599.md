# Shared-moment Adam: layer-level second-moment sharing to halve optimizer state

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `shared-moment-adam-layer-level-second-moment-sharing-to-halve-optimizer-state-06ce9032f599`
Run ID: `shared-moment-adam-layer-level-second-moment-sharing-to-halve-optimizer-state-06ce9032f599-20260622T002203132552+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1dd78a52684f

## What looked useful

Layer-scalar second-moment sharing consistently reduced optimizer state to about 0.5x AdamW. It matched tiny synthetic LM loss but was roughly 2x worse on teacher-MLP MSE and failed the ill-conditioned quadratic by ending near 0.28 loss while AdamW reached numerical zero, showing that one scalar v per layer is too coarse when coordinate curvature varies.

## Boundaries and scale limits

Three-seed synthetic probes only: 4096D quadratic, small teacher MLP regression, and a tiny synthetic Markov language model. No real corpus, GPT-2-small-class run, mixed precision, distributed training, fused optimizer implementation, or long-horizon stability test.

## Claim scope

A local PyTorch prototype of AdamW with per-parameter first moments and one scalar second-moment accumulator per layer/share group halves initialized optimizer-state bytes and trains small synthetic MLP/LM tasks, but loses Adam-like adaptivity on a direct ill-conditioned quadratic diagnostic.

## Why it stopped

Proxy/local early falsification rather than full validation: the direct ill-conditioned diagnostic shows a mechanism-level adaptivity failure for scalar layer sharing, while small synthetic neural tasks are insufficient to overturn that failure or support a paper.

## Recommended next action

Stop this exact scalar layer-shared-v variant as no-paper useful signal; next bounded test should evaluate block/channel/head-level second-moment sharing against AdamW and Adafactor/SM3-style baselines on a real small language-model task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-level shared second moments for AdamW state reduction
- Success threshold: At least 35% optimizer-state reduction versus AdamW, no more than 5% worse final validation loss than AdamW on the real small-LM task across seeds, and no catastrophic gap on the ill-conditioned diagnostic.
- Stop condition: Stop if block-level sharing still shows a large diagnostic failure, defined as more than 10x AdamW final quadratic loss at the same step budget, or if real-LM validation loss is more than 5% worse than AdamW after learning-rate tuning.

## Evidence references

- Artifact root: `<local-path>/projects/shared-moment-adam-layer-level-second-moment-sharing-to-halve-optimizer-state-06ce9032f599`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
