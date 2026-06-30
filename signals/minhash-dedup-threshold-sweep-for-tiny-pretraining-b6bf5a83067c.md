# MinHash Dedup Threshold Sweep for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `minhash-dedup-threshold-sweep-for-tiny-pretraining-b6bf5a83067c`
Run ID: `minhash-dedup-threshold-sweep-for-tiny-pretraining-b6bf5a83067c-20260628T041835239796+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/253d88d48df7

## What looked useful

Across seeds 13, 37, and 101, no deduplication had the best mean clean validation loss. Aggressive thresholds removed complete clusters and monotonically worsened validation loss, indicating that near-duplicate removal can become harmful data loss for tiny corpora.

## Boundaries and scale limits

Synthetic corpus only; character context LM only; no real web corpus, tokenizer, transformer, replacement-data budget, or long/full-scale pretraining evidence.

## Claim scope

Three seeded synthetic tiny-pretraining probes with MinHash 4-word shingles and a NumPy character context LM found no validation benefit from deduplication thresholds 0.95, 0.85, 0.75, 0.65, or 0.55 versus no deduplication.

## Why it stopped

Proxy early falsification: in the tested synthetic tiny-LM setting, MinHash threshold deduplication failed to improve clean validation loss and aggressive thresholds degraded it.

## Recommended next action

Stop this run as no-paper early proxy evidence; a bounded follow-up should test a real tiny corpus with a tiny transformer and replacement-token-budget control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny transformer MinHash threshold sweep with replacement-token control
- Success threshold: A tested threshold improves held-out perplexity by at least 1 percent versus no deduplication across at least three seeds while retaining at least 98 percent of semantic clusters.
- Stop condition: Stop if high thresholds do not improve mean held-out perplexity or if any beneficial threshold depends on losing more than 2 percent of semantic clusters.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-sweep-for-tiny-pretraining-b6bf5a83067c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
