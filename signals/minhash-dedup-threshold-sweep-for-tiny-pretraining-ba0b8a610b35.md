# MinHash dedup-threshold sweep for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-dedup-threshold-sweep-for-tiny-pretraining-ba0b8a610b35`
Run ID: `minhash-dedup-threshold-sweep-for-tiny-pretraining-ba0b8a610b35-20260629T143313205693+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e50efb8a17e4

## What looked useful

High thresholds preserved semantic family coverage while removing near duplicates; lower thresholds caused many false-positive removals, showing that aggressive MinHash dedup can silently sacrifice corpus diversity even when short-run validation loss remains competitive.

## Boundaries and scale limits

Synthetic corpus only; character-level GRU only; 90 optimizer steps per threshold; no real tokenizer, transformer, downstream benchmark, or full-token-budget pretraining validation.

## Claim scope

On a controlled synthetic near-duplicate corpus with three seeded tiny character-GRU pretraining sweeps, MinHash/Jaccard thresholds from 0.95 to 0.85 removed same-family duplicates without false-positive family loss and improved clean validation loss versus no dedup; thresholds at 0.80 and 0.70 over-removed cross-family documents and reduced diversity without a decisive LM benefit.

## Why it stopped

Bounded proxy evidence is informative but not publication-grade; it does not directly validate real tiny-pretraining behavior on natural data.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded action is a real-corpus small-transformer replication with audited duplicate clusters and fixed-token-budget training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus MinHash threshold sweep for small transformer pretraining
- Success threshold: A threshold in the 0.90 to 0.95 range must reduce audited duplicate exposure by at least 25% versus no dedup, preserve at least 98% sampled topic/cluster coverage, and match or improve fixed-token-budget validation loss relative to no dedup and lower-threshold alternatives.
- Stop condition: Stop if audited false-positive removals exceed 2% of sampled non-duplicate pairs or if no threshold improves duplicate exposure without degrading fixed-token-budget validation loss by more than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-sweep-for-tiny-pretraining-ba0b8a610b35`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
