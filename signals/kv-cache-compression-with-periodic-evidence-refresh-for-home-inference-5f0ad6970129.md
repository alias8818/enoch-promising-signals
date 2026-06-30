# KV Cache Compression with Periodic Evidence Refresh for Home Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-with-periodic-evidence-refresh-for-home-inference-5f0ad6970129`
Run ID: `kv-cache-compression-with-periodic-evidence-refresh-for-home-inference-5f0ad6970129-20260607T214055271305+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bf7bbd7d1a18

## What looked useful

Periodic exact evidence anchors improved the naive compressed KV mechanism, especially at 64-token and 32-token recent windows, but mean delta NLL remained 7.97 at 0.57 cache-token ratio and 4.57 even at 0.80 ratio; top-1 match was at most 66.7%.

## Boundaries and scale limits

Single small pretrained GPT-2-style model; CPU-only; one-step logits only; three embedded technical texts repeated to bounded length; no recursive generation, chat tuning, 7B-class model, home GPU/NPU latency, or factual-recall benchmark.

## Claim scope

On distilgpt2 one-step next-token cache replay over 18 prefix samples up to 384 tokens, fixed periodic exact anchors reduce NLL/KL drift versus recent-only or block-pooled KV compression, but absolute drift remains too high for a practical home-inference cache-compression claim.

## Why it stopped

Bounded direct-cache evidence supports the anchor mechanism directionally but early-falsifies the practical viability of this naive fixed periodic refresh variant because absolute NLL/KL drift is large.

## Recommended next action

Stop this fixed-period/block-mean variant as no-paper evidence; a bounded follow-up should test salience-selected exact anchors rather than periodic anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Salience-Selected Evidence Anchors for Compressed KV Cache
- Success threshold: At matched compressed/full cache-token ratio between 0.50 and 0.65, salience anchors reduce mean KL by at least 50% versus fixed periodic anchors and keep top-1 match at or above 60% with no catastrophic delta-NLL outliers above 5 on the bounded benchmark.
- Stop condition: Stop if salience-selected anchors do not beat fixed periodic anchors by at least 25% mean KL at matched cache ratio or still show repeated delta-NLL outliers above 10.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-with-periodic-evidence-refresh-for-home-inference-5f0ad6970129`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
