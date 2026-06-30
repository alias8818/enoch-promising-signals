# Gossip Top-K Sparse Gradients over WebRTC Mesh

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gossip-top-k-sparse-gradients-over-webrtc-mesh-bf740f720dab`
Run ID: `gossip-top-k-sparse-gradients-over-webrtc-mesh-bf740f720dab-20260526T030951460555+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acd2798a41c2

## What looked useful

Error feedback is the required mechanism for sparse gradient gossip in this setting. Top-k 1% with error feedback used 2.87% of dense bytes and had final loss 0.5167 versus dense 0.5184 at 0% message loss; under 5% random message loss it had final loss 0.5170 versus dense 0.5193. Top-k without error feedback had higher loss around 0.531 under both loss settings.

## Boundaries and scale limits

Proxy-only evidence: no real browser WebRTC/SCTP stack, NAT traversal, congestion control, peer churn, large neural model gradients, or real training traces were tested. The workload was CPU-only and synthetic, so this is not publication-grade systems or ML validation.

## Claim scope

In a deterministic NumPy simulator of 16-peer decentralized logistic regression with non-IID synthetic data, random fanout-2 mesh gossip, 300 rounds, 5 seeds, and WebRTC-like byte accounting, top-k sparse gradient gossip with residual error feedback preserved final loss and accuracy while using 2.87% to 10.80% of dense gossip bytes. Plain top-k without error feedback saved bytes but worsened final loss.

## Why it stopped

Proxy-only simulator evidence supports the mechanism but does not directly validate real WebRTC mesh behavior or large-model training, so it should not trigger paper writing.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next action is a bounded real WebRTC datachannel follow-up that reproduces the same dense, top-k, and top-k-with-error-feedback comparison with browser peers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Browser WebRTC Datachannel Validation of Error-Feedback Top-K Gossip
- Success threshold: Top-k with error feedback uses no more than 15% of dense datachannel bytes and finishes within 5% relative final loss of dense gossip across at least 3 seeds or repeated browser runs; plain top-k remains worse or is explained by diagnostics.
- Stop condition: Stop if WebRTC overhead, delivery behavior, or browser resource limits push top-k-with-error-feedback above 30% of dense bytes or more than 10% relative final-loss degradation in two repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-top-k-sparse-gradients-over-webrtc-mesh-bf740f720dab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
