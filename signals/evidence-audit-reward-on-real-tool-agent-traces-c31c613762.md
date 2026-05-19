# Evidence-audit reward on real tool-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-audit-reward-on-real-tool-agent-traces-c31c613762`
Run ID: `evidence-audit-reward-on-real-tool-agent-traces-c31c613762-20260513T202343061358+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71ba98c819f4

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 controlled direct trace test met its mechanism threshold, but the claims were templated and the reward was a hand-written verifier, so this is not publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on free-form model-generated summaries from real tool-agent traces with independent support labels; stop this run because the current templated verifier result is mechanism support, not paper-ready evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Free-form evidence-audit reward on real tool-agent summaries
- Success threshold: Evidence-audit reward AUC >= 0.80 and best accuracy at least 10 percentage points above the strongest baseline on held-out free-form summaries, with no severe calibration collapse on unsupported claims.
- Stop condition: Stop if evidence-audit AUC is below 0.70 or fails to beat the strongest baseline by at least 5 percentage points on the held-out labeled set.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-audit-reward-on-real-tool-agent-traces-c31c613762`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
