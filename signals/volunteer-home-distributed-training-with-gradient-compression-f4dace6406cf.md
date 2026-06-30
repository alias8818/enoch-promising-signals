# Volunteer Home Distributed Training with Gradient Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-home-distributed-training-with-gradient-compression-f4dace6406cf`
Run ID: `volunteer-home-distributed-training-with-gradient-compression-f4dace6406cf-20260610T131529465586+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8545dba6ce37

## What looked useful

Magnitude-aware sparse compression with error feedback was much better than random sparsification at the same payload, and compression quickly hit a latency floor in the volunteer quorum model. Future work should focus as much on straggler/latency scheduling as on byte reduction.

## Boundaries and scale limits

Synthetic data, linear softmax model, simulated network timing, no real multi-host deployment, no secure aggregation, no NAT/churn implementation, no deep neural model, and only three seeds. This does not validate large-scale volunteer training.

## Claim scope

In a local NumPy simulator with 16 non-IID volunteer clients, quorum synchronous aggregation, dropout, and heterogeneous simulated home uplinks, 1% top-k gradient compression with error feedback preserved final softmax-regression accuracy while reducing uploaded gradient bytes about 49x; wall-clock benefit was limited to about 29% by latency/quorum effects.

## Why it stopped

No-paper useful signal: the evidence is a replicated local simulator result, not direct volunteer-home distributed training validation.

## Recommended next action

Run a bounded deepen test with real network emulation and a small neural model, using dense, 1% top-k error feedback, 0.1% top-k error feedback, and sign-scale controls under the same quorum and dropout model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Network-emulated volunteer training with a small neural model
- Success threshold: 1% top-k error feedback achieves at least 98% of dense final accuracy, reduces uploaded gradient bytes by at least 25x, and reports whether measured wall-clock speedup exceeds 1.5x under the chosen network-emulated home profile.
- Stop condition: Stop if 1% top-k error feedback loses more than 2 percentage points of accuracy versus dense in two of three seeds or if measured wall-clock speedup is below 1.1x despite at least 25x byte reduction.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-home-distributed-training-with-gradient-compression-f4dace6406cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
