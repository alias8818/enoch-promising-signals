# Real small-transformer serving ablation for dynamic n-gram speculative cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-small-transformer-serving-ablation-for-dynamic-n-gram-27c64c6721`
Run ID: `real-small-transformer-serving-ablation-for-dynamic-n-gram-27c64c6721-20260609T040822020672+0000`

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

- Parent run decision: Dynamic n-gram cache for speculative decoding: enoch://control-plane/projects/dynamic-n-gram-cache-for-speculative-decoding-8d0d083cc3fa/runs/dynamic-n-gram-cache-for-speculative-decoding-8d0d083cc3fa-20260608T223915352511+0000
- Parent run decision: Small-LLM serving test for dynamic n-gram speculative cache: enoch://control-plane/projects/small-llm-serving-test-for-dynamic-n-gram-speculative-cach-7eef9f09cc/runs/small-llm-serving-test-for-dynamic-n-gram-speculative-cach-7eef9f09cc-20260609T013340496686+0000

## What looked useful

Dynamic generated-context n-gram lookup is materially stronger than static prompt-only lookup for exact greedy speculative serving in this small-transformer CPU test. Static lookup was brittle and sometimes wasted verification on bad candidates; dynamic lookup was exact on all prompts, faster on all prompts, and reduced call count on 15 of 16 prompts, but a low-locality prompt showed overhead without call reduction.

## Boundaries and scale limits

No GPU kernels, concurrent serving, request batching, quantization, stochastic sampling, large models, or broad natural prompt benchmark were tested. The prompt set was hand-built and intentionally included repeated-context cases, so results should be treated as mechanism evidence rather than production readiness.

## Claim scope

On a CPU worker with distilgpt2 exact greedy decoding over 16 fixed-seed repeated/nonrepetitive prompts, dynamic n-gram speculative caching matched baseline tokens exactly while reducing mean forward calls per generated token from 1.0208 to 0.3984 and increasing mean generated tokens/sec from 28.77 to 58.81.

## Why it stopped

Tier 2 local evidence supports the mechanism but is not paper-positive because serving scale, batching, GPU behavior, larger models, and broad prompt robustness were not tested.

## Recommended next action

Run a bounded deepen follow-up that adds adaptive candidate gating for low-locality prompts and evaluates at least 100 fixed prompts from a real text/code corpus against greedy, static lookup, dynamic lookup, and dynamic gated lookup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive-gated dynamic n-gram speculative cache on a real prompt suite
- Success threshold: Gated dynamic lookup must keep mean calls/token at least 40% below greedy baseline, improve mean tokens/sec by at least 25%, and have no more than 5% of prompts slower than baseline while maintaining exact greedy outputs.
- Stop condition: Stop if gated dynamic lookup fails exactness, reduces calls/token by less than 25%, or remains slower than baseline on more than 20% of low-locality prompts.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-transformer-serving-ablation-for-dynamic-n-gram-27c64c6721`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
