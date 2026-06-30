# Federated Residual Averaging for Home Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `federated-residual-averaging-for-home-volunteer-training-9ec50d8c7bfd`
Run ID: `federated-residual-averaging-for-home-volunteer-training-9ec50d8c7bfd-20260528T142303842731+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9eafc81d5e7c

## What looked useful

Across 10 seeds, residual top-k beat naive top-k at equal upload bytes by +1.71 accuracy points at 5% top-k/35% dropout, +4.31 points at 1% top-k/35% dropout, and +2.84 points at 1% top-k/60% dropout; dense FedAvg still had the highest accuracy in the harsher sparse settings.

## Boundaries and scale limits

Proxy-only evidence: no deep model, no language-model-scale baseline, no real home-device traces, no WAN/secure aggregation protocol, no adversarial or privacy evaluation, and byte accounting is modeled rather than implemented as a network protocol.

## Claim scope

Small-scale CPU simulation on sklearn digits with 20 non-IID clients, intermittent participation, and logistic regression shows that top-k federated residual averaging improves final accuracy and convergence over naive top-k compressed FedAvg at identical sparse upload byte budgets.

## Why it stopped

Closed as no-paper useful-signal evidence because the result is a controlled local proxy, not full home volunteer training validation.

## Recommended next action

Run a bounded deepen follow-up on a small non-convex neural model with realistic bandwidth/availability traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Compressed FedAvg on Small Non-Convex Models with Volunteer Availability Traces
- Success threshold: Residual compressed FedAvg beats naive compressed FedAvg by at least 2 accuracy points or equivalent task metric at the same byte budget in at least 2 tasks, while staying within 2 points of dense FedAvg on one task and showing bounded residual norms.
- Stop condition: Stop if residual compression fails to beat naive compression on final metric in 2 consecutive non-convex tasks or if residual norms grow without convergence improvement.

## Evidence references

- Artifact root: `<local-path>/projects/federated-residual-averaging-for-home-volunteer-training-9ec50d8c7bfd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
