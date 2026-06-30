# Asynchronous gossip averaging for local CPU federated training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `asynchronous-gossip-averaging-for-local-cpu-federated-training-51caa8358bac`
Run ID: `asynchronous-gossip-averaging-for-local-cpu-federated-training-51caa8358bac-20260529T064833634983+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05ed41879930

## What looked useful

Asynchronous pairwise gossip reduced simulated time in all 30 paired seeds. In high-straggler settings it kept mean accuracy within about 0.11 percentage points of FedAvg while using 9.2% to 11.1% of FedAvg simulated time; the benefit shrank to 81.6% of FedAvg time when straggler variance was low.

## Boundaries and scale limits

No real multi-process or multi-host execution; no measured networking, serialization, process scheduling, or neural-model training overhead; 10 seeds per case on a small synthetic binary classification task.

## Claim scope

Single-process NumPy simulation of 24-client CPU federated logistic regression with non-IID client data and simulated log-normal client compute costs; gossip compared against full-participation synchronous FedAvg at equal local update budget.

## Why it stopped

The evidence supports the mechanism only in a simulator/proxy setting and is insufficient for paper-ready validation.

## Recommended next action

Stop this run as no-paper useful signal; next, implement a bounded multiprocessing CPU prototype that measures real wall-clock and communication overhead on the same task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured multiprocessing CPU gossip versus FedAvg
- Success threshold: Gossip reaches within 1 percentage point of FedAvg final accuracy and improves measured time-to-target by at least 25% in high-straggler runs without losing more than 3 percentage points in low-straggler controls.
- Stop condition: Stop if gossip loses more than 3 percentage points final accuracy or measured overhead makes time-to-target no better than FedAvg in at least 4 of 5 high-straggler seeds.

## Evidence references

- Artifact root: `<local-path>/projects/asynchronous-gossip-averaging-for-local-cpu-federated-training-51caa8358bac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
