# Commit-Reveal Gradient Verification for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-verification-for-volunteer-training-d7621416eeea`
Run ID: `commit-reveal-gradient-verification-for-volunteer-training-d7621416eeea-20260628T221548648774+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4c26e074009b

## What looked useful

Commit-reveal is useful as a timing/integrity primitive, not as standalone gradient verification. It rejected altered reveals and preserved 0.9618 mean accuracy against a 4x stale precommit attack where no-commit adaptive attack collapsed to 0.5005, but at 8x budget precommitted malicious gradients collapsed accuracy to 0.0612.

## Boundaries and scale limits

Toy convex model only; 40 seeded synthetic runs; no real volunteer network, private-data verification, secure aggregation, straggler timing, non-IID client data, or neural-network-scale training.

## Claim scope

Synthetic 20-client logistic-regression volunteer training with 20% malicious clients shows commit-reveal binds revealed gradient bytes and can block a current-round adaptive last-mover collapse at a 4x honest-gradient norm budget, but it does not verify gradient correctness and fails under larger precommitted malicious updates.

## Why it stopped

Bounded synthetic evidence supports a narrow mechanism but also shows commit-reveal alone cannot verify honest gradient computation or prevent high-budget precommitted poisoning.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add norm clipping plus robust aggregation in a small nonconvex federated-learning benchmark and compare commit-reveal-only against no-commit and robust baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal with Norm Clipping and Robust Aggregation on Small Federated Neural Benchmarks
- Success threshold: Combined commit-reveal plus clipping/robust aggregation preserves >=90% honest-baseline accuracy and improves by >=20 percentage points over no-commit adaptive attack at a matched feasible norm budget.
- Stop condition: Stop if commit-reveal-only and combined defenses both fail to improve accuracy by at least 10 percentage points over no-commit adaptive attack, or if overhead/rejection behavior makes the protocol impractical in the small benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-verification-for-volunteer-training-d7621416eeea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
