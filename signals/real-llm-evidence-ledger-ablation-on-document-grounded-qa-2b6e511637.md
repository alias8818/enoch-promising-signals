# Real LLM Evidence Ledger Ablation on Document-Grounded QA

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-llm-evidence-ledger-ablation-on-document-grounded-qa-2b6e511637`
Run ID: `real-llm-evidence-ledger-ablation-on-document-grounded-qa-2b6e511637-20260530T055043984237+0000`

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

- Parent run decision: Evidence Anchor Ledger for Agent Reasoning Reliability: enoch://control-plane/projects/evidence-anchor-ledger-for-agent-reasoning-reliability-6d25674bc8a1/runs/evidence-anchor-ledger-for-agent-reasoning-reliability-6d25674bc8a1-20260530T021021701293+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8f28ee149113

## What looked useful

The evidence-ledger prompt failed the Tier 1 threshold: grounded accuracy fell from 0.8889 baseline to 0.4028 ledger, answer accuracy fell from 0.8889 to 0.7778, and unsupported-answer rate rose from 0.0000 to 0.4306. Ledger citations worked for simple city/year facts but failed on founder, codename, multihop, and unanswerable cases.

## Boundaries and scale limits

Single small instruction-tuned model, synthetic documents, one prompt family, 72 examples, no broad public QA benchmark, no larger-model replication, and no constrained decoding or few-shot ledger repair.

## Claim scope

Small controlled direct test of prompt-level evidence-ledger ablation on 72 synthetic document-grounded QA items using Qwen/Qwen2.5-0.5B-Instruct with deterministic generation.

## Why it stopped

Tier 1 controlled direct test falsified the stated +10 percentage point grounded-accuracy threshold for the tested prompt-level evidence ledger; this is a small direct early negative, not a full benchmark validation.

## Recommended next action

Run one bounded follow-up that tests whether the observed failure is prompt-format/control related by adding few-shot ledger examples plus constrained output/stop handling on the same 72-item benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Few-Shot and Constrained Evidence Ledger Repair on Controlled Document-Grounded QA
- Success threshold: Repaired ledger grounded accuracy must exceed baseline grounded accuracy by at least 10 percentage points and unsupported-answer rate must be no higher than baseline.
- Stop condition: Stop if repaired ledger grounded accuracy remains below baseline or unsupported-answer rate increases by more than 5 percentage points on the 72-item set.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-evidence-ledger-ablation-on-document-grounded-qa-2b6e511637`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
