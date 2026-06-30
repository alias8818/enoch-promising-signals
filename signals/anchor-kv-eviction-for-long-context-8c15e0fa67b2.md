# Anchor-KV Eviction for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-kv-eviction-for-long-context-8c15e0fa67b2`
Run ID: `anchor-kv-eviction-for-long-context-8c15e0fa67b2-20260602T101343663775+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/18f8c2625857

## What looked useful

Anchor-KV reserve improved calibrated mixed retrieval accuracy from 0.4065 for recency to 0.76125 at 64 reserved anchors, and recovered anchor retrieval from 0.0 to 1.0, while reducing recent-only retrieval from 1.0 to 0.7525. A reserve sweep showed the expected tradeoff curve.

## Boundaries and scale limits

Evidence is limited to synthetic normalized key/query vectors on 8192-token contexts with perfect anchor markers. It does not validate real transformer hidden states, learned anchor detection, multi-layer/head behavior, natural-language QA/perplexity, or production serving throughput.

## Claim scope

In a synthetic single-step retrieval benchmark with known anchor markers, reserving KV-cache slots for marked long-range anchors improves anchor-dependent and anchor-heavy mixed retrieval versus pure recency eviction under a fixed cache budget.

## Why it stopped

No-paper useful signal: this run provides proxy mechanism evidence with perfect anchor markers, not real-model or publication-grade validation.

## Recommended next action

Run a bounded direct transformer follow-up with an instrumented small autoregressive model KV cache on synthetic key-value retrieval and long-context QA, comparing recency, anchor reserve, and practical anchor-detection heuristics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Transformer Anchor-KV Eviction Benchmark
- Success threshold: Anchor-aware eviction should improve anchor-dependent retrieval or QA accuracy by at least 20 percentage points over recency at the same cache budget while losing no more than 10 percentage points on recent-only controls and adding less than 10% decode overhead.
- Stop condition: Stop if anchor-aware eviction fails to beat recency by at least 10 percentage points on direct transformer anchor-dependent tasks, or if recent-control degradation exceeds the anchor-task gain at practical reserve sizes.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-kv-eviction-for-long-context-8c15e0fa67b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
