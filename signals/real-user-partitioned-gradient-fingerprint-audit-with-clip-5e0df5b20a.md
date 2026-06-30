# Real user-partitioned gradient fingerprint audit with clipping and DP noise

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-user-partitioned-gradient-fingerprint-audit-with-clip-5e0df5b20a`
Run ID: `real-user-partitioned-gradient-fingerprint-audit-with-clip-5e0df5b20a-20260609T140735118673+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Gradient fingerprint audit for volunteer federated updates: enoch://control-plane/projects/gradient-fingerprint-audit-for-volunteer-federated-updates-9237af52dbf8/runs/gradient-fingerprint-audit-for-volunteer-federated-updates-9237af52dbf8-20260609T071114766918+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

Same-writer top-1 matching peaked at 0.0625 versus 0.03125 random chance and 0.0344 false-pairing control with no noise; at noise_multiplier >= 0.1, top-1 fell to 0.0177-0.0240, below chance.

## Boundaries and scale limits

Not pretrained OpenAI CLIP; 32 users; handwriting images only; 8 samples per split; no formal privacy accountant; Gaussian noise applied as a DP-style mechanism proxy to clipped user gradients.

## Claim scope

Tier 1 controlled audit on 32 real FEMNIST writer partitions using disjoint per-writer gradient fingerprints from a locally trained CLIP-vision-shaped encoder; clipping alone gave only weak linkability and DP-style Gaussian noise removed it.

## Why it stopped

Tier 1 real-user audit did not support robust gradient fingerprint survival under DP-style Gaussian noise; this is not a full pretrained-CLIP validation.

## Recommended next action

Stop this run as a no-paper useful negative signal; run one bounded follow-up with actual pretrained CLIP weights and 64-256 real users if the model weights can be cached reliably.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained CLIP real-user gradient fingerprint audit with confidence intervals
- Success threshold: At noise_multiplier >= 0.1, same-user top-1 is at least 3x random chance and statistically above the false-pairing control; otherwise close negative.
- Stop condition: Stop if pretrained CLIP top-1 is below 3x chance at noise_multiplier >= 0.1 across two seeds, or if model weights cannot be cached within a bounded setup window.

## Evidence references

- Artifact root: `<local-path>/projects/real-user-partitioned-gradient-fingerprint-audit-with-clip-5e0df5b20a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
