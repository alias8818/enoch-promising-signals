# Near-dedup and low-perplexity filter for tiny pretraining data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `near-dedup-and-low-perplexity-filter-for-tiny-pretraining-data-38396baed526`
Run ID: `near-dedup-and-low-perplexity-filter-for-tiny-pretraining-data-38396baed526-20260530T040033551797+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba852333a41c

## What looked useful

Across 24 seeds, dedup improved useful held-out loss by -0.01319 bpc versus raw with 24/24 seed wins; lowppl_25 improved by -0.01332 bpc with 24/24 wins; combined_05 improved by -0.01105 bpc, but combined_25 worsened loss by +0.00635 bpc with 0/24 wins. This supports filtering repeated/easy contamination, while warning that stacking filters can discard useful data in tiny corpora.

## Boundaries and scale limits

Synthetic data only; proxy character n-gram learner only; no real corpus, tokenizer, transformer, equal-compute neural training, or downstream-task validation. Results should not be generalized to production pretraining without a bounded neural LM replication.

## Claim scope

On controlled synthetic tiny pretraining corpora with repeated boilerplate and near-duplicate contamination, character 5-gram proxy learners get lower held-out useful bits/character after near-deduplication or sufficiently strong low-perplexity filtering, but the combined filter is threshold-sensitive and can be worse than raw when too aggressive.

## Why it stopped

No-paper proxy result: synthetic n-gram evidence supports a useful mechanism but also shows threshold-sensitive failure for the combined filter; it is not direct neural pretraining evidence.

## Recommended next action

Run a bounded real-corpus replication with a small neural LM, equal token budgets, and threshold sweeps before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small neural LM test of dedup versus low-perplexity filtering
- Success threshold: Dedup or conservative combined filtering improves neural validation loss by at least 1% relative to raw in at least 4 of 5 seeds without discarding more than 20% of non-duplicate useful documents.
- Stop condition: Stop if no filter improves validation loss in at least 3 of 5 seeds, or if the only improving settings rely on removing a large fraction of manually inspected useful documents.

## Evidence references

- Artifact root: `<local-path>/projects/near-dedup-and-low-perplexity-filter-for-tiny-pretraining-data-38396baed526`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
