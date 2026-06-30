# Gossip-Averaged Gradients on Local CPU Federation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaged-gradients-on-local-cpu-federation-407e5ded8ea6`
Run ID: `gossip-averaged-gradients-on-local-cpu-federation-407e5ded8ea6-20260525T140751017294+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aea5c8197654

## What looked useful

Multi-step ring gossip recovered all-reduce-like accuracy across heterogeneity settings, but one-step ring gossip degraded loss/consensus badly and local no-communication model averaging was competitive or better on this convex task.

## Boundaries and scale limits

Synthetic convex binary classification only; no real network, no byte-level communication model, no stochastic mini-batch effects, no nonconvex neural network, no asynchronous workers, no privacy/fault-tolerance evaluation, and no production federated deployment.

## Claim scope

On a deterministic local CPU simulation of 8-worker federated logistic regression with synthetic non-IID feature shifts, ring gossip-averaged gradients match all-reduce test loss and accuracy only when using at least two gossip mixing steps per round; one ring step is unstable and produces large model disagreement.

## Why it stopped

Bounded local evidence is mixed: it supports the mechanism only with extra mixing steps, but does not show a practical advantage over simpler baselines on the tested convex CPU-local federation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should move to a nonconvex stochastic federated benchmark and require gossip to beat both all-reduce and local model averaging under matched communication budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Nonconvex Mini-Batch Gossip Gradients Under Matched Communication Budgets
- Success threshold: Gossip must improve validation loss or accuracy by at least 2% relative to local model averaging while using no more communication than all-reduce under the chosen byte/vector-send accounting, with consistent direction across at least 4 of 5 seeds.
- Stop condition: Stop if gossip fails to beat either all-reduce or local model averaging under matched communication budget after the predeclared training budget, or if consensus divergence reproduces the one-step failure seen here.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaged-gradients-on-local-cpu-federation-407e5ded8ea6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
