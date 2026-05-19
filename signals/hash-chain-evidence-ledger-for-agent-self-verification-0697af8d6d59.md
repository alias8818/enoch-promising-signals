# Hash-Chain Evidence Ledger for Agent Self-Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chain-evidence-ledger-for-agent-self-verification-0697af8d6d59`
Run ID: `hash-chain-evidence-ledger-for-agent-self-verification-0697af8d6d59-20260518T115216189794+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2a648939756d

## What looked useful

Hash-chain ledgers are useful for evidence chronology and tamper detection only when the verifier retains non-rewritable anchors or key material; a public unanchored chain is rewritable, and byte-level ledgers do not establish semantic truth of observations.

## Boundaries and scale limits

Synthetic traces only; no live LLM agent, real tool wrapper, remote timestamping, append-only service, trusted execution, or production adversary model. Benchmarks are local Python construction throughput, not deployment overhead.

## Claim scope

In a synthetic local trace simulator, externally anchored public hash chains and verifier-keyed HMAC chains detected byte-level action/observation log edits, deletions, reorders, recompute rewrites, and fake appends, while no tested ledger detected false observation content that was logged consistently from the beginning.

## Why it stopped

Synthetic evidence supports the integrity mechanism but also shows an early limitation: ledger self-verification cannot validate semantic observation truth without independent capture.

## Recommended next action

Run a direct real-agent deepen test with an independent signed observation recorder; stop this run as a synthetic useful-signal result rather than paper-ready validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed Observation Recorder for Real Agent Evidence Ledgers
- Success threshold: Detect at least 95% of injected false final-report claims and 100% of byte-level ledger tampering with less than 10% median wall-clock overhead on local tool episodes.
- Stop condition: Stop as negative if signed observation capture cannot distinguish false claims from true claims above 80% detection at less than 20% overhead, or if integration requires unavailable private infrastructure.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chain-evidence-ledger-for-agent-self-verification-0697af8d6d59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
