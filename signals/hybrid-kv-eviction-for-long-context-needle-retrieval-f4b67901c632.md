# Hybrid KV eviction for long-context needle retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-kv-eviction-for-long-context-needle-retrieval-f4b67901c632`
Run ID: `hybrid-kv-eviction-for-long-context-needle-retrieval-f4b67901c632-20260529T071943373830+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ab3b49546753

## What looked useful

Hybrid KV eviction is useful only when the answer token is write-time salient or still inside the recent window. It matched salience-only at 1.000 success on marked needles and reached 1.000 for very late neutral needles, but old neutral needles remained near random, with hybrid success about 0.022 to 0.030 at positions 0.05 and 0.50 in the positional sweep. The bottleneck is salience quality, not the hybrid cache layout itself.

## Boundaries and scale limits

No trained transformer, real prompts, tokenizer effects, multi-layer or multi-head KV behavior, learned salience predictor, or serving-system throughput/memory validation was tested. The result is a mechanism probe, not full long-context model evidence.

## Claim scope

Synthetic scalar-attention KV-cache benchmark with contexts up to 16,384 tokens and cache budgets of 5% to 10% in the positional sweep. Hybrid eviction was tested against full-cache, recent-only, sink+recent, random, and salience-only policies for neutral, marked, and late-marker needle scenarios.

## Why it stopped

Proxy mechanism evidence is mixed: hybrid supports marked or recent needles but does not solve old neutral needle retrieval and does not outperform salience-only when salience is oracle-quality.

## Recommended next action

Stop this run as no-paper useful signal; next run should test a real small transformer with a non-oracle write-time salience predictor against recent-only and salience-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer KV eviction with learned write-time salience
- Success threshold: Hybrid must improve exact-match retrieval by at least 10 percentage points over both recent-only and salience-only on old non-recent needles at the same KV budget without losing more than 5 percentage points on near-recent needles.
- Stop condition: Stop if learned or heuristic write-time salience cannot retain old neutral answer tokens above random-retention rate, or if hybrid fails to beat the stronger of recent-only and salience-only on old-needle exact match.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-kv-eviction-for-long-context-needle-retrieval-f4b67901c632`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
