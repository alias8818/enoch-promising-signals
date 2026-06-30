# Confidence-Gated Two-Stage Cascade Serving on a Single gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-gated-two-stage-cascade-serving-on-a-single-gb10-8bf53d110bf0`
Run ID: `confidence-gated-two-stage-cascade-serving-on-a-single-gb10-8bf53d110bf0-20260619T090802092593+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/905ab151f450

## What looked useful

Threshold 0.95 routed 7.57% of examples to stage 2, reached 92.78% accuracy versus 92.43% for stage 2 only, and measured 4.03x speedup. Threshold 0.995 routed 20.53% to stage 2, reached 93.92% accuracy, and measured 2.70x speedup; a repeat reproduced the same accuracy/fallback counts and 2.71x speedup.

## Boundaries and scale limits

Tested only 872 classification examples in batch mode. Did not test generative decoding, KV-cache pressure, concurrent serving, long contexts, traffic drift, calibration robustness, or production latency percentiles.

## Claim scope

On one NVIDIA GB10, for SST-2 validation classification with DistilBERT as stage 1 and RoBERTa-large sentiment as stage 2, a confidence-gated cascade preserved or exceeded the stage-2-only accuracy while improving measured batch inference throughput.

## Why it stopped

The mechanism worked on a bounded classification proxy, but the evidence is not direct enough for a paper claim about general two-stage cascade serving.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate the same gate with two small generative instruction models on GB10 under concurrency and latency-percentile measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 Generative Confidence-Gated Cascade With Latency Percentiles
- Success threshold: At a chosen gate threshold, quality is within 1 percentage point of always-stage-2 or better, p95 latency improves by at least 25%, and fallback rate is below 50% on the bounded prompt set.
- Stop condition: Stop if the cascade cannot keep both models resident, if p95 latency is not improved at any quality-preserving threshold, or if quality drops by more than 1 percentage point whenever latency improves.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-two-stage-cascade-serving-on-a-single-gb10-8bf53d110bf0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
