# Layered Memory Stack: Working, Project, User, Operator on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-stack-working-project-user-operator-on-cpu-1cd7f9669349`
Run ID: `layered-memory-stack-working-project-user-operator-on-cpu-1cd7f9669349-20260629T024912055933+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed224b707225

## What looked useful

Layered doctrine memory reached 12/12 exact match versus 8/12 for flat retrieval and 8/12 for transcript search. Flat retrieval failed layer-precedence conflicts; transcript search failed stale supersession cases.

## Boundaries and scale limits

Small synthetic dataset; assumes structured fact extraction; does not test real transcript noise, LLM generation, latency at scale, or long-horizon memory growth.

## Claim scope

Synthetic structured replay of 21 fact events and 12 probes testing working/project/user/operator memory precedence and supersession on CPU.

## Why it stopped

No-paper useful signal: the result is synthetic structured replay evidence, not direct real-trace or publication-grade validation.

## Recommended next action

Run the same layered policy on real repeated-agent traces with noisy extraction and a flat-retrieval control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace noisy extraction test for layered agent memory
- Success threshold: Layered memory improves exact-match accuracy by >=20 percentage points over flat_retrieval and has fewer errors in both stale-supersession and layer-precedence categories.
- Stop condition: Stop if layered memory improves by <5 percentage points over flat_retrieval or introduces more precedence/supersession errors than either baseline.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-stack-working-project-user-operator-on-cpu-1cd7f9669349`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
