# Held-Out Challenge Batches Detect Volunteer Gradient Cheating

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-challenge-batches-detect-volunteer-gradient-cheating-ed482257c392`
Run ID: `held-out-challenge-batches-detect-volunteer-gradient-cheating-ed482257c392-20260628T054933233293+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/befc816e0544

## What looked useful

When challenge gradients occupy an observable sentinel subspace, a relative-error check detected skip-challenge, random, scaled, flipped-challenge, and stale-gradient cheating with 99.5-100% flag rates while honest false positives were 0% in the tested runs. A low-challenge-weight run showed skip-challenge cheating can remain nearly full-gradient-cosine indistinguishable while still being caught by challenge-specific observability.

## Boundaries and scale limits

Not tested on real volunteer infrastructure, LLM training, nonseparable aggregate gradients, compression pipelines, secure protocols, or adaptive attackers aware of the challenge construction.

## Claim scope

Synthetic logistic-regression volunteer-gradient simulation with separable sentinel-coordinate held-out challenge batches; tested honest workers and five simple cheating strategies under small submission noise.

## Why it stopped

Bounded synthetic evidence supports the mechanism, but the claim depends on separable challenge observability and does not yet cover real training systems or adaptive cheaters.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the detector in a small PyTorch model with per-microbatch commitments or a reserved embedding/sentinel subspace and include an adaptive attacker.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Challenge-gradient cheating detector in a small PyTorch volunteer-training loop
- Success threshold: At least 95% detection of skip-work and stale-gradient cheating at <=1% honest false positive rate across three random seeds, with global norm/cosine baselines materially worse on at least one hard scenario.
- Stop condition: Stop if honest false positives exceed 5% at thresholds needed for 90% cheat detection, or if adaptive attackers can satisfy the challenge check while skipping normal-gradient computation in the tested protocol.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-challenge-batches-detect-volunteer-gradient-cheating-ed482257c392`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
