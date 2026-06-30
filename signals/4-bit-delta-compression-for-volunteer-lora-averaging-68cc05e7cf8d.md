# 4-bit Delta Compression for Volunteer LoRA Averaging

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-delta-compression-for-volunteer-lora-averaging-68cc05e7cf8d`
Run ID: `4-bit-delta-compression-for-volunteer-lora-averaging-68cc05e7cf8d-20260610T061435978533+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9adcfa60010b

## What looked useful

Across five seeds, fp32 FedAvg LoRA averaged 0.9293 final accuracy; 4-bit delta uploads averaged 0.9298 final accuracy, a +0.0005 mean delta versus fp32 with 0.0011 sd, while reducing payload from 1818624 to 233472 bits per run including scale overhead.

## Boundaries and scale limits

Synthetic data and a tiny frozen linear classifier with LoRA adapters; no real LLM adapters, no real volunteer hardware, no secure aggregation, no adversarial clients, and no large-scale or long-running training.

## Claim scope

In a five-seed synthetic federated LoRA classification probe with 12 non-IID clients, per-tensor symmetric 4-bit compression of client adapter deltas preserved FedAvg LoRA test accuracy while reducing upload payload by 7.79x versus fp32.

## Why it stopped

The local evidence supports the compression mechanism, but it is synthetic/proxy evidence rather than direct LLM volunteer LoRA averaging validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use real small-model LoRA adapters and a public task with a <=0.5 percentage-point degradation threshold versus fp32 FedAvg.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 4-bit delta FedAvg on real small-model LoRA adapters
- Success threshold: Int4 delta compression achieves at least 7x upload reduction and final task metric no worse than 0.5 percentage points below fp32 FedAvg across at least three seeds.
- Stop condition: Stop if int4 is more than 1.0 percentage point worse than fp32 in two independent seeds or if the real-adapter workload cannot run locally within the controller budget.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-delta-compression-for-volunteer-lora-averaging-68cc05e7cf8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
