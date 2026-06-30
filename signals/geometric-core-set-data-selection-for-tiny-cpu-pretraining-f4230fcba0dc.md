# Geometric core-set data selection for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `geometric-core-set-data-selection-for-tiny-cpu-pretraining-f4230fcba0dc`
Run ID: `geometric-core-set-data-selection-for-tiny-cpu-pretraining-f4230fcba0dc-20260527T192951065721+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1399af805d1d

## What looked useful

Diversity-first geometric core-sets can select harmful extremes for tiny LM pretraining; representativeness-first geometric herding is the more plausible geometric variant, but its observed gain is small.

## Boundaries and scale limits

This is a character n-gram LM proxy on 10 public-domain books, not neural Transformer pretraining, downstream transfer, web-scale selection, or publication-grade validation. The herding gain is small and mostly tied with the best random seed.

## Claim scope

On a ten-book Project Gutenberg character-level tiny CPU pretraining proxy, farthest-first geometric k-center selection under fixed character budgets worsened held-out BPC versus random selection, while mean-matching geometric herding produced a small consistent improvement over the random mean across 6%, 18%, and 30% budgets.

## Why it stopped

No-paper closure: the current result is a proxy useful signal, not direct neural pretraining evidence, and the positive herding effect is too small to be paper-ready.

## Recommended next action

Run a bounded neural follow-up using the implemented selectors on a tiny byte-level GRU/Transformer with multiple random seeds; stop if herding does not beat the random mean by at least 1% validation loss with confidence intervals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LM validation of representativeness-first geometric herding
- Success threshold: Herding improves validation loss or BPC by at least 1% over the random mean and beats the best random-seed baseline in at least two of three budget settings.
- Stop condition: Stop as negative if k-center remains worse and herding is within random/model-seed noise or below 1% relative improvement.

## Evidence references

- Artifact root: `<local-path>/projects/geometric-core-set-data-selection-for-tiny-cpu-pretraining-f4230fcba0dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
