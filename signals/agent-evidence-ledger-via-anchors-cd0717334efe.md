# Agent Evidence Ledger via Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-evidence-ledger-via-anchors-cd0717334efe`
Run ID: `agent-evidence-ledger-via-anchors-cd0717334efe-20260602T102913789033+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/18f8c2625857

## What looked useful

Chunked anchors are a viable local provenance mechanism for agent evidence ledgers, but full-prefix Merkle anchoring is an inefficient default. The 100k chunked run detected all tested tamper cases with practical CPU throughput; the naive prefix design was 11.90x baseline at 10k and a 100k attempt was terminated as too slow for this bounded CPU-only run.

## Boundaries and scale limits

Synthetic events only; local anchors only; no public timestamping, remote transparency log, real agent traces, concurrent writer test, crash recovery test, streaming verifier, or privileged attacker model. JSON storage overhead was about 1.80x baseline in the 100k-event run.

## Claim scope

In a synthetic local agent-event workload, a SHA-256 hash-chain evidence ledger with chunked Merkle anchors every 100 events and chained anchor records detected six controlled post-hoc tamper mutations while appending 100,000 events at median 166,120 events/s and verifying at median 298,026 events/s.

## Why it stopped

Synthetic local-only evidence supports the mechanism but is insufficient for a publication-grade or externally witnessed provenance claim.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test should replay the chunk-anchor ledger on real agent traces with external anchor publication and crash/restart recovery checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Evidence Ledger with External Anchor Publication
- Success threshold: All tested real-trace tamper mutations are detected, clean traces verify after restart, append throughput remains at least 50,000 events/s, verification remains at least 50,000 events/s, peak RSS is bounded below 512 MB for streaming verification, and storage overhead is below 2.5x baseline trace JSON.
- Stop condition: Stop if external anchors cannot be durably published in the local environment, if clean real traces fail verification after crash recovery, or if throughput drops below 10,000 events/s on ordinary traces without a clear implementation fix.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-via-anchors-cd0717334efe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
