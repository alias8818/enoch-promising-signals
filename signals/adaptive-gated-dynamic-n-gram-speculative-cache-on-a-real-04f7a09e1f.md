# Adaptive-gated dynamic n-gram speculative cache on a real prompt suite

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `adaptive-gated-dynamic-n-gram-speculative-cache-on-a-real-04f7a09e1f`
Run ID: `adaptive-gated-dynamic-n-gram-speculative-cache-on-a-real-04f7a09e1f-20260609T082415219668+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real small-transformer serving ablation for dynamic n-gram speculative cache: enoch://control-plane/projects/real-small-transformer-serving-ablation-for-dynamic-n-gram-27c64c6721/runs/real-small-transformer-serving-ablation-for-dynamic-n-gram-27c64c6721-20260609T040822020672+0000
- Parent run decision: Small-LLM serving test for dynamic n-gram speculative cache: enoch://control-plane/projects/small-llm-serving-test-for-dynamic-n-gram-speculative-cach-7eef9f09cc/runs/small-llm-serving-test-for-dynamic-n-gram-speculative-cach-7eef9f09cc-20260609T013340496686+0000

## What looked useful

On 3.33M completion tokens, ungated dynamic n-gram caching achieved 1.1817x ideal target-call speedup and 1.1106x net speedup at draft_cost=0.05, beating static prompt-only n-gram at 1.0992x ideal/1.0395x net. Adaptive gating raised acceptance rate from 14.4% to 33.3% but reduced target-call speedup to 1.0436x and net speedup to 1.0367x at draft_cost=0.05; it only became preferable when draft cost was modeled near 0.2 target-token equivalents.

## Boundaries and scale limits

No real LM serving, GPU inference, wall-clock latency, tokenizer-specific transformer KV-cache behavior, or sampling-quality effects were measured. The evaluator uses regex word/punctuation tokens and exact completion traces, so results support the cache mechanism only, not deployment speedups or publication-grade claims.

## Claim scope

Teacher-forced trace validation on 52,286 real instruction prompt/completion examples from Alpaca, Dolly, and CodeAlpaca shows dynamic n-gram speculative caches can reduce target verification calls versus target-only and static prompt-only baselines, but the tested adaptive confidence gates do not improve the low-draft-cost setting.

## Why it stopped

Bounded real-suite trace validation supports dynamic n-gram cache usefulness but does not support the adaptive-gated variant as the primary claim under a cheap-drafter cost model; evidence is mechanism-level, not full serving validation.

## Recommended next action

Stop this branch as no-paper useful signal: keep the ungated dynamic cache as the supported mechanism and only revisit adaptive gating if a real serving implementation shows draft/cache overhead near or above 0.2 target-token equivalents.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tokenizer and model-serving overhead check for dynamic n-gram speculative cache gates
- Success threshold: Adaptive gating must beat ungated dynamic n-gram by at least 5% end-to-end latency while preserving at least 95% of generated-token agreement/quality on the bounded prompt suite.
- Stop condition: Stop if measured draft/cache overhead is below 0.1 target-token equivalents and ungated dynamic remains faster, or if adaptive gating fails to beat ungated dynamic on two of three suites.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-gated-dynamic-n-gram-speculative-cache-on-a-real-04f7a09e1f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
