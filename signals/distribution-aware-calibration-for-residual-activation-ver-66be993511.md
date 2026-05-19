# Distribution-aware calibration for residual activation verifier correction

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `distribution-aware-calibration-for-residual-activation-ver-66be993511`
Run ID: `distribution-aware-calibration-for-residual-activation-ver-66be993511-20260517T185043480120+0000`

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

- Internal Enoch project: Distribution-aware calibration for residual activation verifier correction: internal_generated:distribution-aware-calibration-for-residual-activation-ver-66be993511

## What looked useful

Residual activation clusters carry calibration-relevant signal beyond a raw correctness verifier and a shuffled-cluster control, especially for Brier/NLL, but the effect is metric- and shift-dependent and not sufficient for paper readiness.

## Boundaries and scale limits

Validated only on sklearn digits with a residual MLP and synthetic image corruptions; not validated on transformer residual streams, LLM answer verifiers, large models, or natural language distribution shifts.

## Claim scope

On a small real digits benchmark with a residual MLP correctness verifier, residual-activation distribution-aware calibration improves Brier score and NLL versus raw verifier, Platt scaling, and shuffled-cluster controls, but it does not beat global isotonic calibration on ECE.

## Why it stopped

Mixed bounded evidence: useful Brier/NLL signal from distribution-aware residual calibration, but global isotonic wins the main ECE metric and the benchmark is a small proxy rather than paper-readiness replication.

## Recommended next action

Stop this depth-4 follow-up lineage; only revisit as a separate direct transformer residual-stream verifier calibration project with ECE, Brier, and NLL pre-registered against isotonic and Platt baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/distribution-aware-calibration-for-residual-activation-ver-66be993511`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
