# Tiny Async Peer Gradient Compression for Home Clusters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-async-peer-gradient-compression-for-home-clusters-c5e66a7464bd`
Run ID: `tiny-async-peer-gradient-compression-for-home-clusters-c5e66a7464bd-20260604T034303703190+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/79f886d5213e

## What looked useful

Top-k 1% with error feedback matched dense async within about 1% final loss while reducing bytes by about 50x at 1 Mbps and 16x at 50 kbps; top-k without error feedback was worse. However, dense async itself was 14x-51x worse than sync on final loss/optimum ratio, so compression improves communication inside a weak async baseline rather than validating the full idea.

## Boundaries and scale limits

Synthetic convex data only; no real multi-host network, no packet/serialization overhead measurement, no neural model, no GPU training, no datacenter-scale validation, and only 5 seeds for the main network settings.

## Claim scope

In a local event-driven convex ridge-regression proxy with 8 non-IID peers, heterogeneous compute timing, and 1 Mbps or 50 kbps modeled home-uplink constraints, error-feedback top-k/sign compression preserves dense async peer-gradient quality at much lower bytes, but the stale peer-gradient async method is far worse than dense synchronous all-reduce on final loss.

## Why it stopped

Proxy evidence supports the compression submechanism but early-falsifies the tested stale async peer-gradient update rule as competitive with synchronous dense training; this is not a full validation or publication-grade result.

## Recommended next action

Stop this stale peer-gradient variant as no-paper; the bounded next test is to replace peer-gradient application with compressed error-feedback model-delta or elastic averaging and rerun the same simulator before any real cluster work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed error-feedback model-delta averaging for tiny home-cluster peers
- Success threshold: At both 1 Mbps/15 ms and 50 kbps/30 ms, compressed async model-delta averaging reaches final loss/optimum no worse than 2x the synchronous dense baseline while sending at least 5x fewer bytes than dense async.
- Stop condition: Stop if compressed model-delta averaging remains above 5x the synchronous dense final loss/optimum ratio or shows instability/NaNs in two or more seeds at any tuned stable learning rate.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-async-peer-gradient-compression-for-home-clusters-c5e66a7464bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
