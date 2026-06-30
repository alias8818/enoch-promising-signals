# Gradient checkpointing granularity vs throughput on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-checkpointing-granularity-vs-throughput-on-cpu-d76fb8da565d`
Run ID: `gradient-checkpointing-granularity-vs-throughput-on-cpu-d76fb8da565d-20260605T005524086801+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/053a5e17c8ff

## What looked useful

CPU gradient checkpointing granularity is useful as a memory-pressure control but was not a throughput optimization in the clearest activation-heavy test. Finer granularity increased recomputation overhead and showed diminishing RSS returns.

## Boundaries and scale limits

Synthetic MLP/residual workloads only; no attention blocks, no GPT-2-small-class model, no dataset pipeline, no Adam-family optimizer state, no multi-socket affinity study, and no long-run thermal or production workload validation.

## Claim scope

Bounded local PyTorch CPU benchmarks of sequential residual MLP stacks show that checkpointing granularity materially trades throughput for RSS savings; in an activation-heavy configuration, coarse checkpointing retained 86.9% of baseline throughput with about 99.5 MB RSS savings, while finer granularity fell to 33.7-53.4% of baseline throughput for a plateau near 180-185 MB RSS savings.

## Why it stopped

Bounded local evidence supports a practical mechanism but is not broad or direct enough for a paper; this is not a full validation of CPU checkpointing for real language-model training.

## Recommended next action

Stop this run as no-paper useful evidence; the bounded next action is a transformer-block CPU benchmark with torch.profiler attribution for recomputation and checkpoint bookkeeping overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-block CPU checkpoint granularity profiler benchmark
- Success threshold: A repeatable transformer-block result where coarse checkpointing preserves at least 80% of no-checkpoint throughput with measurable RSS savings, and finer granularity is either clearly dominated or justified by at least 2x additional memory savings.
- Stop condition: Stop if repeated transformer-block runs show less than 5% RSS savings at all checkpoint granularities or timing variance remains larger than the checkpoint effect after three fresh-process repeats.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-checkpointing-granularity-vs-throughput-on-cpu-d76fb8da565d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
