# Layered memory reduces repeated instructions vs flat vector retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-reduces-repeated-instructions-vs-flat-vector-retrieval-ed3d436d7394`
Run ID: `layered-memory-reduces-repeated-instructions-vs-flat-vector-retrieval-ed3d436d7394-20260629T170032095110+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/218ac87ce6e2

## What looked useful

Flat retrieval repeatedly selected duplicate raw instruction records, producing 103.4 duplicate-instruction tokens and 126.4 mean context tokens at top_k=10 with 0.420 mean recall. Layered memory used 57.1 mean context tokens, 0 duplicate-instruction tokens, and 0.999 mean recall.

## Boundaries and scale limits

Synthetic corpus only; no production transcripts, embedding model, or live LLM downstream task-quality evaluation. Main run used 792 replay tasks and 5177 memory records; sensitivity sweep used 9 smaller runs across 3 seeds and flat top_k values.

## Claim scope

In a deterministic synthetic repeated-agent replay benchmark, layered canonical memory by user/category reduced repeated instruction context versus raw flat TF-IDF retrieval while preserving required-instruction recall.

## Why it stopped

Closed as useful proxy evidence, not paper-ready validation, because the benchmark directly measures retrieval context mechanics but only proxies downstream agent quality.

## Recommended next action

Run a bounded live-LLM replay using the generated tasks, comparing answer correctness and prompt tokens for flat embedding retrieval versus layered canonical memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM replay for layered versus flat repeated-instruction memory
- Success threshold: Layered memory achieves at least equal answer correctness to flat retrieval while reducing mean memory-context tokens by at least 30% and not increasing severe instruction-miss failures.
- Stop condition: Stop if layered memory fails to match flat retrieval correctness or if token savings fall below 15% after correcting implementation errors.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-reduces-repeated-instructions-vs-flat-vector-retrieval-ed3d436d7394`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
