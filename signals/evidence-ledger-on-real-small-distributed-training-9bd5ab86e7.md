# Evidence Ledger on Real Small Distributed Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-on-real-small-distributed-training-9bd5ab86e7`
Run ID: `evidence-ledger-on-real-small-distributed-training-9bd5ab86e7-20260613T134250702225+0000`

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

- Parent run decision: Evidence Ledger for Volunteer/Home Distributed Training: enoch://control-plane/projects/evidence-ledger-for-volunteer-home-distributed-training-88f5aa11beb4/runs/evidence-ledger-for-volunteer-home-distributed-training-88f5aa11beb4-20260613T132427477411+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0fcb32ee4097

## What looked useful

Across three paired baseline/ledger seeds, every ledger chain validated, final parameters stayed synchronized across ranks, and ledger mode had identical average loss to baseline with mean runtime overhead of 30.66% and max overhead of 35.34%.

## Boundaries and scale limits

Tested only on one host, two CPU/Gloo ranks, a small MLP, synthetic data, three measured seeds, and 96 optimization steps per rank per measured run. Not tested on public datasets, multi-GPU NCCL, multi-node failures, restart recovery, or transformer-scale training.

## Claim scope

A local two-process PyTorch 2.12 Gloo DistributedDataParallel training loop can emit per-rank hash-chained evidence records while preserving matched-seed training loss and final rank parameter synchronization on a small deterministic classification task.

## Why it stopped

Tier 1 direct small distributed training supports the mechanism but is too small, synthetic, and CPU/Gloo-bound for paper readiness; the result is useful no-paper evidence rather than full validation.

## Recommended next action

Run a bounded deepen follow-up on a public dataset with at least 1,000 DDP optimization steps and ledger payload ablations; stop paper consideration unless ledger validity remains perfect and overhead drops below 10% or is justified by audit requirements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded public-dataset DDP ledger overhead and payload ablation
- Success threshold: All ledger chains validate, all ranks end with matching parameter hashes, loss or accuracy remains within 1% relative of baseline, and at least one reduced-payload ledger variant has mean overhead below 10% over three paired seeds.
- Stop condition: Stop if any ledger chain fails validation, ranks desynchronize, training behavior diverges by more than 1% relative from baseline, or all ledger variants exceed 20% overhead.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-on-real-small-distributed-training-9bd5ab86e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
