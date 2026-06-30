# CPU inference integration test for anchor-aware KV eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-inference-integration-test-for-anchor-aware-kv-evictio-2a96ab7139`
Run ID: `cpu-inference-integration-test-for-anchor-aware-kv-evictio-2a96ab7139-20260629T035012180393+0000`

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

- Parent run decision: Anchor-Aware KV Eviction for CPU Long-Context Inference: enoch://control-plane/projects/anchor-aware-kv-eviction-for-cpu-long-context-inference-23c31c04429b/runs/anchor-aware-kv-eviction-for-cpu-long-context-inference-23c31c04429b-20260629T032951997781+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed224b707225

## What looked useful

Across 240 cases, anchor-aware eviction achieved aggregate anchor accuracy of 0.950, 1.000, and 1.000 at budgets 32, 64, and 128, versus 0.000, 0.000, and 0.250 for FIFO/sliding-window and 0.000, 0.000, and 0.250 for recency-importance. Budget-32 overcommit control produced the expected anchor-aware failure boundary at 0.800 anchor accuracy for that task.

## Boundaries and scale limits

Proxy-only evidence: no real transformer model, tokenizer, logits, multi-head/multi-layer KV cache, or production CPU inference engine was tested. The smallest-budget overcommit control shows anchor-aware accuracy falls when anchors alone exceed cache capacity.

## Claim scope

In a deterministic CPU KV-cache simulator with synthetic anchor and recent-fact probes, anchor-aware eviction preserves early anchor rows far better than FIFO, sliding-window, and recency-importance baselines at matched cache budgets.

## Why it stopped

Stopped after bounded CPU proxy evidence: the mechanism is supported in a simulator, but this is not full validation or paper-ready inference evidence.

## Recommended next action

Implement the same anchor-aware eviction rule in a real CPU transformer inference path and compare anchor-critical QA/logit accuracy plus latency and memory overhead against sliding-window eviction at matched KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU transformer anchor-aware KV eviction test
- Success threshold: At least 20 percentage-point anchor-critical accuracy improvement over sliding-window at one constrained budget, with recent-critical accuracy degradation below 5 percentage points and latency overhead below 15% on CPU.
- Stop condition: Stop if real-model anchor-critical improvement is below 5 percentage points at all tested budgets or latency overhead exceeds 25% without a compensating accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-inference-integration-test-for-anchor-aware-kv-evictio-2a96ab7139`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
