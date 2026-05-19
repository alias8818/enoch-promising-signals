# Prompt-Complexity Router for Local Model Cascades

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `prompt-complexity-router-for-local-model-cascades-f709678185e6`
Run ID: `prompt-complexity-router-for-local-model-cascades-f709678185e6-20260518T161151457671+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba2a2599325c

## What looked useful

Prompt complexity separated easy, medium, and hard prompts, but the cheap 1.5B tier still missed 20% of easy addition prompts and nearly all medium/hard prompts. A strict parity router selected all-7B and saved 0% latency; a looser easy-to-cheap threshold saved 12.7% held-out latency but lost 6.7 percentage points of accuracy.

## Boundaries and scale limits

Synthetic arithmetic only; 30 prompts with a 15/15 calibration/test split; one model pair; one prompting style; HTTP latency measured after model load; no learned router, no production trace, no repeated random seeds.

## Claim scope

On a 30-prompt synthetic arithmetic benchmark using local llama.cpp Qwen2.5-1.5B-Instruct-Q4_K_M as the cheap tier and Qwen2.5-7B-Instruct-Q4_K_M as the expensive tier, a hand-designed pre-inference prompt-complexity threshold could not preserve 7B held-out accuracy while reducing latency; the parity-selected router routed all held-out prompts to 7B.

## Why it stopped

The tested complexity-only router did not meet the accuracy-preserving latency-reduction success condition; this is a bounded synthetic/local early falsification, not a full production validation.

## Recommended next action

Stop this paper path as a proxy/local early falsification of complexity-only routing; run a bounded deepen test adding cheap-model confidence or verifier gating before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Gated Local Cascade Router
- Success threshold: Held-out latency reduction >=10% versus all-7B with accuracy no more than 2 percentage points below all-7B, and improvement over complexity-only routing under the same split.
- Stop condition: Stop if confidence/verifier gating still routes all prompts to 7B under the 2-point accuracy floor, or if it saves latency only by losing more than 2 percentage points of accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-complexity-router-for-local-model-cascades-f709678185e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
