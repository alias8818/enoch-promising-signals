# Anchor-Gated KV Compression: Exact Anchors with Interleaved Compressed State

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-gated-kv-compression-exact-anchors-with-interleaved-compressed-state-35d0265a341c`
Run ID: `anchor-gated-kv-compression-exact-anchors-with-interleaved-compressed-state-35d0265a341c-20260524T062932842792+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/81f1d9eb3e82

## What looked useful

At 8x KV-slot compression, exact-anchor interleaving with 50% anchor slots preserved anchor target top-1 at 1.000 and reduced all-query MSE versus full attention to 0.004014, while block-mean compression had 0.000 anchor top-1 and 0.007778 MSE. Non-anchor top-1 stayed 0.000 for all compressed exact-anchor variants.

## Boundaries and scale limits

No trained decoder, no learned anchor policy, no natural-language perplexity/task evaluation, no dynamic serving cache implementation, and no comparison against production KV-compression baselines beyond block-mean summaries.

## Claim scope

Synthetic attention-cache retrieval with sequence length 4096, dimension 128, 512 queries, five seeds, and matched compressed KV-slot budgets on GB10. Exact anchors plus interleaved summaries preserve covered anchor retrieval and reduce output MSE versus block-mean compression, but do not recover exact non-anchor retrieval.

## Why it stopped

No-paper useful signal: the mechanism works for covered synthetic anchors but remains proxy-only and fails exact retrieval for non-anchor tokens.

## Recommended next action

Run a bounded trained or pretrained decoder follow-up that learns or applies an anchor-selection policy and measures perplexity/task quality plus decode throughput against full KV and stronger compression baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned anchor selection for exact-anchor interleaved KV compression in a small decoder
- Success threshold: At 8x KV-cache compression, exact-anchor interleaving should recover at least 80% of full-KV task quality or keep perplexity degradation under 10% while outperforming summary-only compression by at least 20% relative error and preserving a decode-memory reduction.
- Stop condition: Stop if learned or heuristic anchors fail to cover at least 80% of retrieval-critical positions or if quality is not materially better than summary-only compression at the same KV budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-compression-exact-anchors-with-interleaved-compressed-state-35d0265a341c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
