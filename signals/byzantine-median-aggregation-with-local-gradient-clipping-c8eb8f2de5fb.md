# Byzantine-Median Aggregation with Local Gradient Clipping

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `byzantine-median-aggregation-with-local-gradient-clipping-c8eb8f2de5fb`
Run ID: `byzantine-median-aggregation-with-local-gradient-clipping-c8eb8f2de5fb-20260607T134155239703+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/db9f9c4c51eb

## What looked useful

Fixed clipping at norm 5.0 eliminated median divergence across attacked medium-sweep settings but worsened median final loss overall (median loss 75.575 versus 16.122 for unclipped median). A targeted threshold sweep showed best calibrated clipping beat no clipping in 14 of 16 heterogeneous attacked conditions, mainly by preventing divergence, with winning thresholds varying from 5 to 100.

## Boundaries and scale limits

Evidence is limited to local NumPy simulations, 50-dimensional linear regression, 40 clients, 12 random seeds per medium/threshold condition, two synthetic Byzantine attacks, and clipping of honest client gradients. It does not validate deep non-convex training, real federated datasets, adaptive adversaries, privacy constraints, network effects, or large-scale multi-node training.

## Claim scope

In synthetic federated convex linear regression with 40 clients, coordinate-wise median aggregation, controlled sign-flip/rank-bias Byzantine clients, and client heterogeneity sweeps, local gradient clipping can prevent median aggregation collapse in high-Byzantine/high-heterogeneity regimes, but fixed low-threshold clipping is not a general improvement and can substantially hurt easier regimes.

## Why it stopped

Proxy synthetic evidence is sufficient to reject a broad paper-positive claim for fixed local clipping, but it is not direct full validation; calibrated clipping remains promising only in specific high-attack/high-heterogeneity regimes.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded real-workload follow-up that compares adaptive local clipping versus no clipping for median aggregation on a small neural/federated benchmark with the same attack families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive local clipping for Byzantine median aggregation on a real federated benchmark
- Success threshold: Adaptive median plus clipping must match unclipped median within 2% relative final accuracy/loss in benign and low-attack regimes while reducing divergence or catastrophic-loss incidence by at least 50% in high-attack/high-heterogeneity regimes across at least 5 seeds.
- Stop condition: Stop if adaptive clipping still degrades benign/low-attack final quality by more than 5% relative to unclipped median, or if it fails to reduce high-attack divergence/catastrophic-loss incidence versus unclipped median.

## Evidence references

- Artifact root: `<local-path>/projects/byzantine-median-aggregation-with-local-gradient-clipping-c8eb8f2de5fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
