# Speculative Decoding via Prompt-Lookback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-via-prompt-lookback-b05211646b1e`
Run ID: `speculative-decoding-via-prompt-lookback-b05211646b1e-20260602T124853469694+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7195814c2f2d

## What looked useful

Prompt-only lookback reached 0.9669 token acceptance and 7.735 mean accepted tokens/event on synthetic copy, 0.4254 and 3.403 on Python stdlib, and 0.3632 and 2.903 on system docs; shuffled-prompt controls collapsed to 0.0000 acceptance for stdlib and 0.0045 for docs.

## Boundaries and scale limits

Local exact-token proxy only; no target-model accept/reject path, no tokenizer/model-logit calibration, no CUDA verifier batching, no end-to-end latency measurement, and only local code/docs plus synthetic copy data.

## Claim scope

A deterministic prompt-only n-gram lookback drafter achieves high exact-token proxy acceptance on synthetic copy continuations and meaningful multi-token exact matches on local Python stdlib and system-doc continuations when repeated prompt spans exist.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the copy-structure mechanism but remains an exact-token proxy rather than full speculative-decoding validation.

## Recommended next action

Run a bounded direct small-model speculative decoding benchmark that measures actual target-model acceptance and latency on copy-heavy and low-copy prompt suites.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-model latency test for prompt-lookback speculative decoding
- Success threshold: At least 1.15x end-to-end tokens/second on copy-heavy prompts with no statistically meaningful slowdown on low-copy controls across at least 100 prompts.
- Stop condition: Stop if actual model acceptance is below 0.20 token acceptance or if verifier overhead prevents any speedup on the copy-heavy suite.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-via-prompt-lookback-b05211646b1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
