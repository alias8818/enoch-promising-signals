# Compute-normalized async volunteer accumulation on a small language model or distributed emulator

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compute-normalized-async-volunteer-accumulation-on-a-small-3345bff964`
Run ID: `compute-normalized-async-volunteer-accumulation-on-a-small-3345bff964-20260608T102756206348+0000`

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

- Parent run decision: Async Volunteer Gradient Accumulation: enoch://control-plane/projects/async-volunteer-gradient-accumulation-7cda75dda157/runs/async-volunteer-gradient-accumulation-7cda75dda157-20260608T045400753476+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de208cd5fa47

## What looked useful

Compute-normalized accumulation had mean relative gradient L2 error 0.0000 versus 0.6683 for naive equal-worker averaging and mean final validation loss 2.5738 versus 2.6870 across 3 seeds, satisfying the Tier 1 mechanism and training-sanity thresholds.

## Boundaries and scale limits

No real distributed networking, no stale model versions, no worker churn or adversarial clients, synthetic corpus only, tiny model only, 180 updates per condition/seed, and no GPT-2-small-class or natural-text benchmark validation.

## Claim scope

In a single-process GB10 small-Transformer language-model emulator with 8 heterogeneous volunteer microbatches per update and same-version gradients, token/compute-normalized accumulation exactly recovers the token-weighted large-batch reference gradient and outperforms naive equal-worker averaging over 3 short seeds.

## Why it stopped

No-paper closure: Tier 1 mechanism support was achieved, but same-version synthetic-emulator evidence is insufficient for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with stale model versions and latency-distributed arrivals, using the same token-weighted reference and validation-loss thresholds before considering larger natural-text experiments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stale-latency async volunteer accumulation on a small language model
- Success threshold: Across at least 3 seeds, compute-normalized relative gradient error is <=0.5x naive equal-worker error under staleness and final validation loss is no more than 0.05 worse than naive; stop early if normalized accumulation is consistently worse on both metrics.
- Stop condition: Stop after 3 seeds of the stale-latency emulator or earlier if compute-normalized accumulation exceeds naive relative gradient error and final validation loss by the stated margins in at least 2 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/compute-normalized-async-volunteer-accumulation-on-a-small-3345bff964`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
