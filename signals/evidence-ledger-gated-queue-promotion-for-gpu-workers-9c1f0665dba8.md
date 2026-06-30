# Evidence-Ledger-Gated Queue Promotion for GPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-gated-queue-promotion-for-gpu-workers-9c1f0665dba8`
Run ID: `evidence-ledger-gated-queue-promotion-for-gpu-workers-9c1f0665dba8-20260601T103111442634+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/268e803ebadc

## What looked useful

Gated promotion is promising as a waste-reduction mechanism only when ledger evidence is timely and predictive of true job readiness. It should include soft-gate or bypass controls for trusted producers and stale-ledger conditions because pure gating raised mean latency by about 146% in the ledger_lag scenario.

## Boundaries and scale limits

Synthetic scheduler-only evidence; no live GPU jobs, production traces, distributed ledger implementation, multi-node queue, real artifact store, or real container startup failure measurements were tested. The ledger_lag counterexample shows latency harm when evidence trails actual readiness.

## Claim scope

In a deterministic discrete-event simulation of 8 GPU workers, 750 queued jobs per seed, 40 seeds, and synthetic readiness/evidence regimes, evidence-ledger-gated promotion eliminates modeled failed GPU attempts and improves useful simulated GPU-hour throughput when missing ledger evidence correlates with jobs that would fail after occupying GPU setup/runtime.

## Why it stopped

Closed as no-paper useful signal: this run is synthetic/proxy evidence, not direct production or live GPU validation.

## Recommended next action

Run a bounded trace-replay deepen test using real or captured GPU-worker queue events with measured ledger update lag, preflight failure cost, retries, and deadline outcomes before considering any live pilot.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay of evidence-gated GPU queue promotion with ledger-lag controls
- Success threshold: At least 20% reduction in wasted GPU occupancy versus FIFO while p95 latency increases no more than 5% and missed deadlines do not increase by more than 2% on the same trace.
- Stop condition: Stop if trace replay shows less than 10% waste reduction, p95 latency increases above 10%, or ledger timestamps are unavailable and cannot be reconstructed with bounded error.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gated-queue-promotion-for-gpu-workers-9c1f0665dba8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
