# Verifiable loss sampling for cheating-resistant volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verifiable-loss-sampling-for-cheating-resistant-volunteer-training-0eb973184242`
Run ID: `verifiable-loss-sampling-for-cheating-resistant-volunteer-training-0eb973184242-20260609T040305196193+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

Loss sampling is useful as an audit primitive for fabricated scalar loss reports, but it is not sufficient as a standalone cheating-resistant volunteer-training protocol because honest reported losses can coexist with harmful updates.

## Boundaries and scale limits

Toy/synthetic CPU-only evidence only. No real LLM training, real volunteer network, checkpoint commitment protocol, nondeterministic kernel handling, privacy mechanism, Sybil resistance, gradient verification, or robust aggregation was tested.

## Claim scope

In a synthetic 500-step worker model where scalar loss reports are committed before verifier-selected deterministic batch audits, verifiable loss sampling detects fabricated loss reports with probability matching 1 - (1 - audit_rate * cheat_event_rate)^steps; at 5% audits and 10% cheat-event rate detection was 0.922 over 1,000 trials.

## Why it stopped

Bounded synthetic evidence supports the audit mechanism for loss-report fabrication but also directly falsifies the stronger standalone cheating-resistance claim via an update-poisoning negative control.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add update-integrity checks around a real small-model training loop rather than scaling this loss-only simulation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model verifiable loss sampling with update-integrity checks
- Success threshold: On a small real model, maintain false positives below 1%, detect at least 90% of frequent fabricated-report adversaries, and reduce poisoned-update final validation-loss degradation by at least 50% versus loss-only auditing at comparable audit overhead.
- Stop condition: Stop if deterministic verifier recomputation cannot be made reliable for the chosen model/data path, or if update-integrity additions fail to reduce poisoned-update degradation by at least 25% in a smoke-scale real training run.

## Evidence references

- Artifact root: `<local-path>/projects/verifiable-loss-sampling-for-cheating-resistant-volunteer-training-0eb973184242`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
