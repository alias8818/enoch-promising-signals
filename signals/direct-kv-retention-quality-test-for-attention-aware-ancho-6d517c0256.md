# Direct KV-retention quality test for attention-aware anchors on small GPT traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-kv-retention-quality-test-for-attention-aware-ancho-6d517c0256`
Run ID: `direct-kv-retention-quality-test-for-attention-aware-ancho-6d517c0256-20260520T044306708618+0000`

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

- Parent run decision: AnchorKV: Exact Anchor Partitioning for Block-wise KV Compression: enoch://control-plane/projects/anchorkv-exact-anchor-partitioning-for-block-wise-kv-compression-9f35f827e683/runs/anchorkv-exact-anchor-partitioning-for-block-wise-kv-compression-9f35f827e683-20260519T223326083038+0000
- Parent run decision: Attention-aware exact anchor partitioning on real small-model KV traces: enoch://control-plane/projects/attention-aware-exact-anchor-partitioning-on-real-small-mo-7f8e4eda74/runs/attention-aware-exact-anchor-partitioning-on-real-small-mo-7f8e4eda74-20260520T043736710025+0000

## What looked useful

Direct cache-slicing evidence supports attention-aware anchors as a mechanism: oracle attention retention reduced KL versus sink+recency from 7.201 to 1.523 at 64 tokens/12.5% budget and from 5.738 to 0.125 at 128 tokens/50% budget, with matching improvements in top-1 agreement. However, the deployable prefix-attention proxy remained much weaker, so this is not paper-ready.

## Boundaries and scale limits

Only GPT-2 small, short contexts, local natural-text snippets, and single-step cache slicing were tested. The best policy is an oracle diagnostic that uses final full-cache attention; no online retention method, long-context generation, larger model, or broad corpus validation was demonstrated.

## Claim scope

On GPT-2-small-class single-step traces with 64- and 128-token contexts, oracle final-query attention anchors preserve next-token logits substantially better than recency, random, sink+recency, and ablated attention-retention policies at equal KV budgets.

## Why it stopped

Tier 2 direct evidence produced a useful mechanism signal but also showed the available online proxy is insufficient, so this run should close as no-paper rather than continue as a positive result.

## Recommended next action

Run one bounded deepen test of an online anchor predictor using sink tokens plus previous-step or query-proxy attention; stop if it cannot beat sink+recency and close at least half the KL gap from prefix_attention to attention_oracle.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online predictor for attention-aware KV anchors on GPT-2 traces
- Success threshold: Across 64- and 128-token contexts and 12.5%, 25%, and 50% budgets, the online policy must beat sink+recency on mean KL in at least 5 of 6 cells and close at least 50% of the mean KL gap between prefix_attention and attention_oracle.
- Stop condition: Stop as negative if the online policy fails to beat sink+recency in at least 4 of 6 aggregate cells or improves mainly by retaining sink tokens without query-aware selection.

## Evidence references

- Artifact root: `<local-path>/projects/direct-kv-retention-quality-test-for-attention-aware-ancho-6d517c0256`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
