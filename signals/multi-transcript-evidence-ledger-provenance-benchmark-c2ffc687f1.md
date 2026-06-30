# Multi-transcript evidence-ledger provenance benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-transcript-evidence-ledger-provenance-benchmark-c2ffc687f1`
Run ID: `multi-transcript-evidence-ledger-provenance-benchmark-c2ffc687f1-20260619T122553486096+0000`

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

- Parent run decision: Real-agent transcript evaluation for evidence-ledger claim provenance: enoch://control-plane/projects/real-agent-transcript-evaluation-for-evidence-ledger-claim-3c3cc7d4f2/runs/real-agent-transcript-evaluation-for-evidence-ledger-claim-3c3cc7d4f2-20260619T112730746101+0000
- Parent run decision: Evidence-Ledger Agent: Falsifiable Claim Provenance on Tool Chains: enoch://control-plane/projects/evidence-ledger-agent-falsifiable-claim-provenance-on-tool-chains-4f7fbebdbca0/runs/evidence-ledger-agent-falsifiable-claim-provenance-on-tool-chains-4f7fbebdbca0-20260619T110754211315+0000

## What looked useful

Strict cited-evidence provenance validation achieved mean held-out F1 1.0 and unsupported rejection 1.0 across three fixed seeds, while the strongest non-strict comparator, no_transcript_scope_ablation, reached mean F1 0.6887 and unsupported rejection 0.7443.

## Boundaries and scale limits

Claims and labels were generated from real local artifacts rather than manually annotated natural-language ledgers. The run did not test ASR noise, diarization errors, long open-domain meetings, LLM/NLI judges, or inter-annotator agreement.

## Claim scope

In a deterministic local benchmark over 12 Enoch project transcript sources and 132 real local evidence artifacts, strict provenance checks over cited transcript ID, evidence ID, evidence hash, and structured value classified generated ledger claims better than non-strict baselines and ablations across three fixed seeds.

## Why it stopped

Tier 2 medium evidence supports the provenance-checking mechanism, but generated labels and deterministic artifact-derived claims are not publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next deepen only with a manually audited natural-language ledger corpus and a locked LLM/NLI or human baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Manual natural-language evidence-ledger provenance audit
- Success threshold: Strict verifier F1 >= 0.90, unsupported rejection >= 0.90, supported recall >= 0.85, and >=0.05 F1 improvement over the strongest locked baseline on the held-out manually audited set.
- Stop condition: Stop as negative/no-paper if strict provenance checks fail to exceed 0.85 F1 or fail to reject at least 85% of unsupported manually audited defects.

## Evidence references

- Artifact root: `<local-path>/projects/multi-transcript-evidence-ledger-provenance-benchmark-c2ffc687f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
