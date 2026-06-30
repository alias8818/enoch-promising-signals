# Cascade-Routed Speculative Decoding for GB10 Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-routed-speculative-decoding-for-gb10-local-serving-1f3cdcd76dfb`
Run ID: `cascade-routed-speculative-decoding-for-gb10-local-serving-1f3cdcd76dfb-20260605T064421090534+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/a116fa268fd9

## What looked useful

Cascade routing was fragile: the main proxy sweep lost 0.73% overall versus the best fixed drafter, gained 2.16% only in one more-expensive-drafter regime, and lost 3.83% with modest router overhead/noise. The mechanism appears worth direct testing only when routing is nearly free and fixed-drafter cost is materially high.

## Boundaries and scale limits

Ran vectorized proxy sweeps and a tiny CUDA microbenchmark only. No real target/draft LLM serving loop, no real prompt corpus, and no measured end-to-end decoder latency.

## Claim scope

Synthetic acceptance/cost proxy for cascade-routed speculative decoding on a GB10 host; not an end-to-end LLM serving validation.

## Why it stopped

Proxy evidence is mixed and fragile, so it does not justify a paper-positive claim or a longer GB10 serving run in this deployment.

## Recommended next action

Stop this run as a no-paper useful signal; next concrete action is a bounded direct GB10 serving harness with real target/draft models and a >=5% median tokens/s gain threshold over the best fixed drafter.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GB10 serving test for cascade-routed speculative decoding
- Success threshold: At least 5% median tokens/s improvement over the best fixed-drafter baseline with no p95 latency regression and no material memory-pressure failure on GB10.
- Stop condition: Stop if cascade routing fails to beat the best fixed drafter by 5% median tokens/s, if router overhead exceeds the gain, or if GB10 memory/latency telemetry makes the approach operationally worse.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-routed-speculative-decoding-for-gb10-local-serving-1f3cdcd76dfb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
