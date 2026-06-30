# Real-trace evidence-ledger false-accept benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evidence-ledger-false-accept-benchmark-41a252477f`
Run ID: `real-trace-evidence-ledger-false-accept-benchmark-41a252477f-20260619T151451221059+0000`

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

- Parent run decision: Adversarial Evidence-Ledger for CPU-Bound Agent Tool-Use: enoch://control-plane/projects/adversarial-evidence-ledger-for-cpu-bound-agent-tool-use-663e78915f36/runs/adversarial-evidence-ledger-for-cpu-bound-agent-tool-use-663e78915f36-20260619T145102222358+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7d5fffda1b4

## What looked useful

The verifier achieved 0 false accepts and 0 false rejects on controlled ledger cases covering missing refs, failed command status, metric mismatch, seed drift, hash mismatch, missing source file, duplicate evidence id, and config drift.

## Boundaries and scale limits

Small controlled benchmark only; no large heterogeneous historical agent corpus, adversarial natural-language claim extraction, multi-run drift campaign, or independent external labeling was tested.

## Claim scope

A strict local evidence-ledger verifier rejected all unsupported claims in a 10-case Tier 1 controlled real-file trace benchmark with 2 valid cases and 8 invalid trap cases.

## Why it stopped

Tier 1 direct controlled benchmark met its false-accept threshold, but the evidence is no-paper useful signal rather than publication-grade validation.

## Recommended next action

Run a bounded medium follow-up on a frozen corpus of real historical agent traces with independent labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-agent trace evidence-ledger false-accept replay
- Success threshold: false_accept_rate <= 0.02 and false_reject_rate <= 0.10 on at least 100 labeled real trace claims.
- Stop condition: Stop if false_accept_rate exceeds 0.02 after 50 labeled invalid cases or if corpus labeling cannot be reproduced from frozen artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-false-accept-benchmark-41a252477f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
