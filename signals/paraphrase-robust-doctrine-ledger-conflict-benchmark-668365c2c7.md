# Paraphrase-Robust Doctrine Ledger Conflict Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `paraphrase-robust-doctrine-ledger-conflict-benchmark-668365c2c7`
Run ID: `paraphrase-robust-doctrine-ledger-conflict-benchmark-668365c2c7-20260613T160032043532+0000`

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

- Parent run decision: Operator-Doctrine Memory: Layered Evidence Ledger: enoch://control-plane/projects/operator-doctrine-memory-layered-evidence-ledger-b70451eaf1a3/runs/operator-doctrine-memory-layered-evidence-ledger-b70451eaf1a3-20260613T143132679904+0000
- Parent run decision: Natural-Language Doctrine Ledger Conflict Benchmark: enoch://control-plane/projects/natural-language-doctrine-ledger-conflict-benchmark-d9317d6e33/runs/natural-language-doctrine-ledger-conflict-benchmark-d9317d6e33-20260613T144929186220+0000

## What looked useful

The benchmark is solvable by explicit modality/action/scope normalization and exposes baseline weaknesses: lexical Jaccard drops 0.115 F1 from canonical to held-out paraphrase, word/char TF-IDF paraphrase F1 stays near 0.46-0.50, and TF-IDF hard-control false-positive rates are 0.56-0.64.

## Boundaries and scale limits

Synthetic templated data only; no real doctrine corpus, no human-authored paraphrases, no transformer/NLI/LLM baseline, and the structured parser uses synonym dictionaries aligned with the generator.

## Claim scope

Fixed-seed synthetic doctrine-ledger conflict benchmark with held-out paraphrases, canonical ablation, hard scope controls, lexical baseline, trained TF-IDF baselines, and a structured-parser sanity baseline.

## Why it stopped

Medium synthetic confirmation supports a benchmark mechanism but remains generator-bound and lacks real-corpus or semantic-model evidence.

## Recommended next action

Stop this run as no-paper useful signal; deepen with independently authored doctrine paraphrases and a transformer/NLI baseline before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent Doctrine Paraphrase Conflict Benchmark with NLI Baselines
- Success threshold: Semantic/NLI baseline improves paraphrase F1 by at least 0.15 over word TF-IDF while keeping hard-control false-positive rate below 0.20, and the result is stable across at least three fixed seeds or bootstrap resamples.
- Stop condition: Stop if independently authored data eliminate the paraphrase/scope-control gap or if semantic baselines cannot beat TF-IDF by 0.05 F1 under the same hard-control constraint.

## Evidence references

- Artifact root: `<local-path>/projects/paraphrase-robust-doctrine-ledger-conflict-benchmark-668365c2c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
