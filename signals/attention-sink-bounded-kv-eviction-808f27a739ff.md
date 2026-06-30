# Attention-Sink Bounded KV Eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `attention-sink-bounded-kv-eviction-808f27a739ff`
Run ID: `attention-sink-bounded-kv-eviction-808f27a739ff-20260602T121813606155+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/250464260a3e

## What looked useful

On 4,608 medium-probe predictions, recency-only added +4.771 NLL at budget 128 and +2.970 at budget 256 versus full cache; sink4+recency reduced those penalties to +0.457 and +0.197. At budget 512, sink4+recency was near full cache (+0.008 NLL). A diagnostic slice showed mean final-layer attention mass 0.4035 on the first 4 tokens.

## Boundaries and scale limits

Not tested on larger or long-context models, contexts beyond GPT-2's 1024-token regime, generation tasks, production serving workloads, or stronger content-aware eviction baselines.

## Claim scope

GPT-2 small fp16 token-by-token inference on WikiText-2 validation windows up to 768 predicted tokens: preserving 1-8 early prefix tokens inside a bounded KV cache sharply reduces next-token NLL penalty versus recency-only eviction at equal budgets.

## Why it stopped

Finalized as no-paper useful signal: local direct evidence supports the mechanism, but the validation is too narrow and lacks stronger eviction baselines.

## Recommended next action

Run a bounded deepen test comparing sink+recency against attention-score/heavy-hitter KV eviction on at least two small model families and two corpora before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compare Attention-Sink Retention Against Heavy-Hitter KV Eviction
- Success threshold: Sink+recency must match or beat the content-aware baseline within 0.05 mean NLL at one or more budgets, or provide at least 20% lower update overhead at no more than 0.10 mean NLL regression.
- Stop condition: Stop if sink+recency is worse than the content-aware baseline by more than 0.25 mean NLL at all tested budgets on both model families.

## Evidence references

- Artifact root: `<local-path>/projects/attention-sink-bounded-kv-eviction-808f27a739ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
