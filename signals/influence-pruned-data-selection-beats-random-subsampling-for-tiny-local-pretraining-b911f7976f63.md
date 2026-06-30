# Influence-pruned data selection beats random subsampling for tiny local pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `influence-pruned-data-selection-beats-random-subsampling-for-tiny-local-pretraining-b911f7976f63`
Run ID: `influence-pruned-data-selection-beats-random-subsampling-for-tiny-local-pretraining-b911f7976f63-20260610T034842769983+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7ed16ef07a68

## What looked useful

Influence-top selection chose 67.67 target docs out of 90 on average versus 24.61 for random, reduced mean target test loss from 2.2550 to 2.1394, lowered mean perplexity from 9.5395 to 8.4947, and beat all 18 same-seed random repeats. Oracle target-only loss was 2.1223, so the influence method approached the upper-bound control in this toy setting.

## Boundaries and scale limits

Synthetic corpus only; 3 seeds; small GRU LM; 360 candidate documents per seed; no natural-language corpus, GPT-style transformer, large-scale pretraining, tokenizer effects, or influence-computation cost scaling tested.

## Claim scope

In a controlled synthetic tiny-language-model setup with 25% target-domain Markov documents and 75% distractors, cosine-normalized validation-gradient alignment selected more target documents and achieved lower target test loss than equal-size random subsampling.

## Why it stopped

No-paper closure: this run gives a useful synthetic mechanism signal, but it is not direct natural-language or transformer evidence and cannot validate the broad claim.

## Recommended next action

Run a bounded real-text confirmation on a small corpus mixture with a tiny transformer, comparing influence selection against random and cheap heuristic selectors before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text tiny-transformer confirmation for influence-pruned data selection
- Success threshold: Influence selection improves mean target test loss versus random by at least 0.05 nats/token, beats at least 80% of same-seed random repeats, and does not lose to the cheap heuristic selector by more than 0.02 nats/token.
- Stop condition: Stop as unsupported if influence fails to beat random mean target test loss in at least 4 of 5 seeds or if scoring cost dominates training by more than 5x without a clear quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/influence-pruned-data-selection-beats-random-subsampling-for-tiny-local-pretraining-b911f7976f63`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
