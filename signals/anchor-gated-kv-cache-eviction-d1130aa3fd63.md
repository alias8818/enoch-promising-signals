# Anchor-Gated KV Cache Eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-gated-kv-cache-eviction-d1130aa3fd63`
Run ID: `anchor-gated-kv-cache-eviction-d1130aa3fd63-20260525T090311811262+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ebb8877a1709

## What looked useful

Anchor-H2O won 27/27 configurations on coherent span-hit rate with +0.0222 mean absolute delta versus the best non-anchor baseline. Anchor-gated policies won 27/27 configurations on first-use value retention with +0.0560 mean absolute delta. Loose value-only retention was mixed: random won 18/27 configurations, showing that anchor protection is useful for coherent retrieval spans but not sufficient as a universal value-retention metric.

## Boundaries and scale limits

Evidence is synthetic and CPU-only. No pretrained transformer, real tokenizer/document anchors, model accuracy or perplexity, serving latency, memory bandwidth, or kernel-level KV-cache measurements were tested.

## Claim scope

In a synthetic streaming KV-cache trace with planted anchor/key/value facts, anchor-gated eviction improves coherent span retention and first-use value retention versus sliding, H2O-style attention history, and random controls under equal cache budgets.

## Why it stopped

Proxy-only medium synthetic evidence supports a mechanism for coherent span and first-use retention but is mixed on loose value-only retention and lacks direct real-model validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement an actual pretrained-transformer KV eviction hook on a bounded long-context retrieval benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model anchor-gated KV eviction on bounded long-context retrieval
- Success threshold: At two or more cache budgets, anchor-gated eviction improves retrieval accuracy by at least 5 absolute percentage points over sliding and H2O-style baselines while keeping decode latency within 10% of the fastest eviction baseline.
- Stop condition: Stop if anchor-gated eviction fails to beat both sliding and H2O-style baselines on retrieval accuracy at every tested cache budget, or if eviction bookkeeping causes more than 25% decode-latency overhead.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-cache-eviction-d1130aa3fd63`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
