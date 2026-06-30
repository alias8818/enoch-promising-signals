# MinHash Dedup Threshold Sweep on Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-dedup-threshold-sweep-on-tiny-pretraining-53e2876223d0`
Run ID: `minhash-dedup-threshold-sweep-on-tiny-pretraining-53e2876223d0-20260613T131731248400+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c2469b6e979

## What looked useful

Aggressive MinHash dedup was beneficial in the controlled proxy: threshold 0.55 kept about 477 of 960 training docs, improved mean validation perplexity from 2.446 to 2.356 versus no dedup, and reduced mean canary memorization gap from 4.120 to 3.919.

## Boundaries and scale limits

Synthetic template corpus only; word-level GRU only; no natural web corpus, tokenizer-matched transformer, downstream tasks, or long training. Results are mechanism evidence, not broad dedup policy validation.

## Claim scope

On a deterministic synthetic tiny pretraining corpus trained with a small word-level GRU, MinHash near-duplicate threshold choice changed both held-out validation perplexity and a canary memorization-gap metric. In the 192-cluster, 5-seed confirmation sweep, thresholds 0.55 and 0.70 outperformed the no-dedup 1.01 control on validation perplexity and reduced memorization gap.

## Why it stopped

No-paper useful signal only: the local evidence is direct for the synthetic tiny-pretraining proxy but does not validate real-corpus transformer pretraining.

## Recommended next action

Run a bounded deepen follow-up on a real small corpus with a GPT-2-small-class tokenizer/model and the same MinHash threshold grid before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus MinHash threshold sweep with tiny transformer pretraining
- Success threshold: At least one threshold reduces memorization exposure by 5% or more versus no dedup while keeping validation perplexity within 2% of the best non-control condition across at least three seeds.
- Stop condition: Stop if no threshold improves memorization exposure without validation perplexity regression, or if real-corpus setup cannot complete a three-seed threshold grid within the available local compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-sweep-on-tiny-pretraining-53e2876223d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
