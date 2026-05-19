# Residual Soft Hidden-State Router for Local LM Specialists

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-soft-hidden-state-router-for-local-lm-specialists-46a55506cc`
Run ID: `residual-soft-hidden-state-router-for-local-lm-specialists-46a55506cc-20260514T171946839661+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa1dbcb12ba5

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 controlled synthetic evidence supports the mechanism but is not direct/full evidence for real local LM specialists or publication readiness.

## Recommended next action

Run a bounded transformer/GPT-2-small-class follow-up with frozen local specialists, parameter-matched dense/adapter baselines, repeated seeds, held-out mixed-domain text, and the same routing diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-scale residual hidden-state router for frozen local LM specialists
- Success threshold: Residual router improves held-out NLL by at least 0.05 versus the strongest parameter-matched baseline in at least 3 seeds and routes to the correct/proxy domain at least 20 percentage points above chance.
- Stop condition: Stop if the residual router fails to beat the strongest baseline by 0.02 NLL after two seeds, or if route-domain accuracy remains within 10 percentage points of chance despite lower training loss.

## Evidence references

- Artifact root: `<local-path>/projects/residual-soft-hidden-state-router-for-local-lm-specialists-46a55506cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
