# Rolling State Checkpoints

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-state-checkpoints-6b3ee65128e7`
Run ID: `rolling-state-checkpoints-6b3ee65128e7-20260523T224414047551+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/032903e20ec6

## What looked useful

Sparse/partitioned state is the condition where rolling checkpoints are promising: across four runs, sparse rolling used 0.1797x full-checkpoint bytes and 0.2304x mean write time with exact restore equality. Dense rolling used 1.0000x bytes and had 7.7808x restore latency, making it unsuitable as a general full-checkpoint replacement.

## Boundaries and scale limits

No real model training loop, optimizer/scheduler/RNG state, distributed ranks, asynchronous writers, object storage, or failure-injection recovery was tested. The benchmark is local, synthetic, and short.

## Claim scope

In a synthetic single-process PyTorch benchmark with 128 MiB of GPU-resident tensor-shard state, rolling base-plus-delta checkpoints preserve exact restore equality and reduce checkpoint bytes/write time when only 4 of 64 shards change per step, but do not reduce bytes for dense all-shard updates and substantially slow restore.

## Why it stopped

No-paper closure: the local synthetic evidence is useful for mechanism triage but is not direct enough for a paper or broad validation.

## Recommended next action

Run a bounded real-training follow-up on a small transformer or MLP with model, optimizer, scheduler, RNG, and dataloader state plus interrupted-write failure injection; stop if sparse/partitioned savings do not persist with exact restore.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Training Rolling Checkpoint Recovery
- Success threshold: At least 3x lower checkpoint bytes and 2x lower mean write latency versus full checkpoints, exact state equality after clean restore, and deterministic recovery behavior after injected interrupted writes.
- Stop condition: Stop if real workload state is dense-changing enough that rolling checkpoints save less than 2x bytes or if interrupted-write recovery cannot be made deterministic without removing the byte/write advantage.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-state-checkpoints-6b3ee65128e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
