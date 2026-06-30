# Speculative Decoding with Bounded Latency Budgets

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-bounded-latency-budgets-776bf9e28a31`
Run ID: `speculative-decoding-with-bounded-latency-budgets-776bf9e28a31-20260605T052301078051+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb58a872501e

## What looked useful

Budgeted speculation reduced target calls/token by 43.5-64.8% versus baseline in stable/near-saturation scenarios and avoided fixed8 tail-latency collapse under mixed acceptance, but it did not dominate tuned fixed4 under overload.

## Boundaries and scale limits

Simulator-only evidence: no real LLM serving stack, no GPU batching, no measured model latencies, no KV-cache pressure, no prompt prefill, and no production arrival traces. Stable-scenario throughput is arrival-limited rather than capacity-limited.

## Claim scope

In a seeded single-server queueing simulator with synthetic speculative-decoding acceptance rates and latency budgets, a budget-aware speculative window acts as a guardrail against oversized fixed windows and can reduce SLO violations while cutting target calls versus baseline decoding.

## Why it stopped

Proxy simulator evidence supports the guardrail mechanism but is insufficient for a paper and mixed against a tuned fixed4 baseline under overload.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete step is to replay the scheduler on measured acceptance and latency traces from a small real draft/target model serving setup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replayed Budgeted Speculative Decoding on a Small Real Serving Stack
- Success threshold: Budgeted policy reduces p95 SLO violation rate by >=25% versus fixed4 and by >=50% versus fixed8 while retaining >=90% of fixed4 throughput on measured traces.
- Stop condition: Stop if measured traces show budgeted selection is within 5% of fixed4 SLO violation rate or loses more than 10% throughput versus fixed4 in two independent workloads.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-bounded-latency-budgets-776bf9e28a31`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
