# Real-LLM Evidence Ledger on Labeled Tool-Use Transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-llm-evidence-ledger-on-labeled-tool-use-transcripts-db311b7e38`
Run ID: `real-llm-evidence-ledger-on-labeled-tool-use-transcripts-db311b7e38-20260611T075426452202+0000`

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

- Parent run decision: Evidence-Ledger Agent: Falsifiable Claim Tracking for Tool-Use Tasks: enoch://control-plane/projects/evidence-ledger-agent-falsifiable-claim-tracking-for-tool-use-tasks-8e3597d11559/runs/evidence-ledger-agent-falsifiable-claim-tracking-for-tool-use-tasks-8e3597d11559-20260611T073401884814+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2d662c61c743

## What looked useful

The Tier 1 run extracted 5213 labeled completed command events from 250 real transcripts. Ledger label accuracy was 1.000 by preserving structured exit_code labels; a text-only heuristic reached 0.954 overall accuracy but only 0.690 failure-class F1, with 87 missed failures and 151 false failure alarms. The ledger also surfaced 219 tee pipeline commands missing pipefail among 1017 tee pipeline commands.

## Boundaries and scale limits

The evidence covers command-level tool execution labels in Codex JSONL transcripts only. It does not validate assistant final-claim truthfulness, human-labeled evidence support, cross-format transcript generalization, adversarial tamper resistance, or publication-grade research-result auditing.

## Claim scope

On a deterministic sample of 250 real local Codex/LLM JSONL transcripts, a structured evidence ledger over completed command_execution records exactly preserved tool success/failure labels from exit_code metadata and supported simple command-audit queries better than a text-output heuristic baseline.

## Why it stopped

No-paper closure: this is a useful direct mechanism signal for command-level ledger extraction on real transcripts, but it is not broad or claim-level evidence sufficient for publication.

## Recommended next action

Run a bounded deepen follow-up that labels assistant final-summary claims as supported, contradicted, or unverified against the ledger evidence and measures claim-level audit precision/recall.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Claim-Level Evidence Ledger Audit on Real Assistant Summaries
- Success threshold: Ledger-based claim support classification improves macro F1 by at least 0.15 over the strongest baseline and reaches at least 0.80 precision on unsupported/contradicted claims.
- Stop condition: Stop if independent labels cannot be produced locally, if fewer than 100 usable claims are available, or if ledger macro F1 is within 0.05 of the strongest baseline after the full held-out evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-evidence-ledger-on-labeled-tool-use-transcripts-db311b7e38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
