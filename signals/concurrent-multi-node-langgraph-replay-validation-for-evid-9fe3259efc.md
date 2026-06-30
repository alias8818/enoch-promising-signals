# Concurrent multi-node LangGraph replay validation for evidence-ledger mismatch halts

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `concurrent-multi-node-langgraph-replay-validation-for-evid-9fe3259efc`
Run ID: `concurrent-multi-node-langgraph-replay-validation-for-evid-9fe3259efc-20260523T190541163821+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Live LangGraph process-kill replay validation for evidence-ledger mismatch halts: enoch://control-plane/projects/live-langgraph-process-kill-replay-validation-for-evidence-6ba862869f/runs/live-langgraph-process-kill-replay-validation-for-evidence-6ba862869f-20260523T183204835098+0000
- Parent run decision: Persistent-checkpoint replay validation for evidence-ledger tool mismatch halts: enoch://control-plane/projects/persistent-checkpoint-replay-validation-for-evidence-ledge-d2a7b34684/runs/persistent-checkpoint-replay-validation-for-evidence-ledge-d2a7b34684-20260523T182155240236+0000

## What looked useful

Complete evidence records need node identity, sequence, input hash, parent evidence hashes, output, and record hash. Full per-node replay detected 30000/30000 injected faults in the medium run with 0/5000 clean false halts, while no-validation missed 30000/30000 faults, end-only replay detected faults only after all nodes completed, and parent/input hash ablations each missed their targeted 5000/5000 tamper trials.

## Boundaries and scale limits

Not tested on real LangGraph APIs, durable checkpoint stores, multi-process or multi-host deployment, network partitions, production ledgers, or nontrivial workflow corpora. The evidence is synthetic/local and does not satisfy Tier 4 paper-readiness replication.

## Claim scope

In a deterministic local LangGraph-style DAG simulator with concurrent supersteps, fixed seeds, six injected evidence-ledger fault classes, and 231000 total trial rows, full per-node replay validation halted on every injected mismatch with zero clean-run false halts and completed fewer downstream nodes than end-only replay.

## Why it stopped

Mechanism supported only in a local synthetic harness; Tier 4 paper-readiness requires direct real-runtime replication and robustness evidence that this run did not produce.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful signal; do not chain another follow-up from this lineage. A separate future project would need real LangGraph multi-process or multi-host replay with durable ledger/checkpoint-store faults before any paper claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-multi-node-langgraph-replay-validation-for-evid-9fe3259efc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
