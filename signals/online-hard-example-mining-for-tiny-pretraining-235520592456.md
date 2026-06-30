# Online hard-example mining for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `online-hard-example-mining-for-tiny-pretraining-235520592456`
Run ID: `online-hard-example-mining-for-tiny-pretraining-235520592456-20260621T040024635652+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3adb369ee78e

## What looked useful

Mild loss-aware online sampling produced a small consistent 5/5 seed validation-loss gain at 2k steps (mean OHEM minus uniform -0.003635), but aggressive OHEM reduced coverage and was worse than uniform (+0.002518). Treat hard-example mining as a mild curriculum with exploration, not pure hard replay.

## Boundaries and scale limits

Single small character-level corpus, single tiny Transformer family, 2k-step schedules, no tokenizer/corpus/model-size robustness, no sampler-overhead-normalized wall-clock budget, and no GPT-2-small-class or web-corpus validation.

## Claim scope

On a Tiny Shakespeare character-level 2-layer Transformer pretraining proxy, mild EMA-loss online hard-example mining with uniform exploration slightly improved held-out validation loss over uniform sampling under equal update/token budgets, while aggressive hard-only mining underperformed.

## Why it stopped

No paper-positive closure: this run produced a bounded tiny character-LM useful signal, but the claim is too narrow and the effect too small for publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up on a subword-tokenized corpus with a GPT-2-small-class or parameter-matched small Transformer, comparing uniform, mild OHEM, and aggressive OHEM under both token-equal and wall-clock-equal budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subword small-Transformer validation of mild online hard-example mining
- Success threshold: Mild OHEM beats uniform on at least 4 of 5 paired seeds or 3 of 3 paired seeds with mean validation-loss improvement at least 0.01 and no worse wall-clock-normalized validation loss; aggressive OHEM does not outperform mild OHEM.
- Stop condition: Stop if mild OHEM fails to beat uniform by at least 0.01 mean validation loss, loses under wall-clock-equal comparison, or the effect is not consistent across paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/online-hard-example-mining-for-tiny-pretraining-235520592456`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
