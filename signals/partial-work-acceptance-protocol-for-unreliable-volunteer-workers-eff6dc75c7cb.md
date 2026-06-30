# Partial work acceptance protocol for unreliable volunteer workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `partial-work-acceptance-protocol-for-unreliable-volunteer-workers-eff6dc75c7cb`
Run ID: `partial-work-acceptance-protocol-for-unreliable-volunteer-workers-eff6dc75c7cb-20260608T021754246009+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4978c02a2ea

## What looked useful

Partial acceptance improved useful efficiency over fixed chunks in all seven synthetic scenarios, from +4.3% in low dropout to +52.5% in high dropout, but it often increased accepted-error rate unless validation sampling was raised.

## Boundaries and scale limits

No real volunteer platform traces, live deployment, adversarial protocol analysis, incentive model, or task-specific validator measurements were tested. The result is bounded to the local simulator and should not be treated as publication-grade evidence.

## Claim scope

Synthetic simulation of unreliable volunteer workers with stochastic dropout, worker quality variation, fatigue errors, validation sampling, and requeueing shows that validated checkpoint-prefix acceptance can improve useful efficiency over fixed chunks under dropout-heavy conditions.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the efficiency mechanism but also shows a correctness tradeoff, so direct trace-driven evidence is required before a paper claim.

## Recommended next action

Run a bounded trace-driven replay with real volunteer dropout/task-duration traces and a measured validator model; stop if partial acceptance does not beat fixed chunks by at least 10% useful efficiency while keeping accepted-error rate within 1 percentage point of fixed chunks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven partial acceptance replay for volunteer computing
- Success threshold: Partial acceptance achieves at least 10% higher useful efficiency than fixed chunks with accepted-error rate no more than 1 percentage point above fixed chunks across the main trace conditions.
- Stop condition: Stop as negative if the efficiency lift is below 10%, the accepted-error gap exceeds 1 percentage point under realistic validation, or the protocol requires validation cost that erases the efficiency gain.

## Evidence references

- Artifact root: `<local-path>/projects/partial-work-acceptance-protocol-for-unreliable-volunteer-workers-eff6dc75c7cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
