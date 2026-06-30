# Direct Local-LLM Learned Router Cascade Benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-local-llm-learned-router-cascade-benchmark-7b13e2cce5`
Run ID: `direct-local-llm-learned-router-cascade-benchmark-7b13e2cce5-20260522T025025392048+0000`

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

- Parent run decision: Learned Router for Local LLM Cascade: enoch://control-plane/projects/learned-router-for-local-llm-cascade-aee89f1d2e54/runs/learned-router-for-local-llm-cascade-aee89f1d2e54-20260522T011804423331+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d176ef2f214d

## What looked useful

Phi produced 0% valid JSON parses and 4% corrected test accuracy; Qwen produced 100% valid parses and 80% test accuracy. The learned router routed 100% of held-out examples to Qwen, matching all-fallback accuracy with no selected-model cost reduction and higher total cascade runtime because it still ran the cheap model first.

## Boundaries and scale limits

Small hand-curated task set; one cheap model and one fallback model; repeated llama-cli startup rather than persistent serving; no public benchmark suite or production trace; no logprob features.

## Claim scope

On a 50-task controlled local GGUF benchmark using Phi-4-mini-instruct Q4 as the cheap model and Qwen2.5-7B-Instruct Q4 as fallback, a learned router trained from cheap-model output features did not improve over all-fallback routing.

## Why it stopped

Controlled direct Tier 1 evidence showed no learned-router advantage: the cheap model was not usable under the tested runtime and the router collapsed to all-fallback.

## Recommended next action

Stop this run as a useful negative; rerun only as a bounded deepen test if a different cheap local model with nontrivial valid-answer rate is available under persistent serving.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent-Serving Cascade With a Valid Cheap Local Model
- Success threshold: Held-out learned-router accuracy within 2 percentage points of all-fallback while reducing fallback calls by at least 25% and improving total cascade runtime by at least 15% versus all-fallback.
- Stop condition: Stop if the cheap model valid parse rate is below 70% on the first 30 tasks or if the learned router cannot beat a confidence threshold at matched fallback rate.

## Evidence references

- Artifact root: `<local-path>/projects/direct-local-llm-learned-router-cascade-benchmark-7b13e2cce5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
