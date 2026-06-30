# N-gram speculative decoding for tiny LLMs with exact draft verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-decoding-for-tiny-llms-with-exact-draft-verification-e1ba28b240f2`
Run ID: `n-gram-speculative-decoding-for-tiny-llms-with-exact-draft-verification-e1ba28b240f2-20260521T221318485798+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1d33469bb5d9

## What looked useful

Exact verification is straightforward and reliable; n-gram drafting can save roughly 12.5% of target calls in this setting, but acceptance is low and longer drafts mostly add failed draft attempts.

## Boundaries and scale limits

One tiny real LM, one corpus, 16 prompts, 48 generated tokens per prompt, greedy decoding only, and a simple research harness without production KV-cache serving optimization.

## Claim scope

On a bounded greedy-decoding test with distilgpt2 over WikiText-2 validation prompts, an n-gram corpus drafter with exact target verification preserved bit-identical greedy output and reduced target forward calls modestly, with the best ablation averaging about 1.14 emitted tokens per target call.

## Why it stopped

No-paper closure: direct small-scale evidence supports exactness and a modest call-reduction mechanism, but the result is not broad or strong enough for publication-grade validation.

## Recommended next action

Run a bounded optimized-KV follow-up only if the goal is a systems result; otherwise stop because the current unoptimized local evidence is useful but not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized KV-cache n-gram speculative decoding latency test
- Success threshold: Across at least three bounded model/corpus conditions, exact-match failures remain zero and p50 end-to-end decode latency improves by at least 10% with no p90 regression over 5%.
- Stop condition: Stop if exact-match failures occur, if optimized latency gain is under 5% in two representative conditions, or if accepted-token rates remain too low to reduce target calls beyond 1.1 emitted tokens per call.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-tiny-llms-with-exact-draft-verification-e1ba28b240f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
