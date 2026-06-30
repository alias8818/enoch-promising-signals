# Canary Minibatch Validation of Volunteer LoRA Updates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `canary-minibatch-validation-of-volunteer-lora-updates-988ea318c79b`
Run ID: `canary-minibatch-validation-of-volunteer-lora-updates-988ea318c79b-20260609T055018060142+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c25c585b944b

## What looked useful

Canary minibatch validation is promising as a cheap filter only if canaries are secret, rotating, and large enough. Very small or leaked canaries are unsafe: 32-example canaries accepted 40/40 leaked harmful overfit updates in this proxy.

## Boundaries and scale limits

Not tested on real LLM LoRA fine-tuning, real volunteer data, secure aggregation, or adaptive adversaries against private rotating canaries. The leakage stress used a synthetic known-canary attack and the largest validation set was 4096 synthetic examples.

## Claim scope

In a synthetic rank-4 LoRA volunteer-update classification proxy, sufficiently large secret canary minibatches predicted full validation loss deltas well; 128-example canaries averaged precision 0.992, recall 0.994, and harmful false-accept rate 0.0188, while 256-example canaries had zero false accepts and zero false rejects across 5 seeds.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy: it supports the mechanism under secrecy/size constraints and demonstrates a leakage failure mode, but does not validate real volunteer LLM LoRA updates.

## Recommended next action

Run a bounded direct LoRA test on a small public transformer and dataset with private rotating 128/256-example canaries, multiple disjoint canary batches, and adaptive volunteers who do not receive canary examples.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-transformer validation of secret rotating canary gates for volunteer LoRA updates
- Success threshold: Across at least 3 seeds, 128/256 private rotating canaries achieve precision >= 0.95, recall >= 0.95, harmful false-accept rate <= 0.05, and no systematic pass condition for stale-canary overfit attackers.
- Stop condition: Stop if 128/256 private canaries show harmful false-accept rate > 0.10 in two seeds or if stale-canary attackers reliably pass the current canary while harming full validation.

## Evidence references

- Artifact root: `<local-path>/projects/canary-minibatch-validation-of-volunteer-lora-updates-988ea318c79b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
