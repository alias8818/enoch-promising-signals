# Cumulative Attention Score KV Eviction for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cumulative-attention-score-kv-eviction-for-long-context-e0fcc4af2476`
Run ID: `cumulative-attention-score-kv-eviction-for-long-context-e0fcc4af2476-20260528T181521111518+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9412444b7082

## What looked useful

Cumulative score alone hoards old high-score tokens and evicts recent tokens before they can accumulate attention credit, producing very low retained attention mass and high top-1 miss rates. A protected recent window is required before cumulative scoring becomes competitive, and decay makes the hybrid mostly recency-equivalent.

## Boundaries and scale limits

No pretrained transformer traces, perplexity, generation quality, serving latency, or hardware KV-cache measurements were run. The result is a mechanism-level proxy, not full long-context model validation.

## Claim scope

Pure cumulative-attention KV eviction, evaluated as an online cache policy on synthetic causal attention traces with sequence length 1024 and capacities 64, 128, and 256, is consistently dominated by a sliding-window recency baseline. A recent-window plus decayed-cumulative hybrid only matches recency-level behavior in this proxy.

## Why it stopped

Proxy early falsification of pure cumulative-attention KV eviction; not a full model-level validation.

## Recommended next action

Stop this no-paper run; only revisit with a bounded real-attention replay that tests decayed cumulative scoring as a secondary selector behind a protected recent window against recency/sink baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay decayed cumulative KV eviction on real pretrained-transformer attention traces
- Success threshold: Decayed cumulative behind a protected recent window improves retained attention mass by at least 3% relative and does not worsen perplexity or next-token loss versus sink+recency at the same KV budget.
- Stop condition: Stop if decayed cumulative fails to beat sink+recency by 1% retained attention mass on real traces or worsens perplexity at matched KV budget.

## Evidence references

- Artifact root: `<local-path>/projects/cumulative-attention-score-kv-eviction-for-long-context-e0fcc4af2476`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
