# Compressed State Machine for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-machine-for-cpu-inference-5d5995630024`
Run ID: `compressed-state-machine-for-cpu-inference-5d5995630024-20260610T113048364959+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/65bbe62591f0

## What looked useful

Compressed rows reduced memory by 15.876x to 120.4704x in the main sweep and were 1.536x to 6.535x faster than dense lookup for 32 MiB to 256 MiB dense tables, with all checksum comparisons matching. A cache sweep found dense lookup faster at 1 to 4 MiB and compressed lookup faster from 8 MiB upward.

## Boundaries and scale limits

Synthetic deterministic transition tables only; no learned automaton, language-model quality metric, production inference integration, batching, multi-thread serving, or hardware-counter validation. The result does not show that arbitrary CPU inference can be losslessly represented this way.

## Claim scope

In a single-thread synthetic CPU transition-loop benchmark, a default-plus-exceptions compressed state-machine representation is faster than a dense uint32 state/token transition table when the dense table is larger than the cache-friendly regime; the observed crossover was 8 MiB dense table size on this host.

## Why it stopped

No-paper useful signal: the local evidence supports the compression/cache mechanism on synthetic transition inference, but it is not direct evidence for real model inference quality or production serving.

## Recommended next action

Run a bounded trace-driven follow-up that builds sparse state tables from real token traces or an n-gram/automaton proxy and measures latency, memory, quality-preserving equivalence, and cache behavior against dense and standard CPU baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven compressed state-machine CPU inference benchmark
- Success threshold: Compressed representation is checksum-equivalent and at least 1.25x faster than dense on tables larger than 64 MiB, with at least 10x memory reduction and no unreported quality loss in the trace/proxy task.
- Stop condition: Stop if trace-derived tables are not sparse/default-structured enough for at least 10x compression or if compressed lookup is slower than dense on the target table sizes after straightforward implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-machine-for-cpu-inference-5d5995630024`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
