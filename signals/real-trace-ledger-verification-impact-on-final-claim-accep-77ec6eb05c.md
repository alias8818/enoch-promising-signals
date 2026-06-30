# Real trace ledger verification impact on final claim acceptance

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `real-trace-ledger-verification-impact-on-final-claim-accep-77ec6eb05c`
Run ID: `real-trace-ledger-verification-impact-on-final-claim-accep-77ec6eb05c-20260601T071820741637+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Independent Trace Corpus Test for Evidence Ledger Verification: enoch://control-plane/projects/independent-trace-corpus-test-for-evidence-ledger-verifica-35fffc8b0a/runs/independent-trace-corpus-test-for-evidence-ledger-verifica-35fffc8b0a-20260531T223030288674+0000
- Parent run decision: Real Independent Trace Corpus Evidence Ledger Verification: enoch://control-plane/projects/real-independent-trace-corpus-evidence-ledger-verification-ee6bbf3e4d/runs/real-independent-trace-corpus-evidence-ledger-verification-ee6bbf3e4d-20260601T024431325238+0000

## What looked useful

Hash verification improved acceptance accuracy from 0.20 to 0.60 and reduced false accept rate from 1.00 to 0.50; adding real evidence-reference validation improved accuracy to 0.80 and false accept rate to 0.25, but wrong final labels in internally consistent rehashed ledgers still passed.

## Boundaries and scale limits

Candidate corruptions were deterministic controls over real SciFact evidence, not naturally generated model traces. No semantic verifier or human adjudication was used, so freshly rehashed wrong-label ledgers remain an accepted failure mode.

## Claim scope

On 188 labeled SciFact dev claims with constructed valid, tampered, and forged trace-ledger variants, hash-chain and real-corpus reference verification improve final-claim acceptance accuracy and reduce false accepts relative to accept-all and schema-only baselines.

## Why it stopped

Mechanism support is not publication readiness: ledger verification catches tampering and invalid references but does not by itself verify the semantic correctness of a freshly rehashed wrong final claim.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful signal; do not chain another follow-up unless a new controller campaign supplies naturally generated traces and semantic or human final-label adjudication.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-ledger-verification-impact-on-final-claim-accep-77ec6eb05c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
