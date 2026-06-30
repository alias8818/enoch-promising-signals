# Cheating-Resistant Volunteer Training via Commitment-Based Gradient Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cheating-resistant-volunteer-training-via-commitment-based-gradient-verification-0fea379ad0db`
Run ID: `cheating-resistant-volunteer-training-via-commitment-based-gradient-verification-0fea379ad0db-20260605T054604023231+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/28a3c5acb135

## What looked useful

Commitment timing matters: audit sets announced before submission let rational malicious workers cheat undetected, while post-commitment audits plus blacklisting caught and removed all malicious workers in every bounded sign-flip run and improved 5-seed mean accuracy from 0.2161 unchecked and 0.2626 announced-audit to 0.7288 versus a 0.7479 honest-worker ceiling.

## Boundaries and scale limits

Synthetic data only; small MLP only; one process; no real distributed networking, privacy-preserving proof system, bandwidth accounting, collusion, adaptive subtle-gradient attackers, data custody failures, or LLM-scale training.

## Claim scope

In a single-process synthetic MLP volunteer-training simulator with deterministic auditable batches, 25% malicious sign-flip workers, and persistent blacklisting after failed audits, sampling audits after gradient commitments restored test accuracy near the honest-worker control while unchecked and pre-announced audit baselines failed.

## Why it stopped

No-paper useful signal: synthetic evidence supports the mechanism, but real distributed verification, privacy, bandwidth, and adaptive-attack evidence are still missing.

## Recommended next action

Run a bounded real distributed PyTorch prototype with signed commitments, deterministic dataloader replay, and adaptive low-magnitude gradient attackers before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distributed Commitment-Audit Gradient Verification with Adaptive Attackers
- Success threshold: At 25% malicious workers and no more than 25% audit rate, preserve at least 95% of honest-control validation accuracy, blacklist at least 90% of malicious workers within the first 20% of training rounds, keep false positives at 0, and add less than 15% wall-clock overhead in the prototype.
- Stop condition: Stop if deterministic audit replay cannot be made reliable, if false positives occur under honest workers, or if adaptive low-magnitude attacks evade detection while reducing validation accuracy by more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-volunteer-training-via-commitment-based-gradient-verification-0fea379ad0db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
