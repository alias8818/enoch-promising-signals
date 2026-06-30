# Operator-Doctrine Memory vs Retrieval Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-vs-retrieval-memory-8498f1849e6f`
Run ID: `operator-doctrine-memory-vs-retrieval-memory-8498f1849e6f-20260611T151249453435+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

Retrieval-memory failures were exactly aligned with absent relevant doctrine chunks: top-1 and top-3 retrieval hit rate was 0.5 and accuracy was 0.5, with 1.0 accuracy on retrieval hits and 0.0 on misses. Full doctrine prompt reached 0.9375 accuracy; oracle retrieval reached 1.0.

## Boundaries and scale limits

Small synthetic dataset, one model, lexical retrieval with deterministic jitter, no multi-step agent tasks, no persistent memory updates, no embedding retriever or reranker, and no independent scenario authoring.

## Claim scope

On a 16-case synthetic single-turn operator-policy classification benchmark with opaque action labels and Qwen2.5-7B-Instruct-Q4_K_M, prompt-resident doctrine was more accurate than naive lexical retrieval when retrieval missed relevant rules, while oracle retrieval was best.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but not publication-grade evidence; result is mixed because imperfect retrieval underperformed prompt doctrine while oracle retrieval outperformed it.

## Recommended next action

Run a bounded deepen follow-up using embedding retrieval plus reranking on a larger independently authored doctrine/scenario set across at least two local models; stop this run as useful no-paper evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding-Reranked Doctrine Retrieval vs Prompt-Resident Doctrine
- Success threshold: Embedding plus reranking reaches at least 95% retrieval hit rate and matches or exceeds prompt-resident doctrine accuracy within 2 percentage points on both models.
- Stop condition: Stop if retrieval hit rate remains below 85% after reranking or if end-task accuracy is more than 10 percentage points below prompt-resident doctrine on both models.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-retrieval-memory-8498f1849e6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
