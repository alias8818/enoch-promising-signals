# Token-Length-Aware Real Serving Test for Queue-Pressure Adaptive Batching

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `token-length-aware-real-serving-test-for-queue-pressure-ad-8b1bc1ba30`
Run ID: `token-length-aware-real-serving-test-for-queue-pressure-ad-8b1bc1ba30-20260621T124403892945+0000`

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

- Parent run decision: Queue-Pressure Adaptive Dynamic Batcher: enoch://control-plane/projects/queue-pressure-adaptive-dynamic-batcher-cefe431c63d5/runs/queue-pressure-adaptive-dynamic-batcher-cefe431c63d5-20260621T122812217339+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6677ab870bb4

## What looked useful

Across five 192-request repeats, length-aware batching improved generated-token throughput by a mean 87.7% with a minimum 82.3% gain, reduced short-request p95 latency by a mean 89.8%, and reduced mean padding waste ratio from 1.499 to 0.177.

## Boundaries and scale limits

Small controllable PyTorch decoder-like workload only; not a production llama.cpp/vLLM/SGLang scheduler patch, not live HTTP traffic, and not a full LLM quality-preserving serving benchmark.

## Claim scope

In a controlled GB10 CUDA serving harness with mixed prompt/output lengths and high queue pressure, token-length-aware wave batching reduced padding waste and improved generated-token throughput versus FIFO fixed request-count batching without hurting short-request p95 latency.

## Why it stopped

No-paper closure: Tier 1 mechanism support is positive, but evidence is from a controlled CUDA harness rather than a production LLM server.

## Recommended next action

Run a bounded deepen test by implementing the same length-aware admission rule in a real local llama.cpp or vLLM serving path and replaying a live concurrent mixed-length client trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real llama.cpp or vLLM Length-Aware Admission Test Under Mixed-Length Queue Pressure
- Success threshold: At least 10% generated-token throughput improvement over FIFO with non-worse short-request p95 and no more than 5% long-request p95 regression across at least three trace permutations.
- Stop condition: Stop if the production server cannot expose/control admission order safely, or if two controlled traces show less than 5% throughput gain or unacceptable long-request tail-latency regression.

## Evidence references

- Artifact root: `<local-path>/projects/token-length-aware-real-serving-test-for-queue-pressure-ad-8b1bc1ba30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
