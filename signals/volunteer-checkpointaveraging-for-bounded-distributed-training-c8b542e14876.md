# Volunteer checkpointaveraging for bounded distributed training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `volunteer-checkpointaveraging-for-bounded-distributed-training-c8b542e14876`
Run ID: `volunteer-checkpointaveraging-for-bounded-distributed-training-c8b542e14876-20260611T091650713120+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/79b0409ff79c

## What looked useful

Normal-delay volunteer averaging reached about 0.77 validation accuracy versus about 0.88 for centralized SGD and synchronous FedAvg. Heavy-delay strict bounded averaging rejected most checkpoints and collapsed to about 0.53 accuracy, while unbounded slow averaging reached about 0.67 but still trailed controls by about 21 points. Hard staleness bounds trade stale-update risk for update starvation.

## Boundaries and scale limits

Synthetic binary classification only; no real volunteer network, no large model, no checkpoint transfer overhead measurement, no adversarial or incentive setting, and no distributed wall-clock throughput validation.

## Claim scope

In a local synthetic non-IID MLP simulator with 24 volunteer shards, 5 seeds, and 80 rounds, simple asynchronous volunteer checkpoint averaging with hard staleness bounds learns above chance only when enough checkpoints are accepted, but remains materially below centralized SGD and synchronous FedAvg controls.

## Why it stopped

Proxy/local simulator early falsification: simple bounded checkpoint averaging was operational but not close to synchronous or centralized controls, and strict bounds failed under slow volunteer returns.

## Recommended next action

Stop this simple hard-bound formulation as no-paper evidence; the bounded next test is adaptive staleness weighting with a minimum accepted-update budget, compared against the same FedAvg and centralized controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive staleness weighting for volunteer checkpoint averaging
- Success threshold: Adaptive weighting beats hard bound-2 by at least 5 absolute validation-accuracy points in slow-delay conditions and is within 5 points of synchronous FedAvg in normal-delay conditions without increasing variance across seeds.
- Stop condition: Stop if adaptive weighting remains more than 10 accuracy points behind synchronous FedAvg in normal-delay conditions or fails to beat hard bound-2 in slow-delay conditions.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-checkpointaveraging-for-bounded-distributed-training-c8b542e14876`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
