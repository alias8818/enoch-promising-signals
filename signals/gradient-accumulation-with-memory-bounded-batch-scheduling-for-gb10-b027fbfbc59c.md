# Gradient accumulation with memory-bounded batch scheduling for gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-accumulation-with-memory-bounded-batch-scheduling-for-gb10-b027fbfbc59c`
Run ID: `gradient-accumulation-with-memory-bounded-batch-scheduling-for-gb10-b027fbfbc59c-20260614T113359033932+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5687ed737c89

## What looked useful

The useful mechanism is not memory-bounded packing alone. Length-aware bucketing plus memory-bounded microbatch packing can convert variable-length gradient accumulation into fewer microsteps with near-minimal padding and higher GB10 throughput; random-order greedy packing can increase padding and erase the benefit.

## Boundaries and scale limits

Synthetic token data, small 6-layer transformer, padded-token memory proxy rather than online activation-memory estimator, short 2048-sample benchmark, no real corpus, no convergence or validation-quality measurement, no GPT-2-small-class or larger model.

## Claim scope

On a GB10 PyTorch synthetic variable-length causal-LM training probe, random-order greedy memory-bounded gradient-accumulation scheduling was not a robust throughput win, but length-aware memory-bounded scheduling reduced microbatches from 512 to 207 and improved mean throughput by 1.28x versus fixed-count bucketed control at the same padded-token cap.

## Why it stopped

No-paper useful signal: the broad idea is mixed because random memory-bounded scheduling is nearly noise, and the positive result depends on length-aware bucketing in a synthetic short-run benchmark.

## Recommended next action

Run a bounded follow-up using a GPT-2-small-class model on a real variable-length corpus with an activation-memory estimator and convergence checks; do not write a paper from this synthetic scheduling probe.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small memory-bounded length-aware accumulation
- Success threshold: At least 15% mean tokens/sec improvement over fixed-count bucketed control with no OOMs, no material increase in peak memory pressure, and validation loss within 2% of the control over the bounded run.
- Stop condition: Stop if length-aware memory-bounded scheduling improves throughput by less than 10%, causes OOM or earlyoom-risk memory pressure, or worsens validation loss by more than 2% in the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-accumulation-with-memory-bounded-batch-scheduling-for-gb10-b027fbfbc59c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
