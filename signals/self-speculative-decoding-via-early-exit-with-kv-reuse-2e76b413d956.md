# Self-Speculative Decoding via Early-Exit with KV Reuse

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-with-kv-reuse-2e76b413d956`
Run ID: `self-speculative-decoding-via-early-exit-with-kv-reuse-2e76b413d956-20260602T194613669052+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97c40ffa75b4

## What looked useful

Early exits accepted 14-22% of drafted tokens with exact-match 1.0 against full greedy when using sequential verification. The exact path was slower than greedy, while an optimistic layer-cost proxy suggested possible shallow-exit savings if a correct optimized KV/block verifier exists. Cached/block verifier diagnostics were not reliable enough for direct speed claims.

## Boundaries and scale limits

No real text corpus, no GPT-2-small-class baseline, no optimized serving kernel, and no validated argmax-equivalent true KV-cache block verifier. Cached/block reconstruction in this toy implementation showed large logit drift and low argmax agreement.

## Claim scope

Toy CUDA probe of a 6-layer synthetic-language transformer with trained early-exit heads and exact sequential full-greedy verification; evidence covers early-exit acceptance, exact correction behavior, local wall-clock overhead, and an optimistic layer-cost proxy only.

## Why it stopped

Proxy/local falsification of paper-ready speedup: exact self-speculative verification was slower than greedy and the attempted cached/block verifier was not argmax-equivalent, although early-exit acceptance and optimistic layer-cost results justify a bounded implementation follow-up.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to implement true per-layer KV caches and require argmax-equivalent block verification before any speedup claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Argmax-Equivalent KV-Cache Block Verifier for Early-Exit Self-Speculation
- Success threshold: Exact-match rate 1.0 against full greedy, cached/block verifier argmax agreement at least 0.999 on the tested prompts, and at least 1.10x wall-clock tokens/sec over optimized greedy for one exit/gamma setting.
- Stop condition: Stop if cached/block verifier cannot reach argmax equivalence or if exact cached verification remains below 1.05x greedy after optimizing obvious Python overhead.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-with-kv-reuse-2e76b413d956`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
