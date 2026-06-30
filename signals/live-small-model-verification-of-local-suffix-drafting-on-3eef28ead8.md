# Live Small-Model Verification of Local Suffix Drafting on Code and RAG Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-small-model-verification-of-local-suffix-drafting-on-3eef28ead8`
Run ID: `live-small-model-verification-of-local-suffix-drafting-on-3eef28ead8-20260629T023437580867+0000`

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

- Parent run decision: Suffix-Tree Draft Model for Local Speculative Decoding: enoch://control-plane/projects/suffix-tree-draft-model-for-local-speculative-decoding-1e3dcf3ec84a/runs/suffix-tree-draft-model-for-local-speculative-decoding-1e3dcf3ec84a-20260629T021842321995+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a6fb9d2552e0

## What looked useful

At draft length 16, nearest local suffix drafting accepted 7,654 of 21,445 code target tokens for a 1.229x mean verifier-pass speedup bound, and 10,010 of 10,800 synthetic RAG target tokens for a 6.490x mean speedup bound. Longer drafts helped RAG more than code.

## Boundaries and scale limits

Measured on 24 local Python code traces and 12 synthetic templated RAG traces with whitespace-preserving lexical tokens; no neural verifier, real RAG logs, GPU serving path, KV-cache behavior, or production latency was tested.

## Claim scope

A CPU-only offline oracle-verification probe found that longest-local-suffix drafting can consume many exact future tokens on repetitive synthetic RAG traces and a modest fraction on local Python code traces.

## Why it stopped

Proxy-only useful signal: the oracle verifier and synthetic RAG traces are enough to justify a focused follow-up, but not a full validation or paper-positive decision.

## Recommended next action

Run a bounded deepen test on real RAG/code traces with an actual small neural verifier or target-model scoring loop before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural verifier validation of local suffix drafting on real RAG and code traces
- Success threshold: Across at least 10,000 real target tokens per domain, show no unsafe false accepts, at least 1.5x measured end-to-end speedup on RAG traces, and no worse than 5% latency regression on code traces.
- Stop condition: Stop if real-trace neural verification yields less than 1.2x measured speedup on RAG traces or introduces any unbounded false-accept path that cannot be eliminated by exact target-model verification.

## Evidence references

- Artifact root: `<local-path>/projects/live-small-model-verification-of-local-suffix-drafting-on-3eef28ead8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
