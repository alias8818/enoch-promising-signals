# Top-K Sparse Updates for Bandwidth-Limited Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `top-k-sparse-updates-for-bandwidth-limited-volunteer-training-d4cba2150fdc`
Run ID: `top-k-sparse-updates-for-bandwidth-limited-volunteer-training-d4cba2150fdc-20260628T014532032029+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f232d869c4a5

## What looked useful

Error feedback was the key mechanism. At 300 rounds across five seeds, dense reached 0.977133 mean validation accuracy. Top-k 1% with error feedback reached 0.977100 at 49.9x fewer bytes, while top-k 1% without error feedback reached 0.973733 and worse loss. Extreme 0.1% top-k with error feedback lagged at round 50 but recovered to dense-like accuracy by round 300, indicating a bandwidth-versus-rounds tradeoff.

## Boundaries and scale limits

Synthetic Gaussian classification only; no real volunteer network, no unreliable clients, no secure aggregation, no privacy mechanism, no natural language or image dataset, no foundation-model scale, and no multi-node systems validation. Final task accuracy saturates, so evidence is strongest for mechanism and byte/round tradeoff, not broad training quality.

## Claim scope

In a single-host synthetic non-IID four-client supervised training simulation with a 25k-parameter MLP, top-k sparse gradient updates with residual error feedback preserved dense-like validation accuracy after 300 synchronous rounds while reducing transmitted update bytes by about 50x at 1% top-k and about 487x at 0.1% top-k.

## Why it stopped

No-paper closure: the local synthetic mechanism result is useful but is not direct volunteer-training evidence and does not support a publication-grade claim.

## Recommended next action

Run a bounded real-data follow-up using the same dense/top-k/error-feedback controls on a small image or language workload with simulated volunteer dropout and report accuracy or perplexity per transmitted byte.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Top-k error-feedback updates on a small real-data volunteer simulation
- Success threshold: 1% top-k with error feedback reaches within 2% relative validation loss or perplexity of dense by the end of the budget while reducing transmitted update bytes by at least 25x and outperforming 1% top-k without error feedback.
- Stop condition: Stop as negative if dense learns but 1% top-k error-feedback remains worse than the 2% relative metric threshold after using the same round budget or if bandwidth savings are erased by the extra rounds needed to recover.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-sparse-updates-for-bandwidth-limited-volunteer-training-d4cba2150fdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
