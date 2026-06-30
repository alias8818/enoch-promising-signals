# OperatorDoctrine: Trace-Derived Memory That Learns Reusable Rules

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operatordoctrine-trace-derived-memory-that-learns-reusable-rules-04450f56e2bd`
Run ID: `operatordoctrine-trace-derived-memory-that-learns-reusable-rules-04450f56e2bd-20260621T071916714165+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/37227f7a15f9

## What looked useful

Trace-derived reusable rules are a plausible mechanism when traces expose reliable state/action structure, but naive clause induction is brittle when both trace labels and observations are noisy.

## Boundaries and scale limits

12 synthetic rule families, 50 random seeds per condition, 4 training traces per family, 10 held-out traces per family; no real operator traces, no LLM extraction, no real shell execution, and no long-horizon memory accumulation.

## Claim scope

In a synthetic operator benchmark with structured trace features and reliable success labels, a simple trace-derived clause learner generalized better than no memory and nearest-trace episodic memory; robustness failed under combined success-label noise and missing observation features.

## Why it stopped

No-paper useful signal: synthetic evidence supports the mechanism in clean settings but combined-noise stress reverses the result, so this is not a publication-grade positive validation.

## Recommended next action

Run a bounded follow-up on semi-real agent traces with a noise-aware rule induction step and require improvement over episodic retrieval under combined label and feature noise.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noise-Aware Doctrine Induction on Semi-Real Operator Traces
- Success threshold: Doctrine must beat the strongest retrieval or summary baseline by at least 10 percentage points mean accuracy across 30 or more seeds/tasks while staying above 80% absolute accuracy under combined noise.
- Stop condition: Stop if doctrine fails to beat episodic retrieval under combined noise or if feature extraction errors exceed the level where learned clauses remain interpretable.

## Evidence references

- Artifact root: `<local-path>/projects/operatordoctrine-trace-derived-memory-that-learns-reusable-rules-04450f56e2bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
