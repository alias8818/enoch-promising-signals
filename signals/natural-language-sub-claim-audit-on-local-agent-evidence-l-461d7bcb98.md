# Natural-language sub-claim audit on local-agent evidence ledgers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-language-sub-claim-audit-on-local-agent-evidence-l-461d7bcb98`
Run ID: `natural-language-sub-claim-audit-on-local-agent-evidence-l-461d7bcb98-20260613T232829496321+0000`

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

- Parent run decision: Evidence-Ledger Sub-Claim Audit for Local Agents: enoch://control-plane/projects/evidence-ledger-sub-claim-audit-for-local-agents-d0f677bd906e/runs/evidence-ledger-sub-claim-audit-for-local-agents-d0f677bd906e-20260613T225158348459+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffdbb53a6b0a

## What looked useful

Sub-claim auditing appears useful for exposing unsupported clauses that whole-claim auditing can miss, but raw token-overlap support is threshold-sensitive and produced a false positive on a supported numeric paraphrase.

## Boundaries and scale limits

Small controlled synthetic dataset only; token-overlap support scoring rather than semantic entailment; no real production agent ledgers; no robustness testing against messy logs, ambiguous claims, or adversarial paraphrases.

## Claim scope

On 12 controlled synthetic local-agent evidence ledgers with multi-clause final claims, a deterministic natural-language sub-claim audit caught all injected unsupported clauses and improved unsupported-claim F1 from 0.8333 to 0.9333, but did not meet the pre-registered +0.20 F1 improvement threshold.

## Why it stopped

Pre-registered Tier 1 threshold was not met: F1 improvement was +0.10 versus required +0.20, despite unsupported injected clause recall of 1.0.

## Recommended next action

Run a bounded follow-up on 50-100 real local-agent evidence ledgers with manually labeled atomic subclaims and a calibrated semantic support scorer; stop if unsupported-clause recall is below 0.85 or false positive rate exceeds 0.15.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-ledger semantic sub-claim audit calibration
- Success threshold: Unsupported-clause recall >= 0.85, false positive rate <= 0.15, and unsupported-claim F1 improvement >= 0.15 over the best whole-claim baseline.
- Stop condition: Stop as negative if semantic sub-claim audit misses more than 15 percent of unsupported clauses or creates false positives on more than 15 percent of fully supported claims.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-sub-claim-audit-on-local-agent-evidence-l-461d7bcb98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
