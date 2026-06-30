# Learned vs Uniform Anchor Placement for KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-vs-uniform-anchor-placement-for-kv-compression-33ffbc53a661`
Run ID: `learned-vs-uniform-anchor-placement-for-kv-compression-33ffbc53a661-20260529T042003274148+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/363be791c845

## What looked useful

Non-uniform learned anchor placement is plausible at low cache budgets, especially where attention mass concentrates in early positions, but this simple learned rule is not a robust replacement for uniform placement across layers and budgets.

## Boundaries and scale limits

Trace reconstruction only; no end-to-end compressed KV-cache generation, no perplexity or latency measurement, only GPT-2 small, two layers, two seeds, one dataset, and sequence length 192.

## Claim scope

On GPT-2 small WikiText-2 attention traces at sequence length 192, an offline attention-mass anchor selector improves held-out full-attention output relative MSE versus uniform anchors in layer 0 and at 8/16-anchor budgets in layer 5, but does not consistently improve cosine similarity or the 32-anchor layer-5 case.

## Why it stopped

The result is a bounded trace-level mixed signal, not a full validation: learned anchors beat uniform on relative MSE in several small settings but lose or become negligible in deeper/high-budget settings and were not tested end to end.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should evaluate end-to-end compressed KV-cache generation with per-layer/head learned anchors against uniform at equal cache budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end learned anchor KV-cache compression on GPT-2 small
- Success threshold: At two or more anchor budgets, learned anchors must improve held-out next-token KL or perplexity by at least 5% relative to uniform compression error without reducing generation throughput at the same cache size.
- Stop condition: Stop if learned anchors fail to beat uniform on end-to-end KL/perplexity in GPT-2 small at two anchor budgets, even if trace reconstruction improves.

## Evidence references

- Artifact root: `<local-path>/projects/learned-vs-uniform-anchor-placement-for-kv-compression-33ffbc53a661`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
