# Input-Adaptive Draft Model Selection for Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `input-adaptive-draft-model-selection-for-speculative-decoding-8d9e02b5af94`
Run ID: `input-adaptive-draft-model-selection-for-speculative-decoding-8d9e02b5af94-20260524T035543412597+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d46c994fc477

## What looked useful

In this tested draft pool, prompt-level agreement variation did not create useful adaptive selection. The trained router underperformed the best fixed draft by 1.21%, the draft-only oracle had 0.00% gain over always using distilgpt2, and a practical oracle including no-draft chose target-only on 23 of 24 held-out prompts.

## Boundaries and scale limits

Not a production speculative decoder; no exact rejection sampling, no end-to-end serving throughput, no larger target models, no broad public prompt benchmark, and no robustness sweep over block size, temperature, batching, or draft pools.

## Claim scope

Bounded CUDA probe with GPT-2 target, distilgpt2 and sshleifer/tiny-gpt2 drafts, 48 mixed-domain prompts, greedy agreement acceptance proxy, measured model latencies, and a fixed speculative latency model.

## Why it stopped

Early bounded falsification for this candidate draft pool: the cheap tiny draft had zero agreement, distilgpt2 was the only useful draft but remained slower than target-only in the measured-cost model, and adaptive selection had no meaningful complementary option to exploit.

## Recommended next action

Stop this run as a bounded negative/useful signal; the next concrete test should use an actual speculative decoder and a draft pool with at least two nontrivially aligned drafts plus a no-draft policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Small-Model Speculative Decoder With Complementary Draft Pool
- Success threshold: Adaptive policy achieves at least 5% held-out wall-clock tokens/sec improvement over both best fixed draft and no-draft, with unchanged sampled output distribution under exact speculative acceptance.
- Stop condition: Stop if no candidate draft beats target-only on at least 20% of held-out prompts, or if oracle selection including no-draft is below 3% gain over the best fixed policy.

## Evidence references

- Artifact root: `<local-path>/projects/input-adaptive-draft-model-selection-for-speculative-decoding-8d9e02b5af94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
