# Real-text threshold and baseline ablation for MinHash tiny-pretraining dedup

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-text-threshold-and-baseline-ablation-for-minhash-tiny-348c511674`
Run ID: `real-text-threshold-and-baseline-ablation-for-minhash-tiny-348c511674-20260611T003339552421+0000`

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

- Parent run decision: MinHash deduplication impact on tiny pretraining: enoch://control-plane/projects/minhash-deduplication-impact-on-tiny-pretraining-687d0464e1f9/runs/minhash-deduplication-impact-on-tiny-pretraining-687d0464e1f9-20260611T001259723626+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5e21c5e3a066

## What looked useful

High-threshold MinHash was an early negative: threshold 0.80 matched exact normalized hashing at precision 1.000, recall 0.500, F1 0.667. Lower thresholds showed the real tradeoff: with 3-token shingles, threshold 0.50 reached recall 0.858 and F1 0.779 but flagged 83/120 borderline overlaps; threshold 0.60 reached precision 0.961 and recall 0.617.

## Boundaries and scale limits

No actual tiny-LM pretraining, downstream memorization test, larger corpus, multilingual/code data, semantic paraphrase generation, or production-scale index was run. The evidence is local and controlled, not publication-grade.

## Claim scope

Tier 1 controlled small direct test on Wikitext real passages with injected train/eval duplicate labels: exact duplicates, light edits, borderline partial overlaps, and topic-mix nonduplicates. A 0.80 MinHash threshold over 3- or 5-token shingles did not improve recall over exact normalized hashing.

## Why it stopped

Tier 1 direct threshold ablation completed; the high-threshold MinHash claim is unsupported and not paper-ready, while the low-threshold result is only a useful signal requiring training-impact validation.

## Recommended next action

Run one bounded tiny-training deepen test comparing exact hash, 3-shingle MinHash at 0.50/0.60, and no dedup on the same real-text contamination setup, measuring held-out contamination leakage, eval loss, and retained-token fraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-training impact of low-threshold MinHash real-text dedup
- Success threshold: A low-threshold MinHash condition must improve duplicate leakage or memorization by at least 20% relative to exact hashing while retaining at least 90% of non-labeled training tokens and not worsening clean validation loss by more than 2%.
- Stop condition: Stop if low-threshold MinHash either fails to beat exact hashing on leakage/memorization or loses more than 10% of non-labeled tokens without a clean validation benefit.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-threshold-and-baseline-ablation-for-minhash-tiny-348c511674`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
