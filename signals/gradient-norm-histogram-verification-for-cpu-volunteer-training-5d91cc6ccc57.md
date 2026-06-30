# Gradient Norm Histogram Verification for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-norm-histogram-verification-for-cpu-volunteer-training-5d91cc6ccc57`
Run ID: `gradient-norm-histogram-verification-for-cpu-volunteer-training-5d91cc6ccc57-20260620T160912318632+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dd37f5976891

## What looked useful

Magnitude-only norm histograms detect crude magnitude anomalies but fail the core correctness check: sign-flipped gradients preserve the histogram and norm features, match the honest flag rate, and have cosine nearly -1 to the honest update.

## Boundaries and scale limits

Synthetic data, small NumPy MLP, single-process CPU run, no real volunteer network, no large-model pretraining, no byzantine aggregation protocol, no signed sketches or cryptographic verification.

## Claim scope

Bounded CPU-only synthetic MLP test of magnitude-only gradient histogram and per-layer norm features for volunteer gradient-update verification.

## Why it stopped

Proxy early falsification: the directly tested magnitude-only histogram verifier cannot distinguish honest gradients from sign-inverted malicious gradients, so it is insufficient as a CPU volunteer training correctness verifier.

## Recommended next action

Stop this histogram-only verification path as a no-paper negative; next bounded work should compare magnitude histograms against signed random projections or redundant spot-check gradients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed sketch gradient verification versus magnitude-only histograms
- Success threshold: At <=5% honest validation false-positive rate, catch >=95% sign-flip updates and improve label-shift detection by at least 25 percentage points over magnitude-only histograms without more than 4x payload growth.
- Stop condition: Stop if signed compact checks still miss sign-flip updates or require payload size close to transmitting the full gradient.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-histogram-verification-for-cpu-volunteer-training-5d91cc6ccc57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
