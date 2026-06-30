# Agent planner/executor cascade: tiny planner routes each sub-task to the right local model on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-planner-executor-cascade-tiny-planner-routes-each-sub-task-to-the-right-local-model-on-gb1-393bf14c7b14`
Run ID: `agent-planner-executor-cascade-tiny-planner-routes-each-sub-task-to-the-right-local-model-on-gb1-393bf14c7b14-20260619T212822146862+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1312b6fa4da

## What looked useful

Naive type/difficulty routing is not enough: tiny_planner scored 6/12 versus all_phi 7/12 and all_qwen 8/12. However, model-specific correctness differences exist: an oracle conservative policy matched all_qwen accuracy and reduced summed latency from 13.707 s to 11.022 s, showing a measurable target for a calibrated router.

## Boundaries and scale limits

Small toy task suite; two quantized local models only; llama.cpp build reported no usable GPU offload; no learned planner; no concurrent serving; no multi-turn agent decomposition; no broad or production workload validation.

## Claim scope

On 12 objective toy sub-tasks using two local GGUF instruction models through CPU-backed llama.cpp chat serving on a GB10 host, a fixed coarse tiny planner underperformed static baselines, while an oracle conservative router matched all-Qwen accuracy at 8/12 with 19.6% lower summed latency.

## Why it stopped

Proxy/local early test: the fixed tiny planner failed to preserve accuracy, so this is no-paper evidence rather than full validation.

## Recommended next action

Run a bounded deepen follow-up that trains or calibrates a tiny router on held-out objective sub-tasks and requires it to match all-Qwen accuracy while reducing latency by at least 15%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated tiny router for local Phi/Qwen sub-task cascades
- Success threshold: On held-out tasks, router accuracy is no worse than all-Qwen by more than one task or one percentage point, and summed latency is at least 15% lower than all-Qwen.
- Stop condition: Stop if the router cannot beat all-Qwen latency by 15% without losing more than one task of accuracy, or if both models have overlapping failures that dominate the task suite.

## Evidence references

- Artifact root: `<local-path>/projects/agent-planner-executor-cascade-tiny-planner-routes-each-sub-task-to-the-right-local-model-on-gb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
