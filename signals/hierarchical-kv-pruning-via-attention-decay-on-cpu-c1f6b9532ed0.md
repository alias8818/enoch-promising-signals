# Hierarchical KV Pruning via Attention Decay on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-pruning-via-attention-decay-on-cpu-c1f6b9532ed0`
Run ID: `hierarchical-kv-pruning-via-attention-decay-on-cpu-c1f6b9532ed0-20260604T140646507720+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45c91285252e

## What looked useful

Age-only hierarchy is consistently worse than sliding. Salience hierarchy is nearly tied with sliding overall and slightly better only in mixed-anchor regimes at 25% and 50% budgets, while remaining slower than dense attention end-to-end on this CPU harness. Uniform attention is a clear failure mode.

## Boundaries and scale limits

No real transformer, real text perplexity, generation quality, production KV cache, layer/head-specific traces, or optimized kernel was tested. CPU timings are for a Python/NumPy harness and should not be treated as optimized inference-engine throughput.

## Claim scope

Bounded NumPy CPU probe of KV pruning policies on synthetic attention regimes with sequence lengths 512/1024/2048, budgets 12.5%/25%/50%, and three seeds. The evidence supports only a narrow mechanism claim: decayed historical salience can preserve persistent anchor tokens slightly better than sliding-window retention at moderate/high budgets, but it does not improve pure recency decay and does not produce CPU speedup in this implementation.

## Why it stopped

Proxy/early falsification rather than full validation: the naive CPU optimization claim is unsupported because salience hierarchy did not beat sliding broadly and was slower than dense attention in the corrected end-to-end CPU timing.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run a bounded deepen test inside a tiny autoregressive transformer with real text perplexity and optimized retention overhead measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace KV pruning test for salience hierarchy
- Success threshold: At 25% KV budget, salience hierarchy must reduce perplexity or next-token-loss degradation by at least 10% relative to sliding-window retention while keeping end-to-end decode latency no worse than sliding by more than 5%.
- Stop condition: Stop if salience hierarchy fails to beat sliding on real-text loss at 25% KV budget or if bookkeeping overhead makes decode latency worse than sliding by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-pruning-via-attention-decay-on-cpu-c1f6b9532ed0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
