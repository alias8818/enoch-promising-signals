# Direct KV Eviction Generation Test for Draft-Scored Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-kv-eviction-generation-test-for-draft-scored-cascad-429543f9ee`
Run ID: `direct-kv-eviction-generation-test-for-draft-scored-cascad-429543f9ee-20260515T050547330746+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7250694f55c4

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct KV slicing on synthetic fact recall supports draft-scored eviction, but this is controlled Tier 1 evidence rather than publication-grade validation.

## Recommended next action

Stop this run as a Tier 1 mechanism-positive but paper-negative result; next run should test natural long-context tasks with serving-style KV eviction and matched recency/H2O-style baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Long-Context Draft-Scored KV Eviction Benchmark
- Success threshold: Draft-scored eviction must beat the best non-oracle baseline by at least 10% relative quality-loss reduction at the same KV budget on two natural task families, with at least 40% KV-token reduction and less than 15% end-to-end latency overhead.
- Stop condition: Stop if draft-scored eviction fails to beat recency/H2O-style baselines on either natural task family, if quality loss exceeds 5 percentage points versus full cache at 40% KV reduction, or if scoring overhead exceeds 15% latency without a clear batching path.

## Evidence references

- Artifact root: `<local-path>/projects/direct-kv-eviction-generation-test-for-draft-scored-cascad-429543f9ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
