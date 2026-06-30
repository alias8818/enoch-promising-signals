# Queue-Depth Adaptive Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `queue-depth-adaptive-speculative-decoding-fa05eaf0068c`
Run ID: `queue-depth-adaptive-speculative-decoding-fa05eaf0068c-20260529T232123405891+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba9392f21335

## What looked useful

Across 15 load/acceptance scenarios and a 46-policy search including 42 queue-threshold/linear adaptive policies, no adaptive policy met the useful-win threshold of at least 5% p95 end-to-end latency improvement within 2% of best fixed-k throughput. The best adaptive p95 delta was only -0.24%, effectively a tie.

## Boundaries and scale limits

No real model, GPU kernel timing, KV-cache pressure, production scheduler, or traffic trace was used. The result is an early synthetic falsification of queue-depth-only control, not a full speculative decoding serving benchmark.

## Claim scope

In a bounded synthetic batched-serving simulator with Poisson arrivals, independent speculative-token acceptance, and calibrated draft/verify cost terms, queue-depth-only adaptive speculative block length did not produce a useful p95 latency improvement over the best fixed-k baseline while preserving throughput.

## Why it stopped

Proxy/early synthetic falsification: queue depth alone did not beat a tuned fixed-k baseline by a useful margin, so the result is not paper-ready and does not justify larger validation as stated.

## Recommended next action

Stop this no-paper line unless a future run tests acceptance-rate-aware or cost-aware adaptation in a real speculative decoding server; do not invest in queue-depth-only adaptation as the primary mechanism.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-adaptive-speculative-decoding-fa05eaf0068c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
