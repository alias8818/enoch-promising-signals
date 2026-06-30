# Memory-Mapped Adam States for Out-of-Core Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-mapped-adam-states-for-out-of-core-training-b439252226cb`
Run ID: `memory-mapped-adam-states-for-out-of-core-training-b439252226cb-20260524T171218037546+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7fced0aef310

## What looked useful

Plain mmap preserves Adam update semantics but does not by itself reduce RSS for dense updates because every touched state page becomes resident. Chunked mmap with msync and MADV_DONTNEED kept post-allocation VmRSS growth near 192 KiB for a 512 MiB state proxy, but slowed throughput from 106.629M element-updates/s for RAM to 26.613M element-updates/s.

## Boundaries and scale limits

No end-to-end neural network training, no GPU overlap, no autograd integration, no distributed optimizer, no checkpoint/restart validation, and maximum tested optimizer-state size was 512 MiB over 67,108,864 elements.

## Claim scope

Mechanism-level CPU proxy for float32 dense Adam updates with optimizer first/second moments stored in file-backed memory maps. Correctness matched heap-backed Adam in the tested smoke run, and explicit chunk flush plus MADV_DONTNEED reduced resident optimizer-state growth in bounded local runs.

## Why it stopped

Bounded CPU proxy supports the mechanism only with explicit eviction and shows a large throughput cost; it is not full validation of out-of-core training.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate chunked mmap Adam state into an actual small training loop and require convergence parity plus explicit wall-clock/RSS tradeoff versus standard Adam.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-integrated chunked mmap AdamW on a small real training task
- Success threshold: Final validation loss within 1% of standard AdamW, resident optimizer-state memory at least 50% lower than baseline after warmup, and wall-clock slowdown no worse than 2x on the tested small task.
- Stop condition: Stop as negative if convergence diverges, restart cannot reproduce optimizer state, or the slowdown exceeds 2x while memory reduction is below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-adam-states-for-out-of-core-training-b439252226cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
