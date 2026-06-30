# Gradient accumulation with optimizer state eviction between steps

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-accumulation-with-optimizer-state-eviction-between-steps-0c7d9d25a649`
Run ID: `gradient-accumulation-with-optimizer-state-eviction-between-steps-0c7d9d25a649-20260525T090311107900+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/de2d5cca39c6

## What looked useful

The mechanism works in the scoped probe: optimizer state is unnecessary during accumulation windows and can be freed without changing the tested Adam update. The naive synchronous file-backed implementation is too slow for a paper claim, with 2.66x total slowdown and 6.30x optimizer-step slowdown.

## Boundaries and scale limits

Synthetic CPU benchmark only; no real model convergence, PyTorch allocator behavior, GPU memory pressure, async transfer overlap, distributed sharding, or comparison to ZeRO/FSDP optimizer offload was tested.

## Claim scope

In a deterministic single-process C benchmark with 25M float parameters, three Adam-style optimizer steps, and four gradient-accumulation microsteps per step, evicting Adam first/second moment state between optimizer steps preserved the final parameter digest and reduced accumulation-window RSS by 49.7%, but did not reduce optimizer-step peak RSS.

## Why it stopped

Bounded direct mechanism evidence is positive, but publication-grade evidence is absent and the naive synchronous eviction path has substantial I/O overhead.

## Recommended next action

Stop this run as no-paper useful signal; a separate deepen test should implement asynchronous prefetch/re-eviction in a real PyTorch training loop and compare against optimizer-offload baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Async optimizer-state eviction in a real PyTorch gradient-accumulation loop
- Success threshold: At least 40% reduction in accumulation-window accelerator memory with final loss within 1% of baseline and throughput no worse than 15% below resident-state or optimizer-offload baseline.
- Stop condition: Stop if async eviction remains more than 25% slower than the best standard baseline or if memory savings disappear once real framework allocator and step peak are measured.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-accumulation-with-optimizer-state-eviction-between-steps-0c7d9d25a649`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
