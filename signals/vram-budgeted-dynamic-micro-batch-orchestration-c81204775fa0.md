# VRAM-Budgeted Dynamic Micro-Batch Orchestration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `vram-budgeted-dynamic-micro-batch-orchestration-c81204775fa0`
Run ID: `vram-budgeted-dynamic-micro-batch-orchestration-c81204775fa0-20260601T095031931507+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e1263501b224

## What looked useful

Dynamic scheduling reduced micro-batch count from 192 to 130 and improved true-token throughput from 29,682.68 to 38,585.56 tokens/s with peak torch allocation 767.53 MB against a 766.31 MB calibrated budget, but padding overhead increased from 44.76% to 54.68%.

## Boundaries and scale limits

Synthetic random-token stream, small encoder model, single GPU, artificial sub-GB memory budget, no real corpus, no GPT-2-small-class decoder baseline, no length-aware buffering baseline, and no long-horizon quality or distributed-training validation.

## Claim scope

On a single GB10 GPU with a small synthetic bf16 Transformer training workload of 384 variable-length samples, a calibrated dynamic micro-batch scheduler improved useful-token throughput by 30.0% versus a fixed worst-case micro-batch while staying near the calibrated memory budget and avoiding OOM.

## Why it stopped

No-paper useful signal: the mechanism worked on a narrow synthetic CUDA benchmark, but the evidence is not broad or direct enough for publication-grade validation.

## Recommended next action

Run a bounded deepen test with GPT-2-small-class decoder training semantics, gradient accumulation, and a length-aware buffered dynamic scheduler baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-Aware VRAM-Budgeted Micro-Batching for GPT-2-Small-Class Training
- Success threshold: Length-aware dynamic scheduling achieves at least 20% higher true-token throughput than fixed worst-case batching, does not increase padding overhead versus fixed by more than 5 percentage points, stays within 5% of calibrated peak memory budget, and shows no worse short-run validation loss trend.
- Stop condition: Stop as negative if the length-aware scheduler fails to beat fixed batching by 10% true-token throughput or cannot stay within 10% of the calibrated memory budget without OOM on two attempted calibrations.

## Evidence references

- Artifact root: `<local-path>/projects/vram-budgeted-dynamic-micro-batch-orchestration-c81204775fa0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
