# Gradient Residual Channels for Home Distributed Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-residual-channels-for-home-distributed-training-553cef7e50ae`
Run ID: `gradient-residual-channels-for-home-distributed-training-553cef7e50ae-20260604T094419046350+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f397d98905f

## What looked useful

At 1% top-k compression, residual top-k sent the same 2,695,680 bytes as no-residual top-k and improved mean final validation loss from 1.7435 to 1.5900 and mean validation accuracy from 0.3953 to 0.4513 across three seeds; the loss improvement held in every seed.

## Boundaries and scale limits

Tested only a small synthetic teacher-generated classification task, one MLP size, four simulated workers, three seeds, 240 steps, synchronous aggregation, and a byte-budget proxy. Did not test real residential WAN latency, packet loss, asynchronous stragglers, non-IID household data, optimizer-state interactions, real datasets, or LLM-scale training.

## Claim scope

In a deterministic synthetic synchronous multi-worker PyTorch training proxy, top-k gradient compression with per-worker residual/error-feedback buffers improves validation loss and accuracy versus top-k dropping at identical transmitted bytes, while using about 2% of dense-gradient bytes.

## Why it stopped

Closed as a no-paper useful signal because this was a synthetic proxy mechanism test, not a full validation of home distributed training.

## Recommended next action

Run a bounded WAN-emulated multi-process follow-up with non-IID data partitions, explicit bandwidth/latency limits, and stronger error-feedback SGD baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: WAN-emulated gradient residual channels under non-IID worker data
- Success threshold: At matched transmitted bytes, residual channels improve final validation loss by at least 5% versus top-k dropping in at least two of three seeds and do not lose more than 10% wall-clock-normalized progress versus dense under the emulated link budget.
- Stop condition: Stop if residual channels fail to beat top-k dropping on validation loss in at least two of three seeds or if residual norms grow monotonically without improving validation quality.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-residual-channels-for-home-distributed-training-553cef7e50ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
