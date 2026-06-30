# Real-corpus tiny-transformer domain-mix classifier scoring

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-tiny-transformer-domain-mix-classifier-scoring-d32faa00aa`
Run ID: `real-corpus-tiny-transformer-domain-mix-classifier-scoring-d32faa00aa-20260621T182839078966+0000`

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

- Parent run decision: Domain-mix data selection via small-classifier scoring for tiny pretraining: enoch://control-plane/projects/domain-mix-data-selection-via-small-classifier-scoring-for-tiny-pretraining-9fee6c723db6/runs/domain-mix-data-selection-via-small-classifier-scoring-for-tiny-pretraining-9fee6c723db6-20260621T174312112334+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41859764a854

## What looked useful

Tiny transformer test macro-F1 was 0.4878 versus 0.0667 for length-only and 0.6235 for multinomial Naive Bayes. The mechanism has some signal but is not compelling as a tiny-transformer scoring method at this scale.

## Boundaries and scale limits

Single-seed CPU-only test; weak labels from project names; 405 train, 135 validation, and 135 test chunks from held-out project directories; no pretrained transformer or GPT-2-small-class baseline; local Enoch corpus only.

## Claim scope

On a controlled Tier 1 real local Enoch project-corpus split with weak directory-keyword labels, a 1-layer from-scratch tiny transformer learned domain signal above a length-only control but failed the predeclared domain-mix scoring threshold and underperformed a lexical Naive Bayes baseline.

## Why it stopped

Controlled Tier 1 direct test failed the declared threshold: tiny transformer macro-F1 0.4878 was below the 0.70 target and below Naive Bayes macro-F1 0.6235, so this is an early falsification of the from-scratch tiny-transformer domain-mix scoring claim rather than a full validation.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded follow-up if testing stronger labels and pretrained or parameter-matched transformer controls across multiple seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed pretrained tiny-transformer domain-mix scoring ablation
- Success threshold: Transformer macro-F1 >= 0.70, at least +0.05 above Naive Bayes, and no class F1 below 0.50 on held-out project directories across the median of at least three seeds.
- Stop condition: Stop if the median transformer macro-F1 remains below Naive Bayes or below 0.70 after the stronger labels and pretrained/parameter-matched control are tested.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-transformer-domain-mix-classifier-scoring-d32faa00aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
