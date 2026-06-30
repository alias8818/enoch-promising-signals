# Local serving-engine weak-vs-strong prefix-cache boundary replay test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `local-serving-engine-weak-vs-strong-prefix-cache-boundary-d11fcb81a1`
Run ID: `local-serving-engine-weak-vs-strong-prefix-cache-boundary-d11fcb81a1-20260527T172744689563+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: GPT-2-small KV trace replay for exact anchor bypass: enoch://control-plane/projects/gpt-2-small-kv-trace-replay-for-exact-anchor-bypass-d205253d99/runs/gpt-2-small-kv-trace-replay-for-exact-anchor-bypass-d205253d99-20260526T012812868919+0000
- Parent run decision: Serving-boundary KV cache binding test for hidden-anchor replay: enoch://control-plane/projects/serving-boundary-kv-cache-binding-test-for-hidden-anchor-r-29b5cab4c0/runs/serving-boundary-kv-cache-binding-test-for-hidden-anchor-r-29b5cab4c0-20260527T151143648950+0000

## What looked useful

Across 5 fixed seeds and 4096 requests per seed, weak token-only cache keys under boundary conflicts produced mean nonzero logit error rate 0.9422 and mean top-1 mismatch rate 0.6409, while strong boundary-aware keys and same-boundary controls had zero logit errors and zero top-1 mismatches.

## Boundaries and scale limits

Synthetic Numpy model and local replay only; no production serving engine, GPU runtime, real LLM weights, real tokenizer/chat-template stack, multi-tenant deployment, or long-running traffic trace was validated.

## Claim scope

Deterministic local serving replay with a causal-attention KV cache: token-only weak prefix-cache keys are unsafe when hidden-state-affecting serving boundary fields vary across shared token prefixes; boundary-aware strong keys preserve exact equivalence to no-cache recomputation in the tested harness.

## Why it stopped

Mechanism supported in a direct local replay, but evidence remains synthetic/local and is insufficient for paper-positive closure under the Tier 3 paper gate.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded step is a real serving-engine integration replay that exercises LoRA/template/cache-salt or comparable hidden-state boundary fields against an actual prefix-cache implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real serving-engine boundary-aware prefix-cache integration replay
- Success threshold: For a weak/ablated key, observe at least one reproducible cross-boundary unsafe cache hit with nonzero logit divergence or token mismatch; for the strong/current key, observe zero divergence across at least 1000 shared-prefix requests with boundary conflicts.
- Stop condition: Stop if the chosen engine cannot expose or instrument prefix-cache key boundaries locally within the bounded run, or if current engine keys are proven to include the tested hidden-state-affecting fields and no ablation/instrumented weak-key replay is feasible.

## Evidence references

- Artifact root: `<local-path>/projects/local-serving-engine-weak-vs-strong-prefix-cache-boundary-d11fcb81a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
