# Exact-Anchor KV Compression for CPU Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-kv-compression-for-cpu-long-context-9d64efbf542a`
Run ID: `exact-anchor-kv-compression-for-cpu-long-context-9d64efbf542a-20260629T060212328418+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a3c7fc187826

## What looked useful

Exact-anchor KV preservation achieved 100% true-anchor retrieval and full-attention label agreement at 64x compression on the calibrated synthetic task. Budget-matched uniform compression reached 0.59% and sliding-window plus block compression reached 0.78%. With 20% anchor misses, exact-anchor accuracy fell to 79.1%, showing dependence on anchor identification recall.

## Boundaries and scale limits

No end-to-end language model, tokenizer-derived anchors, multi-layer KV scheduling, real decode loop, or publication-grade corpus evaluation was tested. Evidence is CPU-only synthetic mechanism evidence.

## Claim scope

In a deterministic synthetic single-layer attention benchmark with 65,536 context slots, 512 marked anchors, and 512 anchor-recall queries, preserving anchor K/V rows exactly while block-compressing non-anchor rows preserved anchor retrieval at 64x slot compression better than budget-matched uniform or recency-only compression.

## Why it stopped

No-paper closure: this run produced useful synthetic mechanism evidence, but it is proxy evidence rather than direct end-to-end transformer validation.

## Recommended next action

Implement a bounded real-model KV-cache intervention on a small transformer and compare exact-anchor compression against equal-memory uniform and recency controls on long-range retrieval plus perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model exact-anchor KV cache intervention on a small transformer
- Success threshold: At the same KV memory budget, exact-anchor compression improves long-range retrieval accuracy by at least 20 percentage points over both controls without more than 5% relative perplexity degradation versus full KV on the evaluated contexts.
- Stop condition: Stop if equal-memory exact-anchor compression fails to beat both controls on retrieval accuracy or causes more than 5% relative perplexity degradation in two independent seeds/tasks.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-cpu-long-context-9d64efbf542a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
