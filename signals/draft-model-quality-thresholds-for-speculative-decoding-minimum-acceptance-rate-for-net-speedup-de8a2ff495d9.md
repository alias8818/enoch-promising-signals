# Draft-Model Quality Thresholds for Speculative Decoding: Minimum Acceptance Rate for Net Speedup

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `draft-model-quality-thresholds-for-speculative-decoding-minimum-acceptance-rate-for-net-speedup-de8a2ff495d9`
Run ID: `draft-model-quality-thresholds-for-speculative-decoding-minimum-acceptance-rate-for-net-speedup-de8a2ff495d9-20260603T181343757940+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a66a38a90554

## What looked useful

A draft model can have surprisingly low iid acceptance and still speed up decoding when draft cost is very low, but thresholds rise with draft cost, verification overhead, and larger gamma. Mean acceptance alone is insufficient when acceptance varies by position because expected emitted tokens depend on prefix survival products.

## Boundaries and scale limits

No real draft/target model logits, GPU serving traces, batching behavior, KV-cache effects, or production kernel timings were measured. Results should be used as a screening model, not as full serving validation.

## Claim scope

For the normalized speculative-decoding latency model with iid or specified per-position acceptance probabilities, the break-even acceptance threshold is determined by expected emitted prefix length exceeding beta plus gamma times draft cost plus overhead. The run provides exact thresholds and Monte Carlo validation for synthetic/proxy acceptance settings.

## Why it stopped

Proxy analytic and Monte Carlo evidence supports the threshold mechanism, but this is not full validation because no real serving implementation or model-pair measurements were run.

## Recommended next action

Stop this worker run as no-paper useful-signal evidence; next bounded action is to collect real accepted-prefix traces and latency for a small open draft/target model pair and compare against the analytic thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate speculative-decoding threshold predictions on a small real draft/target model pair
- Success threshold: For at least two gamma settings, predicted speedup from measured prefix-survival statistics is within 15% relative error of observed speculative speedup and distinguishes a speedup case from a no-speedup case.
- Stop condition: Stop if a small real stack cannot produce reliable accepted-prefix traces and latency within a bounded local run, or if measured overhead dominates enough that all tested configurations are below 1.0x speedup.

## Evidence references

- Artifact root: `<local-path>/projects/draft-model-quality-thresholds-for-speculative-decoding-minimum-acceptance-rate-for-net-speedup-`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
