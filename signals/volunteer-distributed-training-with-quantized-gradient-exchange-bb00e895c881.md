# Volunteer Distributed Training with Quantized Gradient Exchange

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-distributed-training-with-quantized-gradient-exchange-bb00e895c881`
Run ID: `volunteer-distributed-training-with-quantized-gradient-exchange-bb00e895c881-20260609T010617834648+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1df1b8106c17

## What looked useful

Across five-seed medium and stress probes, q4 quantized gradient exchange retained fp32-level convergence with about 7.5x byte reduction. The stress probe also found a practical boundary: the implemented 2-bit stochastic symmetric quantizer with error feedback degraded badly under heavier heterogeneity/dropout, while 1-bit sign-with-scale remained close in this logistic setup but should not be generalized without deeper tests.

## Boundaries and scale limits

No real volunteer network, asynchronous stale-gradient execution, adversarial clients, deep model, transformer, optimizer-state exchange, checkpoint/restart, or datacenter-scale training was tested.

## Claim scope

Synthetic non-IID logistic distributed training with stochastic worker dropout: 4-bit quantized gradient exchange matched fp32 final loss/accuracy within observed seed noise while reducing communicated gradient bytes by about 7.5x.

## Why it stopped

No-paper useful signal: evidence is synthetic/logistic and proxy-only for real volunteer distributed training, though it directly supports a bounded 4-bit gradient-exchange mechanism and identifies a 2-bit failure boundary.

## Recommended next action

Run a bounded real-dataset neural benchmark with asynchronous worker delay modeling before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Dataset Async Quantized Gradient Exchange Probe
- Success threshold: q4 with error feedback achieves final validation accuracy within 1 percentage point or loss within 0.01 absolute of fp32 while reducing communicated gradient bytes by at least 4x under asynchronous dropout/staleness.
- Stop condition: Stop if q4 loses more than 2 percentage points of validation accuracy versus fp32 in two consecutive seeds, diverges under the async schedule, or the implementation cannot produce a direct real-dataset baseline within the local compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-with-quantized-gradient-exchange-bb00e895c881`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
