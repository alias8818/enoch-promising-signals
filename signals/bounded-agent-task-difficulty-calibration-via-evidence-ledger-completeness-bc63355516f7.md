# Bounded Agent Task Difficulty Calibration via Evidence Ledger Completeness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-agent-task-difficulty-calibration-via-evidence-ledger-completeness-bc63355516f7`
Run ID: `bounded-agent-task-difficulty-calibration-via-evidence-ledger-completeness-bc63355516f7-20260525T102431060892+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/74ba39470e6c

## What looked useful

Metadata plus evidence-ledger completeness reduced Brier error by a mean 0.0606 in the informative condition and 0.0390 in the noisy-ledger condition versus task metadata; AUC for metadata+ELC averaged 0.8574 and 0.8692 respectively. This supports a mechanism worth testing on real traces, but not a paper-ready claim.

## Boundaries and scale limits

Synthetic-only evidence; no live LLM agents, real coding/research tasks, human-rated ledgers, or external trace validation. Two medium seeds completed before stopping the serial CPU loop to stay within the resource-efficiency budget.

## Claim scope

In a deterministic synthetic bounded-agent simulator with explicit required evidence slots, evidence-ledger completeness features improved held-out success calibration over coarse task metadata and raw work/progress proxies across two 10k-task medium seeds and a smoke run.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic mechanism validation rather than direct real-agent validation.

## Recommended next action

Run a bounded deepen follow-up on real or replayed agent traces with auditable required-evidence ledgers and compare ELC calibration against task metadata, token/action counts, and reviewer difficulty labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Calibration of Evidence Ledger Completeness
- Success threshold: Metadata plus ELC improves held-out Brier score by at least 0.03 over the strongest non-ledger baseline and does not worsen ECE by more than 0.02 on at least 50 real/replayed tasks.
- Stop condition: Stop if required evidence cannot be audited for the traces, or if ELC fails to beat the strongest non-ledger baseline by 0.03 Brier improvement.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-agent-task-difficulty-calibration-via-evidence-ledger-completeness-bc63355516f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
