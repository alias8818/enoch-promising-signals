# Learned Per-Head KV Autoencoder for 125M 8K Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-per-head-kv-autoencoder-for-125m-8k-context-39b85f07a3df`
Run ID: `learned-per-head-kv-autoencoder-for-125m-8k-context-39b85f07a3df-20260528T001213923809+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8e6317e9d84d

## What looked useful

AE beat PCA on mean K and V relative MSE at both bottlenecks and reduced mean attention relative MSE from 0.0585 to 0.0408 at 4x and from 0.0881 to 0.0554 at 8x, while random projection was far worse. But AE beat PCA on K/V/attention simultaneously for only 4/12 heads and had severe stress-proxy failure on at least one early-layer head.

## Boundaries and scale limits

No true 8k-context model was trained or evaluated; 8192-position behavior was a cache-length concatenation proxy. No downstream perplexity, generation quality, or decode throughput was measured. Only 12 heads across layers 0, 5, and 11 of GPT-2 small were tested on repeated local prose.

## Claim scope

Bounded activation-level GPT-2-small probe: independent per-head nonlinear autoencoders at 4x and 8x fp32 element-count compression can beat random projection and improve mean K/V reconstruction and mean attention-output distortion versus PCA on selected real GPT-2 heads, but the improvement is not consistent across heads.

## Why it stopped

No-paper useful signal: this run is an activation-level and 8192-cache proxy, not a direct 125M 8k-context language-model validation, and head-level attention improvements are inconsistent.

## Recommended next action

Run a bounded integrated GPT-2-small compressed-KV perplexity and decode-memory benchmark against PCA/SVD and quantized-cache baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated GPT-2-small compressed-KV perplexity benchmark for per-head autoencoders
- Success threshold: AE compressed cache has <=5% perplexity degradation versus uncompressed GPT-2-small and is better than PCA/SVD at equal compression on both perplexity and attention-output distortion for at least two of three tested layers.
- Stop condition: Stop if AE compressed cache is worse than PCA/SVD on perplexity at both 4x and 8x compression or if any compression setting causes >15% perplexity degradation on the validation subset.

## Evidence references

- Artifact root: `<local-path>/projects/learned-per-head-kv-autoencoder-for-125m-8k-context-39b85f07a3df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
