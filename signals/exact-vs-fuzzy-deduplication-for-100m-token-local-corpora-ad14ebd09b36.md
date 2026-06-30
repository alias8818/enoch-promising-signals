# Exact vs Fuzzy Deduplication for 100M-Token Local Corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-vs-fuzzy-deduplication-for-100m-token-local-corpora-ad14ebd09b36`
Run ID: `exact-vs-fuzzy-deduplication-for-100m-token-local-corpora-ad14ebd09b36-20260619T060002008726+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5b380ea115a

## What looked useful

Fuzzy deduplication can materially increase token removal and near-duplicate recall over exact hashing for local corpora, but it is not a drop-in replacement: threshold choice trades recall against false positives, and topic-similar unique documents can be removed at medium scale.

## Boundaries and scale limits

The largest direct run was 50,000 documents and 9,984,974 tokens, not 100M tokens. The 100M-token numbers are throughput extrapolations from local CPU-only Python runs. Real corpus artifacts, manual false-positive auditing, and downstream model or retrieval quality were not tested.

## Claim scope

On deterministic synthetic corpora up to about 10M tokens with known exact and controlled fuzzy duplicate groups, exact hashing is very fast and precise but only recovered about one third of removable duplicate documents, while SimHash-style fuzzy deduplication recovered 86-100% of removable duplicate documents depending on threshold and mutation mode, at about 50-65x lower throughput and with threshold-sensitive false positives.

## Why it stopped

Closed as a no-paper useful signal: synthetic medium evidence supports a practical tradeoff but does not directly validate 100M-token real-corpus deduplication or downstream quality.

## Recommended next action

Run a bounded real-corpus validation on a 5-20M token local sample with exact, SimHash thresholds 10/12/14, and manual audit of at least 200 fuzzy-only removals before considering any 100M-token full pass.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus audit of fuzzy-only deduplication removals
- Success threshold: Fuzzy-only removals add at least 10 percentage points of token reduction over exact deduplication with audited false-positive rate below 5% and runtime projected under 30 minutes for 100M tokens on this host.
- Stop condition: Stop if audited fuzzy-only false positives exceed 10% at every threshold that adds at least 5 percentage points of token reduction over exact deduplication, or if projected 100M-token runtime exceeds 30 minutes without clear quality benefit.

## Evidence references

- Artifact root: `<local-path>/projects/exact-vs-fuzzy-deduplication-for-100m-token-local-corpora-ad14ebd09b36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
