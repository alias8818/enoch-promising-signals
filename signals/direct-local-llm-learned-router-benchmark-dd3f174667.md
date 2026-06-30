# Direct Local LLM Learned Router Benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-local-llm-learned-router-benchmark-dd3f174667`
Run ID: `direct-local-llm-learned-router-benchmark-dd3f174667-20260610T152142441710+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Learned Task-Complexity Router for Local Cascade: enoch://control-plane/projects/learned-task-complexity-router-for-local-cascade-5cc4a7f7f200/runs/learned-task-complexity-router-for-local-cascade-5cc4a7f7f200-20260610T113441810110+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc32965b9de5

## What looked useful

The learned router matched Qwen fixed routing at 0.6944 held-out accuracy and 0.0930 s mean latency, with bootstrap learned-minus-best-fixed accuracy delta exactly 0.0. Phi scored 0.0 and never beat Qwen in train or test, so even the oracle router had no headroom.

## Boundaries and scale limits

Small exact-answer workload only; two local GGUF backends; one deterministic decoding configuration; no open-ended human/LLM-judge quality labels; no repeated model pairs or seeds beyond deterministic task generation and one train/test split.

## Claim scope

For a 90-prompt controlled exact-answer benchmark using local llama-server inference over Phi-4-mini-instruct-Q4_K_M and Qwen2.5-7B-Instruct-Q4_K_M, a learned logistic router did not improve accuracy or latency over the best fixed backend.

## Why it stopped

Direct Tier 1 controlled local LLM test falsified the improvement threshold for this backend pair: learned routing gave no gain over best fixed routing, and the second backend was invalid/dominated under the local serving stack.

## Recommended next action

Stop this backend-pair claim; a retry should first require two smoke-verified local backends with complementary wins before training a learned router.

## Follow-up

- Recommended: `true`
- Type: `retry`
- Title: Healthy Complementary Local Backend Router Test
- Success threshold: Learned router improves held-out accuracy by >= 5 percentage points over the best fixed backend, bootstrap p05 delta > 0, and mean latency is <= always-slower-backend latency.
- Stop condition: Stop early if either backend fails the health check or if training complementarity is below 15% unique wins for either backend.

## Evidence references

- Artifact root: `<local-path>/projects/direct-local-llm-learned-router-benchmark-dd3f174667`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
