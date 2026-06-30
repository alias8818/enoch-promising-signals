# Natural-language final-report claim gating on real CPU-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-final-report-claim-gating-on-real-cpu-age-58f7e6ba62`
Run ID: `natural-language-final-report-claim-gating-on-real-cpu-age-58f7e6ba62-20260604T060644774181+0000`

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

- Parent run decision: Evidence-ledger gating on real CPU-agent traces: enoch://control-plane/projects/evidence-ledger-gating-on-real-cpu-agent-traces-0eb7d940b9/runs/evidence-ledger-gating-on-real-cpu-agent-traces-0eb7d940b9-20260604T030505373450+0000
- Parent run decision: Structured Evidence-Ledgers for Safer CPU Agent Tool Use: enoch://control-plane/projects/structured-evidence-ledgers-for-safer-cpu-agent-tool-use-9a1fc8ebe59a/runs/structured-evidence-ledgers-for-safer-cpu-agent-tool-use-9a1fc8ebe59a-20260604T011235754687+0000

## What looked useful

A value-checking evidence gate substantially beat accept-all and citation-only baselines and modestly beat a strong raw-text overlap baseline on real CPU-agent final reports paired with real decision/result/path artifacts; channel ablations showed the mechanism depends on the cited evidence channel.

## Boundaries and scale limits

Unsupported claims were fixed-seed perturbations of real final-report claims, not naturally occurring false claims with human labels. The extractor covered structured checkable claims only and did not evaluate semantic paraphrases, causal interpretations, or broad free-form report claims.

## Claim scope

On 220 completed local Enoch CPU-agent projects, deterministic gating of extracted natural-language final-report claims about artifact paths, decision fields, and numeric metrics against cited durable artifacts achieved 0.9989 mean accuracy and 0.9978 mean unsupported-claim rejection over five fixed seeds with perturbation-generated unsupported claims.

## Why it stopped

Tier 2 medium validation supports the bounded mechanism but remains perturbation-labeled and limited to structured checkable claim types, so it is not publication-grade closure.

## Recommended next action

Stop as no-paper useful signal; the next bounded deepen test should build a human-audited multi-project corpus of naturally occurring final-report claims before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-audited natural final-report claim benchmark for evidence gating
- Success threshold: Full gate recall >= 0.90, unsupported or overclaim rejection >= 0.85, and accuracy at least 0.05 above the best non-gated baseline on human-audited naturally occurring claims.
- Stop condition: Stop if audited naturally occurring claims are too sparse for at least 300 labeled claims, or if the full gate fails to beat the best non-gated baseline by 0.05 accuracy while meeting recall and rejection thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-final-report-claim-gating-on-real-cpu-age-58f7e6ba62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
