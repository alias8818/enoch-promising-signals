# Real-crawl tiny neural LM ablation for quality and MinHash filtering

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-crawl-tiny-neural-lm-ablation-for-quality-and-minhash-4279f676d7`
Run ID: `real-crawl-tiny-neural-lm-ablation-for-quality-and-minhash-4279f676d7-20260527T194000992696+0000`

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

- Parent run decision: MinHash-quality pipeline vs raw crawl for tiny pretraining: enoch://control-plane/projects/minhash-quality-pipeline-vs-raw-crawl-for-tiny-pretraining-e91f9bc0d5d0/runs/minhash-quality-pipeline-vs-raw-crawl-for-tiny-pretraining-e91f9bc0d5d0-20260527T173811088493+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1399af805d1d

## What looked useful

Quality filtering produced mean held-out loss deltas of -0.009657 on quality validation and -0.008363 on all validation versus raw across three seeds. Quality+MinHash beat raw by a similar amount, but the MinHash-specific delta versus quality-only was only -0.000272 and cannot be interpreted as a real deduplication effect because almost no documents were removed.

## Boundaries and scale limits

Single WET shard, 520-document train pool per seed, 120 validation documents per seed, 320k training bytes, 900 optimization steps, byte-level MLP LM rather than GPT-style transformer, heuristic quality scoring, and near-zero natural duplicate prevalence. This does not validate large-scale crawl filtering or publication-grade MinHash deduplication benefits.

## Claim scope

On one Common Crawl 2025 WET shard with 750 collected documents, three seeds of a tiny NumPy byte-level neural LM showed a small consistent held-out loss improvement from median quality filtering under an equal 320k-byte training budget. MinHash near-deduplication was not meaningfully exercised because it removed only 0, 1, and 0 documents across the three seed splits.

## Why it stopped

No-paper closure: the Tier 1 direct test supports a useful small quality-filtering mechanism signal but does not support a MinHash benefit or publication-grade crawl-filtering claim.

## Recommended next action

Run a bounded multi-shard deepen test that first verifies at least 2% natural near-duplicate removal, then repeats the equal-token LM ablation to isolate quality-only versus quality+MinHash.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-shard duplicate-prevalence controlled MinHash ablation
- Success threshold: At least 2% documents removed by MinHash and mean quality+MinHash validation loss at least 0.01 nats lower than quality-only across three seeds without harming all-validation loss.
- Stop condition: Stop as inconclusive or negative if natural duplicate removal is below 2%, if quality+MinHash does not beat quality-only by 0.01 nats, or if the effect appears only on one seed.

## Evidence references

- Artifact root: `<local-path>/projects/real-crawl-tiny-neural-lm-ablation-for-quality-and-minhash-4279f676d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
