# Real-Agent Evidence Ledger Integrity Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-evidence-ledger-integrity-replay-36e6aa972e`
Run ID: `real-agent-evidence-ledger-integrity-replay-36e6aa972e-20260524T222131443358+0000`

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

- Parent run decision: Evidence-Ledger Agent Integrity: enoch://control-plane/projects/evidence-ledger-agent-integrity-556a687c49dd/runs/evidence-ledger-agent-integrity-556a687c49dd-20260524T220110997952+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e971ea2dbc86

## What looked useful

Unanchored replay passed clean verification and detected 6/7 tamper classes but missed payload edit with full hash-chain recomputation. Anchored replay passed clean verification and detected 7/7 tamper classes, including recomputation via anchored_head_hash_mismatch.

## Boundaries and scale limits

Single workspace, 5 ledger entries, 7 artifact checks, 7 controlled tamper classes, simulated external anchor only; no production agent traces, real transparency log, key-management path, crash recovery, concurrent writers, or distributed storage adversary were tested.

## Claim scope

In a small controlled local replay test over real command/file artifacts, hash-chained evidence ledgers with artifact digests detected ordinary entry, artifact, deletion, reordering, digest, and timestamp tampering; preserving the original ledger head hash as an external anchor also detected full-chain recomputation.

## Why it stopped

Tier 1 controlled direct test completed with a useful mechanism signal, but the evidence is too narrow and uses a simulated anchor, so it is no-paper rather than paper-positive.

## Recommended next action

Run a bounded deepen test using a real signed or append-only external anchor across multiple agent traces with crash and concurrent-write cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed External Anchor Evidence Ledger Replay
- Success threshold: Clean replay passes on all traces and anchored replay detects at least 95% of injected tamper cases overall, including 100% of full-chain recomputation cases, with baseline unanchored recomputation failure reproduced.
- Stop condition: Stop if the real anchor cannot be verified offline, clean replay fails on more than one trace due to ledger design rather than injected corruption, or full-chain recomputation is not reliably detected.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-integrity-replay-36e6aa972e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
