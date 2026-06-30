# Perplexity-filtered curriculum vs shuffled order on tiny GPT-2

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-filtered-curriculum-vs-shuffled-order-on-tiny-gpt-2-ca09a7ed3e13`
Run ID: `perplexity-filtered-curriculum-vs-shuffled-order-on-tiny-gpt-2-ca09a7ed3e13-20260620T020334465014+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/616dd4252f11

## What looked useful

Corrected per-chunk perplexity filtering produced a near-zero, seed-unstable effect: shuffled won 2 of 3 seeds, curriculum won 1 of 3, mean curriculum-minus-shuffled validation perplexity was +9.3254 (+0.0211%). This is an early falsification of a free easiest-first ordering benefit in the bounded setup.

## Boundaries and scale limits

Small public corpus, tiny pretrained GPT-2 proxy, 768 chunks, 80 steps per arm, three seeds, CPU-only; does not test GPT-2-small-class or larger models, long schedules, larger corpora, hard-to-easy curricula, dynamic curricula, or unfiltered baselines.

## Claim scope

On sshleifer/tiny-gpt2 fine-tuned for 80 CPU-bounded optimizer steps on Tiny Shakespeare 64-token chunks, ordering the lowest-base-perplexity 50% of train chunks easiest-first did not improve final validation perplexity versus shuffling the same filtered chunks across three corrected seeds.

## Why it stopped

Proxy-scale direct test found no stable advantage for perplexity-filtered easiest-first ordering; this is early falsification, not full validation or broad curriculum-learning disproof.

## Recommended next action

Stop this run as a bounded no-paper useful signal; only revisit with a preregistered longer GPT-2-small-class multi-seed experiment including unfiltered and hard-to-easy controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class perplexity-filtered curriculum with order and filtering controls
- Success threshold: Easiest-first must beat shuffled-filtered by at least 1% final validation perplexity and show the same direction in at least 4 of 5 seeds without losing to hard-to-easy.
- Stop condition: Stop if after two seeds the absolute mean relative delta remains below 0.25% or directions disagree with no early-learning trace advantage.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-curriculum-vs-shuffled-order-on-tiny-gpt-2-ca09a7ed3e13`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
