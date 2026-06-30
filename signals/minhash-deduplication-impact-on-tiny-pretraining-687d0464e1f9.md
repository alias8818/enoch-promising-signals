# MinHash deduplication impact on tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-deduplication-impact-on-tiny-pretraining-687d0464e1f9`
Run ID: `minhash-deduplication-impact-on-tiny-pretraining-687d0464e1f9-20260611T001259723626+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5e21c5e3a066

## What looked useful

MinHash removed about 49.0% of duplicate copies with 0 observed unique false positives, admitted 220.7 more unique records into the same 30,000-token budget than raw, lowered held-out record loss by 0.695 nats/token, and reduced the heldout-minus-duplicate memorization gap by 1.069 nats/token. Exact full-document dedup was effectively a no-op on mutated duplicates.

## Boundaries and scale limits

Synthetic token records only; 2-layer 96-wide tiny Transformer; 450 optimizer steps; 3 seeds; fixed MinHash threshold; no real tokenizer, real corpus, downstream benchmark, threshold sweep, or GPT-2-small-class validation.

## Claim scope

In a controlled synthetic fixed-token-budget tiny causal Transformer pretraining setup with mutated near-duplicate record clusters, MinHash near-deduplication admitted substantially more unique records than raw or exact-document deduplication and improved clean held-out record loss while reducing duplicate memorization pressure.

## Why it stopped

No-paper useful signal: the mechanism is supported in a bounded synthetic tiny-training test, but this is not a full validation of MinHash deduplication for real pretraining corpora.

## Recommended next action

Run one bounded real-text follow-up with injected and natural near-duplicates, threshold sweeps, exact n-gram/suffix-array baselines, and stable validation perplexity before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text threshold and baseline ablation for MinHash tiny-pretraining dedup
- Success threshold: MinHash beats raw and exact-document dedup on clean validation perplexity in at least 3 seeds while keeping unique-document false positives below 2% and matching or exceeding exact n-gram/suffix baseline quality per retained token.
- Stop condition: Stop if MinHash cannot beat raw/exact dedup on clean validation perplexity or if the threshold needed for quality causes unique false positives above 2%.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-deduplication-impact-on-tiny-pretraining-687d0464e1f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
