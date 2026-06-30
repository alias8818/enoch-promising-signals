# Claim-Level Evidence Ledger Audit on Real Assistant Summaries

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `claim-level-evidence-ledger-audit-on-real-assistant-summar-730d5cdd8e`
Run ID: `claim-level-evidence-ledger-audit-on-real-assistant-summar-730d5cdd8e-20260611T080948791085+0000`

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

- Parent run decision: Real-LLM Evidence Ledger on Labeled Tool-Use Transcripts: enoch://control-plane/projects/real-llm-evidence-ledger-on-labeled-tool-use-transcripts-db311b7e38/runs/real-llm-evidence-ledger-on-labeled-tool-use-transcripts-db311b7e38-20260611T075426452202+0000
- Parent run decision: Evidence-Ledger Agent: Falsifiable Claim Tracking for Tool-Use Tasks: enoch://control-plane/projects/evidence-ledger-agent-falsifiable-claim-tracking-for-tool-use-tasks-8e3597d11559/runs/evidence-ledger-agent-falsifiable-claim-tracking-for-tool-use-tasks-8e3597d11559-20260611T073401884814+0000

## What looked useful

Evidence retrieval plus support scoring is useful relative to random evidence and coarse summary overlap, but claim splitting itself added essentially no value over sentence-level evidence retrieval. Spearman: summary_overlap 0.2761, sentence_ledger 0.3231, claim_ledger 0.3231, random_evidence_control 0.0443. Claim minus sentence delta was 0.0000 with bootstrap CIs spanning roughly -0.017 to +0.016.

## Boundaries and scale limits

Single public benchmark; machine-generated summaries rather than private assistant traces; deterministic lexical scorer; regex claim splitting; no learned NLI/LLM judge; no human claim-ledger spot-checking.

## Claim scope

On mteb/summeval, a deterministic claim-level evidence-ledger audit over 1,600 real machine-generated CNN/DailyMail summaries correlates with human consistency, but does not outperform a sentence-level evidence-ledger baseline.

## Why it stopped

Tier-2 threshold was directly tested and not met: claim_ledger beat random evidence but failed to improve by +0.05 Spearman over both real baselines, and was indistinguishable from sentence_ledger.

## Recommended next action

Stop this run as no-paper evidence; the next bounded test should replace lexical support scoring with a learned NLI/LLM support judge while retaining the sentence-ledger baseline and the same predeclared delta threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: NLI-Scored Claim Ledger vs Sentence Ledger on Factuality Benchmarks
- Success threshold: Claim_ledger improves Spearman by at least +0.05 over sentence_ledger on SumEval and on one additional factuality dataset, with paired bootstrap CI lower bound above 0 on at least SumEval and no regression in AUC.
- Stop condition: Stop if claim_ledger remains within +/-0.02 Spearman of sentence_ledger on SumEval after semantic scoring, or if the second dataset cannot be evaluated with a real source-summary factuality target.

## Evidence references

- Artifact root: `<local-path>/projects/claim-level-evidence-ledger-audit-on-real-assistant-summar-730d5cdd8e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
