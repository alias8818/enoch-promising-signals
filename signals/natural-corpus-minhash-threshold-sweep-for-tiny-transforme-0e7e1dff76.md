# Natural-corpus MinHash threshold sweep for tiny transformer pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-corpus-minhash-threshold-sweep-for-tiny-transforme-0e7e1dff76`
Run ID: `natural-corpus-minhash-threshold-sweep-for-tiny-transforme-0e7e1dff76-20260609T212221961472+0000`

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

- Parent run decision: MinHash Deduplication Threshold Sweep for Tiny Pretraining: enoch://control-plane/projects/minhash-deduplication-threshold-sweep-for-tiny-pretraining-dc4b969a8803/runs/minhash-deduplication-threshold-sweep-for-tiny-pretraining-dc4b969a8803-20260609T163955345161+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/000e22f99bde

## What looked useful

MinHash dedup did not yield a robust held-out validation-loss win. Thresholds 0.70 and 0.80 removed many duplicate-family documents but worsened mean validation loss by about 0.005 and 0.004 respectively; 0.95 barely changed the corpus and worsened by about 0.003; 0.90 was essentially neutral/slightly better on mean (-0.0015) but inconsistent across seeds.

## Boundaries and scale limits

Not GPT-2-small-class, not web-scale, near duplicates were controlled perturbations of natural documents rather than only naturally occurring duplicate clusters, and the comparison used equal update budgets rather than matched effective unique-token exposure.

## Claim scope

Tier 1 controlled small direct test on Wikitext-2-derived natural text with 35% traceable near-duplicate contamination, MinHash thresholds 0.70/0.80/0.90/0.95, and identical tiny character-level Transformer training for 600 updates across three seeds.

## Why it stopped

Controlled Tier 1 direct evidence found no robust threshold benefit; this is useful no-paper evidence, not a full validation or publication-grade positive.

## Recommended next action

Run one bounded deepen test only if continuing this line: threshold 0.90 versus no dedup on a larger naturally duplicated corpus with family-aware retention and token-exposure-matched training; otherwise stop because this Tier 1 run does not support a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Family-aware 0.90 MinHash dedup with token-exposure-matched tiny Transformer training
- Success threshold: Mean held-out validation loss improves by at least 0.005 versus no dedup across at least five seeds, with duplicate recall at least 0.15 and unique/original false-removal rate no more than 0.07.
- Stop condition: Stop if 0.90 fails to beat no dedup by 0.005 mean validation loss, if the effect is not positive in at least four of five seeds, or if unique/original false-removal exceeds 0.07.

## Evidence references

- Artifact root: `<local-path>/projects/natural-corpus-minhash-threshold-sweep-for-tiny-transforme-0e7e1dff76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
