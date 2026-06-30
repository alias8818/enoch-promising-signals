# Evidence-ledger routing for local-serving cascade with queue pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-routing-for-local-serving-cascade-with-queue-pressure-a0c1d0ab7adc`
Run ID: `evidence-ledger-routing-for-local-serving-cascade-with-queue-pressure-a0c1d0ab7adc-20260601T092007354416+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fbcb5243d472

## What looked useful

Queue-pressure routing reduced high-load tail latency and 500 ms SLA misses, but the tested evidence-ledger plus pressure policy failed to preserve the 0.90 target accuracy at 14-18 rps. At 18 rps, ledger_queue with pressure alpha 0.18 improved p95 latency by 19.6% versus static confidence but reduced accuracy from 0.9004 to 0.8865; alpha 0.08 improved p95 by 8.0% but still reached only 0.8948 accuracy.

## Boundaries and scale limits

No live LLMs, real production traces, GPU contention, human labels, or measured model confidence calibration were used. Results should be treated as proxy evidence for routing mechanics only.

## Claim scope

Synthetic discrete-event simulation of a two-tier local-serving cascade with a small first-pass model, two large-model fallback servers, noisy uncertainty evidence, and Poisson arrivals from 6 to 18 rps.

## Why it stopped

Proxy simulation produced a mixed useful signal rather than publication-grade support: queue pressure helps latency, but the tested ledger-pressure rule did not maintain the stated accuracy target.

## Recommended next action

Run a bounded real-trace replay with logged small-model evidence, measured service times, correctness labels, and a constrained threshold optimizer that must maintain the target accuracy floor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay of queue-pressure cascade routing with constrained accuracy floor
- Success threshold: On a held-out trace replay, ledger_queue reduces p95 latency or 500 ms SLA miss rate by at least 10% versus static confidence while keeping accuracy within 0.2 percentage points of the predeclared target floor.
- Stop condition: Stop as a negative result if no pressure-aware policy meeting the accuracy floor improves p95 latency or 500 ms SLA miss rate by at least 5% on the held-out trace.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-routing-for-local-serving-cascade-with-queue-pressure-a0c1d0ab7adc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
