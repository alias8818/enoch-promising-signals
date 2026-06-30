# Public-corpus volunteer minhash dedup validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `public-corpus-volunteer-minhash-dedup-validation-31cba8f7df`
Run ID: `public-corpus-volunteer-minhash-dedup-validation-31cba8f7df-20260522T044816585438+0000`

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

- Parent run decision: Local minhash volunteer cluster matches central deduplication: enoch://control-plane/projects/local-minhash-volunteer-cluster-matches-central-deduplication-1817ba95bd37/runs/local-minhash-volunteer-cluster-matches-central-deduplication-1817ba95bd37-20260521T194634213666+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/230fe5f044c9

## What looked useful

MinHash-LSH is supported as a high-recall candidate generator for public-corpus dedup review, but raw LSH candidates have low precision at recall-preserving settings. In the primary 32-band run, recall for injected Jaccard>=0.80 duplicates was 1.00 and workload reduction was 99.83%, but precision was 0.419. A sweep showed 8 bands reached precision 1.00 but recall fell to 0.821, while 16 bands reached recall 0.974 but precision only 0.623.

## Boundaries and scale limits

Small English public-domain passage corpus only; human volunteer judgement was proxied by exact word-shingle Jaccard and injected labels; no full-document, multilingual, web-scale, or human adjudication validation was run.

## Claim scope

On a controlled Tier 1 test using four Project Gutenberg books split into 336 passage records with 96 injected duplicate or near-duplicate variants, raw MinHash-LSH can reduce review pairs by more than 99.8% and recover all injected pairs with exact 5-word-shingle Jaccard >= 0.80 at recall-oriented settings, but it does not meet a practical volunteer precision threshold without a second-stage filter.

## Why it stopped

Tier 1 direct validation completed; raw MinHash-LSH failed the predefined precision threshold for volunteer review despite strong recall and workload reduction, so this is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen test that adds a second-stage exact Jaccard or containment scorer after MinHash candidates, then evaluate on a larger cached public-domain corpus plus a small manual adjudication sample.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-stage MinHash plus exact-containment volunteer dedup validation
- Success threshold: At least one two-stage setting must achieve recall >= 0.95 for held-out injected high-similarity duplicates, candidate precision >= 0.80 by exact/proxy labels, workload reduction >= 0.90 versus all-pairs review, and no more than 10% disagreement in the manual adjudication sample.
- Stop condition: Stop if every two-stage setting with recall >= 0.95 has precision < 0.80 or if manual adjudication shows the automatic similarity proxy is not aligned with volunteer judgement.

## Evidence references

- Artifact root: `<local-path>/projects/public-corpus-volunteer-minhash-dedup-validation-31cba8f7df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
