# Dynamic Context-Routing RAG Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-context-routing-rag-compression-732c0de21e5d`
Run ID: `dynamic-context-routing-rag-compression-732c0de21e5d-20260629T045101983139+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/95600b59db12

## What looked useful

Routing beats uncompressed top-k and weak generic compression, but a simple task-aware uniform compressor matches or beats routed answer availability at tight and medium budgets. The useful mechanism is limited to skeletonizing irrelevant chunks after required fields are preserved.

## Boundaries and scale limits

Synthetic corpus only; answer availability in packed context only; no downstream LLM generation, no real embedding retrieval, no real public QA corpus, no serving latency or cost measurements.

## Claim scope

On a deterministic synthetic two-entity RAG packing benchmark, metadata-aware routing can match a strong uniform code-preserving compressor on answer-fact availability and reduce surplus tokens only at loose budgets after perfect answer availability is already achieved.

## Why it stopped

Local synthetic evidence is useful but not paper-positive because the routed method does not outperform the strongest simple baseline on answer availability and only saves tokens in one loose-budget regime.

## Recommended next action

Run a bounded public QA/RAG follow-up comparing metadata/query-aware routing against a strong uniform query-field compressor at matched token budgets before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus routed compression versus uniform query-field compression
- Success threshold: At least a 5 percentage point absolute improvement in exact answer availability or answer accuracy over uniform query-field compression at one or more tight budgets, without worse latency-adjusted cost.
- Stop condition: Stop if uniform query-field compression matches or exceeds routed compression across tight and medium token budgets, or if routing overhead erases token savings.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-context-routing-rag-compression-732c0de21e5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
