# Layered Memory vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-memory-vs-flat-retrieval-on-repeated-tasks-70cda4e5a9ce`
Run ID: `layered-memory-vs-flat-retrieval-on-repeated-tasks-70cda4e5a9ce-20260611T051147982556+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a1a3c6f35e71

## What looked useful

Layered retrieval improved exact item accuracy when noisy cross-task interference degraded flat retrieval, especially with sufficient task cue strength, but it underperformed flat retrieval in clean conditions or weak-routing regimes because routing errors became hard failures.

## Boundaries and scale limits

CPU-only synthetic benchmark; no learned embeddings, no natural-language repeated-task workload, no LLM agent memory loop, no approximate nearest-neighbor production index, and no long-horizon memory write/compaction dynamics.

## Claim scope

Synthetic repeated-task vector retrieval with shared keys across tasks, task-dependent labels, flat nearest-neighbor retrieval, and a two-stage task-prototype layered retriever.

## Why it stopped

The result is mixed synthetic evidence rather than full validation: layered memory is conditionally useful under noisy cross-task interference but not a general replacement for flat retrieval.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on a natural-language repeated-task benchmark with a router-confidence fallback against the same flat baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Router-Confidence Layered Memory on Natural-Language Repeated Tasks
- Success threshold: Layered retrieval with fallback improves exact answer accuracy by at least 5 percentage points over flat retrieval or matches accuracy within 1 point while reducing p95 retrieval latency by at least 30%, with wrong-task errors no higher than flat retrieval.
- Stop condition: Stop if router accuracy stays below 85% after confidence calibration or if fallback removes the latency advantage while accuracy remains within 1 point of flat retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-vs-flat-retrieval-on-repeated-tasks-70cda4e5a9ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
