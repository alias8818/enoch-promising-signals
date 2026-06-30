# Curriculum ordering sweep for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-ordering-sweep-for-tiny-pretraining-d799e5d4a2e7`
Run ID: `curriculum-ordering-sweep-for-tiny-pretraining-d799e5d4a2e7-20260620T235758573393+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3adb369ee78e

## What looked useful

All tested curriculum orderings lost to shuffle on all three seeds: easy_to_hard +0.2943 mean validation-loss delta, hard_to_easy +0.1948, and banded_easy_hard +0.2646. This suggests naive monotonic difficulty sorting can harm tiny pretraining by reducing data mixture quality.

## Boundaries and scale limits

Tiny character-level dataset and model only; no BPE/tokenized corpus, no GPT-2-small-class model, no semantic difficulty metric, no long-run or large-corpus validation.

## Claim scope

On Tiny Shakespeare character-level pretraining with a 4-layer 128-wide causal Transformer, fixed 1000-step token budget, and 3 seeds, simple block sorting by character entropy plus transition-rate difficulty consistently worsened validation loss relative to shuffled block order.

## Why it stopped

Bounded local experiment produced consistent early falsification of the simple entropy/transition curriculum; this is not a full validation of all curriculum learning strategies.

## Recommended next action

Stop this exact curriculum-sorting direction; if continuing locally, test an interleaved/reweighted curriculum that preserves batch mixture instead of globally sorting blocks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Interleaved curriculum weighting for tiny pretraining
- Success threshold: Mean final validation loss at least 0.03 nats/token lower than shuffle with no seed worse than shuffle by more than 0.01 nats/token.
- Stop condition: Stop if interleaved weighting is worse than or indistinguishable from shuffle across 3 seeds, or if improvements appear only in one seed without paired consistency.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-sweep-for-tiny-pretraining-d799e5d4a2e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
