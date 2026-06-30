# Fuzz a Real Signed Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `fuzz-a-real-signed-agent-evidence-ledger-7a97c4f8cb`
Run ID: `fuzz-a-real-signed-agent-evidence-ledger-7a97c4f8cb-20260528T000703446652+0000`

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

- Parent run decision: Stochastic Fuzzing of Agent Evidence Ledgers: enoch://control-plane/projects/stochastic-fuzzing-of-agent-evidence-ledgers-789c13335bb7/runs/stochastic-fuzzing-of-agent-evidence-ledgers-789c13335bb7-20260527T212213127006+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ca1df01e51ec

## What looked useful

Strict verification with checkpoint accepted 0/20,000 tampered ledgers. Controls showed signatures-only verification accepts structural mutations, while chain verification without a checkpoint accepts truncation/prefix and same-key authorized rewrite cases.

## Boundaries and scale limits

This was a controlled local harness, not a deployed third-party ledger. It did not test concurrency, distributed storage, key rotation, multi-signer policies, crash recovery, cross-language canonicalization, or coverage-guided parser fuzzing.

## Claim scope

In a local Ed25519 signed 8-entry agent evidence ledger with canonical JSON, sequence numbers, previous-entry hashes, entry hashes, and an externally pinned length/head checkpoint, deterministic mutation fuzzing rejected all tested tampering classes across 20,000 trials.

## Why it stopped

Tier 1 controlled direct mechanism test completed; result is useful but no-paper because it is a local harness rather than a real deployed target evaluation.

## Recommended next action

Run the same mutation suite against an existing production or open-source ledger/transparency-log-backed agent evidence implementation before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fuzz a production signed evidence ledger verifier with checkpoint and key-rotation cases
- Success threshold: Across at least 50,000 mutations plus targeted key-rotation/canonicalization fixtures, the production verifier accepts zero tampered ledgers when a checkpoint is pinned; any accepted case must have a minimized reproducer.
- Stop condition: Stop if no real target implementation is available, if the verifier lacks a documented checkpoint trust boundary, or if any tampered ledger is accepted and minimized.

## Evidence references

- Artifact root: `<local-path>/projects/fuzz-a-real-signed-agent-evidence-ledger-7a97c4f8cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
