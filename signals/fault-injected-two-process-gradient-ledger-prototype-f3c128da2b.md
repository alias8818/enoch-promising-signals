# Fault-Injected Two-Process Gradient Ledger Prototype

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `fault-injected-two-process-gradient-ledger-prototype-f3c128da2b`
Run ID: `fault-injected-two-process-gradient-ledger-prototype-f3c128da2b-20260528T224111014999+0000`

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

- Parent run decision: Ring-Reduce Gradient Ledger for 2-Node Homes: enoch://control-plane/projects/ring-reduce-gradient-ledger-for-2-node-homes-f5d564a0f769/runs/ring-reduce-gradient-ledger-for-2-node-homes-f5d564a0f769-20260528T191204224153+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9ad70054129c

## What looked useful

Across three Tier 1 variants, the ledger detected 36/36 injected faults with 0 false positives and final replica L_inf difference 0.0; no-ledger controls diverged for sign-flip and scale faults and became non-finite for NaN faults.

## Boundaries and scale limits

Small synthetic model, one host, one CUDA device, two redundant workers, deterministic identical mini-batches, 80 steps per variant, 36 total injected faults. Not tested on real distributed all-reduce, multi-node links, heterogeneous nondeterminism, process crashes, adversarial workers, larger models, longer runs, or real datasets.

## Claim scope

In a controlled two-process CUDA PyTorch prototype where both workers compute identical deterministic gradients, a parent gradient ledger detected injected post-backward/pre-optimizer sign-flip, scale, and NaN gradient faults, rejected faulty steps, and kept final worker parameters exactly synchronized.

## Why it stopped

Tier 1 direct mechanism threshold was met, but evidence remains a small controlled prototype and is not paper-positive.

## Recommended next action

Run a bounded medium confirmation that integrates the ledger with an explicit all-reduce or distributed optimizer path, measures overhead, and injects the same faults under realistic nondeterminism controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Distributed Gradient Ledger Confirmation with Overhead and Recovery Metrics
- Success threshold: At least 100 injected faults across multiple seeds are all detected, clean-step false positives remain 0, final replicas stay synchronized within L_inf <= 1e-7 after recovery, and median wall-clock overhead is <= 10% versus the clean distributed baseline.
- Stop condition: Stop if clean-step false positives occur under deterministic controls, any injected corruption is accepted, recovery leaves replicas desynchronized above L_inf > 1e-7, or overhead exceeds 25% in the small distributed confirmation.

## Evidence references

- Artifact root: `<local-path>/projects/fault-injected-two-process-gradient-ledger-prototype-f3c128da2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
