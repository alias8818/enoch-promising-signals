# Sparse Upcycling for Optimizer States

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-upcycling-for-optimizer-states-9ce8be0a18c2`
Run ID: `sparse-upcycling-for-optimizer-states-9ce8be0a18c2-20260525T191231465881+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/87cf7ae9cf69

## What looked useful

Sparse optimizer-state upcycling is not falsified as a compression/reset tactic, but the distinctive top-k high-moment mechanism is unsupported because random retention and reset controls also beat dense carryover. The useful signal is that stale Adam state can hurt after a resume/upcycling boundary, and aggressive state thinning may function more like state reset/regularization than information-preserving compression.

## Boundaries and scale limits

Small MLP proxy only; PyTorch still stored dense optimizer tensors; no language-model token training, no distributed optimizer, no realized memory or bandwidth savings, and only three seeds per task.

## Claim scope

On two small synthetic regression tasks with Adam resume after 300 warmup steps, zeroing most optimizer moments at the boundary preserved or improved short-horizon validation loss relative to dense Adam state, but top-k moment retention was not meaningfully better than random retention or reset controls.

## Why it stopped

Proxy evidence is useful but not publication-grade: top-k sparse state retention did not separate from random retention/reset controls, and memory savings were estimated rather than realized by the optimizer implementation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should implement a real block-sparse Adam state backend and compare dense, reset, random, and top-k controls on an identical-token small language-model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-sparse Adam state upcycling on a small language model
- Success threshold: At 10% or lower realized optimizer-state storage, top-k block retention matches dense Adam within 1% validation loss/perplexity and beats both random retention and full reset by at least 2% on mean final validation loss across seeds.
- Stop condition: Stop if random retention or full reset matches top-k within noise, if realized memory savings are not achieved, or if sparse-state overhead erases any practical memory/throughput benefit.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-upcycling-for-optimizer-states-9ce8be0a18c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
