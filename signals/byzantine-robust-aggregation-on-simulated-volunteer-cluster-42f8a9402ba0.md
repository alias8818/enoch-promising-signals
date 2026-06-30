# Byzantine-Robust Aggregation on Simulated Volunteer Cluster

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `byzantine-robust-aggregation-on-simulated-volunteer-cluster-42f8a9402ba0`
Run ID: `byzantine-robust-aggregation-on-simulated-volunteer-cluster-42f8a9402ba0-20260628T055947486429+0000`

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

Geometric median averaged 0.8878 final accuracy across attacked runs versus 0.8921 in its clean baseline and 0.4136 for attacked mean aggregation. Coordinate median and Krum were similarly robust; trimmed mean was attack-sensitive, dropping to 0.2618 accuracy under omniscient mean reversal.

## Boundaries and scale limits

Synthetic binary classification only; no real volunteer network, asynchronous staleness, real image/language data, secure aggregation, heterogeneous hardware timing, or adaptive adversary validation. Medium sweep was 5 seeds, 3 attacks, 5 aggregators, and 60 rounds.

## Claim scope

In a small synthetic logistic-regression federated simulation with 40 volunteers, 65% random participation, non-IID client data, and 25% Byzantine clients, geometric median, coordinate median, and Krum preserved near-clean held-out accuracy under sign-flip, ALIE, and omniscient mean-reversal attacks, while plain mean failed and fixed 20% trimmed mean failed under the omniscient attack.

## Why it stopped

No-paper useful signal: the local synthetic experiment supports the mechanism but is not direct enough for a publication-grade claim about volunteer clusters.

## Recommended next action

Run a bounded deepen follow-up on a real small dataset such as MNIST/Fashion-MNIST with simulated volunteer staleness and adaptive Byzantine attacks; stop treating this synthetic run as paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data volunteer staleness benchmark for robust aggregation
- Success threshold: At 25% Byzantine clients, geometric median or coordinate median reaches at least 90% of the clean-baseline final accuracy and exceeds attacked mean aggregation by at least 20 absolute accuracy points across at least 5 seeds.
- Stop condition: Stop as negative if robust aggregators fail to beat attacked mean by 10 absolute accuracy points or fall below 80% of clean-baseline accuracy in two independent attack settings.

## Evidence references

- Artifact root: `<local-path>/projects/byzantine-robust-aggregation-on-simulated-volunteer-cluster-42f8a9402ba0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
