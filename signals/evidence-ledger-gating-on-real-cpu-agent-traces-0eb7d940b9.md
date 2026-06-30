# Evidence-ledger gating on real CPU-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gating-on-real-cpu-agent-traces-0eb7d940b9`
Run ID: `evidence-ledger-gating-on-real-cpu-agent-traces-0eb7d940b9-20260604T030505373450+0000`

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

- Parent run decision: Structured Evidence-Ledgers for Safer CPU Agent Tool Use: enoch://control-plane/projects/structured-evidence-ledgers-for-safer-cpu-agent-tool-use-9a1fc8ebe59a/runs/structured-evidence-ledgers-for-safer-cpu-agent-tool-use-9a1fc8ebe59a-20260604T011235754687+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4c5e4892e116

## What looked useful

On 4,118 claims from 95 real local CPU-agent projects, the full ledger gate reached 1.000 supported recall and 1.000 unsupported rejection, while a raw transcript lexical baseline reached 0.339 supported recall and 0.662 unsupported rejection. Channel ablations degraded the expected claim families.

## Boundaries and scale limits

Claims were controlled templates generated from real trace fields; labels were deterministic from the same taxonomy used by the gate. This does not validate natural-language report extraction, semantic paraphrase handling, independent human labels, or live agent-loop intervention.

## Claim scope

A structured evidence-ledger gate can distinguish supported from contradicted templated process claims over real local CPU-agent Codex/Enoch trace fields across a bounded 95-project, 300-command-event corpus.

## Why it stopped

Tier 1 direct mechanism threshold was met, but the evidence remains no-paper because claim generation and labels are controlled templates over the same structured trace taxonomy rather than independently audited natural-language final reports.

## Recommended next action

Run a bounded deepen follow-up that extracts natural-language final-report claims from held-out real agent runs and scores ledger gating against independently labeled support/contradiction judgments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language final-report claim gating on real CPU-agent traces
- Success threshold: Unsupported-claim rejection >= 0.90, supported-claim recall >= 0.80, and unsupported rejection at least 0.20 above the lexical baseline on independently labeled natural-language claims.
- Stop condition: Stop as no-paper negative if independent labels cannot be obtained locally, if unsupported rejection is below 0.80, or if the ledger advantage over lexical baseline is below 0.10.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gating-on-real-cpu-agent-traces-0eb7d940b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
