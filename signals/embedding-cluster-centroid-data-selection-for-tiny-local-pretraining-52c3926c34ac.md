# Embedding-cluster centroid data selection for tiny local pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-cluster-centroid-data-selection-for-tiny-local-pretraining-52c3926c34ac`
Run ID: `embedding-cluster-centroid-data-selection-for-tiny-local-pretraining-52c3926c34ac-20260628T085856991761+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1545f58672e5

## What looked useful

Centroid selection appears useful only in the very data-starved tested regime: at 128 chunks it improved mean validation loss versus random by 0.009476 and was better in 5/5 paired seeds, while at 512 chunks it was indistinguishable from random with a +0.000201 mean loss delta.

## Boundaries and scale limits

Single corpus, character-level modeling, small 2-layer transformer, 5 seeds per method, two subset budgets, local hashed n-gram embeddings rather than semantic embedding models; no downstream tasks, tokenizer-level LLM training, GPT-2-small-class baseline, or multi-corpus validation.

## Claim scope

On Tiny Shakespeare character-level tiny local pretraining with hashed character n-gram TF-IDF clustering, centroid subset selection gave no measurable validation-loss benefit at a 512-chunk budget but gave a small paired validation-loss improvement at a 128-chunk budget.

## Why it stopped

Bounded local evidence is mixed: the method has a small low-budget signal but fails to improve at the larger tested budget, so it is not publication-grade or broadly validated.

## Recommended next action

Stop this run as no-paper useful signal; next run should repeat the low-budget centroid advantage on at least two additional corpora with tokenized language modeling and stronger selection baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-corpus tokenized low-budget centroid selection check
- Success threshold: Centroid selection beats random and cluster-random by at least 0.5% relative validation loss on mean paired results in at least two corpora, without losing to k-center/farthest-first by more than 0.2%.
- Stop condition: Stop if centroid selection is not better than random on mean paired validation loss in either additional corpus, or if the observed gain remains below 0.2% relative validation loss across corpora.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-cluster-centroid-data-selection-for-tiny-local-pretraining-52c3926c34ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
