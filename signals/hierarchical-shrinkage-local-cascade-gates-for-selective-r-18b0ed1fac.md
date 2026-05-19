# Hierarchical shrinkage local cascade gates for selective-risk control

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `hierarchical-shrinkage-local-cascade-gates-for-selective-r-18b0ed1fac`
Run ID: `hierarchical-shrinkage-local-cascade-gates-for-selective-r-18b0ed1fac-20260518T165005773755+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Hierarchical shrinkage local cascade gates for selective-risk control: internal_generated:hierarchical-shrinkage-local-cascade-gates-for-selective-r-18b0ed1fac

## What looked useful

Shrinkage/cascade gates suppress local risk violations, but mainly by abstaining much more aggressively than a global finite-sample baseline. At alpha=0.10, cascade_shrink had 0 violation rate and lower mean worst-leaf risk (0.0318) but only 0.3649 mean coverage versus global_ucb's 0.9690 mean coverage. At alpha=0.03, shrinkage variants accepted zero examples in all 180 runs.

## Boundaries and scale limits

No large neural model, LLM cascade, production routing, learned semantic hierarchy, or multi-node/datacenter-scale validation was run. The tested evidence is bounded local selective-classification validation, not broad paper-ready proof.

## Claim scope

On three sklearn classification datasets, two standard classifier families, 30 fixed seeds, unsupervised local group hierarchies, and exact-binomial calibration baselines, hierarchical shrinkage cascade gates reduce realized selective and local risk but are not coverage-efficient and fail operationally at a stricter alpha=0.03 target.

## Why it stopped

Bounded direct selective-risk validation found that the hierarchical shrinkage cascade reduces risk by excessive abstention, is dominated by the global exact-binomial baseline on coverage at alpha=0.10, and collapses to zero coverage at alpha=0.03.

## Recommended next action

Stop this follow-up chain: the depth is 4 and the bounded direct validation produced a no-paper useful negative signal rather than a coverage-efficient risk-control method.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-shrinkage-local-cascade-gates-for-selective-r-18b0ed1fac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
