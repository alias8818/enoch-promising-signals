# Real-Agent Evidence-Bound Ledger Hallucination Audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-evidence-bound-ledger-hallucination-audit-15a45b1385`
Run ID: `real-agent-evidence-bound-ledger-hallucination-audit-15a45b1385-20260519T132406993020+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f936603008ce

## What looked useful

Evidence-bound ledger prompting is feasible and improves schema/citation compliance under answer pressure, but this test does not establish broad hallucination reduction or paper readiness.

## Boundaries and scale limits

One local 7B-class GGUF instruction model, synthetic single-turn QA documents, 24 cases, rule-based scoring, no real corpus, no multi-model robustness, no long-horizon tool-agent traces, and no human claim-level audit labels.

## Claim scope

A controlled 24-task synthetic local-document QA audit with Qwen2.5-7B-Instruct found that an evidence-bound ledger prompt preserved 100% answer accuracy and citation validity, matched a careful baseline, and improved strict parse/citation reliability over an answer-pressure baseline. It did not show a hallucination-rate reduction because corrected unsupported false-positive rates were already 0 for both baselines.

## Why it stopped

Closed as no-paper useful signal: direct Tier 1 evidence supports compliance robustness but not a publication-grade hallucination-reduction claim.

## Recommended next action

Run a bounded deepen test with harder unsupported traps and at least three local or API models, requiring a clear unsupported-claim reduction without supported-answer regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard Unsupported-Claim Ledger Audit Across Models
- Success threshold: Ledger unsupported false-positive rate at least 30 percentage points lower than unbound baseline on tasks where baseline unsupported false-positive rate is at least 20%, with supported-answer accuracy no more than 5 percentage points worse.
- Stop condition: Stop if baselines again have under 10% unsupported false-positive rate on the hard set or if ledger reduces supported-answer accuracy by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-bound-ledger-hallucination-audit-15a45b1385`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
