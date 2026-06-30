# Real llama.cpp or vLLM Length-Aware Admission Test Under Mixed-Length Queue Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-llama-cpp-or-vllm-length-aware-admission-test-under-m-c66abd8fc3`
Run ID: `real-llama-cpp-or-vllm-length-aware-admission-test-under-m-c66abd8fc3-20260621T132644143386+0000`

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

- Parent run decision: Queue-Pressure Adaptive Dynamic Batcher: enoch://control-plane/projects/queue-pressure-adaptive-dynamic-batcher-cefe431c63d5/runs/queue-pressure-adaptive-dynamic-batcher-cefe431c63d5-20260621T122812217339+0000
- Parent run decision: Token-Length-Aware Real Serving Test for Queue-Pressure Adaptive Batching: enoch://control-plane/projects/token-length-aware-real-serving-test-for-queue-pressure-ad-8b1bc1ba30/runs/token-length-aware-real-serving-test-for-queue-pressure-ad-8b1bc1ba30-20260621T124403892945+0000

## What looked useful

Across 3 fixed seeds and 792 real generations, length-aware shortest-fit admission versus FIFO count improved short p95 sojourn by 79.3%, medium p95 by 50.9%, all-request p95 by 5.2%, and reduced throughput by 3.2%, but worsened long p95 by 6.4%. FIFO token-budget without reordering was worse than baseline, supporting reordering as the mechanism but exposing fairness risk.

## Boundaries and scale limits

Single small GGUF model, single GB10 host, single llama.cpp commit, one server slot/context configuration, synthetic prompts, non-streaming /completion endpoint, and no production trace or multi-model/datacenter validation.

## Claim scope

On a locally built CUDA llama.cpp server running Gemma 3 270M Q8_0 on GB10 with 4 slots and deterministic mixed short/medium/long prompts, shortest-fit length-aware client admission reduced short and medium end-to-end sojourn tail latency while preserving most throughput, but worsened long-request p95 latency.

## Why it stopped

Medium local evidence supports a useful mechanism but is mixed and not paper-ready because the simple shortest-fit policy improves short/medium latency at the expense of long-request p95.

## Recommended next action

Run a bounded aging/deadline-aware length-admission follow-up on the same llama.cpp setup and require short/medium p95 gains without long p95 regression across at least two token budgets and two slot counts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Aging-Guarded Length-Aware Admission on Real llama.cpp Mixed-Length Serving
- Success threshold: Aging-guarded length-aware admission improves short and medium p95 sojourn by at least 30% versus FIFO count, keeps all-request throughput within 5% of FIFO count, and keeps long p95 no worse than 2% above FIFO count in every tested configuration.
- Stop condition: Stop if aging-guarded admission cannot keep long p95 within 2% of FIFO count in any token-budget/slot-count configuration, or if short/medium p95 gains fall below 30%.

## Evidence references

- Artifact root: `<local-path>/projects/real-llama-cpp-or-vllm-length-aware-admission-test-under-m-c66abd8fc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
