# Tiny Agent Evidence Ledger with Rollback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-with-rollback-f5c19585376b`
Run ID: `tiny-agent-evidence-ledger-with-rollback-f5c19585376b-20260527T225836456869+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1649e0e8edf2

## What looked useful

Corrected contradiction-rate sweep showed rollback accuracy stayed at 1.0 with zero stale active claims, while no-rollback accuracy fell from 1.0 at contradiction rate 0.0 to 0.315873 at rate 0.5 and retained about 1603 stale active claims per trial. Runtime overhead for the naive rollback scan was about 13x to 16x but absolute rollback runtime remained about 0.03 to 0.04 seconds per 1000-event trial.

## Boundaries and scale limits

Tested only on synthetic CPU-only streams up to 100 trials, 200 entities, and 1000 events per trial. No real LLM agent traces, persistent database backend, concurrent writers, stronger recompute baseline, or production durability testing were evaluated.

## Claim scope

In a deterministic synthetic evidence stream where events explicitly invalidate prior evidence and derived task claims depend on those evidence ids, rollback of dependent claims prevents stale final beliefs and preserves final task accuracy better than an append-only no-rollback ledger.

## Why it stopped

Synthetic evidence supports the mechanism but does not provide direct real-agent or production-ledger validation, so this is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is to replay real or realistic agent traces against rollback, append-only, and latest-valid-recompute baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Realistic Agent Traces Through Rollback and Recompute Ledgers
- Success threshold: Rollback reduces stale action rate by at least 50% versus append-only and is within 2 percentage points of latest-valid-recompute final accuracy while using less total recomputation time.
- Stop condition: Stop if rollback does not beat append-only stale action rate by at least 20% on the trace corpus or if the recompute baseline is simpler and no slower at the tested scale.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-with-rollback-f5c19585376b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
