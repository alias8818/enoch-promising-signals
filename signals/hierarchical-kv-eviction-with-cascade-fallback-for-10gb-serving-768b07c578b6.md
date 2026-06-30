# Hierarchical KV eviction with cascade fallback for 10GB serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-eviction-with-cascade-fallback-for-10gb-serving-768b07c578b6`
Run ID: `hierarchical-kv-eviction-with-cascade-fallback-for-10gb-serving-768b07c578b6-20260607T151358895770+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14ba056c8bbc

## What looked useful

Compressed older-KV fallback improved full-cache attention-output approximation by 16.7% to 82.4% versus the best exact-only baseline across 0.05 to 0.35 normalized memory budgets, but quality-preserving cascade settings required fallback scans on roughly 81% to 98% of queries.

## Boundaries and scale limits

No real transformer server, no actual 10GB KV deployment, no measured tokens/s, no perplexity/task metric, synthetic traces only, and compressed KV was modeled with low-bit dequantized arrays rather than a production quantizer.

## Claim scope

Bounded synthetic KV-cache serving proxy: hierarchical compressed fallback reduced attention-output error versus exact-only sliding/sink eviction under equal normalized memory budgets on topic-recurring traces.

## Why it stopped

Proxy useful signal only: the synthetic attention oracle supports the compressed fallback quality mechanism, but the cascade gate did not preserve quality without frequent compressed-tier scans, so the 10GB serving claim is not validated.

## Recommended next action

Run a bounded real-transformer follow-up that implements compressed fallback in a small inference stack and measures perplexity plus decode tokens/s under a fixed KV memory budget; stop this run because current evidence is proxy-only and mixed on cascade efficiency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer KV fallback under a fixed memory budget
- Success threshold: At one or more fixed KV budgets, hierarchical fallback improves perplexity or task metric by at least 10% relative to the best exact-only baseline while keeping measured decode throughput within 20% of that baseline and using no more memory.
- Stop condition: Stop if the real implementation cannot beat exact-only quality at equal memory, or if all quality-preserving thresholds reduce decode throughput by more than 20% versus the best exact-only baseline.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-eviction-with-cascade-fallback-for-10gb-serving-768b07c578b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
