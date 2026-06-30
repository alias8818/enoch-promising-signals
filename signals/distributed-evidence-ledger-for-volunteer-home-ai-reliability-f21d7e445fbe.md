# Distributed evidence ledger for volunteer home AI reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distributed-evidence-ledger-for-volunteer-home-ai-reliability-f21d7e445fbe`
Run ID: `distributed-evidence-ledger-for-volunteer-home-ai-reliability-f21d7e445fbe-20260605T191825182171+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c229376e617b

## What looked useful

The ledger mechanism caught 5/5 validly re-signed payload tamper trials and 5/5 unsigned payload tamper trials while the flat baseline caught 0/5 for both; it also had 0/5 false positives on clean logs and about 65,994 verified records/s median throughput in pure Python.

## Boundaries and scale limits

Synthetic local evidence only: HMAC stands in for public-key signatures, nodes are generated rather than networked, reliability reports are synthetic, and the run does not test partitions, gossip, privacy constraints, long-lived storage, real volunteer churn, or 1M+ report scale.

## Claim scope

In a deterministic synthetic prototype with 64 volunteer nodes and 10,000 generated reliability reports per trial, per-node authenticated hash chains plus periodic Merkle checkpoints detected payload tampering, validly re-signed payload tampering, omission, replay, and validly signed equivocation across 5 seeds, including ledger-only detection of payload changes missed by a flat-log baseline.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic and local; it supports the integrity mechanism but does not validate a deployed distributed volunteer reliability ledger.

## Recommended next action

Run a bounded networked deepen test with public-key volunteer identities, checkpoint gossip, and replayed or real inference telemetry before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Networked public-key checkpoint gossip for volunteer AI reliability evidence
- Success threshold: Detect at least 99% of injected integrity failures with zero clean-run false positives across three seeds, sustain at least 10,000 reports/s aggregate verification, and keep verifier storage overhead under 2 KB per report including checkpoints.
- Stop condition: Stop if public-key/gossip overhead drops below 1,000 reports/s, if clean runs produce false positives, or if any validly signed payload tamper/equivocation class is missed in repeated trials.

## Evidence references

- Artifact root: `<local-path>/projects/distributed-evidence-ledger-for-volunteer-home-ai-reliability-f21d7e445fbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
