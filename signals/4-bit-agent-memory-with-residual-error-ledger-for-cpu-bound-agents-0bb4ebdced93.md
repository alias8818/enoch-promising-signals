# 4-bit agent memory with residual error ledger for CPU-bound agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-agent-memory-with-residual-error-ledger-for-cpu-bound-agents-0bb4ebdced93`
Run ID: `4-bit-agent-memory-with-residual-error-ledger-for-cpu-bound-agents-0bb4ebdced93-20260607T063924684042+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/26d63467276c

## What looked useful

On the residual-sensitive proxy, plain int4 dropped target top-1 from 1.000 to 0.041, while int4 plus 16 residual entries per vector recovered 0.951 top-1 and 0.998 recall@10 at 5.22x storage compression versus fp32. On a Gaussian control, the ledger gave only small/no target-metric improvement over plain int4.

## Boundaries and scale limits

20,000 vectors, 256 dimensions, 512 queries, synthetic data, NumPy dense reconstruction for scoring; no real agent traces, no real text embeddings, no optimized packed int4 CPU kernel, and no long-running memory updates.

## Claim scope

Synthetic CPU vector-memory retrieval only: sparse residual ledgers restore retrieval quality for a residual-sensitive fingerprint distribution under rowwise 4-bit quantization, but do not reliably improve ordinary dense Gaussian-like vectors.

## Why it stopped

Synthetic proxy evidence supports a distribution-dependent mechanism but is insufficient for a paper or broad agent-memory claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use real sentence embeddings or agent-memory traces and compare plain int4 versus residual-ledger int4 at matched storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-ledger int4 retrieval on real embedding traces
- Success threshold: At matched storage, residual-ledger int4 improves recall@10 by at least 3 absolute percentage points over plain int4 or a matched-storage baseline on real embeddings, with CPU query latency no more than 1.25x the best compressed baseline.
- Stop condition: Stop if two real embedding/agent-memory datasets show less than 1 percentage point recall@10 improvement or if ledger maintenance/query cost exceeds 1.5x compressed baseline latency.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-agent-memory-with-residual-error-ledger-for-cpu-bound-agents-0bb4ebdced93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
