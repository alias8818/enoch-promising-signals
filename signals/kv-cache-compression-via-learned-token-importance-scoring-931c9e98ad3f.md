# KV Cache Compression via Learned Token Importance Scoring

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-via-learned-token-importance-scoring-931c9e98ad3f`
Run ID: `kv-cache-compression-via-learned-token-importance-scoring-931c9e98ad3f-20260605T093054354886+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/28a3c5acb135

## What looked useful

Learned scores had positive Spearman correlation with measured token-removal loss deltas (0.3939 on tiny GPT-2, 0.5826 on distilGPT-2). Learned retention beat recency at all tiny-GPT-2 budgets and at 50%/75% keep on distilGPT-2, but failed at 25% keep and lost to raw attention at 25%/50% on distilGPT-2.

## Boundaries and scale limits

Short static prose prompts only; prefix length 40-48 and continuation length 10-12; tiny/distil GPT-2-class models; attention-mask simulation rather than a real autoregressive KV-cache eviction implementation; no throughput, memory-movement, long-context, or larger-model validation.

## Claim scope

Bounded local probes on sshleifer/tiny-gpt2 and distilgpt2 show that oracle loss-delta token importance can be partially predicted from cheap features and can beat recency at moderate retention budgets, but learned scoring is not consistently better than raw attention sorting.

## Why it stopped

Mixed bounded evidence: learned token importance is learnable and sometimes useful, but the current scorer is not consistently superior to simpler attention-based retention and was tested only through short-context masking.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should train a budget-aware or nonlinear scorer and require it to beat raw attention as well as recency on held-out distilGPT-2/GPT-2-small prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget-aware learned KV retention against raw-attention controls
- Success threshold: Learned retention beats both recency and raw attention at 25%, 50%, and 75% keep with positive mean Spearman correlation and at least a 10% reduction in excess NLL versus the best non-learned baseline at two or more budgets.
- Stop condition: Stop if learned retention fails to beat raw attention at two or more budgets on the held-out split, or if scorer overhead dominates the measured KV-memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-via-learned-token-importance-scoring-931c9e98ad3f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
