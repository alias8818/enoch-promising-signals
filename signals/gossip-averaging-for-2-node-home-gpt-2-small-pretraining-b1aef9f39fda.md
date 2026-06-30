# Gossip averaging for 2-node home GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaging-for-2-node-home-gpt-2-small-pretraining-b1aef9f39fda`
Run ID: `gossip-averaging-for-2-node-home-gpt-2-small-pretraining-b1aef9f39fda-20260608T145401731405+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5936459271af

## What looked useful

Periodic averaging is feasible and cadence matters: interval-8 gossip improved validation loss by 0.2322 absolute / 6.13% relative over late-only averaging on the direct control, but averaged 0.3484 absolute / 10.86% worse validation loss than centralized training across three seeds.

## Boundaries and scale limits

Learning comparison used synthetic data, a much smaller model than GPT-2-small, one-process local simulation rather than real two-node networking, parameter-only averaging without optimizer-state averaging, and 160-step runs. GPT-2-small-shape evidence was only a two-step reduced-vocabulary feasibility probe.

## Claim scope

On a GB10 local GPU simulation with a 3.49M-parameter GPT-2-style model and synthetic autoregressive token streams, two-replica parameter gossip averaging every 8 local steps learns substantially better than late-only averaging but remains worse than an equal-token centralized baseline after 160 steps.

## Why it stopped

Bounded local evidence supports the gossip mechanism versus late averaging but does not support a paper-level or full GPT-2-small pretraining claim, because the main result is synthetic, short-run, smaller than GPT-2-small, and worse than the centralized baseline.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use real text tokenization and a GPT-2-small-class/full-vocabulary model with measured two-node communication overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text two-node GPT-2-small-class gossip averaging cadence study
- Success threshold: A gossip interval achieves validation loss within 3% of the centralized equal-token baseline while reducing synchronization events by at least 4x and maintaining better wall-clock progress than every-step averaging under measured network constraints.
- Stop condition: Stop if all gossip intervals remain more than 8% worse than centralized validation loss after the planned token budget or if measured communication overhead makes wall-clock progress slower than centralized/synchronous alternatives.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaging-for-2-node-home-gpt-2-small-pretraining-b1aef9f39fda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
