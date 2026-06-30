# Evidence Ledger Cuts False Completion Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-cuts-false-completion-claims-277c52fda1da`
Run ID: `evidence-ledger-cuts-false-completion-claims-277c52fda1da-20260621T155122255574+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfcc11fbd0c4

## What looked useful

The scaffolded evidence ledger catches common false-completion patterns when evidence records are explicit, task-bound, schema-checkable, and contain expected observations. This is a reproducible mechanism sanity check, not broad publication-grade validation.

## Boundaries and scale limits

Synthetic corpus only; no live LLM agents, real tool traces, human labels, adversarial evidence fabrication, or long-running production tasks were tested.

## Claim scope

In a deterministic synthetic proxy with 1,000 generated agent handoff claims and three required machine-checkable evidence items per task, evidence-ledger gating reduced false completion acceptance from 350/350 under text-only acceptance to 0/350, with 0/650 false rejects.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy that supports the mechanism but does not validate broad real-agent reliability.

## Recommended next action

Run a bounded real-trace follow-up using independently labeled agent handoffs and compare text-only review against ledger-gated review with false accept and false reject confidence intervals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating on independently labeled real agent traces
- Success threshold: At least 50% relative reduction in false completion acceptance versus text-only review, ledger false reject rate no greater than 10%, and at least 100 independently labeled claims.
- Stop condition: Stop if fewer than 100 independently labeled claims are available, if labels are not independent of the ledger, or if ledger false rejects exceed 10% without an offsetting false-accept reduction.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-cuts-false-completion-claims-277c52fda1da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
