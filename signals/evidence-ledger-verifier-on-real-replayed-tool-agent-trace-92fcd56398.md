# Evidence-ledger verifier on real replayed tool-agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-verifier-on-real-replayed-tool-agent-trace-92fcd56398`
Run ID: `evidence-ledger-verifier-on-real-replayed-tool-agent-trace-92fcd56398-20260613T024222059118+0000`

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

- Parent run decision: Evidence-ledger auditability on replayed tool-agent traces: enoch://control-plane/projects/evidence-ledger-auditability-on-replayed-tool-agent-traces-9cd0d6bf0c/runs/evidence-ledger-auditability-on-replayed-tool-agent-traces-9cd0d6bf0c-20260613T000631606074+0000
- Parent run decision: Evidence-Ledger Auditability for Multi-Step Agent Tasks: enoch://control-plane/projects/evidence-ledger-auditability-for-multi-step-agent-tasks-d49ff8030a67/runs/evidence-ledger-auditability-for-multi-step-agent-tasks-d49ff8030a67-20260612T233921925346+0000

## What looked useful

Full ledger verification reached mean accuracy 1.000 and unsupported rejection 1.000 across seeds 11, 23, 37, 41, and 53, versus schema-only baseline accuracy 0.500 and unsupported rejection 0.000. The no-hash ablation had 6 false accepts per seed, supporting the value of output fingerprints.

## Boundaries and scale limits

The observations are real local replayed tool outputs, but the claims are generated mutations rather than naturally emitted LLM-agent claims; only 5 seeds and 240 total claims were evaluated.

## Claim scope

On 6 replayed local tool-command observations with fixed-seed generated supported/unsupported claims, a predicate-level evidence-ledger verifier eliminated schema-only false accepts and outperformed exit-only and no-hash ablations.

## Why it stopped

Mechanism support is reproducible but partially proxied by generated claims, so it is not a Tier 2 paper-ready validation on real agent trace claims.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded corpus of real archived tool-agent traces containing naturally emitted or independently annotated claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger verifier on annotated real tool-agent trace claims
- Success threshold: Full verifier improves unsupported rejection by >=0.50 absolute over schema-only baseline with false reject rate <=0.05 on naturally emitted or independently annotated claims.
- Stop condition: Stop if annotated real traces cannot be obtained locally without exposing private/operator data, or if the full verifier improves unsupported rejection by <0.20 absolute over baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-verifier-on-real-replayed-tool-agent-trace-92fcd56398`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
