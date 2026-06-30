# CPU cascade router on real text serving workload

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-cascade-router-on-real-text-serving-workload-7f8b73b92e`
Run ID: `cpu-cascade-router-on-real-text-serving-workload-7f8b73b92e-20260524T001742828370+0000`

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

- Parent run decision: CPU Cascade Router for Latency-Quality Tradeoff: enoch://control-plane/projects/cpu-cascade-router-for-latency-quality-tradeoff-07bfb5e4fcd1/runs/cpu-cascade-router-for-latency-quality-tradeoff-07bfb5e4fcd1-20260523T233503370717+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12311a2acc01

## What looked useful

A predeclared Tier 1 threshold was met: threshold 0.70 achieved 0.871667 cascade accuracy versus 0.878333 always-large accuracy, 0.99241 accuracy retention, 0.105833 large-call fraction, and 2.26254x mean latency speedup on 1,200 real text requests.

## Boundaries and scale limits

This did not test LLM generation, production traffic, concurrent serving, queueing, batching, human quality labels, GPU/CPU interaction, or datacenter-scale cost. It is a small controlled direct test of CPU text cascade mechanics, not publication-grade validation.

## Claim scope

On a 4-class real-text 20 Newsgroups CPU classification serving benchmark with 2,200 training examples and 1,200 single-request test examples, a cheap confidence router preserved 99.24% of the stronger CPU model's accuracy while calling the stronger model for 10.58% of requests and improving mean latency by 2.26x.

## Why it stopped

No-paper closure: the mechanism is supported in a small real-text CPU classification benchmark, but evidence is not direct enough for deployed LLM text serving or publication readiness.

## Recommended next action

Run a bounded deepen test on a local LLM-style QA or generation workload with quality labels, always-small/always-large/cascade controls, and concurrent serving latency before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU cascade router on local LLM-style labeled text workload
- Success threshold: At least 99% quality retention versus always-large, no more than 70% large-model calls, and at least 1.10x mean or p95 latency improvement under the measured serving condition.
- Stop condition: Stop if no threshold reaches 99% quality retention without routing more than 70% of requests to the large model, or if router overhead removes the latency benefit under concurrent serving.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-router-on-real-text-serving-workload-7f8b73b92e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
