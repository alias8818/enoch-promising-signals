# Trace-Derived Semantic Compression with Anchor-Linked Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-compression-with-anchor-linked-retrieval-e0259426ab2f`
Run ID: `trace-derived-semantic-compression-with-anchor-linked-retrieval-e0259426ab2f-20260613T212251779085+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffda7f9aacb9

## What looked useful

On 96 generated tasks and 384 queries, anchor-linked compression reached 0.888 accuracy versus 0.674 for flat retrieval and 0.453 for transcript search. Anchor memory used 15,824 tokens versus 36,559 full trace tokens. The main failure mode was constraint-field retrieval under the 48-token budget.

## Boundaries and scale limits

Synthetic structured traces only; deterministic parser rather than learned or LLM compression; exact-answer retrieval only; no real production traces, human labels, unstructured trace noise, end-to-end assistant generation, or multi-session persistence validation.

## Claim scope

In a deterministic synthetic replay benchmark with structured traces, noisy distractors, one correction per task, and a 48-token retrieval budget, anchor-linked compressed memory improved exact-answer retrieval accuracy over raw transcript search and flat compressed retrieval while using less than 44% of full trace tokens.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic and parser-driven, not direct production or LLM-compression validation.

## Recommended next action

Run a bounded deepen follow-up on real or semi-real agent traces with human-labeled replay answers and an LLM or learned compression stage; stop paper consideration until that direct evidence exists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace anchor-linked compression replay validation
- Success threshold: At least 10 percentage point exact-answer accuracy improvement over flat retrieval at matched or lower memory tokens, with unsupported-answer rate no higher than the best baseline.
- Stop condition: Stop if anchor-linked compression fails to beat flat retrieval by 5 percentage points on the labeled real-trace replay set or if unsupported answers increase above baseline.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-with-anchor-linked-retrieval-e0259426ab2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
