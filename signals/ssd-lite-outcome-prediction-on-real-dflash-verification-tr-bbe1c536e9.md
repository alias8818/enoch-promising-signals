# SSD-lite outcome prediction on real DFlash verification traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ssd-lite-outcome-prediction-on-real-dflash-verification-tr-bbe1c536e9`
Run ID: `ssd-lite-outcome-prediction-on-real-dflash-verification-tr-bbe1c536e9-20260519T233514486181+0000`

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

- Parent run decision: SSD-lite Verification-Outcome Prediction for DFlash: enoch://control-plane/projects/ssd-lite-verification-outcome-prediction-for-dflash-cc1d23c80a4f/runs/ssd-lite-verification-outcome-prediction-for-dflash-cc1d23c80a4f-20260519T231446393478+0000
- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Real DFlash verification outcomes have a strong position prior: held-out position-only AUC was 0.8449. SSD-lite trace-visible features reached AUC 0.8594 and AP 0.5616, but the AUC gain over position-only was only +0.0145, below the +0.03 threshold.

## Boundaries and scale limits

Only 15 periodic server-log trace intervals were available, reconstructed into weighted per-position observations. The logs do not include raw per-token labels, draft logits, target probabilities, hidden states, token IDs, or online intervention results.

## Claim scope

On saved real vLLM DFlash speculative-decoding summaries for Qwen3-4B, draft acceptance is strongly predictable from draft position, but the tested SSD-lite trace-visible features do not clear the predeclared incremental AUC margin over a position-only control.

## Why it stopped

Controlled small direct test on real DFlash verification summaries failed the incremental SSD-lite threshold over the strongest simple control; this is direct trace evidence but not full per-token validation.

## Recommended next action

Stop this branch as no-paper evidence; a bounded deepen follow-up should instrument DFlash to persist per-token pre-verification features and exact accept/reject labels before retesting SSD-lite against position-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-token DFlash outcome labels for SSD-lite verification prediction
- Success threshold: Held-out AUC >= 0.70 and at least +0.03 AUC and +0.03 AP over the strongest simple control, with no measured quality regression in a small intervention if one is run.
- Stop condition: Stop if per-token instrumentation cannot be obtained, if SSD-lite fails to beat the strongest simple control by +0.03 AUC/AP, or if an intervention reduces answer quality beyond the scorer tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/ssd-lite-outcome-prediction-on-real-dflash-verification-tr-bbe1c536e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
