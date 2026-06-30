# Layered User/Project Memory Hierarchy vs Flat Vector Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-user-project-memory-hierarchy-vs-flat-vector-retrieval-435a9eeb3857`
Run ID: `layered-user-project-memory-hierarchy-vs-flat-vector-retrieval-435a9eeb3857-20260620T201252260570+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Layered memory achieved 1.000 answer accuracy and 1.000 override accuracy versus flat retrieval at 0.677 answer accuracy and 0.415 override accuracy, while using 32.4 average context tokens versus 60.4. This supports the scoped-memory mechanism but not a paper-ready claim.

## Boundaries and scale limits

Evidence is synthetic and local: 2742 generated memories, 3840 generated queries, one seed for the default run, dependency-free token cosine flat baseline rather than a production vector database or embedding model, no LLM answer-generation loop, no real user traces, and no privacy or extraction-quality evaluation.

## Claim scope

In a deterministic synthetic replay benchmark with explicit user defaults, project overrides, stale memories, and lexical distractors, indexed layered user/project memory retrieval outperformed flat vector-style retrieval for scoped preference lookup.

## Why it stopped

Completed bounded synthetic proxy evaluation; result is useful but not publication-grade because direct real-trace and production-retrieval evidence is missing.

## Recommended next action

Run a bounded deepen test on real or realistically extracted multi-session agent traces with an actual embedding/vector-DB flat baseline and downstream LLM answer scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace layered memory versus vector retrieval confirmation
- Success threshold: Layered retrieval improves downstream answer accuracy by at least 10 percentage points over flat vector retrieval on scoped project-override queries without increasing average context tokens.
- Stop condition: Stop if layered retrieval fails to beat flat vector retrieval by 5 percentage points on override-query answer accuracy across two corpus splits, or if ground-truth scoped traces cannot be produced without private operator data.

## Evidence references

- Artifact root: `<local-path>/projects/layered-user-project-memory-hierarchy-vs-flat-vector-retrieval-435a9eeb3857`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
