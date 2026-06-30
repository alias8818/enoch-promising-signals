# Noisy natural-language trace compression versus recency-aware and embedding retrieval baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `noisy-natural-language-trace-compression-versus-recency-aw-b459a1a614`
Run ID: `noisy-natural-language-trace-compression-versus-recency-aw-b459a1a614-20260619T181400145470+0000`

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

- Parent run decision: Trace-derived semantic compression vs flat retrieval for CPU agent memory: enoch://control-plane/projects/trace-derived-semantic-compression-vs-flat-retrieval-for-cpu-agent-memory-d9043ef4e0d2/runs/trace-derived-semantic-compression-vs-flat-retrieval-for-cpu-agent-memory-d9043ef4e0d2-20260619T174452193123+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e4e06b2a7886

## What looked useful

Noisy natural-language compression achieved 1.000 exact-match accuracy versus 0.867 for lexical embedding, 0.783 for recency-aware embedding, and 0.000 for pure recency on the controlled direct test. The mechanism appears useful for old-but-current facts under noisy traces, but the evidence is not publication-grade.

## Boundaries and scale limits

Synthetic traces only; deterministic slot/name extraction; no real user/operator traces; no neural embedding model; no LLM generation from retrieved context; one seed and one primary token budget.

## Claim scope

In a deterministic 180-task synthetic Tier 1 benchmark with noisy natural-language traces, stale updates, and an 80-token query budget, query-ranked natural-language fact compression recovered current target facts more accurately than pure recency, lexical embedding retrieval, and recency-aware lexical retrieval baselines.

## Why it stopped

Closed as no-paper useful signal: the controlled direct test supports the mechanism but is synthetic and parser-aligned, so it is not full validation or paper-ready evidence.

## Recommended next action

Run a deepen follow-up using model-generated or real replay traces, a sentence-transformer embedding baseline, multiple budgets/seeds, and LLM answer generation from retrieved context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust noisy-trace compression against semantic embedding retrieval on model-generated replay traces
- Success threshold: Compression improves exact-match accuracy by at least 5 percentage points over the best embedding or recency-aware baseline at two or more budgets, without increasing mean context tokens.
- Stop condition: Stop if compression fails to beat the strongest retrieval baseline by at least 2 percentage points on the first two seeds, or if extraction errors erase the advantage under realistic paraphrase noise.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-natural-language-trace-compression-versus-recency-aw-b459a1a614`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
