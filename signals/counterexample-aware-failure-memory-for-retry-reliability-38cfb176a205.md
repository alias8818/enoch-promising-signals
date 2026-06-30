# Counterexample-Aware Failure Memory for Retry Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-aware-failure-memory-for-retry-reliability-38cfb176a205`
Run ID: `counterexample-aware-failure-memory-for-retry-reliability-38cfb176a205-20260622T005353790509+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46b12fc240fc

## What looked useful

Counterexample content was the active mechanism. Main success rates were 0.55% naive retry, 0.70% failure-hash memory, 6.55% with 4 counterexamples, 47.70% with 8 counterexamples, and 100.00% with 12 counterexamples; five-seed replicate means preserved the same ordering.

## Boundaries and scale limits

Proxy-only CPU benchmark: 16-bit affine functions, exact counterexample oracle, realizable hypothesis class, 2,000 tasks per main arm plus five seed replicates. No real LLM, code-repair, theorem-proving, noisy-feedback, or production retry traces were tested.

## Claim scope

In a synthetic affine-Boolean CEGIS retry benchmark, adding concrete oracle counterexamples to retry memory sharply improves exact recovery relative to naive retry or remembering only failed candidate hashes.

## Why it stopped

Proxy mechanism test is complete and positive as a useful signal, but it is not direct/full validation and is not paper-ready.

## Recommended next action

Run a bounded direct-evidence follow-up on real LLM retry traces comparing no memory, failure-summary memory, and concrete counterexample memory under equal context budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample Memory on Real LLM Retry Traces
- Success threshold: Concrete counterexample memory improves final task success by at least 10 percentage points over both baselines with overlapping-task paired significance and no more than 25% added context cost.
- Stop condition: Stop if counterexample memory fails to beat both baselines by at least 5 percentage points on the first 100 tasks or if context cost dominates the observed success gain.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-aware-failure-memory-for-retry-reliability-38cfb176a205`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
