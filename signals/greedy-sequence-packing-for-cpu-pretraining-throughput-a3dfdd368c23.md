# Greedy sequence packing for CPU pretraining throughput

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `greedy-sequence-packing-for-cpu-pretraining-throughput-a3dfdd368c23`
Run ID: `greedy-sequence-packing-for-cpu-pretraining-throughput-a3dfdd368c23-20260614T000331981166+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/673e4bee7fe3

## What looked useful

Streaming greedy reduced blocks by 81.53% on short_web and 60.63% on mixed_web, with estimated total speedups of 5.41x and 2.54x. On near_full sequences it reduced zero blocks; offline first-fit decreasing was slower after packing overhead.

## Boundaries and scale limits

Synthetic length distributions and a NumPy fixed-block CPU kernel proxy only; no real transformer pretraining loop, dataloader-worker measurement, attention-boundary semantics test, optimizer overhead, or model-quality validation.

## Claim scope

In a synthetic 512-token CPU proxy benchmark, order-preserving streaming greedy sequence packing materially reduces fixed-block compute for short and mixed-length document distributions, but provides no benefit when examples are already near the target block size.

## Why it stopped

This run produced a useful synthetic/proxy mechanism test and an early boundary condition, but not direct full pretraining evidence or paper-ready validation.

## Recommended next action

Run a bounded real CPU transformer pretraining comparison with matched real tokens, packed versus unpacked dataloaders, and explicit EOS or attention-boundary semantics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU transformer pretraining loop for streaming greedy sequence packing
- Success threshold: At least 1.5x real-token throughput improvement on a short or mixed-length corpus with no material loss degradation over a bounded run.
- Stop condition: Stop if packed throughput is below 1.2x baseline, if packing overhead dominates, or if boundary semantics make the comparison invalid.

## Evidence references

- Artifact root: `<local-path>/projects/greedy-sequence-packing-for-cpu-pretraining-throughput-a3dfdd368c23`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
