# Real-model batched KV-cache n-gram speculative serving validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `real-model-batched-kv-cache-n-gram-speculative-serving-val-3697c35d07`
Run ID: `real-model-batched-kv-cache-n-gram-speculative-serving-val-3697c35d07-20260527T013607928313+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Batched fp16/bf16 KV-cache n-gram speculative serving test: enoch://control-plane/projects/batched-fp16-bf16-kv-cache-n-gram-speculative-serving-test-73df4b00e0/runs/batched-fp16-bf16-kv-cache-n-gram-speculative-serving-test-73df4b00e0-20260526T190441243998+0000
- Parent run decision: KV-cache serving benchmark for n-gram draft-free speculative decoding: enoch://control-plane/projects/kv-cache-serving-benchmark-for-n-gram-draft-free-speculati-fba5b4b00b/runs/kv-cache-serving-benchmark-for-n-gram-draft-free-speculati-fba5b4b00b-20260525T131701548243+0000

## What looked useful

Bounded direct validation supports the mechanism: multi-token n-gram draft acceptance reduces forward calls per generated token and yields 1.35x-2.55x mean speedups on repetitive/mixed GPT-2 float32 batched KV-cache decoding, while a draft_len=1 ablation is slower and adversarial heterogeneous batches can lose speed due to synchronized commit stalls.

## Boundaries and scale limits

One GPT-2-class model, local synthetic/text prompt suites, float32 exact validation only, no production trace replay, no 7B+ model, no vLLM/TensorRT-LLM integration, and conservative synchronized batch commit rather than per-row production cache scheduling. BF16 calibration showed rare exact-token divergences at batch 8.

## Claim scope

On GPT-2 float32 running on a GB10 GPU, an exact synchronized batched KV-cache n-gram prompt-lookup speculative decoder with ngram=3 and draft_len=4 matched greedy decoding exactly and improved mean throughput across local repetitive, mixed, and shuffled adversarial prompt suites at batch sizes 1, 4, 8, and 16, with strongest and most stable gains on repetitive/mixed prompts.

## Why it stopped

Tier-3 bounded local validation produced a useful direct mechanism signal, but evidence is not broad or production-grade enough for publication readiness.

## Recommended next action

Do not write a paper from this run; next, implement per-row cache compaction or request grouping and validate BF16 exact/approximate behavior on a real serving stack with natural traffic traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-row batched KV-cache scheduling for n-gram speculative serving
- Success threshold: At least 1.25x mean throughput speedup over greedy KV baseline with no worse than 1% p95 latency regression and exact or predeclared acceptable output equivalence on heterogeneous batch-8 and batch-16 trace workloads.
- Stop condition: Stop if BF16 exactness cannot be maintained or bounded as acceptable, or if per-row/grouped scheduling fails to beat the greedy KV baseline by 1.10x mean throughput on mixed natural traces.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-batched-kv-cache-n-gram-speculative-serving-val-3697c35d07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
