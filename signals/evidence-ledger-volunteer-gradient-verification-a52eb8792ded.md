# Evidence-Ledger Volunteer Gradient Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-volunteer-gradient-verification-a52eb8792ded`
Run ID: `evidence-ledger-volunteer-gradient-verification-a52eb8792ded-20260531T100403313943+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/059565658986

## What looked useful

Across 19,200 submissions with 3,879 malicious gradients, full deterministic replay detected 3,879/3,879 malicious submissions with 0 replay false positives, and all ledger tamper mutations were detected. Random spot-check detection scaled with the check probability, while norm-only screening caught only 24.77% of malicious submissions and mostly missed same-norm attacks.

## Boundaries and scale limits

Tested only synthetic data, a small MLP, one local GPU worker, deterministic replay with verifier access to seeds, 19,200 total submissions across three seeds, and four simple attack classes. Did not test real volunteer networking, privacy-preserving data, Sybil/collusion resistance, large transformer workloads, or production throughput economics.

## Claim scope

In a local synthetic CUDA MLP simulation with deterministic model/data seeds, an append-only hash-chained evidence ledger plus exact replay of checked gradient receipts detects altered volunteer gradient submissions with zero observed replay false positives, and ledger field mutation invalidates the chain.

## Why it stopped

The local simulation supports the scoped replay-and-ledger mechanism but is not direct/full validation of volunteer gradient verification under real distributed, privacy, adversarial, or large-model conditions.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded work should implement the same receipt/replay protocol on a real model/data loader with a volunteer-style RPC submission path and measure verifier overhead against accepted training throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Volunteer RPC Gradient Receipt Replay on Real Model/Data Pipeline
- Success threshold: At p=0.10, replay verification has zero false positives over at least 10,000 honest audited receipts, detects at least 99% of checked malicious receipts, ledger restart validation catches all injected tamper events, and verifier overhead remains below 15% of accepted training step wall-clock.
- Stop condition: Stop as negative if deterministic replay produces any unexplained honest false positives, if checked malicious receipts evade exact replay, or if verifier overhead exceeds 50% of training step wall-clock in the bounded RPC setup.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-volunteer-gradient-verification-a52eb8792ded`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
