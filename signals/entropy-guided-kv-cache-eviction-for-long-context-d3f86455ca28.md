# Entropy-Guided KV Cache Eviction for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-guided-kv-cache-eviction-for-long-context-d3f86455ca28`
Run ID: `entropy-guided-kv-cache-eviction-for-long-context-d3f86455ca28-20260604T072315482204+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ede08e12091f

## What looked useful

The mechanism worth preserving is attention-mass salience for retaining relevant facts under cache pressure. The entropy term is not justified by these bounded results because it alternated between helping and hurting relative to attention_mass.

## Boundaries and scale limits

Toy transformer only; synthetic key-value recall only; weak full-context learned recall; retained-context recomputation proxy rather than exact hidden-state-preserving KV eviction; no pretrained LLM, natural long-context benchmark, latency, throughput, or production-serving validation.

## Claim scope

In a tiny synthetic key-value recall proxy, attention-derived cache salience improved target fact retention over FIFO/random, but entropy-adjusted salience did not consistently beat simpler attention-mass eviction and did not produce reliable downstream accuracy gains.

## Why it stopped

Proxy/local evidence only: entropy-guided eviction did not consistently outperform attention-mass eviction, and the trained toy models had weak full-context recall, so the result is not a full validation or paper-positive claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; a bounded deepen follow-up should first establish a strong full-context small-model recall baseline before retesting entropy-adjusted eviction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retest entropy-guided KV eviction after establishing strong small-model recall
- Success threshold: Entropy-adjusted eviction improves end-to-end accuracy by at least 5 percentage points over attention_mass at two or more cache budgets while maintaining strong full-context baseline accuracy.
- Stop condition: Stop if full-context accuracy remains below 70% after a bounded training/curriculum attempt, or if entropy_adjusted fails to beat attention_mass by 5 percentage points on end-to-end accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-guided-kv-cache-eviction-for-long-context-d3f86455ca28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
