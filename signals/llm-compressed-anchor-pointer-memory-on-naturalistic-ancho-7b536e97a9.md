# LLM-compressed anchor-pointer memory on naturalistic anchored facts

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `llm-compressed-anchor-pointer-memory-on-naturalistic-ancho-7b536e97a9`
Run ID: `llm-compressed-anchor-pointer-memory-on-naturalistic-ancho-7b536e97a9-20260630T004725804015+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Anchor-Pinned Compressed Context: Exact-Pointer Memory Beyond RAG: enoch://control-plane/projects/anchor-pinned-compressed-context-exact-pointer-memory-beyond-rag-0dbc57b1b929/runs/anchor-pinned-compressed-context-exact-pointer-memory-beyond-rag-0dbc57b1b929-20260630T002705157983+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/889938e71ba1

## What looked useful

Naive abstractive LLM pointer compression improved slightly over title-only anchors but consistently discarded discriminative numeric/date details and underperformed simple same-budget extractive baselines.

## Boundaries and scale limits

Short lead-section Wikipedia facts only; TF-IDF retrieval only; generated cloze-style queries; FLAN-T5-small compressor only; no 7B-scale training, learned pointer memory integration, long-context persistence, or answer generation from retrieved memory.

## Claim scope

In a 40-fact Wikipedia-derived anchored-fact retrieval probe, FLAN-T5-small abstractive compressed pointers under 4-12 word budgets were worse than same-budget extractive truncation and heuristic keyword pointers.

## Why it stopped

Proxy/early falsification of naive LLM-compressed anchor pointers: main 8-word run Top-1 was 0.45 for LLM pointers versus 0.95 for lead truncation and 1.00 for heuristic keywords; this is not a full-scale validation.

## Recommended next action

Stop this no-paper run; run one bounded deepen follow-up that enforces preservation of all numbers/dates and anchor entities in compressed pointers before considering larger-scale architecture work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained extractive anchor-pointer compression for numeric anchored facts
- Success threshold: Constrained pointer Top-1 within 5 percentage points of heuristic_keyword at the 8-word budget and at least 20 percentage points above unconstrained LLM pointers.
- Stop condition: Stop if constrained pointers remain more than 10 percentage points below lead_truncation or heuristic_keyword at 8 words, or if preserving numeric/date spans requires exceeding the fixed word budget on more than 20% of facts.

## Evidence references

- Artifact root: `<local-path>/projects/llm-compressed-anchor-pointer-memory-on-naturalistic-ancho-7b536e97a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
