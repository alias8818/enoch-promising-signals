# Tiny Draft Plus N-Gram Verification for Local Speedup

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-draft-plus-n-gram-verification-for-local-speedup-5befaa6c7bff`
Run ID: `tiny-draft-plus-n-gram-verification-for-local-speedup-5befaa6c7bff-20260607T163645200313+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/94ace52d2eee

## What looked useful

The mechanism split is clear: the tiny draft was too mismatched for local context n-grams to accept any proposals; a stronger same-family draft could trigger about 69% n-gram acceptance, but with a larger target it degraded exact agreement to 34%, worsened target NLL by about 0.69 nats/token, and still measured slower than target greedy decoding.

## Boundaries and scale limits

This was a bounded local inference probe using distilgpt2, sshleifer/tiny-gpt2, gpt2, WikiText-2 validation prompts, greedy decoding, and a simple non-KV-cache Python implementation. It does not test optimized exact speculative decoding, large production models, sampling, long external n-gram memories, or datacenter serving.

## Claim scope

On GPT-2-family greedy decoding on GB10, a genuinely tiny GPT-2 draft model plus prompt/generated-context n-gram verification did not provide local speedup: n=2/3/4 accepted zero tokens across 4,800 tested generated positions, so the hybrid added draft overhead and ran about 0.62x as fast as target greedy decoding.

## Why it stopped

Proxy/local early falsification rather than full validation: the directly tested tiny-draft plus local context n-gram verifier failed to accept tokens and did not speed decoding; broader optimized or large-scale variants remain untested.

## Recommended next action

Stop this variant as a no-paper bounded negative; only revisit via an optimized KV-cache follow-up that must show >1.1x wall-clock speedup with near-zero target NLL delta and nonzero acceptance from a genuinely cheap draft model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache exactness check for context n-gram assisted drafting
- Success threshold: Mean wall-clock speedup greater than 1.1x versus KV-cache target decoding, accepted-token rate greater than 10% for the cheap draft, target NLL delta no more than 0.05 nats/token, and exact agreement not materially worse than the non-ngram draft control.
- Stop condition: Stop if cheap-draft acceptance remains below 5%, if speedup is below 1.0x after KV-cache optimization, or if target NLL delta exceeds 0.1 nats/token at any useful acceptance rate.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-draft-plus-n-gram-verification-for-local-speedup-5befaa6c7bff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
