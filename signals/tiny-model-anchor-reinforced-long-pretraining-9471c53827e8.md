# Tiny Model Anchor-Reinforced Long Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-model-anchor-reinforced-long-pretraining-9471c53827e8`
Run ID: `tiny-model-anchor-reinforced-long-pretraining-9471c53827e8-20260522T222459985667+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

Anchor reinforcement preserved probability mass for the earlier distribution under synthetic distribution shift, but the effect was partial: cross-entropy retention improved reproducibly while the stronger A top-1 behavior was still forgotten and B adaptation became worse.

## Boundaries and scale limits

Tiny pure-Python bigram model, synthetic Markov data, 5 seeds, 250 A steps and 500 B continuation steps. No transformer, no real corpus, no GPT-2-small-class baseline, no long wall-clock pretraining, and no robustness ablations over anchor size or weight.

## Claim scope

In a 5-seed synthetic tiny bigram language-model proxy with conflicting Markov-chain pretraining phases, fixed A-anchor loss during B continuation reduced final A validation loss by 1.324 nats versus B-only continuation, but increased final B validation loss by 0.176 nats and did not preserve A top-1 transitions.

## Why it stopped

Proxy-only mixed result: anchor loss improved earlier-distribution validation loss but did not preserve top-1 behavior and imposed a measurable new-distribution loss cost, so this is not a full validation of anchor-reinforced long pretraining.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded deepen test should repeat the same protocol with a small transformer and real or semi-real token data before considering any scale-only validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer anchor loss retention under controlled text shift
- Success threshold: Anchor variant improves earlier-distribution loss by at least 10% relative to B-only and preserves a behavior/task metric without increasing new-distribution loss by more than 5%, consistently across seeds.
- Stop condition: Stop if anchor loss fails to improve earlier-distribution loss in at least 2 of 3 seeds or if new-distribution loss cost exceeds 10% at all tested anchor weights.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-model-anchor-reinforced-long-pretraining-9471c53827e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
