# Delayed-Gradient Home Distributed Training Toy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `delayed-gradient-home-distributed-training-toy-b24e9a5243d6`
Run ID: `delayed-gradient-home-distributed-training-toy-b24e9a5243d6-20260529T030903470864+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84537678186a

## What looked useful

The toy mechanism is plausible for tens of queued stale updates, but the benefit depends on a real pipeline achieving enough in-flight work to hide 10-100 ms latencies. Very large staleness is harmful on validation loss even in the convex proxy.

## Boundaries and scale limits

No real multi-host networking, straggler behavior, transformer/GPT-2-class model, heterogeneous home devices, or measured distributed-system throughput was tested. The throughput result is a latency-hiding model using measured local gradient time, not an end-to-end distributed benchmark.

## Claim scope

On a local synthetic convex logistic-regression proxy, delayed-gradient SGD with tuned learning rate preserved validation loss within 0.6% of synchronous SGD for delays up to 64 queued updates across 8 seeds; delays of 128 and 256 showed clear validation-loss degradation in a stress sweep.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/local and supports only a proxy mechanism, not full home-distributed training viability.

## Recommended next action

Run a bounded local multi-process parameter-server test with injected 10-100 ms latency and heterogeneous worker speeds, comparing synchronous and delayed modes at matched update and wall-clock budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured local parameter-server delayed-gradient simulation
- Success threshold: Delayed mode achieves at least 2x measured wall-clock update throughput over synchronous mode at 50 ms injected latency while final validation loss is no more than 2% worse than synchronous at the same update budget.
- Stop condition: Stop if measured delayed throughput is below 1.5x synchronous at 50 ms latency or if validation loss is more than 5% worse than synchronous for all delays tested.

## Evidence references

- Artifact root: `<local-path>/projects/delayed-gradient-home-distributed-training-toy-b24e9a5243d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
