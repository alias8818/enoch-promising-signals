# CPU N-Gram Speculative Draft for GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-draft-for-gb10-c9d4811be25e`
Run ID: `cpu-n-gram-speculative-draft-for-gb10-c9d4811be25e-20260604T190154516898+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3c542971de2e

## What looked useful

CPU n-gram drafting reached 456k to 1.13M draft tokens/s and produced a repeatable proxy speedup, but only 7.6-8.0% of proposed tokens were accepted and order-1 matched order-3/order-5 performance, weakening the long-context n-gram-specific hypothesis.

## Boundaries and scale limits

This run used GPT-2, Wikitext-2 subsets, 512 generated tokens per medium configuration, greedy decoding only, and a standalone Python verifier without production KV-cache integration, batching, sampling, larger target models, or learned draft-model controls.

## Claim scope

On GB10 with GPT-2 greedy decoding over Wikitext-2 prompts, a CPU token n-gram proposer is fast enough to be negligible and reduces target forward passes by about 21-22% in a small block-verification proxy, yielding about 1.34-1.36x measured throughput.

## Why it stopped

Proxy evidence supports cheap CPU drafting but not a publication-grade or deployment-grade claim; acceptance is low and the measured benefit is not specific to higher-order n-grams.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test is a KV-cache-aware inference-engine prototype comparing CPU n-gram draft, no draft, and a small learned draft model on the same GB10 target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache CPU n-gram draft verifier on GB10
- Success threshold: At least 1.15x end-to-end throughput improvement over target-only greedy decoding on GB10 with exact output equivalence and no worse than 5% p95 latency regression.
- Stop condition: Stop if KV-cache integration reduces throughput below 1.05x target-only or if synchronization/proposal overhead consumes more than half of the theoretical target-forward reduction.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-draft-for-gb10-c9d4811be25e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
