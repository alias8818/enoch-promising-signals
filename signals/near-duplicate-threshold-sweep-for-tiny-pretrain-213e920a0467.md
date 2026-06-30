# Near-Duplicate Threshold Sweep for Tiny Pretrain

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `near-duplicate-threshold-sweep-for-tiny-pretrain-213e920a0467`
Run ID: `near-duplicate-threshold-sweep-for-tiny-pretrain-213e920a0467-20260613T151548827821+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ee0ff0d24823

## What looked useful

Strict filtering at threshold 0.35 kept 30.9% of tokens, removed 100% of injected noisy near duplicates, and improved combined validation loss from 5.1668 at no-dedupe threshold 1.01 to 4.8845.

## Boundaries and scale limits

Synthetic corpus only; 2 seeds; 220 training steps per threshold; NumPy next-token MLP rather than Transformer; no real web corpus, tokenizer study, downstream evaluation, or full tiny pretraining run.

## Claim scope

In a synthetic fact-template corpus with injected exact duplicates, near duplicates, and noisy near duplicates, a tiny NumPy next-token model achieved lower validation loss after strict word 5-gram Jaccard near-duplicate filtering; the best tested threshold was 0.35.

## Why it stopped

No-paper useful signal: the local result supports the scoped synthetic mechanism but is proxy-only and not full validation of tiny pretraining deduplication.

## Recommended next action

Run a bounded direct follow-up with a small Transformer on a real small corpus plus controlled near-duplicate/noisy injection; this run should stop as no-paper proxy evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Near-Duplicate Threshold Sweep on Real Tiny Corpus
- Success threshold: A thresholded filter improves validation perplexity by at least 3% versus no dedupe without worsening clean held-out paraphrase loss by more than 1%, across at least 3 seeds.
- Stop condition: Stop if thresholded filtering does not beat no dedupe on validation perplexity in at least 2 of 3 seeds or if improvements only appear on synthetic injected examples and not real-corpus validation.

## Evidence references

- Artifact root: `<local-path>/projects/near-duplicate-threshold-sweep-for-tiny-pretrain-213e920a0467`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
