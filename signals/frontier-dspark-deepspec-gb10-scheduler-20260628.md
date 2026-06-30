# DSpark/DeepSpec GB10 speculative-decoding scheduler experiment

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `57`
Project ID: `frontier-dspark-deepspec-gb10-scheduler-20260628`
Run ID: `frontier-dspark-deepspec-gb10-scheduler-20260628-20260629T074541253044+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `57`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Linear ALI-206 frontier research issue: linear-ALI-206
- DSpark/DeepSpec GB10 speculative-decoding scheduler experiment: https://github.com/deepseek-ai/DeepSpec
- DSpark/DeepSpec GB10 speculative-decoding scheduler experiment: https://raw.githubusercontent.com/deepseek-ai/DeepSpec/refs/heads/main/DSpark_paper.pdf
- Jeremy frontier AI research intake: DSpark, post-training, dataset quality: user-frontier-ai-research-tracks-20260628

## What looked useful

Naive per-request adaptive draft scheduling lost 15.0% to 49.3% versus the best fixed-K baseline because batch max-length costs dominate. Batch-common adaptation avoided the large loss but only matched the tuned fixed baseline, with at most +0.19% in the high-acceptance proxy scenario.

## Boundaries and scale limits

No real LLM serving stack, draft/target model pair, KV cache, prompt traces, or production batching overheads were measured. Results are proxy evidence only and cannot support a paper-positive throughput claim.

## Claim scope

Bounded GB10 proxy experiment: local CUDA matmul-calibrated speculative decoding scheduler simulation comparing fixed draft lengths, naive per-request adaptation, and batch-common adaptation across synthetic acceptance distributions.

## Why it stopped

Proxy early falsification of a broad adaptive scheduler claim: per-request adaptation was clearly harmful and batch-common adaptation did not meaningfully beat best fixed-K. This is not a full validation.

## Recommended next action

Stop this run as no-paper proxy evidence; a bounded follow-up should test batch-aware or bucketed adaptation in a real speculative serving stack and require at least 5% throughput gain over a tuned fixed-K baseline without latency regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model batch-aware speculative scheduler benchmark on GB10
- Success threshold: At least 5% accepted-token throughput improvement over the best tuned fixed-K baseline with no p95 latency regression greater than 2%.
- Stop condition: Stop if batch-aware adaptation fails to exceed best fixed-K by 5% in two representative prompt/acceptance regimes or if scheduler overhead erases the throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/frontier-dspark-deepspec-gb10-scheduler-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
