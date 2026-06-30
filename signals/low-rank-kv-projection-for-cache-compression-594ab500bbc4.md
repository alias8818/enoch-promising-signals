# Low-rank KV projection for cache compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `low-rank-kv-projection-for-cache-compression-594ab500bbc4`
Run ID: `low-rank-kv-projection-for-cache-compression-594ab500bbc4-20260529T075613300120+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ab3b49546753

## What looked useful

On GPT-2, rank 32 gives only 2x KV compression but still has 0.528 mean relative attention-output MSE; rank 16 gives 4x compression with 0.775 mean relative MSE. DistilGPT-2 shows the same pattern. Full-rank controls are near exact, validating the probe.

## Boundaries and scale limits

Tested only GPT-2 and DistilGPT-2 on short text batches up to 96 tokens; did not measure end-to-end perplexity, generation quality, long-context serving, learned projections, or larger models.

## Claim scope

Naive fixed per-layer/per-head PCA projection of GPT-2-family K/V caches, without retraining, does not preserve causal self-attention outputs at useful compression ratios in this local held-out activation probe.

## Why it stopped

Proxy early falsification: direct attention-output reconstruction on real GPT-2-family activations fails at practical low ranks, but this is not a full end-to-end serving validation.

## Recommended next action

Stop this naive PCA/no-retraining variant as a no-paper useful negative; if continuing, run a bounded learned-projection fine-tuning probe with perplexity and exact KV-cache memory accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned low-rank KV projection with tiny fine-tuning objective
- Success threshold: At rank 32, held-out perplexity degradation under 2% relative and mean attention-output relative MSE under 0.10 versus exact KV; at rank 16, degradation under 5% would justify further scale-out.
- Stop condition: Stop if learned rank 32 remains above 0.20 mean attention-output relative MSE or causes more than 5% relative held-out perplexity degradation after a bounded fine-tuning run.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-kv-projection-for-cache-compression-594ab500bbc4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
