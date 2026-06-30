# Manual natural-language evidence-ledger provenance audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `manual-natural-language-evidence-ledger-provenance-audit-0c9b54c260`
Run ID: `manual-natural-language-evidence-ledger-provenance-audit-0c9b54c260-20260619T124922272505+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-agent transcript evaluation for evidence-ledger claim provenance: enoch://control-plane/projects/real-agent-transcript-evaluation-for-evidence-ledger-claim-3c3cc7d4f2/runs/real-agent-transcript-evaluation-for-evidence-ledger-claim-3c3cc7d4f2-20260619T112730746101+0000
- Parent run decision: Multi-transcript evidence-ledger provenance benchmark: enoch://control-plane/projects/multi-transcript-evidence-ledger-provenance-benchmark-c2ffc687f1/runs/multi-transcript-evidence-ledger-provenance-benchmark-c2ffc687f1-20260619T122553486096+0000

## What looked useful

Across five fixed seeds and 25,000 claim instances per protocol, full ledgers reached mean fault recall 0.99955 with zero false positives, citation-only notes reached 0.0 direct audit recall, no-line ablation reached 0.7448, and no-quote ablation reached 0.7283.

## Boundaries and scale limits

Synthetic generated documents only; deterministic grammar-aware auditor; no human auditors; no real-world PDFs, OCR, tables, multi-hop claims, or mature provenance-management baseline. This is not paper-positive evidence.

## Claim scope

In a seeded synthetic provenance-fault benchmark, natural-language evidence ledgers with explicit source IDs, line addresses, and quotes made claim-level provenance faults directly auditable and substantially improved deterministic fault recall over citation-only notes.

## Why it stopped

Useful synthetic mechanism signal only; no-paper closure because the evidence is generated/protocol-shaped rather than real-world or human-validated.

## Recommended next action

Run a bounded human-auditor study on a small real-document corpus before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human audit validation of natural-language evidence ledgers on real documents
- Success threshold: Full ledger improves human fault recall by at least 0.20 absolute over citation-only notes, false-positive rate remains below 0.10, and median audit time does not increase by more than 50%.
- Stop condition: Stop if full ledger recall improvement is below 0.10 absolute, false-positive rate exceeds 0.10, or authoring/audit overhead makes the workflow impractical on the small corpus.

## Evidence references

- Artifact root: `<local-path>/projects/manual-natural-language-evidence-ledger-provenance-audit-0c9b54c260`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
