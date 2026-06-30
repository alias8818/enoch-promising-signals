# Difficulty-based curriculum learning for local pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `difficulty-based-curriculum-learning-for-local-pretraining-7a3260b8c218`
Run ID: `difficulty-based-curriculum-learning-for-local-pretraining-7a3260b8c218-20260522T202624135372+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72a1352c3750

## What looked useful

Ordered curricula produced strong recency bias and forgetting across difficulty bands: final mean validation loss was 0.1197 for random sampling, 1.8343 for easy-to-hard, and 1.7048 for hard-to-easy.

## Boundaries and scale limits

Synthetic character-level corpus, 815k-parameter Transformer, 420 training steps per run, three seeds; no real corpus, subword tokenizer, GPT-2-small-class model, downstream transfer, or long-horizon pretraining was tested.

## Claim scope

Strict difficulty-ordered batch schedules, easy-to-hard or hard-to-easy, did not improve a small causal Transformer's local-pretraining efficiency on a controlled synthetic easy/medium/hard corpus at equal token budget; random sampling was far better across three seeds.

## Why it stopped

Early proxy falsification: strict difficulty ordering was consistently worse than random sampling across three seeds at equal token budget, so this run is no-paper useful negative evidence rather than full validation.

## Recommended next action

Run a bounded follow-up testing difficulty-stratified replay/mixing against random sampling; stop if it cannot beat random by at least 5% final validation loss on this corpus and one real small-text corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Difficulty-stratified replay curriculum for local pretraining
- Success threshold: Replay/mixed curriculum improves final balanced validation loss by at least 5% versus random sampling on both corpora and does not worsen any difficulty band by more than 2%.
- Stop condition: Stop if replay/mixing fails to beat random on the synthetic corpus across three seeds or shows the same per-band forgetting pattern as strict ordering.

## Evidence references

- Artifact root: `<local-path>/projects/difficulty-based-curriculum-learning-for-local-pretraining-7a3260b8c218`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
