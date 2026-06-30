# Tiny Agent Tool-Call Verification via Local Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-agent-tool-call-verification-via-local-evidence-ledger-794500027688`
Run ID: `tiny-agent-tool-call-verification-via-local-evidence-ledger-794500027688-20260607T234800560726+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e3a7643c1d8a

## What looked useful

A minimal local evidence ledger is a cheap and reproducible consistency verifier for tiny agent tool-call transcripts, improving over an accept-all transcript baseline in the synthetic task, but it does not establish end-to-end truth without protecting the ledger writer and append-only storage.

## Boundaries and scale limits

Synthetic deterministic tools only; no real LLM agent runtime, concurrent tool execution, OS append-only enforcement, external timestamping, or compromised ledger-writer adversary was tested. Collusive transcript-and-ledger rewrites remain accepted when internally consistent.

## Claim scope

In a synthetic local setting with honest ledger creation and append-only preservation, canonical JSON hashes plus a hash-chained local evidence ledger detected all tested non-collusive transcript/ledger mismatches across two 20,000-trial runs with 8 tool calls per transcript.

## Why it stopped

No-paper closure: this is useful synthetic mechanism evidence, not publication-grade validation of robust agent tool-call verification.

## Recommended next action

Run a bounded real-runtime follow-up that wraps an actual agent tool interface with append-only ledger writes and adversarial transcript/file tampering over at least 1,000 mixed tool calls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-runtime append-only ledger verification for tiny agent tools
- Success threshold: Verifier rejects at least 99% of non-collusive tampering attempts with zero honest false rejects and p95 per-call overhead below 1 ms on local CPU.
- Stop condition: Stop as negative if honest runs produce any unexplained false reject, if non-collusive tamper detection falls below 95%, or if p95 overhead exceeds 5 ms per call without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-tool-call-verification-via-local-evidence-ledger-794500027688`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
