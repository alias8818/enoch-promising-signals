# Budgeted KV Eviction for 32k Context on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `budgeted-kv-eviction-for-32k-context-on-10gb-74a0a84d511e`
Run ID: `budgeted-kv-eviction-for-32k-context-on-10gb-74a0a84d511e-20260529T035343335095+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f91fc069d69e

## What looked useful

At 32k context with a 20,480-token/10GiB-equivalent KV budget, budgeted_score retained 100% of old salient tokens outside the recency budget and improved cosine from 0.5917 to 0.8893 and relative L2 from 0.8948 to 0.7137 versus recent-only. In scattered-salient traces it retained all salient tokens and improved cosine but had worse relative L2 than recency-only.

## Boundaries and scale limits

No real transformer integration, no language-model quality metrics, no multi-token generation, no production KV-cache implementation, and no measured scoring overhead. Scattered-salient synthetic traces had mixed output-fidelity results.

## Claim scope

Synthetic 32k single-step attention probes show that a score-budgeted KV retention policy can preserve planted old salient tokens outside a 10GiB-equivalent recency cache and improve attention-output cosine/L2 versus recent-only eviction in that targeted failure mode.

## Why it stopped

Proxy-only synthetic evidence supports the old-token preservation mechanism in one targeted scenario but is mixed on exact output fidelity and lacks real-model validation.

## Recommended next action

Stop this run as a no-paper useful signal; next, implement the policy in a small real transformer KV cache and measure retrieval/perplexity, latency, and memory against recent and sink+recent baselines at 8k-32k.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer KV eviction validation at 8k-32k
- Success threshold: Budgeted eviction improves retrieval/perplexity by at least 10% relative over recent-only at 32k while staying within the matched KV budget and adding less than 15% generated-token latency overhead.
- Stop condition: Stop if real-model quality is not better than recent-only at matched budget, if scoring overhead exceeds 15% without quality gains, or if memory remains above the 10GiB-equivalent KV budget.

## Evidence references

- Artifact root: `<local-path>/projects/budgeted-kv-eviction-for-32k-context-on-10gb-74a0a84d511e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
