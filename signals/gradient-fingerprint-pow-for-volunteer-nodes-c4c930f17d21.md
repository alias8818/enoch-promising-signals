# Gradient-Fingerprint PoW for Volunteer Nodes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-fingerprint-pow-for-volunteer-nodes-c4c930f17d21`
Run ID: `gradient-fingerprint-pow-for-volunteer-nodes-c4c930f17d21-20260609T000642054911+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48099f486882

## What looked useful

Gradient fingerprints can be statistically usable commitments, but the practical PoW construction needs a verifier that avoids full-gradient recomputation. With ordinary autograd, median sampled-check time was 0.991x prover time, so the local evidence does not support a cheap-verification volunteer-node PoW.

## Boundaries and scale limits

Synthetic data, one small two-layer MLP, 48 challenge seeds, one GPU host, no real volunteer-node network, no adversarial approximation kernels, and no cheap coordinate-gradient verifier implementation.

## Claim scope

Bounded synthetic test of gradient-sign fingerprints for a small MLP on GB10: fingerprints were high-entropy and challenge-sensitive, and hidden sampled checks strongly detected random or substantially incomplete fingerprints, but a straightforward autograd verifier had essentially the same cost as proving.

## Why it stopped

Proxy/local evidence is mixed: fingerprint entropy and sampled fraud detection are promising, but the straightforward verifier fails the core verification-asymmetry requirement and this is not a full validation.

## Recommended next action

Stop this as no-paper useful signal unless a concrete cheap unpredictable coordinate-gradient verifier is proposed; then test that verifier against the same hidden-sample commitment model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cheap coordinate-gradient verification for hidden sampled gradient fingerprints
- Success threshold: Median verifier/prover time ratio below 0.25 for 256 or more hidden sampled bits, with empirical pass rates matching the theoretical fraud model for provers computing 90% or less of fingerprint bits.
- Stop condition: Stop if coordinate-only verification is still at least 0.5x full-backprop cost or if approximation attacks pass 256 sampled checks above 1e-4 empirical rate.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-fingerprint-pow-for-volunteer-nodes-c4c930f17d21`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
