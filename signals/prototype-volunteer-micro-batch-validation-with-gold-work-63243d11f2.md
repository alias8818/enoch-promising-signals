# Prototype Volunteer Micro-Batch Validation with Gold Work and Randomized Assignment

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prototype-volunteer-micro-batch-validation-with-gold-work-63243d11f2`
Run ID: `prototype-volunteer-micro-batch-validation-with-gold-work-63243d11f2-20260524T061141332117+0000`

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

- Parent run decision: Redundant Cross-Validation of Micro-Batches for CPU Volunteers: enoch://control-plane/projects/redundant-cross-validation-of-micro-batches-for-cpu-volunteers-49918802d154/runs/redundant-cross-validation-of-micro-batches-for-cpu-volunteers-49918802d154-20260524T055844955537+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27bbaca74165

## What looked useful

Gold-informed weighting improved aggregate accuracy consistently but did not meet the predeclared base-population threshold: +1.02 pp lift over majority, 0.8585 bad-worker recall, 0.4694 bad-worker precision, 0.0226 false-good rejection, and 0.9995 filtered vote coverage. Balanced assignment improved gold exposure fairness but still failed precision and lift thresholds. Under 30% spammer/adversary stress, lift rose to +6.62 pp, but precision remained just below threshold at 0.7688.

## Boundaries and scale limits

No real volunteers, no multi-class or ambiguous tasks, no UI/retention effects, no collusion, and no long-running deployment. Base run used 80 simulated volunteers, 600 target items, 160 gold items, 5 votes per target, and 500 Monte Carlo scenarios.

## Claim scope

Controlled simulation of binary volunteer micro-batch validation with randomized assignment, embedded gold work, heterogeneous known worker accuracies, and aggregate majority/gold-weighted/gold-filtered labeling.

## Why it stopped

Tier 1 controlled direct test failed the stated threshold, especially bad-worker precision and base-population accuracy lift, while still showing conditional mechanism value.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate an adaptive two-stage gold audit or probabilistic worker model that separates borderline noisy workers from spammers before filtering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Gold Audit for Volunteer Micro-Batch Validation
- Success threshold: At 10% spammer/adversary contamination, achieve at least +2 pp aggregate accuracy lift over majority, bad-worker precision and recall both at least 0.80, false-good rejection at most 0.05, filtered vote coverage at least 0.95, and total gold assignments no more than 1.5x the fixed-filter baseline.
- Stop condition: Stop if adaptive allocation cannot reach both 0.80 precision and 0.80 recall in the 10% contamination setting after using up to 1.5x gold budget, or if accuracy lift remains below +2 pp.

## Evidence references

- Artifact root: `<local-path>/projects/prototype-volunteer-micro-batch-validation-with-gold-work-63243d11f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
