# Claim-Ledger Audit with Strong Independent NLI Verification

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `claim-ledger-audit-with-strong-independent-nli-verificatio-1b04378348`
Run ID: `claim-ledger-audit-with-strong-independent-nli-verificatio-1b04378348-20260519T141545189547+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Claim-Ledger Audit with Strong Independent NLI Verification: internal_generated:claim-ledger-audit-with-strong-independent-nli-verificatio-1b04378348

## What looked useful

Across three 1,000-bundle SNLI dev seeds, claim-ledger transformer NLI reached mean F1 0.8624 and AUPRC 0.9487 versus whole-answer NLI F1 0.8333 and AUPRC 0.9065; a held-out SNLI test run gave ledger F1 0.8750 versus whole-answer F1 0.8504.

## Boundaries and scale limits

Constructed from SNLI premise/hypothesis labels rather than real generated-answer factuality data; limited to two-claim bundles; no claim extraction, retrieval, long-document, human factuality, or cross-domain benchmark was evaluated.

## Claim scope

On fixed-seed two-claim same-premise SNLI-derived unsupported-claim detection bundles, independent transformer NLI over an atomic claim ledger outperforms whole-answer NLI and lexical distance.

## Why it stopped

Moderate bounded evidence supports the mechanism but not publication readiness; current run uses a constructed SNLI audit task rather than direct real-world claim-ledger factuality evaluation.

## Recommended next action

Stop this depth-4 follow-up at useful-signal/no-paper: the mechanism is supported in a constructed NLI benchmark, but Tier 4 paper readiness would require real generated-answer factuality data and the controller lineage is already at the follow-up cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/claim-ledger-audit-with-strong-independent-nli-verificatio-1b04378348`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
