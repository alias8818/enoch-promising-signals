# Suffix-automaton near-dedup on a tiny pretraining corpus

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-automaton-near-dedup-on-a-tiny-pretraining-corpus-65340f07210f`
Run ID: `suffix-automaton-near-dedup-on-a-tiny-pretraining-corpus-65340f07210f-20260619T134035124522+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/616dd4252f11

## What looked useful

Naive SAM coverage best F1 was 0.117 with precision 0.090 and recall 0.167. DF-filtered SAM improved to best F1 0.197 with precision 0.112 and recall 0.833, showing common-token suppression is necessary but insufficient.

## Boundaries and scale limits

Synthetic word-token corpus only; no real web corpus, no tokenizer-specific effects, no large index, no throughput stress test, and no downstream model-training validation.

## Claim scope

On a deterministic 90-document synthetic tiny pretraining-like corpus, naive suffix-automaton substring coverage is not viable as a standalone near-dedup detector under shared boilerplate/template controls; document-frequency-filtered SAM gives a weak useful signal but remains low precision.

## Why it stopped

Proxy early falsification for standalone suffix-automaton coverage: synthetic tiny-corpus evidence shows high false-positive rates from shared template/boilerplate, not full validation on real pretraining data.

## Recommended next action

Stop this run as no-paper evidence; next bounded test should combine DF-filtered SAM with a candidate-generation/blocking stage and evaluate on a real small public corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: DF-filtered SAM with candidate blocking on a real small public corpus
- Success threshold: At least 0.80 recall and 0.90 precision on labeled near-duplicate pairs, with fewer false positives than the strongest n-gram/MinHash baseline at comparable recall.
- Stop condition: Stop if precision remains below 0.50 at 0.80 recall after candidate blocking and common-token filtering.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-automaton-near-dedup-on-a-tiny-pretraining-corpus-65340f07210f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
