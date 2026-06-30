# Stratified coverage sampling for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stratified-coverage-sampling-for-tiny-pretraining-8f84a2d6d8f9`
Run ID: `stratified-coverage-sampling-for-tiny-pretraining-8f84a2d6d8f9-20260520T114547352371+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b491ee72200a

## What looked useful

Coverage/stratified sampling behaves like an explicit distribution tradeoff: it raises domain/token coverage and cuts rare-domain perplexity by about 44 percent, but increases natural-distribution perplexity by about 31-32 percent. Treat it as a targeted rare/balanced-data sampler, not a free general pretraining improvement.

## Boundaries and scale limits

Synthetic corpus only; small word-level neural LM rather than a transformer; five seeds; no real tokenizer, dedup, quality filtering, or large-scale pretraining. The result tests the data-selection mechanism under controlled skew, not broad real-corpus pretraining performance.

## Claim scope

In a synthetic skewed multi-domain corpus with a tiny NumPy neural next-token model and a 10,080-token selected pretraining budget, domain-stratified and coverage-greedy sampling improved balanced and rare-domain held-out language-model loss relative to uniform random sampling, but worsened natural-distribution and common-domain loss.

## Why it stopped

No-paper closure: the proxy produced a useful mixed mechanism signal but not direct publication-grade evidence for real tiny pretraining.

## Recommended next action

Run a bounded direct follow-up on a real small text corpus with a tokenizer and tiny transformer, comparing random, temperature/domain reweighting, domain-stratified, and coverage-greedy sampling at equal tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny transformer test of coverage-stratified sampling
- Success threshold: Balanced and rare-domain loss improve by at least 5 percent over random while natural-distribution loss is no worse than 5 percent relative to the best simple baseline.
- Stop condition: Stop if coverage/stratified sampling still causes more than 10 percent natural-distribution perplexity regression without a compensating balanced or rare-domain gain.

## Evidence references

- Artifact root: `<local-path>/projects/stratified-coverage-sampling-for-tiny-pretraining-8f84a2d6d8f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
