# Deterministic Replay Lotteries for Volunteer Gradient Auditing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-replay-lotteries-for-volunteer-gradient-auditing-7dfd689f8b10`
Run ID: `deterministic-replay-lotteries-for-volunteer-gradient-auditing-7dfd689f8b10-20260515T001551285115+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/37d210749f4c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy-only evidence supports post-commit detection but directly falsifies the pre-revealed deterministic variant; no publication-grade full-system validation was produced.

## Recommended next action

Stop this run as a proxy/early falsification of pre-revealed deterministic replay lotteries; run one bounded direct follow-up only if commit-reveal transcript auditing on a real training workload is desired.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-reveal replay lotteries on a real optimizer trace
- Success threshold: At least 90% detection of 2% corrupted steps at <=10% replay overhead, zero honest false positives under the declared numeric tolerance, and replayable gradients across two environments for >=1000 audited steps.
- Stop condition: Stop as negative if deterministic replay fails across environments, honest false positives exceed 0.1%, or detection falls below 90% at <=10% replay overhead.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-lotteries-for-volunteer-gradient-auditing-7dfd689f8b10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
