# Gradient Sparsification for Home CPU Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-sparsification-for-home-cpu-distributed-training-55abcb04f104`
Run ID: `gradient-sparsification-for-home-cpu-distributed-training-55abcb04f104-20260529T145223387303+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/18d97d379b2d

## What looked useful

1% top-k error feedback reduced gradient payload by 98% and averaged 1.83x modeled step speedup at 100 Mbps with 1.03x dense final loss; 0.1% sparsity was too aggressive at 2.17x dense loss; 1 Gbps gains were modest because CPU compression overhead dominated.

## Boundaries and scale limits

No real multi-host networking, no packet latency/jitter, no deep model, no production distributed optimizer; model has 20k parameters and three seeds only.

## Claim scope

CPU-only NumPy proxy: synthetic linear regression with four simulated data-parallel workers, measured top-k/error-feedback CPU overhead, and modeled 100 Mbps/1 Gbps communication time.

## Why it stopped

Closed as no-paper useful signal: proxy evidence supports a narrow slow-link mechanism but is not direct/full validation of home CPU distributed training.

## Recommended next action

Run a bounded two-host direct network experiment using a real distributed training loop before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-host home-link gradient sparsification validation
- Success threshold: At 50-100 Mbps, sparse training achieves >=1.4x end-to-end step speedup with final validation loss <=1.05x dense for either 1% or 5% top-k across at least two of three seeds.
- Stop condition: Stop if measured networked sparse runs are <1.2x faster than dense at 100 Mbps or if all sparse settings exceed 1.10x dense validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-sparsification-for-home-cpu-distributed-training-55abcb04f104`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
