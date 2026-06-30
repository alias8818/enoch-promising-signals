# Held-out GPT-2 suffix n-gram speculative decoding benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-gpt-2-suffix-n-gram-speculative-decoding-benchmar-48a02c3fe0`
Run ID: `held-out-gpt-2-suffix-n-gram-speculative-decoding-benchmar-48a02c3fe0-20260609T065255334197+0000`

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

- Parent run decision: Speculative Suffix: N-Gram Draft for GPT-2 Decoding: enoch://control-plane/projects/speculative-suffix-n-gram-draft-for-gpt-2-decoding-d7cc67e01b74/runs/speculative-suffix-n-gram-draft-for-gpt-2-decoding-d7cc67e01b74-20260609T031634307240+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/480fb0c46c7f

## What looked useful

Float32 exact-output runs reduced GPT-2 target calls by 18.9% for n=2 and 13.6% for n=3; n=4 was just below threshold at 10.0% rounded but 9.98% exact. The mechanism depends more on suffix coverage than high proposal acceptance.

## Boundaries and scale limits

24 validation prompts, 48 generated tokens per prompt, GPT-2 only, WikiText-2 only, 500k-token draft table, unoptimized Python loop, no KV-cache serving implementation, and fp16/auto verification failed exactness.

## Claim scope

On a controlled small GPT-2/WikiText-2 greedy decoding benchmark, a held-out suffix n-gram drafter with n=2 or n=3 reduced target-model calls by at least 10% while preserving exact output when verification used float32.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but not publication-grade breadth, robustness, or serving-quality evidence.

## Recommended next action

Run a cache-aware, precision-safe medium confirmation on a larger held-out prompt set before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium cache-aware GPT-2 suffix n-gram speculative decoding confirmation
- Success threshold: exact_match_rate == 1.0 and either target_call_reduction >= 0.10 or end_to_end_latency_speedup >= 1.10 for n=2 or n=3 on the larger held-out benchmark
- Stop condition: Stop if exactness fails under precision-safe verification, if both n=2 and n=3 fall below 10% target-call reduction, or if cache-aware wall-clock is slower despite call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-gpt-2-suffix-n-gram-speculative-decoding-benchmar-48a02c3fe0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
