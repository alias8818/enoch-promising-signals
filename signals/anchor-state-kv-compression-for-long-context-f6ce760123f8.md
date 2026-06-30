# Anchor-State KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-state-kv-compression-for-long-context-f6ce760123f8`
Run ID: `anchor-state-kv-compression-for-long-context-f6ce760123f8-20260525T153922104824+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccacb4f92101

## What looked useful

Anchor-state KV compression is promising as a conditional sparse long-context retrieval policy when anchor positions are known, but the evidence argues against claiming a universal KV compression improvement; pure segment means were better on neutral random attention.

## Boundaries and scale limits

No real transformer perplexity, long-context QA, learned anchor selection, multi-layer accumulation, production KV cache implementation, or full serving benchmark was tested. Sequence lengths were 2048-8192 with d_model 128 and synthetic known anchors.

## Claim scope

Synthetic single-head attention probe: exact retention of known old anchor KV plus non-anchor segment means preserves anchor-targeted retrieval and attention outputs much better than recent, uniform exact, or pure segment-mean compression at 9.3x to 37.3x mean compression, but is not generally best for neutral random attention.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct model-level evidence; stopping as no-paper evidence rather than presenting proxy-only results as validation.

## Recommended next action

Run a bounded deepen follow-up implementing the policy in a GPT-2-small-class or comparable small transformer and compare real retrieval/perplexity against recency, uniform exact, and segment-summary KV baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-level anchor-state KV compression on small long-context retrieval tasks
- Success threshold: At equal KV budget, anchor-state compression improves long-context retrieval accuracy by at least 10 percentage points over the best non-anchor baseline while keeping perplexity/loss degradation within 5 percent on the non-retrieval control.
- Stop condition: Stop if anchor-state compression fails to beat the best equal-budget baseline on retrieval or causes more than 5 percent loss/perplexity degradation on the control workload.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-state-kv-compression-for-long-context-f6ce760123f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
