# Serving-boundary KV cache binding test for hidden-anchor replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `serving-boundary-kv-cache-binding-test-for-hidden-anchor-r-29b5cab4c0`
Run ID: `serving-boundary-kv-cache-binding-test-for-hidden-anchor-r-29b5cab4c0-20260527T151143648950+0000`

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

- Parent run decision: GPT-2-small KV trace replay for exact anchor bypass: enoch://control-plane/projects/gpt-2-small-kv-trace-replay-for-exact-anchor-bypass-d205253d99/runs/gpt-2-small-kv-trace-replay-for-exact-anchor-bypass-d205253d99-20260526T012812868919+0000
- Parent run decision: 4-Bit KV Quantization with Exact Anchor Bypass: enoch://control-plane/projects/4-bit-kv-quantization-with-exact-anchor-bypass-504fbc022423/runs/4-bit-kv-quantization-with-exact-anchor-bypass-504fbc022423-20260525T230611019329+0000

## What looked useful

Across 216 fixed-seed GPT-2-small trials, misbound hidden-anchor cache reuse raised the anchor token logprob by 5.09 nats on average versus visible-only full recompute, with 210/216 trials above a 1.0-nat threshold. The wrong-anchor control was also beaten in 209/216 trials. Cache/full equivalence checks stayed within 2.29e-4 max logit delta.

## Boundaries and scale limits

Synthetic anchors and templates only; no actual production serving engine, cache-key implementation, concurrency, tenant isolation, eviction pressure, larger instruction-tuned model, or top-1/generation-level leakage validation was tested.

## Claim scope

On local GPT-2-small inference, deliberately reusing a hidden-anchor past_key_values cache across a synthetic serving boundary produces a large next-token logprob replay bias for the hidden anchor, while visible-only full recompute and correctly reset visible-cache baselines agree up to small floating-point differences.

## Why it stopped

Tier 2 local evidence supports the injected cache-binding mechanism, but it does not demonstrate a real serving stack vulnerability or generation-level leakage, so it is not paper-ready.

## Recommended next action

Stop this run as no-paper useful mechanism evidence; the next concrete step is a bounded local serving-engine harness that compares weak versus strong prefix-cache keys under multi-request schedules.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Local serving-engine weak-vs-strong prefix-cache boundary replay test
- Success threshold: Weak-key mode shows at least 1.0 nat mean hidden-anchor logprob lift versus visible-only baseline and at least 0.5 nat versus wrong-anchor control, while strong-key mode keeps mean absolute logprob delta below 0.05 nat and zero cache-hit provenance crossing request boundaries.
- Stop condition: Stop if weak-key mode cannot reproduce a replay lift on the same GPT-2-small schedule, or if strong-key mode still shows cross-boundary cache provenance after key hardening.

## Evidence references

- Artifact root: `<local-path>/projects/serving-boundary-kv-cache-binding-test-for-hidden-anchor-r-29b5cab4c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
