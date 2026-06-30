# INT8 Delta KV from Exact Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-delta-kv-from-exact-anchors-864a68116bfd`
Run ID: `int8-delta-kv-from-exact-anchors-864a68116bfd-20260604T104613736363+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2322373383a0

## What looked useful

Exact anchors lower delta dynamic range and attention error on smooth traces: best interval 4 reduced mean relative attention L2 to 0.150x of standard INT8 on smooth_ar and 0.278x on piecewise_jump, but with compression 1.585x versus 1.969x for standard INT8. On iid_gaussian the best anchored setting was 1.203x worse in mean attention error and still less compressed.

## Boundaries and scale limits

No pretrained LLM KV traces, perplexity/task metrics, decode throughput, real kernels, or long-context serving measurements were run. This is CPU-only synthetic evidence and is not paper-ready.

## Claim scope

Synthetic NumPy causal-attention tests at seq=512, dim=128, 5 seeds show fixed exact-anchor INT8 deltas reduce attention-output error versus per-token INT8 only when KV-like traces have strong local temporal smoothness; they are worse on IID KV-like traces and always carry anchor storage overhead.

## Why it stopped

Synthetic bounded evidence supports a conditional mechanism but falsifies the fixed-anchor scheme as a robust general KV-cache replacement; full validation would require real model traces and decode metrics.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the concrete next test is a bounded pretrained-model KV trace study with adaptive smoothness-gated fallback to standard INT8.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive exact-anchor INT8 deltas on pretrained decoder KV traces
- Success threshold: At comparable compression within 5 percent of standard INT8, adaptive anchored deltas reduce mean attention-output error or logit drift by at least 25 percent on real-model traces without worse p95 error.
- Stop condition: Stop if real-model KV blocks are not locally smooth enough for adaptive anchoring or if fallback overhead eliminates the error/compression advantage versus standard INT8.

## Evidence references

- Artifact root: `<local-path>/projects/int8-delta-kv-from-exact-anchors-864a68116bfd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
