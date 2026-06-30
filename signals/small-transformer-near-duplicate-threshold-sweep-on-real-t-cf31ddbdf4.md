# Small-Transformer Near-Duplicate Threshold Sweep on Real Tiny Corpus

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-near-duplicate-threshold-sweep-on-real-t-cf31ddbdf4`
Run ID: `small-transformer-near-duplicate-threshold-sweep-on-real-t-cf31ddbdf4-20260613T155700587420+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Near-Duplicate Threshold Sweep for Tiny Pretrain: enoch://control-plane/projects/near-duplicate-threshold-sweep-for-tiny-pretrain-213e920a0467/runs/near-duplicate-threshold-sweep-for-tiny-pretrain-213e920a0467-20260613T151548827821+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ee0ff0d24823

## What looked useful

A small-transformer threshold near 0.87 is a concrete candidate for edited near-duplicate detection on real tiny text corpora, with a large observed score gap: positive min 0.8753 versus negative max 0.3256 in this run.

## Boundaries and scale limits

Tiny corpus only; positives are controlled deterministic edits rather than naturally labeled duplicates; one seed and one small transformer model; char n-gram TF-IDF reached the same perfect F1, so this is not transformer-specific or paper-ready.

## Claim scope

On a 40-document real 20 Newsgroups tiny corpus with deterministic near-duplicate edits and same/cross-category controls, all-MiniLM-L6-v2 cosine threshold 0.87 separated 120 positive and 80 negative pairs with precision 1.000, recall 1.000, and F1 1.000.

## Why it stopped

Tier 1 direct small test completed and produced a useful threshold signal, but the result is no-paper because labels are controlled edits, the corpus is tiny, and the lexical baseline matched transformer performance.

## Recommended next action

Run a bounded deepen follow-up on naturally labeled duplicate or boilerplate-heavy document pairs and require the transformer threshold to outperform lexical char-TFIDF before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Duplicate and Boilerplate-Hard Negative Threshold Check
- Success threshold: At matched recall >= 0.95, transformer precision is at least 0.95 and F1 is at least 0.05 above char-TFIDF, or transformer high-score false positives are reduced by at least 50% on boilerplate-heavy hard negatives.
- Stop condition: Stop as no-paper negative if natural positives or hard negatives produce F1 below 0.90 at thresholds near 0.87, or if char-TFIDF remains equal or better across the matched-recall operating region.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-near-duplicate-threshold-sweep-on-real-t-cf31ddbdf4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
