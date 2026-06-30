# Bounded Failure Mode Catalog for Local CPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-failure-mode-catalog-for-local-cpu-agents-09962245cbda`
Run ID: `bounded-failure-mode-catalog-for-local-cpu-agents-09962245cbda-20260619T232012264541+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d95f05653d68

## What looked useful

Layered doctrine/scope/recency memory reached 11/12 accuracy versus flat retrieval 10/12, transcript search 9/12, and no-memory 1/12. Residual failures show absent persisted memory remains unrecoverable, transcript search selects stale corrections, and flat retrieval can select ambiguous metadata.

## Boundaries and scale limits

Synthetic replay only; deterministic retrieval policies rather than live LLM agents; 12 tasks, 4 strategies, 48 predictions; no production traces or human blind labels.

## Claim scope

A 12-task deterministic local CPU replay catalog can separate repeated-agent memory failure mechanisms across no-memory, transcript-search, flat-retrieval, and layered doctrine-memory policies.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy replay, not direct production-agent or LLM-agent validation.

## Recommended next action

Run a bounded deepen follow-up on 50 to 100 real or semi-real local-agent traces with blind expected labels using the same strategy matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-backed local CPU agent memory failure catalog
- Success threshold: Layered doctrine memory improves overall accuracy by at least 10 percentage points over flat retrieval and reduces stale/scope/metadata failures by at least 25% without increasing omission failures.
- Stop condition: Stop if fewer than 50 labeled traces are available locally, if flat retrieval matches layered accuracy within 5 percentage points, or if failures do not map cleanly to the catalog categories.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-failure-mode-catalog-for-local-cpu-agents-09962245cbda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
