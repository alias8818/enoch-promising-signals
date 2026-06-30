# Exact-Anchor Tiered KV with Int4 Gap Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-tiered-kv-with-int4-gap-compression-d7c641d6f041`
Run ID: `exact-anchor-tiered-kv-with-int4-gap-compression-d7c641d6f041-20260529T090933269992+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/65c8d6114888

## What looked useful

Tiered gap compression achieved about 3.05x compression with mean output relative L2 0.0276 on distilgpt2 KV versus direct int4 at about 3.56x compression and mean error about 0.048. On smooth synthetic AR(1) rho 0.99, stride 16 reached 3.21x compression with mean error 0.0031 versus direct int4 mean 0.0147. The same method failed on iid and alternating KV, where direct int4 was better.

## Boundaries and scale limits

No packed int4 serving kernel, no end-to-end decode latency, no perplexity/logit drift test, one small cached language model for real KV, and synthetic controls only for broader regimes.

## Claim scope

Proxy accuracy result for exact fp16 anchors plus int4 residual gap compression on synthetic KV tensors and cached distilgpt2 KV tensors. The mechanism reduces attention-output drift versus direct int4 when KV has local continuity, but is unsafe on iid or high-frequency KV.

## Why it stopped

Proxy and small-model evidence supports a conditional mechanism but is insufficient for publication-grade claims; the result also identifies clear failure regimes.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should implement an end-to-end decode/perplexity probe with packed or simulated packed tiered KV on a small causal LM and gate compression by measured layer/head smoothness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer-head adaptive tiered KV decode probe
- Success threshold: At comparable KV memory budget, adaptive tiered KV must reduce mean logit KL or perplexity delta by at least 25% versus direct int4 without more than 10% decode-time overhead in the bounded local setup.
- Stop condition: Stop if adaptive tiered KV does not beat direct int4 on logit/perplexity drift at matched memory, or if measured decode overhead exceeds 10% in the local implementation.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-tiered-kv-with-int4-gap-compression-d7c641d6f041`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
