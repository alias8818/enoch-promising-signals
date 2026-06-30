# Draft-Size Sweep for Speculative Decoding with Exact No-Spec Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `draft-size-sweep-for-speculative-decoding-with-exact-no-spec-baseline-92c671203a75`
Run ID: `draft-size-sweep-for-speculative-decoding-with-exact-no-spec-baseline-92c671203a75-20260628T130233354164+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3761ac6f7de5

## What looked useful

Exact-output speculative decoding reduced target calls and improved throughput versus exact no-spec greedy decoding. Best median speedups were 2.26x at 0.55 draft correctness, 3.39x at 0.70, 6.49x at 0.85, and 17.49x at 0.95. Low/medium draft quality peaked before the largest tested draft size, while high draft quality kept improving through draft size 64.

## Boundaries and scale limits

Synthetic single-sequence proxy only; no learned draft model, transformer attention, KV cache, tokenizer, natural prompts, multi-user serving, or production inference stack was tested.

## Claim scope

In a bounded GB10 CUDA microbenchmark with a deterministic Markov target MLP and oracle-noisy draft proposer, speculative decoding exactly matched the no-spec greedy baseline and showed draft-size optima that increased with draft correctness: 16 tokens at 0.55/0.70 accuracy, 32 tokens at 0.85, and 64 tokens at 0.95.

## Why it stopped

The result is useful but proxy-only: it tests exactness and draft-size mechanics on a synthetic CUDA target, not a real LLM serving setup.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with a real small transformer draft and exact greedy target baseline before making any serving claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer Draft-Size Sweep with Exact Greedy Baseline
- Success threshold: All speculative outputs exactly match the no-spec greedy baseline and at least one nontrivial draft size gives a median speedup above 1.25x across prompts with no more than 10% p10 latency regression.
- Stop condition: Stop if exactness fails, if all draft sizes are at or below 1.05x median speedup after including draft compute, or if the run exceeds the bounded local budget without producing per-prompt metrics.

## Evidence references

- Artifact root: `<local-path>/projects/draft-size-sweep-for-speculative-decoding-with-exact-no-spec-baseline-92c671203a75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
