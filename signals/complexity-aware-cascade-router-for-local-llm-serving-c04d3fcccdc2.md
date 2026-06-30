# Complexity-aware cascade router for local LLM serving

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `complexity-aware-cascade-router-for-local-llm-serving-c04d3fcccdc2`
Run ID: `complexity-aware-cascade-router-for-local-llm-serving-c04d3fcccdc2-20260620T195237340346+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/56f71e69a40f

## What looked useful

Static complexity routing cut large calls to 0.667/query and mean latency to 0.0687 s but reduced accuracy from 0.5833 always-large to 0.4167. Small-first confidence cascade reached 0.5625 accuracy but used 0.9583 large calls/query after running the small model first, increasing mean latency to 0.1275 s versus 0.0840 s always-large.

## Boundaries and scale limits

Synthetic multiple-choice benchmark only; no real serving traces, no batched/concurrent queueing, no learned router, no semantic free-form grading, no larger 7B+ local models, and no production scheduler integration.

## Claim scope

On a 48-item test split of generated arithmetic, algebra, and word-problem multiple-choice prompts scored by local Qwen2.5 0.5B and 1.5B models on GB10, a cheap prompt-complexity plus small-model-margin cascade did not jointly preserve large-model quality and reduce latency.

## Why it stopped

Bounded direct local inference showed no tested policy achieved the claimed quality-preserving latency reduction; this is an early/proxy falsification, not a full-scale serving-system validation.

## Recommended next action

Stop this run as a proxy-scale early falsification; any future work should first replace the hand-built threshold router with a learned router on real traces and require accuracy within 2 percentage points of always-large while reducing large calls by at least 30%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned router on real local-serving traces
- Success threshold: Learned router test accuracy within 2 percentage points of always-large while reducing large-model calls by at least 30% and reducing measured mean latency by at least 15%.
- Stop condition: Stop if the learned router cannot beat static complexity routing on held-out data or if latency remains higher than always-large after accounting for small-model prepass overhead.

## Evidence references

- Artifact root: `<local-path>/projects/complexity-aware-cascade-router-for-local-llm-serving-c04d3fcccdc2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
