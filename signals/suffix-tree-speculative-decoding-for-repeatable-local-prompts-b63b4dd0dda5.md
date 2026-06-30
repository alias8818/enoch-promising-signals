# Suffix-tree speculative decoding for repeatable local prompts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-for-repeatable-local-prompts-b63b4dd0dda5`
Run ID: `suffix-tree-speculative-decoding-for-repeatable-local-prompts-b63b4dd0dda5-20260613T040351898309+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/adcb2dee845f

## What looked useful

Suffix-trie proposals achieved 5.834x, 5.005x, and 3.765x mean target-call upper-bound speedups across five seeds on exact-repeat, near-repeat, and weak-repeat local prompt workloads, respectively; unique-noise control stayed at 1.000x with zero accepted draft tokens.

## Boundaries and scale limits

No neural LLM, GPU verifier, real tokenizer, KV-cache scheduler, or production vLLM/Arctic implementation was benchmarked. Speedups are target-call upper bounds from an oracle proxy, not measured LLM wall-clock speedups. The broad algorithm is already public as SuffixDecoding, so this is not standalone novelty evidence.

## Claim scope

In a deterministic oracle proxy for repeatable local prompts, a variable-context suffix-trie cache reduced target verification calls more than exact prompt caching and fixed 4-gram lookup on exact, near-repeat, and boilerplate-repeat workloads, while providing no benefit on deliberately unique noisy completions.

## Why it stopped

The run produced a useful controlled mechanism signal, but it is proxy-only and the broad suffix-tree speculative decoding idea already exists publicly, so it is not paper-positive evidence.

## Recommended next action

Stop this run as no-paper proxy evidence; the next concrete step is a bounded real-LLM local benchmark with tokenizer-level traces, wall-clock latency, correctness checks, and vLLM/Arctic suffix decoding comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer local LLM validation of suffix-cache speculation on repeatable prompt traces
- Success threshold: At least 1.3x measured tokens/sec improvement over no speculation on near-repeat traces with identical greedy outputs, no speed regression above 5% on unique/noisy traces, and clear advantage over exact prompt caching.
- Stop condition: Stop if real-tokenizer LLM runs show less than 1.1x measured speedup on near-repeat traces or any recurring correctness divergence from non-speculative greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-for-repeatable-local-prompts-b63b4dd0dda5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
