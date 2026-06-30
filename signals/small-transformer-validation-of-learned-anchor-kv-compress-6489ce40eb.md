# Small Transformer Validation of Learned Anchor KV Compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-transformer-validation-of-learned-anchor-kv-compress-6489ce40eb`
Run ID: `small-transformer-validation-of-learned-anchor-kv-compress-6489ce40eb-20260520T070748393154+0000`

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

- Parent run decision: Learnable Anchor Tokens with Compressed KV Buffer: enoch://control-plane/projects/learnable-anchor-tokens-with-compressed-kv-buffer-7b70966d0206/runs/learnable-anchor-tokens-with-compressed-kv-buffer-7b70966d0206-20260520T070003438189+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/cd36c05e0d83

## What looked useful

Learned budget-4 anchors reduced KL to the full-cache model versus fixed budget-4 controls and slightly improved accuracy, but preserved only 35.2% of full-cache accuracy and beat the best fixed budget-4 accuracy by only 0.5 points, missing the predeclared 80% preservation and 5-point advantage thresholds.

## Boundaries and scale limits

Toy synthetic task, short context, CPU-scale training, final-token-only evaluation, no natural-language corpus, no GPT-2-small-class baseline, no multi-token generation cache benchmark, and only a simple query-independent learned anchor formulation.

## Claim scope

Small direct controlled validation on a 2-layer 64-dimensional causal transformer trained to 100% held-out accuracy on an 8-key unique associative-recall task; learned query-independent anchor KV summaries were evaluated only for final-token compressed decoding at budgets 4 and 8.

## Why it stopped

Direct small validation failed the stated accuracy-preservation threshold despite a valid full-cache baseline and matched fixed compression controls.

## Recommended next action

Stop this formulation as no-paper evidence; if continuing, test a query-conditioned anchor compressor on the same unique-key recall task before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Query-Conditioned Anchor KV Compression on Unique-Key Recall
- Success threshold: At budget 4, learned query-conditioned anchors preserve at least 80% of full-cache accuracy, beat the best fixed budget-4 accuracy by at least 5 points, and reduce KL to full-cache logits versus the best fixed budget-4 KL baseline.
- Stop condition: Stop if learned query-conditioned anchors miss either the 80% full-cache accuracy preservation threshold or the 5-point advantage over fixed controls after a valid dense baseline is established.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-validation-of-learned-anchor-kv-compress-6489ce40eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
