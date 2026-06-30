# Residual Gradient Channels for 1-Bit Home Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-gradient-channels-for-1-bit-home-distributed-training-fc5605a1595e`
Run ID: `residual-gradient-channels-for-1-bit-home-distributed-training-fc5605a1595e-20260527T171243983449+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe6b5049c075

## What looked useful

Residual sign channels are worth one bounded direct follow-up because they consistently repaired plain sign compression in 300-step 3-seed proxy runs, including an interval-8 variant at about 1.124 bits/parameter/step. The practical advantage over error feedback remains uncertain.

## Boundaries and scale limits

Synthetic teacher classification only; simulated workers in one process; no real network, no multi-host execution, no real dataset, no large model, no long-horizon training.

## Claim scope

On a deterministic 4-worker synthetic non-IID MLP training proxy, a periodic residual 1-bit sign correction channel closed the plain scaled-sign loss gap versus dense gradients at 1.12-1.25 bits/parameter/step, but only slightly outperformed standard 1-bit error feedback.

## Why it stopped

Proxy evidence supports the mechanism but is not full validation and does not yet establish a strong advantage over the standard error-feedback baseline.

## Recommended next action

Stop this run as no-paper useful-signal evidence; run one bounded real-data distributed-process follow-up that compares RGC against tuned error feedback at matched communication and wall-clock budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual sign channels on a real small-model distributed benchmark
- Success threshold: RGC must beat tuned EF-sign by at least 2% relative validation loss or reach the same target at least 10% faster wall-clock while using no more than 1.25x EF-sign communication, across at least 3 seeds.
- Stop condition: Stop if RGC does not beat tuned EF-sign under matched communication on the first real-data benchmark or if network overhead removes any time-to-target gain.

## Evidence references

- Artifact root: `<local-path>/projects/residual-gradient-channels-for-1-bit-home-distributed-training-fc5605a1595e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
