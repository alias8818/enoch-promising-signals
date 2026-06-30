# Natural summary claim extraction for real agent evidence-ledger correction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `natural-summary-claim-extraction-for-real-agent-evidence-l-281d25790b`
Run ID: `natural-summary-claim-extraction-for-real-agent-evidence-l-281d25790b-20260527T022333243504+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-ledger correction on real small-agent tool traces: enoch://control-plane/projects/evidence-ledger-correction-on-real-small-agent-tool-traces-4ae6b44b24/runs/evidence-ledger-correction-on-real-small-agent-tool-traces-4ae6b44b24-20260525T094348568390+0000
- Parent run decision: Evidence-Ledger Self-Correction for Small CPU Agents: enoch://control-plane/projects/evidence-ledger-self-correction-for-small-cpu-agents-42ca459e440e/runs/evidence-ledger-self-correction-for-small-cpu-agents-42ca459e440e-20260525T091321098709+0000

## What looked useful

The thresholded claim extractor reached 0.553 mean field accuracy, 0.000 exact ledger accuracy, and 0.213 correction F1, versus 0.549 field accuracy for no-correction and 0.949 field accuracy / 0.943 correction F1 for a bag-of-words Naive Bayes baseline.

## Boundaries and scale limits

Tested on local Enoch/Codex run_notes.md summaries and injected corruptions of 10 structured project_decision fields across 5 fixed train/test seeds. It does not cover human-labeled naturally occurring ledger mistakes, free-form evidence-item claims, or non-Enoch agent corpora.

## Claim scope

On 482 real local Enoch agent run summaries paired with project decision ledgers, a conservative hand-built natural-summary claim extractor does not materially repair corrupted decision-ledger fields and is dominated by simple trained text baselines.

## Why it stopped

Tier 2 medium validation on real local agent summaries found the proposed extractor barely above no-correction and far below the trained baseline, so this is a no-paper negative useful signal rather than a paper-positive result.

## Recommended next action

Stop pursuing the hand-built natural-summary claim extractor for this ledger-correction task; any future system should first beat the fixed-seed bag-of-words baseline on this corpus with low false-edit rate.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/natural-summary-claim-extraction-for-real-agent-evidence-l-281d25790b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
