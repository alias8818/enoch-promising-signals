# Shared KV-Cache Across Cascade Tiers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `shared-kv-cache-across-cascade-tiers-9f1ce49c7291`
Run ID: `shared-kv-cache-across-cascade-tiers-9f1ce49c7291-20260601T021358534903+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/02a91e825c70

## What looked useful

KV sharing should be treated as an architectural co-design/tied-projection constraint, not a drop-in optimization for arbitrary existing cascade tiers. Across five seeds, independent tiers had mean attention-output relative RMSE 1.409 with raw sharing and 0.981 with linear adapters; tied K/V projections were exactly lossless.

## Boundaries and scale limits

No full LLM, no multi-layer accumulation, no autoregressive quality, no real cascade acceptance dynamics, and no GPU serving latency were measured.

## Claim scope

Single-layer synthetic attention probe: cross-tier KV-cache sharing is lossless with identical K/V projections, but produces large attention-output mismatch for independently initialized tiers; simple linear adapters do not make independent tiers safe.

## Why it stopped

Proxy mechanism evidence supports a conditional design constraint but does not provide full validation or a paper-ready result.

## Recommended next action

Stop this run as a bounded no-paper useful signal; next, test a tiny two-tier transformer with tied versus independent K/V projections on real token sequences.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Validation of Tied Cross-Tier KV Sharing
- Success threshold: Tied-K/V shared-cache variant has next-token KL delta below 0.01 or perplexity increase below 1% while reducing two-tier K/V memory by at least 35%; independent-control variant fails the same quality threshold.
- Stop condition: Stop if tied-K/V sharing exceeds the quality threshold in two independent seeds or if memory/latency savings disappear after implementation overhead.

## Evidence references

- Artifact root: `<local-path>/projects/shared-kv-cache-across-cascade-tiers-9f1ce49c7291`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
