# Loss-trajectory curriculum for tiny model pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `loss-trajectory-curriculum-for-tiny-model-pretraining-24dbf38a6a76`
Run ID: `loss-trajectory-curriculum-for-tiny-model-pretraining-24dbf38a6a76-20260527T175410761417+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1399af805d1d

## What looked useful

Per-example loss trajectories were measurable and heterogeneous, but using them for naive biased sampling hurt validation NLL. Random reached 2.7551 mean final validation NLL; the best trajectory curriculum, drop_then_hard, reached 2.8282 (+0.0730 worse), and every tested trajectory curriculum was worse than random in every seed.

## Boundaries and scale limits

Tested a one-hidden-layer character LM with 10,000 train examples, 2,000 validation examples, 3 seeds, 180-step probe trajectories, and 450-step final training. Did not test transformer LMs, tokenized web corpora, epoch-balanced curricula, or long-horizon pretraining.

## Claim scope

A bounded NumPy tiny character-LM pretraining probe on Tiny Shakespeare found that four naive loss-trajectory-derived sampling curricula underperformed matched random sampling after the same update and batch budget.

## Why it stopped

Proxy/direct-small early falsification: the tested tiny LM pretraining mechanism consistently degraded validation NLL versus random, so larger validation is not justified for the naive scheduler.

## Recommended next action

Stop this naive loss-trajectory sampling line as an early negative; only revisit with an epoch-balanced transformer LM curriculum that preserves coverage while using trajectory scores.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/loss-trajectory-curriculum-for-tiny-model-pretraining-24dbf38a6a76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
