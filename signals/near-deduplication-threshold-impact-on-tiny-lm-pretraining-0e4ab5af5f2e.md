# Near-deduplication threshold impact on tiny LM pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `near-deduplication-threshold-impact-on-tiny-lm-pretraining-0e4ab5af5f2e`
Run ID: `near-deduplication-threshold-impact-on-tiny-lm-pretraining-0e4ab5af5f2e-20260608T004021019109+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d4d11440c3cb

## What looked useful

A bounded reproducible probe found a threshold tradeoff: aggressive dedup around 0.55 reduced duplicate memorization and improved general held-out BPC versus lenient/no dedup, while no dedup lowered canary BPC, indicating stronger repeated-string memorization.

## Boundaries and scale limits

Synthetic corpus, character n-gram proxy, no neural transformer, no real web corpus, no fixed-SGD-token-budget training, and coarse thresholds only. This is not publication-grade evidence for real LM pretraining.

## Claim scope

In a controlled 90-family synthetic corpus with exact Jaccard 5-shingle near-deduplication and a character 6-gram tiny-LM proxy, deduplication threshold materially changed held-out bits-per-character and duplicate-string memorization: threshold 0.55 gave the best general held-out BPC across 5/5 seeds, while no dedup produced the strongest canary memorization across 5/5 seeds.

## Why it stopped

Closed as no-paper useful signal because the evidence is a controlled synthetic character n-gram proxy rather than direct neural tiny-LM pretraining on a real corpus.

## Recommended next action

Run a bounded deepen follow-up on a real small corpus with a tiny transformer at matched token/update budgets, preserving the held-out perplexity, canary memorization, retained-token diversity, and threshold-retention metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny transformer near-dedup threshold sweep
- Success threshold: A non-no-dedup threshold improves held-out validation loss by at least 1 percent relative to no dedup while reducing canary memorization by at least 10 percent, consistently across at least 3 seeds.
- Stop condition: Stop if all dedup thresholds are within run-to-run noise of no dedup on held-out loss and memorization, or if aggressive thresholds reduce retained diversity without improving validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/near-deduplication-threshold-impact-on-tiny-lm-pretraining-0e4ab5af5f2e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
