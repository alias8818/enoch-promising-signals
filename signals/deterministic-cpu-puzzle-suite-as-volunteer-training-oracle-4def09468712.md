# Deterministic CPU Puzzle Suite as Volunteer Training Oracle

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-cpu-puzzle-suite-as-volunteer-training-oracle-4def09468712`
Run ID: `deterministic-cpu-puzzle-suite-as-volunteer-training-oracle-4def09468712-20260611T070129385804+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e509d1003508

## What looked useful

The prototype supports the mechanism that public-seed deterministic CPU puzzles can provide reproducible task generation, answer-key regeneration, cheap validation, and basic difficulty calibration; earlier failed runs also showed that satisfiability and calibration checks are necessary for oracle construction.

## Boundaries and scale limits

Evidence is local and synthetic: 300 cases, one machine, one Python runtime, three puzzle families, no human volunteer study, no cross-platform replay, no large puzzle-bank robustness run, and no comparison against existing training or benchmark systems.

## Claim scope

A dependency-free local Python prototype generated, solved, verified, and replayed 300 deterministic CPU puzzle cases across subset-sum, maze, and N-Queens families with a usable five-level timing ladder on this worker.

## Why it stopped

Local prototype evidence supports the mechanism but is insufficient for a paper because it lacks human-training outcomes, cross-platform reproducibility, large-bank robustness, and baseline comparisons.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded action is a multi-seed, cross-machine robustness replay before any volunteer-training claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-seed and cross-machine robustness for deterministic CPU puzzle oracle
- Success threshold: 100% valid cases, exact digest match across environments, and Spearman >= 0.8 with all 4/4 adjacent median solve-time transitions nondecreasing for each family or predeclared calibrated variant.
- Stop condition: Stop if any family has repeated solvability failures, cross-environment digest mismatch, or difficulty calibration below threshold after one targeted generator correction.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-cpu-puzzle-suite-as-volunteer-training-oracle-4def09468712`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
