# Speculative decoding with tiny draft model for 2x inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-decoding-with-tiny-draft-model-for-2x-inference-b16e8eea4377`
Run ID: `speculative-decoding-with-tiny-draft-model-for-2x-inference-b16e8eea4377-20260605T084601072234+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/bdff207184ae

## What looked useful

A very tiny draft (`sshleifer/tiny-gpt2`) delivered 0.286x baseline throughput and no target-forward reduction; stronger controls reduced target forwards but still ran at only about 0.5x baseline, showing overhead dominated at GPT-2 scale.

## Boundaries and scale limits

This does not evaluate custom exact speculative decoding kernels, batched production serving, tuned draft training, or 7B+ target models where target compute may dominate more strongly.

## Claim scope

On the local GB10 worker using Transformers 4.57.6 assisted generation, GPT-2 target-only greedy decoding was faster than assisted generation with a tiny GPT-2 draft across 8 fixed prompts and 512 generated tokens.

## Why it stopped

Proxy-scale/local early falsification: the tiny-draft configuration failed the 2x throughput threshold and did not preserve exact target-only greedy continuations under the tested Transformers assisted-generation path.

## Recommended next action

Stop this run as an early bounded falsification; a next run should only proceed if it uses exact-output speculative decoding on a larger locally runnable target with output-equivalence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-output speculative decoding on a larger local target
- Success threshold: At least 1.5x tokens/sec improvement with exact output match on a larger target; stop early if speedup remains below 1.0x after one target/draft pair and one tuning pass.
- Stop condition: Stop if exact-output equivalence cannot be achieved locally or if a larger target still fails to beat target-only throughput after bounded tuning.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-tiny-draft-model-for-2x-inference-b16e8eea4377`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
