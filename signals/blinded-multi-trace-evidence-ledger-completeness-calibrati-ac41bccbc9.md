# Blinded Multi-Trace Evidence Ledger Completeness Calibration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blinded-multi-trace-evidence-ledger-completeness-calibrati-ac41bccbc9`
Run ID: `blinded-multi-trace-evidence-ledger-completeness-calibrati-ac41bccbc9-20260525T123621534041+0000`

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

- Parent run decision: Bounded Agent Task Difficulty Calibration via Evidence Ledger Completeness: enoch://control-plane/projects/bounded-agent-task-difficulty-calibration-via-evidence-ledger-completeness-bc63355516f7/runs/bounded-agent-task-difficulty-calibration-via-evidence-ledger-completeness-bc63355516f7-20260525T102431060892+0000
- Parent run decision: Real Trace Calibration of Evidence Ledger Completeness: enoch://control-plane/projects/real-trace-calibration-of-evidence-ledger-completeness-2a30c1b191/runs/real-trace-calibration-of-evidence-ledger-completeness-2a30c1b191-20260525T120601050819+0000

## What looked useful

Independent blinded multi-trace ledgers carry useful completeness signal: sample coverage reached MAE 0.03155 in the blinded scenario versus 0.03789 for single-trace prior and 0.05781 for count prior. However, the bespoke consensus-penalized multi-trace capture-recapture variant lost to the real sample-coverage baseline in all scenarios, and correlated/unblinded traces weakened or reversed the multi-trace advantage.

## Boundaries and scale limits

No real human/model evidence ledgers were used; evidence-item distributions, false positives, semantic duplicates, annotator dependence, and blinding/copying behavior were simulated. The result is not a full real-world validation and is not paper-ready.

## Claim scope

Synthetic hidden-gold evidence-ledger calibration with 5 fixed seeds, 3 trace-dependence scenarios, 37,500 test cases, and calibrated completeness metrics at a 90% stopping threshold.

## Why it stopped

Tier-2 synthetic direct-metric validation found mechanism support but failed the strict real-baseline novelty gate; the result is a bounded useful signal rather than paper-positive evidence.

## Recommended next action

Stop this run as no-paper useful signal; any next work should test the same metrics on a real multi-annotator evidence-ledger dataset and require beating sample coverage, not just count or single-trace baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Multi-Annotator Evidence Ledger Completeness Calibration
- Success threshold: Across at least 3 fixed splits, the proposed real-ledger method must reduce MAE by at least 10% versus sample coverage with no worse ECE and must keep 90% stopping precision at or above 0.90 in the blinded condition.
- Stop condition: Stop as negative if sample coverage matches or beats the proposed method on MAE, if stopping precision drops below 0.90, or if trace dependence explains the apparent gain.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-multi-trace-evidence-ledger-completeness-calibrati-ac41bccbc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
