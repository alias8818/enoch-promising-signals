# Direct GB10 local-LLM calibrated cascade router validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-gb10-local-llm-calibrated-cascade-router-validation-b7f0be933f`
Run ID: `direct-gb10-local-llm-calibrated-cascade-router-validation-b7f0be933f-20260610T154001071475+0000`

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

- Parent run decision: Calibrated local cascade router for GB10: enoch://control-plane/projects/calibrated-local-cascade-router-for-gb10-4de9b2b9081a/runs/calibrated-local-cascade-router-for-gb10-4de9b2b9081a-20260610T151131897111+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98409dfd7687

## What looked useful

Direct local GB10 inference supports the mechanism that top-token confidence can gate safe accepts on a small controlled set, but the independent cheap-model cascade remains unvalidated.

## Boundaries and scale limits

Not a full cascade validation: Phi-4-mini failed smoke with incoherent generations under the available llama.cpp build; a compatible Qwen2.5-1.5B download did not complete in the bounded run; escalation accuracy is an answer-key oracle upper bound rather than a measured second-model branch.

## Claim scope

On a 32-item controlled multiple-choice Tier 1 test run directly on GB10 with Qwen2.5-7B-Instruct-Q4_K_M, a calibration-only confidence threshold of 0.99 accepted 75% of validation items with 100% accepted accuracy, rejecting all observed Qwen validation errors.

## Why it stopped

No-paper useful signal: the direct confidence gate worked on a small validation split, but the true two-model cascade was not completed and the escalation branch was only an oracle upper bound.

## Recommended next action

Run a bounded deepen follow-up only after pre-staging a compatible small Qwen GGUF; measure real small-model accepts, 7B escalations, latency, and accuracy against always-small and always-7B baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pre-staged small-Qwen to Qwen-7B calibrated local cascade on GB10
- Success threshold: Cascade validation accuracy is at least 95% of always-7B accuracy while reducing 7B calls by at least 30%, with accepted-branch accuracy at least 95% on held-out validation.
- Stop condition: Stop as negative if the small model cannot smoke cleanly, if calibration accepts fewer than 20% of items at 95% accepted accuracy, or if held-out cascade accuracy falls below 95% of always-7B.

## Evidence references

- Artifact root: `<local-path>/projects/direct-gb10-local-llm-calibrated-cascade-router-validation-b7f0be933f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
