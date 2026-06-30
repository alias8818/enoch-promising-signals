# Perplexity-Gated CPU Model Cascade

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-gated-cpu-model-cascade-d9b19d9b81d4`
Run ID: `perplexity-gated-cpu-model-cascade-d9b19d9b81d4-20260608T190942365474+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f715af5ee7e

## What looked useful

The larger CPU model was 2.40x slower per chunk and reduced test perplexity from 266.06 to 180.10, but small-model perplexity had near-zero correlation with larger-model marginal NLL gain (-0.0279). Perplexity-gated routing was slightly worse than random routing at 10%, 25%, and 50% large-model budgets.

## Boundaries and scale limits

Single corpus, n-gram language models, 240 held-out 96-token chunks, no neural transformer inference, no instruction/task quality evaluation, and no production serving load.

## Claim scope

On a bounded CPU-only word n-gram proxy using Tiny Shakespeare, raw small-model perplexity did not improve cascade routing over random routing at matched larger-model budgets, even though the validation-selected larger model improved held-out perplexity.

## Why it stopped

Bounded proxy falsified the simple perplexity-gated routing mechanism; this is not full neural validation, but it is enough to avoid claiming the idea works from small-model perplexity alone.

## Recommended next action

Stop this run as a no-paper useful negative; a bounded follow-up should test learned or margin-based routers against random controls on multiple small corpora before any neural CPU cascade scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned CPU Cascade Router Versus Perplexity-Only Routing
- Success threshold: Learned router beats random routing by at least 2% relative NLL at two or more large-model budgets without exceeding the matched CPU budget.
- Stop condition: Stop if learned-router gains are within +/-1% of random routing on all budgets or fail to replicate on a second corpus.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gated-cpu-model-cascade-d9b19d9b81d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
