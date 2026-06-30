# Real GPT-2 KV-trace test of causal attention x residual allocation against norm allocation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-gpt-2-kv-trace-test-of-causal-attention-x-residual-al-60f60ea257`
Run ID: `real-gpt-2-kv-trace-test-of-causal-attention-x-residual-al-60f60ea257-20260522T210402648424+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Causal attention-predicted residual KV allocation with metadata-inclusive bit budget: enoch://control-plane/projects/causal-attention-predicted-residual-kv-allocation-with-met-23e9d18730/runs/causal-attention-predicted-residual-kv-allocation-with-met-23e9d18730-20260522T205711963114+0000
- Parent run decision: Attention-aware residual codebooks with per-channel scaling for sub-2-bit KV cache: enoch://control-plane/projects/attention-aware-residual-codebooks-with-per-channel-scalin-0c15c7b71f/runs/attention-aware-residual-codebooks-with-per-channel-scalin-0c15c7b71f-20260522T204150870196+0000

## What looked useful

Across 16,709 WikiText KV-path ablations, signed KV-trace achieved mean within-prompt Pearson 0.9485 and Spearman 0.8494 against direct causal logit effects, with top-5 positive precision 0.983. Norm allocation was near zero/negative on correlation and captured much less positive effect mass.

## Boundaries and scale limits

Validated on GPT-2-small only, 64-token context cap, 200 WikiText prompt samples across two fixed seeds plus embedded prompt checks; candidate ablations were method-enriched plus random rather than exhaustive over all paths, and no larger model families, long-context settings, or downstream pruning/editing tasks were tested.

## Claim scope

Within pretrained GPT-2-small on bounded WikiText-2 next-token contexts, signed causal-attention x residual KV-trace predicts measured final-query KV-path ablation effects far better than norm-only, attention-only, unsigned trace, or random allocation controls.

## Why it stopped

Bounded local evidence supports the mechanism but is not broad enough for publication-grade claims about general residual allocation or practical model intervention utility.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up would test exhaustive or wider sampled KV-path ablations across more corpora and at least one additional GPT-2-class model size.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Broader GPT-2 KV-trace ablation validation across corpora and model sizes
- Success threshold: Signed KV-trace mean within-prompt Spearman exceeds norm and attention baselines by at least 0.25 on each corpus/model condition, and top-5 positive effect share is at least 2x the norm baseline in the aggregate.
- Stop condition: Stop if the advantage falls below the threshold on any added corpus/model condition or if exhaustive/wider ablations show the current method-enriched candidate set materially overstated the effect.

## Evidence references

- Artifact root: `<local-path>/projects/real-gpt-2-kv-trace-test-of-causal-attention-x-residual-al-60f60ea257`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
