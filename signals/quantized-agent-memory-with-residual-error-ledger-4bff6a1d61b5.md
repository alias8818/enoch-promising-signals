# Quantized agent memory with residual error ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-agent-memory-with-residual-error-ledger-4bff6a1d61b5`
Run ID: `quantized-agent-memory-with-residual-error-ledger-4bff6a1d61b5-20260522T112005526066+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4286aa1c5b71

## What looked useful

In the clustered int3 stress proxy, no-residual recall@1 was 0.08000; top-8 sparse residual reached 0.70875 recall@1 at 4.27x logical compression; top-32/full residual reached 1.00000 recall@1 at 1.64x compression. Int8/int4 proxies improved reconstruction error but did not change saturated retrieval.

## Boundaries and scale limits

No real agent traces, no downstream task evaluation, no packed runtime implementation, no latency benchmarking, and no model-scale embedding distribution validation.

## Claim scope

Synthetic vector-memory proxy: residual error ledgers reduce repeated low-bit quantization drift and can recover nearest-neighbor retrieval under a clustered 3-bit stress setting.

## Why it stopped

No-paper closure: this run produced a useful synthetic proxy signal, not direct publication-grade agent-system evidence.

## Recommended next action

Run a bounded direct validation on recorded agent-memory embedding traces with true update/rewrite events and downstream retrieval relevance labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-ledger quantized memory on real agent embedding traces
- Success threshold: Sparse residual ledger improves recall@10 or nDCG@10 by at least 10% relative over plain quantization while retaining at least 3x measured memory compression versus fp32 and adding less than 20% update latency.
- Stop condition: Stop if real-trace retrieval improvement is below 3% relative at every residual sparsity that retains at least 3x measured compression, or if update latency exceeds 50% over plain quantization.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-memory-with-residual-error-ledger-4bff6a1d61b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
