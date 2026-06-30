# Operator-Trace Memory Compression vs Flat Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-trace-memory-compression-vs-flat-retrieval-18ab5f998d61`
Run ID: `operator-trace-memory-compression-vs-flat-retrieval-18ab5f998d61-20260629T182146791775+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d384553fe35e

## What looked useful

Compact operator-trace memory achieved 1.000 mean accuracy across 2,160 synthetic queries at 64, 128, 256, and 512 token budgets, while flat event BM25 ranged from 0.529 to 0.987 and flat chunk BM25 ranged from 0.000 to 0.666. The mechanism appears strongest for latest-state and final-status questions.

## Boundaries and scale limits

Synthetic traces only; oracle evidence checker rather than LLM answerer; no real operator logs, human-validated questions, production retrieval stack, or long-running scale test.

## Claim scope

Synthetic operator-trace benchmark with known-answer queries over generated cases, comparing compact fact-level trace memory against flat BM25 retrieval over raw events and raw chunks under 64-512 token context budgets.

## Why it stopped

Synthetic/proxy-only evidence supports the mechanism but is not direct enough for paper-positive closure.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded evidence should replay the same harness on real operator traces with human-validated questions and an LLM answerer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Operator Memory Retrieval Evaluation
- Success threshold: At least 10 percentage points absolute answer-accuracy improvement over the strongest flat retrieval baseline at <=256 context tokens, with no increase in hallucination rate and at least 1.5x raw-to-compressed token reduction.
- Stop condition: Stop if compressed memory fails to beat flat event retrieval by 5 percentage points on real-trace answer accuracy or if human labels show the synthetic query types do not map to real operator needs.

## Evidence references

- Artifact root: `<local-path>/projects/operator-trace-memory-compression-vs-flat-retrieval-18ab5f998d61`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
