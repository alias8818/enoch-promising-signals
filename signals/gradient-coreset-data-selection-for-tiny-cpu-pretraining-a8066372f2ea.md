# Gradient Coreset Data Selection for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-coreset-data-selection-for-tiny-cpu-pretraining-a8066372f2ea`
Run ID: `gradient-coreset-data-selection-for-tiny-cpu-pretraining-a8066372f2ea-20260604T215523730115+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/78b7f7db23db

## What looked useful

Naive gradient-direction diversity can over-diversify the selected subset and hurt tiny pretraining loss; preserving pool-like frequency mass mattered more in this probe. Gradient norm selection improved mean validation loss by 0.0164 and beat random in 6/8 seeds, which is only a bounded follow-up signal.

## Boundaries and scale limits

Synthetic 4-topic corpus, NumPy embedding-plus-linear language model, 2,000-sequence selection pool, 800-sequence validation set, 18 epochs, CPU-only. No real corpus, tokenizer, transformer, GPT-2-small-class baseline, or long schedule was tested.

## Claim scope

On an 8-seed synthetic tiny next-token pretraining proxy with a 20% subset budget, projected gradient-direction farthest-first coreset selection was consistently worse than random selection; projected gradient norm selection showed a small non-paper-ready improvement.

## Why it stopped

Closed as a no-paper useful signal: the direct local proxy falsified naive gradient-direction coreset selection, but the small gradient-norm benefit needs real-corpus confirmation before any paper claim.

## Recommended next action

Run one bounded real-corpus follow-up on WikiText-2 or TinyStories with a tiny transformer/GRU, comparing random, gradient norm, and gradient-direction coreset under the same token budget and including selection overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny LM check for gradient-norm data selection
- Success threshold: Gradient norm selection beats random by at least 0.03 validation-loss points on mean across seeds and wins at least 4/5 seeds without more than 20% end-to-end overhead.
- Stop condition: Stop if gradient norm fails to beat random in at least 3/5 seeds or if selection overhead exceeds the training-time savings under the fixed compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-data-selection-for-tiny-cpu-pretraining-a8066372f2ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
