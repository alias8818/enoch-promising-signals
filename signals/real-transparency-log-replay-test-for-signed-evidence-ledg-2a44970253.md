# Real Transparency-Log Replay Test for Signed Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-transparency-log-replay-test-for-signed-evidence-ledg-2a44970253`
Run ID: `real-transparency-log-replay-test-for-signed-evidence-ledg-2a44970253-20260524T231211311543+0000`

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

- Parent run decision: Signed External Anchor Evidence Ledger Replay: enoch://control-plane/projects/signed-external-anchor-evidence-ledger-replay-dcd1bf37ca/runs/signed-external-anchor-evidence-ledger-replay-dcd1bf37ca-20260524T230201532570+0000
- Parent run decision: Real-Agent Evidence Ledger Integrity Replay: enoch://control-plane/projects/real-agent-evidence-ledger-integrity-replay-36e6aa972e/runs/real-agent-evidence-ledger-integrity-replay-36e6aa972e-20260524T222131443358+0000

## What looked useful

500/500 live Rekor entries verified in 82.394 seconds at 6.07 entries/s with 0 cryptographic failures; matched fetch-only baseline was 500/500 in 91.176 seconds; body, checkpoint, and SET tamper controls each failed 5/5 as expected.

## Boundaries and scale limits

No full 1.5B-entry log replay; no historic-to-latest consistency-proof validation; no arbitrary underlying artifact signature/certificate/policy validation; public Rekor API rate-limited naive 1000-entry multi-thread fetching with HTTP 429.

## Claim scope

A dependency-light Python/OpenSSL harness independently replay-verified 500 randomly sampled live Sigstore Rekor V1 public-log entries by checking RFC6962 inclusion proofs, signed checkpoint binding, and signed entry timestamp signatures; body/checkpoint/SET tamper controls were rejected.

## Why it stopped

Bounded real-log replay supports the mechanism but does not meet paper-ready evidence depth because it omits full-log replay, append-only consistency validation to latest checkpoints, and arbitrary artifact-level signature policy checks.

## Recommended next action

Stop this branch as no-paper useful signal; next bounded deepening should add consistency-proof verification from sampled checkpoints to current tree heads and compare against an established Rekor monitor/omniwitness workflow.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Consistency-Proof Replay for Sampled Rekor Checkpoints
- Success threshold: For supported Rekor shards, >=99.5% of sampled entries pass inclusion, checkpoint, SET, and consistency verification with all tamper controls rejected; any non-API-rate-limit failure must be triaged by entry/shard.
- Stop condition: Stop if Rekor APIs cannot provide the required consistency proofs for sampled checkpoints, if more than 0.5% of non-rate-limited entries fail cryptographic validation, or if production-monitor comparison disagrees without a documented API/version explanation.

## Evidence references

- Artifact root: `<local-path>/projects/real-transparency-log-replay-test-for-signed-evidence-ledg-2a44970253`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
