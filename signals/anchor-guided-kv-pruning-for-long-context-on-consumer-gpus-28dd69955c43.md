# Anchor-Guided KV Pruning for Long Context on Consumer GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-guided-kv-pruning-for-long-context-on-consumer-gpus-28dd69955c43`
Run ID: `anchor-guided-kv-pruning-for-long-context-on-consumer-gpus-28dd69955c43-20260603T215043787610+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3b9552bce518

## What looked useful

At 16k context with 1,024 KV budget, anchor-guided pruning reduced relative output error to 0.3284 versus 0.8258 for recency and 0.6673 for heavy-hitter while retaining 74.4% full-attention mass. At 32k, anchor-guided error was 0.6721 versus 0.9180 for recency. A bad-anchor local-only control reversed the result: anchor-guided error was 0.8916 versus 0.3942 for recency, showing anchor reliability is critical.

## Boundaries and scale limits

No trained LLM integration, no real prompt/perplexity/retrieval-QA evaluation, no multi-layer cache interaction, and no online anchor discovery cost measured. Contexts were synthetic 16k to 32k with 512 evaluation queries.

## Claim scope

Synthetic GPU attention replay on GB10 shows anchor-guided KV pruning can preserve full-attention outputs better than recency, uniform stride, and calibration-heavy-hitter baselines at equal KV budgets when future queries depend on valid sparse long-range anchors.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic attention-mechanism validation, not direct end-to-end LLM quality validation.

## Recommended next action

Run a bounded deepen follow-up that integrates online anchor selection and KV eviction into a small causal LM decode path, then compare retrieval QA or perplexity, memory, and latency against recency and heavy-hitter baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online Anchor-Guided KV Eviction in a Small Causal LM
- Success threshold: At 16k or larger context and at least 90% KV reduction, anchor-guided eviction improves retrieval accuracy or perplexity versus recency and heavy-hitter baselines while keeping decode latency within 10% of the fastest pruned baseline.
- Stop condition: Stop if online anchor-guided eviction does not beat recency on real prompt quality metrics, or if anchor selection overhead eliminates the latency benefit at the tested KV budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-guided-kv-pruning-for-long-context-on-consumer-gpus-28dd69955c43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
