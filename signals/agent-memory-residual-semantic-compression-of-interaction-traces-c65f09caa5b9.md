# Agent Memory: Residual Semantic Compression of Interaction Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-residual-semantic-compression-of-interaction-traces-c65f09caa5b9`
Run ID: `agent-memory-residual-semantic-compression-of-interaction-traces-c65f09caa5b9-20260621T201532309208+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59f15e12bd75

## What looked useful

Across five seeds, residual semantic compression matched flat retrieval at 100% latest-fact accuracy and averaged 75.57% lower retained memory tokens than transcript search; a hash-only compressed negative control averaged 26.87% accuracy, indicating semantic field identity is necessary.

## Boundaries and scale limits

Five synthetic seeds only; no real agent traces, no learned extraction, no adversarial phrasing, no production retrieval loop, and no long-horizon multi-session deployment.

## Claim scope

On deterministic synthetic repeated-interaction traces with canonicalizable entity/field/value facts, residual semantic compression preserved latest-fact recall while reducing retained memory-token footprint versus transcript search.

## Why it stopped

Stopped after a reproducible synthetic proxy validation; evidence is useful but not broad or direct enough for paper-positive closure.

## Recommended next action

Run a bounded deepen follow-up on real or realistic agent traces with noisy extraction and the same memory-footprint and task-success metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual semantic compression on noisy real agent interaction traces
- Success threshold: Residual memory achieves at least 95% task accuracy, matches flat retrieval within 2 percentage points, and reduces retained memory tokens by at least 50% versus transcript search on at least three seeds or folds.
- Stop condition: Stop if residual memory falls more than 5 percentage points below flat retrieval accuracy or fails to reduce retained tokens by 30% on the first complete trace split.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-residual-semantic-compression-of-interaction-traces-c65f09caa5b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
