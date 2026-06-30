# N-gram Speculative Decoding on CPU with Exact Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-with-exact-verification-c2f1070643e2`
Run ID: `n-gram-speculative-decoding-on-cpu-with-exact-verification-c2f1070643e2-20260605T000411257177+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/752afe044432

## What looked useful

Exact verification worked in all 80 full-sweep configurations. Repetitive periodic traces reached 31.99x verifier-call reduction, bursty-copy traces reached 2.34x, random traces had no useful reduction, and tiny_shakespeare natural text reached only 1.11x with very low draft acceptance. Aggressive drafts can reduce call count while wasting verifier-token work.

## Boundaries and scale limits

This run used a recorded target-greedy trace rather than an actual transformer verifier. It did not measure CPU LLM tokens/sec, KV-cache behavior, tokenizer effects, sampling-mode acceptance, or large/model-serving workloads.

## Claim scope

On deterministic token traces, history n-gram speculative decoding with exact greedy verification reproduces the target output exactly and reduces verifier calls only when the output has repeated spans; on the tiny_shakespeare natural-text trace it achieved only about 1.09x-1.11x verifier-call reduction and was often slower under nonzero per-token verification cost models.

## Why it stopped

Bounded trace/oracle evidence is mixed and not publication-grade: exactness is supported, but practical speedup on natural text is weak and only proxied by a cost model rather than directly measured on an LLM.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded real CPU transformer benchmark with adaptive draft sizing to test whether measured tokens/sec can exceed greedy decoding by at least 1.2x on natural/code prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer Benchmark for Adaptive N-gram Speculation
- Success threshold: At least 1.2x measured tokens/sec over greedy decoding with exact output equality on both natural-text and code-like prompt sets, without increasing peak memory by more than 25%.
- Stop condition: Stop if measured speedup is below 1.05x on natural-text prompts or if adaptive control cannot keep rejected verifier-token overhead below the baseline-equivalent cost.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-with-exact-verification-c2f1070643e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
