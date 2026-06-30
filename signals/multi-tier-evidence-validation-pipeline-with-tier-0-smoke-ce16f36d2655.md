# Multi-Tier Evidence Validation Pipeline with Tier-0 Smoke

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-tier-evidence-validation-pipeline-with-tier-0-smoke-ce16f36d2655`
Run ID: `multi-tier-evidence-validation-pipeline-with-tier-0-smoke-ce16f36d2655-20260628T163223439774+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/deb7aa3d971c

## What looked useful

Tier-0 smoke checks improved invalid rejection from 4/6 to 6/6 and avoided two Tier-1 exceptions compared with a Tier-1-only baseline, while keeping supported acceptance and unsupported rejection at 2/2 each on valid cases.

## Boundaries and scale limits

Synthetic fixture only; no real research corpus, model-generated evidence packets, noisy operator traces, production validator integration, or long-run human-review workload measurement.

## Claim scope

On a 10-case deterministic synthetic fixture, a Tier-0 smoke gate before Tier-1 metric validation rejected all malformed or overclaimed evidence cases, avoided downstream Tier-1 exceptions, and preserved expected decisions for valid supported and unsupported cases.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct/full validation and should not be presented as paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next run should validate the same tiered pipeline on a larger real or semi-real evidence corpus with a production-like baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tier-0 evidence smoke validation on noisy real-style research packets
- Success threshold: Tier-0 plus Tier-1 improves invalid rejection by at least 20 percentage points or reduces downstream exceptions by at least 80% versus baseline, while valid false rejection remains at or below 5%.
- Stop condition: Stop if Tier-0 false rejects more than 10% of valid evidence or fails to improve invalid rejection/downstream error metrics over the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/multi-tier-evidence-validation-pipeline-with-tier-0-smoke-ce16f36d2655`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
