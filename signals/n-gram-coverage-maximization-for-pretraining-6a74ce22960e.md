# N-gram Coverage Maximization for Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-coverage-maximization-for-pretraining-6a74ce22960e`
Run ID: `n-gram-coverage-maximization-for-pretraining-6a74ce22960e-20260630T022355810641+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/4d70856a2150

## What looked useful

Greedy 3-gram coverage selected about 2.7% more unique 3-grams than random and achieved mean validation loss 4.4496 versus 4.4836 for random, 4.4765 for topic-balanced, and 4.5170 for frequency-matched controls. Topic balancing slightly beat greedy on rare held-out 3-gram recall, so coverage maximization is promising but not uniformly dominant.

## Boundaries and scale limits

Synthetic corpus only; no natural-language corpus, real tokenizer, transformer pretraining run, downstream evaluation, or large-scale data-selection cost analysis. The result should not be generalized to GPT-scale or natural-text pretraining without a real-corpus confirmation.

## Claim scope

On a controlled synthetic topic/rare-motif corpus, greedy 3-gram coverage selection at a fixed 240-document budget improved tiny-GRU held-out validation loss versus random, topic-balanced, and unigram frequency-matched controls across three repeated seeds.

## Why it stopped

No-paper closure: the local synthetic proxy supports the mechanism but is not direct natural-text pretraining evidence.

## Recommended next action

Run a bounded real-corpus deepen test with a real tokenizer and parameter-matched tiny transformer before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus n-gram coverage selection for small transformer pretraining
- Success threshold: Greedy coverage must improve mean validation loss over the strongest baseline by at least one baseline standard deviation across repeated seeds while preserving or improving rare-token/rare-ngram metrics.
- Stop condition: Stop if greedy coverage fails to beat random and the strongest balancing/distribution baseline on validation loss, or if it improves coverage while degrading validation loss or rare-token metrics.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-coverage-maximization-for-pretraining-6a74ce22960e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
