# Bounded public-dataset DDP ledger overhead and payload ablation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-public-dataset-ddp-ledger-overhead-and-payload-abl-b14c9e6450`
Run ID: `bounded-public-dataset-ddp-ledger-overhead-and-payload-abl-b14c9e6450-20260613T135800757517+0000`

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

- Parent run decision: Evidence Ledger on Real Small Distributed Training: enoch://control-plane/projects/evidence-ledger-on-real-small-distributed-training-9bd5ab86e7/runs/evidence-ledger-on-real-small-distributed-training-9bd5ab86e7-20260613T134250702225+0000
- Parent run decision: Evidence Ledger for Volunteer/Home Distributed Training: enoch://control-plane/projects/evidence-ledger-for-volunteer-home-distributed-training-88f5aa11beb4/runs/evidence-ledger-for-volunteer-home-distributed-training-88f5aa11beb4-20260613T132427477411+0000

## What looked useful

Across three fixed seeds in the longer confirmation run, metadata-only ledger overhead averaged 4.82% with high noise, local hash payload variants averaged -0.64% to -1.06% overhead, and all_gather_object payload variants averaged about 45.8% step-time overhead with about 29.8% throughput loss. Validation accuracy was unchanged at 0.9811 mean across variants.

## Boundaries and scale limits

Tested only MNIST, a small ConvNet, one host, two CPU/Gloo ranks, payloads up to 64 KiB, and synchronous per-step ledger operations. Did not test multi-GPU NCCL, multi-node networking, large models, durable ledger storage, asynchronous writers, or payloads above 64 KiB.

## Claim scope

On single-host two-process CPU/Gloo PyTorch DDP training over MNIST, local per-step ledger metadata and local deterministic payload hashing up to 64 KiB are near baseline, but naive per-step distributed object gathering of ledger payloads adds large overhead.

## Why it stopped

Tier-2 local evidence supports a mechanism-level warning but not publication readiness because DDP was limited to single-host CPU/Gloo and did not cover multi-GPU or multi-node production conditions.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace per-step all_gather_object with tensor all_gather and batched/asynchronous ledger commits to determine whether the distributed ledger overhead can be reduced below 10%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: DDP ledger batching and tensor-collective overhead reduction
- Success threshold: At least one distributed ledger payload variant must keep mean step-time overhead below 10% versus same-seed baseline across all three seeds while preserving validation accuracy within 0.2 percentage points.
- Stop condition: Stop if tensor/batched variants still exceed 10% mean overhead or if reduced overhead only appears by dropping distributed payload synchronization.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-public-dataset-ddp-ledger-overhead-and-payload-abl-b14c9e6450`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
