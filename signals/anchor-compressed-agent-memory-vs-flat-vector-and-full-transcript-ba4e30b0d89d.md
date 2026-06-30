# Anchor-compressed agent memory vs flat-vector and full-transcript

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-compressed-agent-memory-vs-flat-vector-and-full-transcript-ba4e30b0d89d`
Run ID: `anchor-compressed-agent-memory-vs-flat-vector-and-full-transcript-ba4e30b0d89d-20260629T191222120781+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cdcc5f8089e1

## What looked useful

Anchors reached 1.000 mean answerability at all tested budgets. Flat TF-IDF reached 0.0618, 0.4160, 0.7633, and 1.000 at 128, 256, 512, and 1024 words respectively. Transcript tail remained 0.1878 or lower even at 1024 words. The result supports testing anchor-compressed memory on direct agent traces, but not paper writing from this proxy alone.

## Boundaries and scale limits

Synthetic data only; no real agent transcripts, modern embedding model, lossy summarization, LLM answer generation, multi-hop reasoning, or production latency/cost measurement. Medium run covered 12 seeds, 256 facts per seed, 16 updates per fact, and budgets up to 1024 words.

## Claim scope

In a controlled synthetic mutable-fact retrieval benchmark, latest-value anchor compression preserved answerability under 128-512 word context budgets better than flat TF-IDF event retrieval and bounded transcript tail, while using about 3.23% of full transcript storage.

## Why it stopped

Synthetic proxy produced useful mechanism evidence but not direct production or paper-grade validation.

## Recommended next action

Run a bounded direct-evidence follow-up using real or LLM-generated agent traces, embedding retrieval, lossy anchor compression, and downstream LLM answer accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-compressed memory on LLM-generated agent traces with lossy summaries
- Success threshold: At 256-512 selected context words, anchor-compressed memory improves downstream answer accuracy by at least 10 percentage points over embedding retrieval on at least 500 held-out realistic queries without more than 5% compression-induced wrong-current-value errors.
- Stop condition: Stop if anchor compression fails to beat embedding retrieval by 5 percentage points at 512 context words, or if compression-induced wrong-current-value errors exceed 10%.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-compressed-agent-memory-vs-flat-vector-and-full-transcript-ba4e30b0d89d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
