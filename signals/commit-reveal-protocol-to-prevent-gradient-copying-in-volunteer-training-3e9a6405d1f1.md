# Commit-Reveal Protocol to Prevent Gradient Copying in Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-protocol-to-prevent-gradient-copying-in-volunteer-training-3e9a6405d1f1`
Run ID: `commit-reveal-protocol-to-prevent-gradient-copying-in-volunteer-training-3e9a6405d1f1-20260521T230934391652+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/54c0cbaef63c

## What looked useful

Commit-reveal reduced same-round copy success from 1.0 in the naive visible-gradient protocol to 0.0, with 0 binding failures when a committed adversary attempted to reveal a copied current gradient. However, stale replay remains a concrete limitation: in a smooth-gradient sweep, previous-round replay reached 0.816 mean cosine to the best current honest gradient and 0.667 mean cosine to the honest mean.

## Boundaries and scale limits

Evidence is local and synthetic: 64-dimensional logistic regression, 8 honest workers, 12 main seeds plus four 8-seed robustness sweeps. It does not include large neural models, real volunteer networking, dropout, collusion, abort-after-reveal griefing, slashing, or production reward accounting.

## Claim scope

In a synthetic federated logistic-regression loop with 8 honest workers and one adversary, SHA-256 commit-before-reveal prevents exact same-round copying of another worker's current gradient under the modeled wait-and-copy attack.

## Why it stopped

Bounded synthetic evidence supports commit-reveal as a same-round copying barrier, but the broader gradient-copy prevention claim is mixed because stale replay can remain effective and real volunteer-training protocol economics were not tested.

## Recommended next action

Stop this run as a no-paper useful signal; a complete protocol should next test stale replay, abort-after-reveal, and reward/slashing rules in an actual federated or volunteer-training implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reward and Slashing Rules for Commit-Reveal Against Stale Replay and Reveal Aborts
- Success threshold: Across at least 10 seeds, same-round copy success remains 0, failed reveals are excluded or penalized, stale/transformed replay earns at least 50% less reward than median honest workers, and final validation loss is within 2% of clean training.
- Stop condition: Stop if stale replay or abort adversaries still earn at least 75% of median honest reward under the best tested freshness/slashing rule, or if the rule increases clean validation loss by more than 2%.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-protocol-to-prevent-gradient-copying-in-volunteer-training-3e9a6405d1f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
