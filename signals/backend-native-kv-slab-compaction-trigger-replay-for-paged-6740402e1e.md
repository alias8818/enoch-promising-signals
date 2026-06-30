# Backend-native KV slab compaction trigger replay for paged attention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `backend-native-kv-slab-compaction-trigger-replay-for-paged-6740402e1e`
Run ID: `backend-native-kv-slab-compaction-trigger-replay-for-paged-6740402e1e-20260630T091832079354+0000`

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

- Parent run decision: KV-Cache Slab Compaction for Long-Context Inference on GB10: enoch://control-plane/projects/kv-cache-slab-compaction-for-long-context-inference-on-gb10-e09fede454f1/runs/kv-cache-slab-compaction-for-long-context-inference-on-gb10-e09fede454f1-20260630T081604516527+0000
- Parent run decision: GB10 paged-attention decode harness for KV slab compaction triggers: enoch://control-plane/projects/gb10-paged-attention-decode-harness-for-kv-slab-compaction-850339c9b5/runs/gb10-paged-attention-decode-harness-for-kv-slab-compaction-850339c9b5-20260630T085822114994+0000

## What looked useful

Trigger replay looks useful as a metadata-work reduction mechanism, but the proxy exposes a move-amplification risk that could erase the benefit in real serving unless copy scheduling or trigger thresholds are tuned.

## Boundaries and scale limits

CPU-only simulator; no real GPU KV copies, no production request trace, no integration with vLLM/TensorRT-LLM/SGLang paged-attention backends, and no end-to-end latency or throughput measurement.

## Claim scope

In a deterministic synthetic paged-attention KV slab allocator simulator, backend-local trigger replay reduced slab metadata scans by 96.97% to 99.83% versus scan-based policies and reduced average live slabs by 1.85% to 3.83%, but increased live page moves by 2.19x to 214.48x depending on workload and baseline.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal but not direct backend evidence; the proxy also showed substantial live-page move amplification.

## Recommended next action

Implement a bounded backend microbenchmark in a real paged-attention allocator that replays sparse-slab triggers and measures p95 decode latency, GPU copy bytes, average KV footprint, and compactor CPU time against the current allocator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Backend KV trigger replay microbenchmark with measured copy latency
- Success threshold: At least 50% lower compactor CPU metadata time and at least 2% lower average KV footprint with p95 decode latency no more than 2% worse than baseline on a reproducible trace.
- Stop condition: Stop if trigger replay increases p95 decode latency by more than 5% or KV copy bytes by more than 25% without at least 2% average footprint reduction.

## Evidence references

- Artifact root: `<local-path>/projects/backend-native-kv-slab-compaction-trigger-replay-for-paged-6740402e1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
