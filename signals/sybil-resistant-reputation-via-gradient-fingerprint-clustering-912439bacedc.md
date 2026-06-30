# Sybil-resistant reputation via gradient fingerprint clustering

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sybil-resistant-reputation-via-gradient-fingerprint-clustering-912439bacedc`
Run ID: `sybil-resistant-reputation-via-gradient-fingerprint-clustering-912439bacedc-20260628T112317440385+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6807a94e26b3

## What looked useful

Fingerprint clustering is useful as a near-duplicate collusion detector. At Sybil noise 0.03 it reduced Sybil weight from 0.3333 to 0.0244 and improved final accuracy by about 0.96 versus uniform averaging. At strict threshold 0.985 it failed by Sybil noise 0.10; threshold 0.90/0.80 recovered noise 0.10 but still failed at noise 0.25.

## Boundaries and scale limits

Evidence is synthetic only: 80-dimensional logistic regression, local NumPy simulation, fixed attacker family, no real FL benchmark, no production reputation trace, and no comparison against a broad robust-aggregation suite.

## Claim scope

In a synthetic federated logistic-regression setting with 40 honest clients and 20 coordinated Sybils, cosine gradient-fingerprint clustering can sharply downweight near-identical Sybil gradients and preserve clean accuracy, but it is not robust to sufficiently noisy/adaptive Sybil gradients.

## Why it stopped

Bounded synthetic evidence supports a narrow mechanism but also found a clear adaptive-noise failure mode; this does not justify a broad Sybil-resistant reputation paper.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate adaptive covariance-matching Sybils and threshold selection on a real or standard federated benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive gradient-fingerprint Sybil benchmark with covariance-matching attackers
- Success threshold: Fingerprint reputation cap improves clean utility or attack-resistance by at least 10 percentage points over norm clipping while keeping honest-only false cluster rate below 5% across at least three non-IID settings.
- Stop condition: Stop if adaptive covariance-matching Sybils retain at least 80% of uniform Sybil weight or if honest-only false cluster rate exceeds 5% at thresholds needed for attack detection.

## Evidence references

- Artifact root: `<local-path>/projects/sybil-resistant-reputation-via-gradient-fingerprint-clustering-912439bacedc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
