# Difficulty-Classifier Cascade Router

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `difficulty-classifier-cascade-router-865dc8269cdc`
Run ID: `difficulty-classifier-cascade-router-865dc8269cdc-20260611T210851810855+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3da898a765a2

## What looked useful

Learned difficulty routing had higher average precision for helpful escalations than confidence scoring (0.2624 vs 0.2279 mean over five seeds) and improved accuracy over confidence by 0.85, 0.62, and 0.36 percentage points at 10%, 20%, and 30% routed, but was 0.25 percentage points worse at 50% routed.

## Boundaries and scale limits

Single benchmark family, classical text classifiers, five random seeds, CPU-only local run; does not validate LLM cascade routing, production latency/cost, generative quality, distribution shift, or larger model families.

## Claim scope

On 20 Newsgroups with a Naive Bayes cheap classifier, LinearSVC strong classifier, and logistic difficulty router, learned routing improves low-budget escalation accuracy over random routing and slightly over cheap-confidence routing at 10-30% routed, but not at 50% routed or across the full routing curve.

## Why it stopped

No-paper useful signal: the local evidence supports a small low-budget routing mechanism, but the learned router does not robustly dominate simple confidence thresholding across routing budgets.

## Recommended next action

Run a bounded multi-dataset router ablation with calibrated confidence baselines and at least three cheap/strong model pairs before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-dataset calibrated difficulty-router ablation
- Success threshold: Mean learned-router accuracy is at least 1 percentage point above calibrated confidence routing at 10-30% routed on at least two thirds of dataset/model-pair combinations, with no more than 0.2 percentage point loss at 50% routed.
- Stop condition: Stop if calibrated confidence matches or beats the learned router at 10-30% routed on most combinations, or if learned-router gains disappear under calibration.

## Evidence references

- Artifact root: `<local-path>/projects/difficulty-classifier-cascade-router-865dc8269cdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
