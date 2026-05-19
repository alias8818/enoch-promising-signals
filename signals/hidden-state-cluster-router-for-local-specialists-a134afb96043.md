# Hidden-State Cluster Router for Local Specialists

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hidden-state-cluster-router-for-local-specialists-a134afb96043`
Run ID: `hidden-state-cluster-router-for-local-specialists-a134afb96043-20260514T171115917295+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa1dbcb12ba5

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy/early falsification: hard hidden-state clusters produced specialists that consistently beat random routing but were consistently worse than a single global linear head on the same frozen LM hidden states and labels.

## Recommended next action

Stop this simple hard-router run as a proxy/early negative; only pursue a bounded residual-or-soft-routing follow-up that must beat the global linear/full-LM baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Soft Hidden-State Router for Local LM Specialists
- Success threshold: Residual or soft hidden-state specialists reduce validation NLL by at least 2% versus the best dense/global baseline at matched active parameters across at least three seeds, while beating random routing.
- Stop condition: Stop if the residual/soft router fails to beat the dense/global baseline in two seeds or if gains disappear under the random-router control.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-cluster-router-for-local-specialists-a134afb96043`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
