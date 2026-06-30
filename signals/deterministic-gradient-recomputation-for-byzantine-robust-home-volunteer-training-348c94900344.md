# Deterministic Gradient Recomputation for Byzantine-Robust Home Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-gradient-recomputation-for-byzantine-robust-home-volunteer-training-348c94900344`
Run ID: `deterministic-gradient-recomputation-for-byzantine-robust-home-volunteer-training-348c94900344-20260630T034008998394+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10b86387d25e

## What looked useful

Deterministic recomputation is an exact verifier for checked computation tampering in this simulator, but it does not by itself make volunteer training robust unless the coordinator recomputes a large fraction of updates. With a sign-flip attack, 0.5 audit left 49.8% of Byzantine updates accepted, mean aggregate cosine remained negative (-0.1969), and final accuracy was only 0.3186; 1.0 audit rejected all Byzantine updates and reached 0.9840 accuracy.

## Boundaries and scale limits

Toy convex model and synthetic data only. No real home-volunteer network, heterogeneous-device determinism, large model, privacy constraint, data poisoning, churn, or wall-clock distributed training validation. Full recomputation cost was represented by audit fraction, not measured as a real distributed systems overhead.

## Claim scope

Bounded deterministic federated-style simulator with 20 clients, 20% Byzantine clients, logistic regression, deterministic per-client data and batches, and server recomputation of submitted gradients. Full recomputation detected and rejected all checked forged gradients in sign-flip, random, and scale attacks; partial spot-checking alone was insufficient against sign-flip attacks below high audit rates.

## Why it stopped

Proxy/local simulator evidence shows full recomputation works as a verifier, but practical spot-check-only deterministic recomputation is not robust enough against targeted sign-flip attacks at moderate audit rates; this is not full validation of real home-volunteer training.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test deterministic spot-checking combined with robust aggregation under the same sign-flip setting before considering larger distributed validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic spot-checking plus robust aggregation under targeted Byzantine gradients
- Success threshold: At 0.5 audit or lower with 20% sign-flip Byzantine clients, recomputation plus robust aggregation reaches at least 0.95 final accuracy and mean aggregate cosine at least 0.8 while outperforming robust aggregation alone and recomputation alone.
- Stop condition: Stop if no combined method reaches 0.9 final accuracy or if robust aggregation alone matches the combined method within 0.01 accuracy and 0.05 aggregate cosine, because recomputation would add no useful benefit in this bounded setting.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-gradient-recomputation-for-byzantine-robust-home-volunteer-training-348c94900344`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
