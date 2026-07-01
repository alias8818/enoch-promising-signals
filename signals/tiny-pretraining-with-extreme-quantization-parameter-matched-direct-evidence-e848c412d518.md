# Tiny Pretraining with Extreme Quantization: Parameter-Matched Direct Evidence

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-pretraining-with-extreme-quantization-parameter-matched-direct-evidence-e848c412d518`
Run ID: `tiny-pretraining-with-extreme-quantization-parameter-matched-direct-evidence-e848c412d518-20260609T065011534477+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/25069159f620

## What looked useful

Same-parameter extreme quantized tiny pretraining learned nontrivially but lagged dense controls: binary mean validation loss was 2.7971 versus dense 2.2529 (+24.2%), and ternary was 2.5873 (+14.8%), both missing the 10% success threshold.

## Boundaries and scale limits

Toy char-level MLP only; 3 seeds per mode; 1,000 optimizer steps; simple binary/ternary per-tensor scaling; no transformer blocks, no GPT-2-small-class baseline, no large corpus, no specialized low-bit optimizer, and no low-bit kernel efficiency measurement.

## Claim scope

In a 141,665-parameter NumPy char-level MLP trained from scratch on Tiny Shakespeare for 128,000 tokens per seed, binary and ternary forward-pass weight quantization with STE shadow training did not retain dense validation loss within the predeclared 10% tolerance under a matched trainable-parameter budget.

## Why it stopped

Proxy-scale direct test falsified the local success threshold; this is not a full validation of all large-scale extreme-quantized pretraining recipes.

## Recommended next action

Stop this exact claim as an early negative; a bounded follow-up should test a GPT-2-small-class or small transformer baseline with the same parameter-matched binary/ternary comparison and a mature QAT recipe.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched low-bit pretraining in a small transformer
- Success threshold: Ternary or binary mean validation loss within 10% of dense across at least 3 seeds while preserving nontrivial learning from initialization.
- Stop condition: Stop if the best quantized transformer variant remains more than 10% worse than dense after the matched sequence-item budget or shows unstable/non-monotonic learning in at least 2 of 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretraining-with-extreme-quantization-parameter-matched-direct-evidence-e848c412d518`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
