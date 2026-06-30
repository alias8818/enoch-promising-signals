# DistBin: Home-Distributed 1-Bit Training with Residual Gradient Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distbin-home-distributed-1-bit-training-with-residual-gradient-channels-305177fa1a01`
Run ID: `distbin-home-distributed-1-bit-training-with-residual-gradient-channels-305177fa1a01-20260628T072101945988+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c84415f6acd

## What looked useful

Residual side channels reduce stored quantization residuals and can recover dense-like validation quality in the moderate proxy, but they spend extra bits and are not robustly better than ordinary error-feedback sign updates in the stress proxy.

## Boundaries and scale limits

No transformer, GPT-2-small-class model, real multi-machine transport, asynchronous staleness, home-network latency, energy, or wall-clock distributed throughput was tested. Results are CPU-only NumPy simulations with 12 clients, 256-dimensional logistic regression, 5 seeds, and 300 rounds.

## Claim scope

In a seeded local synthetic non-IID logistic-regression proxy with client dropout, 1-bit error feedback plus a 5% residual side channel can match dense validation metrics in a moderate setting at about 10x fewer transmitted bits, but the advantage does not persist over plain error feedback under harsher heterogeneity and dropout.

## Why it stopped

No-paper useful signal: proxy evidence is mixed and does not directly validate real home-distributed 1-bit model training.

## Recommended next action

Run a bounded deepen follow-up on a small neural network or GPT-2-small-class training task with dense, sign, error-feedback sign, and residual-channel controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural training confirmation for DistBin residual channels
- Success threshold: Residual-channel variant improves validation loss per transmitted bit by at least 10% over ordinary error-feedback sign updates without losing more than 1% absolute validation accuracy versus the best compressed baseline in both regimes.
- Stop condition: Stop if residual channels fail to beat error-feedback sign on loss-per-bit in either regime, or if implementation overhead eliminates the communication advantage.

## Evidence references

- Artifact root: `<local-path>/projects/distbin-home-distributed-1-bit-training-with-residual-gradient-channels-305177fa1a01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
