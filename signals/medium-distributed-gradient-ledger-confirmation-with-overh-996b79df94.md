# Medium Distributed Gradient Ledger Confirmation with Overhead and Recovery Metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-distributed-gradient-ledger-confirmation-with-overh-996b79df94`
Run ID: `medium-distributed-gradient-ledger-confirmation-with-overh-996b79df94-20260529T012541046954+0000`

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

- Parent run decision: Fault-Injected Two-Process Gradient Ledger Prototype: enoch://control-plane/projects/fault-injected-two-process-gradient-ledger-prototype-f3c128da2b/runs/fault-injected-two-process-gradient-ledger-prototype-f3c128da2b-20260528T224111014999+0000
- Parent run decision: Ring-Reduce Gradient Ledger for 2-Node Homes: enoch://control-plane/projects/ring-reduce-gradient-ledger-for-2-node-homes-f5d564a0f769/runs/ring-reduce-gradient-ledger-for-2-node-homes-f5d564a0f769-20260528T191204224153+0000

## What looked useful

Medium fixed-seed evidence supports the detection/recovery mechanism but also shows that naive full-gradient hashing dominates runtime overhead. Confirmation logic itself is cheap; ledger materialization/copying is the bottleneck. A stride-10 ablation preserves detection in this injected-fault benchmark while reducing overhead substantially.

## Boundaries and scale limits

Not validated on real torch.distributed processes, multi-node networks, real datasets, replicated consensus ledgers, stealthy/collusive adversaries, delayed gradients, replay attacks, or long training runs. Full-gradient every-step hashing added about 146% overhead; stride-10 ledgering reduced overhead to about 36-38% for confirm/recover but weakens full coverage.

## Claim scope

In a single-process CUDA PyTorch simulation of 4-worker data-parallel SGD on a synthetic teacher classification task, a gradient ledger with synchronous confirmation detected all injected 100x worker-gradient corruptions at zero-step latency and prevented corrupted updates; hash-only ledgering recorded but did not prevent corruption.

## Why it stopped

Tier 2 medium confirmation completed, but evidence remains a bounded synthetic/simulated useful signal rather than publication-grade distributed-system validation.

## Recommended next action

Run a local multi-process torch.distributed follow-up with the same metrics, real process failures, and a compressed or sampled ledger design before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process distributed gradient ledger with compressed ledger overhead
- Success threshold: Detection rate 1.0 for injected corruptions, zero bad updates applied by confirm/recover, validation accuracy within 0.5 percentage points of baseline, and clean confirm/recover overhead below 25% versus standard distributed SGD.
- Stop condition: Stop as negative if compressed commitments miss any injected corruption, apply any corrupted update in confirm/recover mode, or exceed 50% overhead without a clear path to below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/medium-distributed-gradient-ledger-confirmation-with-overh-996b79df94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
