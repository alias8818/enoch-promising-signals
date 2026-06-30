# Fuzz a production signed evidence ledger verifier with checkpoint and key-rotation cases

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `fuzz-a-production-signed-evidence-ledger-verifier-with-che-2afb5d38b2`
Run ID: `fuzz-a-production-signed-evidence-ledger-verifier-with-che-2afb5d38b2-20260528T132003249641+0000`

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

- Parent run decision: Fuzz a Real Signed Agent Evidence Ledger: enoch://control-plane/projects/fuzz-a-real-signed-agent-evidence-ledger-7a97c4f8cb/runs/fuzz-a-real-signed-agent-evidence-ledger-7a97c4f8cb-20260528T000703446652+0000
- Parent run decision: Stochastic Fuzzing of Agent Evidence Ledgers: enoch://control-plane/projects/stochastic-fuzzing-of-agent-evidence-ledgers-789c13335bb7/runs/stochastic-fuzzing-of-agent-evidence-ledgers-789c13335bb7-20260527T212213127006+0000

## What looked useful

A fixed-seed semantic fuzz/control run produced 0/5004 mismatches in baseline single-key controls and 4996/4996 mismatches in targeted key-rotation cases. A 45s native Go fuzz run of FuzzSignedCheckpoint completed 1,901,534 executions with no crash.

## Boundaries and scale limits

Local generated ECDSA keys and package-level Rekor verifier tests only; no live public Rekor deployment, historical public checkpoint corpus, external TUF key history, Cosign, or sigstore-go end-to-end client impact was tested.

## Claim scope

At Rekor commit 3b75cd9c9a101bae26eecf1ad261d94aba247ee9, direct tests of pkg/util SignedNote.Verify show deterministic rejection of signed checkpoints containing valid signatures from two different keys, even when one signature matches the supplied verifier key. Single-key and same-key duplicate-signature controls pass.

## Why it stopped

Medium local confirmation found an actionable production verifier key-rotation bug, but this is no-paper useful signal rather than publication-grade evidence.

## Recommended next action

Prepare an upstream Rekor regression test and fix SignedNote.Verify to continue past non-matching signatures and accept when any signature verifies, then validate the same scenario through an end-to-end Sigstore client path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end Rekor key-rotation checkpoint verification impact
- Success threshold: Patched verifier passes 100% of dual-signed rotation acceptance cases and 100% of negative controls across fixed generated corpora and at least one end-to-end client verification path.
- Stop condition: Stop if maintainers document that Rekor intentionally requires all signatures to match one key, or if end-to-end clients do not consume this verifier path for checkpoint trust decisions.

## Evidence references

- Artifact root: `<local-path>/projects/fuzz-a-production-signed-evidence-ledger-verifier-with-che-2afb5d38b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
