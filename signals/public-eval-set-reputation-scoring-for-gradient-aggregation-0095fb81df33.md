# Public Eval-Set Reputation Scoring for Gradient Aggregation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `public-eval-set-reputation-scoring-for-gradient-aggregation-0095fb81df33`
Run ID: `public-eval-set-reputation-scoring-for-gradient-aggregation-0095fb81df33-20260628T220513199260+0000`

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

Public-eval reputation strongly suppresses malicious weight when bad gradients visibly hurt clean public loss, but the broader idea is vulnerable or weak under public-set gaming geometry: adaptive-public proxy cases retained substantial malicious weight and stayed below the oracle.

## Boundaries and scale limits

Evidence is synthetic and local only: no real federated benchmark, no high-dimensional language/image model, no robust aggregation baselines beyond FedAvg and honest-client oracle, and only a proxy adaptive public-set gaming attack.

## Claim scope

On a synthetic 2D binary classification task with a small MLP, public-eval one-step loss scoring plus EMA reputation nearly recovers the honest-client oracle under non-adaptive sign-flip and label-flip gradient attacks across tested public-set sizes and malicious fractions.

## Why it stopped

Synthetic evidence supports a narrow mechanism but the adaptive-public proxy prevents a broad positive claim; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should compare public reputation against robust aggregation baselines and a private or rotating challenge eval set under adaptive attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive-resistant public reputation with rotating challenge eval sets
- Success threshold: Challenge-set reputation beats FedAvg and public-only reputation by at least 2 accuracy points under adaptive-public attacks while staying within 1 point of the honest oracle under sign-flip and label-flip attacks.
- Stop condition: Stop if challenge-set reputation still leaves more than 25% malicious weight or remains more than 3 accuracy points below the honest oracle in 40% adaptive-public scenarios.

## Evidence references

- Artifact root: `<local-path>/projects/public-eval-set-reputation-scoring-for-gradient-aggregation-0095fb81df33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
