# Exact-Anchor Low-Rank KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-low-rank-kv-compression-ba9f8c415708`
Run ID: `exact-anchor-low-rank-kv-compression-ba9f8c415708-20260609T053525091299+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/df7ee48e93fd

## What looked useful

Exact anchors produced near-zero attention-output error in a lowrank-plus-anchors regime at about 3.20x compression, improved correlated-stream error modestly, failed on full-rank random KV, and reduced distilgpt2 one-step KL in several rank-16 anchored settings while lowering compression ratio.

## Boundaries and scale limits

Synthetic attention probes used tokens=1024, dim=64, three regimes, and three seeds. The pretrained-model probe used locally cached distilgpt2, three fixed prompts, and prefix lengths 128 and 256 only. The implementation reconstructs dense approximations and does not validate optimized serving latency, perplexity over a corpus, long-context generation, GPT-2-small-class robustness, or larger-model behavior.

## Claim scope

Bounded mechanism evidence on synthetic KV tensors and one-step cached distilgpt2 logits: exact anchors can substantially improve low-rank KV approximation when important tokens are sparse/outlier-like, and can modestly reduce logit drift at rank 16 on short real-model prompts.

## Why it stopped

Evidence is bounded and mixed: it supports the mechanism under structured KV and short distilgpt2 probes, but does not provide optimized-kernel, corpus-level, long-context, or larger-model validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should deepen with a corpus-level GPT-2-small/distilgpt2 perplexity and KL benchmark using deployable anchor policies at matched compression ratios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-level exact-anchor low-rank KV drift benchmark
- Success threshold: At matched compression ratio between 2x and 4x, anchored low-rank must reduce mean KL or perplexity delta by at least 25% versus plain low-rank on both tested models or context bands without degrading top-5 overlap.
- Stop condition: Stop if anchored policies fail to beat plain low-rank by 10% mean KL reduction at matched compression on the first 1000 evaluated positions, or if compression ratios cannot be matched fairly.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-low-rank-kv-compression-ba9f8c415708`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
