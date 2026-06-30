# GDI Byzantine Detection on CPU Volunteer Federation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gdi-byzantine-detection-on-cpu-volunteer-federation-febd18d546ab`
Run ID: `gdi-byzantine-detection-on-cpu-volunteer-federation-febd18d546ab-20260611T064311976352+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e509d1003508

## What looked useful

GDI achieved mean AUROC 0.9996 and F1@k 0.9900 for sign-flip attacks across 10-40% Byzantine clients, but AUROC/F1 were 0.0 for same-direction high-norm attacks and collapsed to 0.0 for stealth-opposite attacks at 20-40% Byzantine clients. GDI-filtered mean improved sign-flip accuracy versus plain mean (-0.0732 vs -0.5112 delta from clean), but was worse than plain mean for stealth-opposite (-0.1711 vs -0.0111).

## Boundaries and scale limits

Synthetic binary classification only; 5 seeds; 50 clients; 80 rounds; known attacker count for filtering; no real volunteer churn, secure aggregation, sybils, stale gradients, large models, real datasets, or adaptive adversaries.

## Claim scope

In a bounded NumPy CPU simulation with 50 non-IID clients training synthetic logistic regression, pure gradient direction integrity detects sign-flip Byzantine updates very well and offers limited value for random-direction attacks, but it is not a reliable general Byzantine detector.

## Why it stopped

Bounded synthetic evidence is sufficient to reject pure direction-only GDI as a general Byzantine detector; the result is not a full validation and not publication-grade.

## Recommended next action

Stop this run as a no-paper useful signal; next test should evaluate a bounded hybrid direction-plus-norm detector with a consensus reliability gate on the same synthetic suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid GDI plus norm reliability gate for CPU Byzantine detection
- Success threshold: Hybrid detector meets the sign_flip preservation threshold and avoids more than 0.02 accuracy harm versus plain mean on high-fraction stealth_opposite while improving or matching pure GDI on random_direction.
- Stop condition: Stop if the hybrid detector still has AUROC below 0.75 on random_direction or causes more than 0.02 additional accuracy loss versus plain mean on stealth_opposite at 20-40% Byzantine clients.

## Evidence references

- Artifact root: `<local-path>/projects/gdi-byzantine-detection-on-cpu-volunteer-federation-febd18d546ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
