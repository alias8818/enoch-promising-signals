# Confidence-gated CPU cascade for local LLM serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-gated-cpu-cascade-for-local-llm-serving-e5e7ab110102`
Run ID: `confidence-gated-cpu-cascade-for-local-llm-serving-e5e7ab110102-20260611T103459274259+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7c9d6f5d0952

## What looked useful

Raw-request cascade threshold 0.60 escalated 0.95% of 67,040 repeated test requests, reduced mean latency from 0.605 ms to 0.0689 ms, and stayed within the predeclared 0.5 percentage-point accuracy tolerance versus large-only, but F1 fell by 1.73 points. Threshold 0.85 matched large-only accuracy/F1 on this split while escalating 8.47% and reducing latency by 78.9%.

## Boundaries and scale limits

Not an LLM decode benchmark. No autoregressive generation, batching, KV cache, quantized local LLM, prompt-answer benchmark, or real LLM confidence calibration was tested. Absolute latency and escalation rates should not be generalized to 7B-class local serving.

## Claim scope

On a CPU text-classification proxy using UCI SMS Spam, a confidence-gated cascade from a cheap hashed unigram classifier to a larger hashed word/character n-gram classifier reduced raw-request latency while preserving large-proxy accuracy at suitable thresholds.

## Why it stopped

Proxy evidence supports the mechanism but is not direct local LLM serving evidence, so it is insufficient for a paper-ready positive claim.

## Recommended next action

Stop this run as a no-paper useful signal; next run should perform the same threshold sweep on real local CPU LLMs with measured decode latency and judged answer quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM confidence-gated cascade benchmark
- Success threshold: At least one threshold achieves >=50% fewer large-model calls, >=25% lower mean latency than large-only, and <=1 percentage-point quality loss on the bounded prompt benchmark.
- Stop condition: Stop negative if no threshold reduces mean latency by at least 15% while staying within 2 quality points of large-only, or if confidence is uncorrelated with correctness/disagreement.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cpu-cascade-for-local-llm-serving-e5e7ab110102`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
