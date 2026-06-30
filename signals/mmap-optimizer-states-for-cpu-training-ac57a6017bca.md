# MMAP Optimizer States for CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mmap-optimizer-states-for-cpu-training-ac57a6017bca`
Run ID: `mmap-optimizer-states-for-cpu-training-ac57a6017bca-20260602T162913653867+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a71d140b24df

## What looked useful

mmap optimizer state can make Adam state file-backed and potentially reclaimable, but hot state still remains resident when touched every step. In the medium benchmark, no-flush mmap had similar or better per-step time than RAM blocked updates but paid a 3.34 second final flush; flushing every step slowed mean step time to 2.60 seconds.

## Boundaries and scale limits

This was an isolated optimizer-state placement benchmark, not an end-to-end transformer or GPT-2-small-class training run. It did not test cgroup memory pressure, page reclaim under low MemAvailable, PyTorch AdamW integration, dataloading, checkpoint restore, distributed training, or filesystem variation.

## Claim scope

On a CPU worker, a NumPy Adam update benchmark over 50M float32 parameters showed that mmap-backed first/second moment buffers are mechanically viable and move about 400 MB of hot optimizer state from anonymous RSS into file-backed RSS, with matching convergence on a quadratic objective.

## Why it stopped

No-paper closure: this run provides a direct optimizer-state mechanism signal but only proxy evidence for full CPU training, so it should not be treated as full validation.

## Recommended next action

Run a bounded PyTorch CPU AdamW follow-up under a cgroup memory limit to test whether mmap-backed optimizer state permits a real model that standard in-memory AdamW cannot train without OOM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cgroup-limited PyTorch AdamW mmap-state CPU training test
- Success threshold: mmap-backed AdamW completes at least 200 training steps and reaches the same loss band as standard AdamW when standard AdamW either OOMs under the memory cap or requires at least 25% more memory; throughput penalty should stay below 50% after warmup.
- Stop condition: Stop as negative if standard AdamW fits under the same cap with similar memory, mmap-backed AdamW OOMs, mmap incurs sustained major-fault stalls with more than 50% throughput loss, or loss diverges relative to the standard optimizer.

## Evidence references

- Artifact root: `<local-path>/projects/mmap-optimizer-states-for-cpu-training-ac57a6017bca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
