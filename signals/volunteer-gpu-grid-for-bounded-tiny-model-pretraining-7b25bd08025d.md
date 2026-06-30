# Volunteer GPU Grid for Bounded Tiny Model Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-gpu-grid-for-bounded-tiny-model-pretraining-7b25bd08025d`
Run ID: `volunteer-gpu-grid-for-bounded-tiny-model-pretraining-7b25bd08025d-20260607T110642239791+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a400e038d654

## What looked useful

Measured tiny-transformer steps were 7.55 ms for 2.6M parameters, 11.00 ms for 13.8M parameters, and 14.41 ms for 33.7M parameters. At 20 Mbps, FP16 upload+download synchronization costs 4.15 s, 22.15 s, and 53.88 s respectively, requiring 549 to 3740 local steps for even 50% communication efficiency and 2196 to 14957 local steps for 80% efficiency.

## Boundaries and scale limits

Direct evidence is single-host GPU throughput plus deterministic communication simulation. It does not include real volunteer nodes, WAN churn, heterogeneous GPUs, optimizer-quality effects from long local-SGD intervals, or full-corpus pretraining.

## Claim scope

On a GB10 synthetic tiny-GPT benchmark, naive coordinator-style volunteer WAN synchronization is communication-dominated for 3M to 35M parameter models over residential-class 20 Mbps links unless workers perform hundreds to tens of thousands of local steps between synchronization rounds.

## Why it stopped

Proxy early falsification of frequent-synchronization volunteer pretraining: communication dominates measured tiny-model compute at residential WAN bandwidth, but full validation would require multi-worker optimization-quality and real-WAN evidence.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is a local-SGD quality experiment at k=512, 2048, and 8192 steps against a same-token serial baseline before any real volunteer deployment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Local-SGD Quality Threshold for Volunteer Tiny-GPT Pretraining
- Success threshold: At least one local-SGD interval that is communication-efficient at 20 Mbps must stay within 5% validation loss of the serial baseline at matched token budget while improving simulated wall-clock throughput by at least 2x.
- Stop condition: Stop if all communication-efficient intervals exceed 5% validation-loss degradation or fail to improve simulated wall-clock throughput by 2x at matched token budget.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-gpu-grid-for-bounded-tiny-model-pretraining-7b25bd08025d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
