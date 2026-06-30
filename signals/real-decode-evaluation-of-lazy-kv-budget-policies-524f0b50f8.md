# Real Decode Evaluation of Lazy KV Budget Policies

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-decode-evaluation-of-lazy-kv-budget-policies-524f0b50f8`
Run ID: `real-decode-evaluation-of-lazy-kv-budget-policies-524f0b50f8-20260610T051937188062+0000`

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

- Parent run decision: Lazy KV-Cache with Dynamic Memory Budget Allocation: enoch://control-plane/projects/lazy-kv-cache-with-dynamic-memory-budget-allocation-cea80f6b5c46/runs/lazy-kv-cache-with-dynamic-memory-budget-allocation-cea80f6b5c46-20260610T003601833102+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b33d95b272d0

## What looked useful

A sink-plus-recent lazy compaction policy passed the pre-registered Tier 1 threshold at 128 and 256 tokens; sink preservation appears essential, because recent-only lazy policies failed once cache reduction became material.

## Boundaries and scale limits

Single small model, short prompt set, greedy decoding only, Python-level cache pruning, no batched serving, no long-context benchmark, no larger model, no sampling, no downstream task accuracy, and no kernel-level memory-bandwidth counters.

## Claim scope

On distilgpt2 with 8 mixed short prompts and greedy real CUDA decode for 128-256 new tokens, sink-preserving lazy KV budget policies preserved at least 99.5% greedy-token agreement with full KV while reducing mean cache length by 52-73%, reducing compactions to 6.0-13.5 per prompt, and improving measured tokens/sec by about 8-9%. Recent-only lazy policies did not meet the logprob threshold.

## Why it stopped

Tier 1 direct evidence supports the mechanism only in a narrow local setting; this is useful no-paper evidence, not publication-grade validation.

## Recommended next action

Run a bounded deepen test on a larger local causal LM with longer contexts, batched decode, and the same full-vs-eager-vs-lazy sink-preserving policy comparison before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger-model batched decode test for sink-preserving lazy KV compaction
- Success threshold: Lazy sink-plus-recent must reduce compactions by at least 10x versus eager sink-plus-recent, improve tokens/sec or peak-memory behavior by at least 5%, preserve at least 95% full-KV token agreement, and keep mean baseline-token logprob delta no worse than -0.10 nats/token.
- Stop condition: Stop if lazy sink-plus-recent falls below 95% token agreement, worse than -0.10 nats/token mean logprob delta, or shows no throughput or memory benefit versus eager sink-plus-recent under batched decode.

## Evidence references

- Artifact root: `<local-path>/projects/real-decode-evaluation-of-lazy-kv-budget-policies-524f0b50f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
