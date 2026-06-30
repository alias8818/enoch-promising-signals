# Multi-Task Anchored Replay for Tiny Evidence Ledgers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `multi-task-anchored-replay-for-tiny-evidence-ledgers-697321e510`
Run ID: `multi-task-anchored-replay-for-tiny-evidence-ledgers-697321e510-20260528T125210330528+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-Agent Replay Test for a Tiny Evidence Ledger: enoch://control-plane/projects/real-agent-replay-test-for-a-tiny-evidence-ledger-4003d2786a/runs/real-agent-replay-test-for-a-tiny-evidence-ledger-4003d2786a-20260528T123221801857+0000
- Parent run decision: Tiny Evidence Ledger for Safer Local Tool-Calling Agents: enoch://control-plane/projects/tiny-evidence-ledger-for-safer-local-tool-calling-agents-fbfa21ee327a/runs/tiny-evidence-ledger-for-safer-local-tool-calling-agents-fbfa21ee327a-20260528T120113794662+0000

## What looked useful

Replay improves over no replay and FIFO, but centroid anchored replay does not beat ordinary same-budget stratified or reservoir replay. Anchored final mean accuracy was 0.7818 versus stratified 0.7832, and anchored forgetting was 0.0500 versus stratified 0.0486, missing the preregistered +0.05 accuracy and 20% forgetting-reduction threshold.

## Boundaries and scale limits

Synthetic Gaussian evidence tasks only; no real evidence-ledger corpus, no large language model integration, and no datacenter-scale training. Results should not be generalized beyond same-budget tiny-ledger replay behavior without real-task validation.

## Claim scope

Medium synthetic continual multi-task evidence-ledger benchmark with 10 binary tasks, 80 total ledger slots, 8 fixed seeds, direct final accuracy and forgetting metrics, real FIFO/reservoir/stratified replay baselines, and a random-anchor ablation.

## Why it stopped

Tier-2 medium confirmation directly falsified the stated anchored-replay success threshold on the controlled benchmark; this is a no-paper useful negative signal, not a full real-world validation.

## Recommended next action

Stop this anchored-replay paper path unless future work supplies real evidence-ledger tasks where centroid anchors beat same-budget stratified replay under the same fixed-seed and ablation standard.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-task-anchored-replay-for-tiny-evidence-ledgers-697321e510`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
