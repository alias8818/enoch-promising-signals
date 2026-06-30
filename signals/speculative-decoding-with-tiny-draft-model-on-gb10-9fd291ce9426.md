# Speculative Decoding with Tiny Draft Model on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-tiny-draft-model-on-gb10-9fd291ce9426`
Run ID: `speculative-decoding-with-tiny-draft-model-on-gb10-9fd291ce9426-20260605T113421807748+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/ffc50c4ab94f

## What looked useful

Tiny-draft speculative decoding on GB10 can help, but only with conservative lookahead in this tested pairing. Assistant-token lookahead 2 matched raw greedy output on all prompts and reached 31.50 tok/s versus 25.56 tok/s baseline. Larger lookahead settings were fragile: settings 4/6/8 failed all-prompt exactness and settings 6/8 lost average throughput.

## Boundaries and scale limits

Small local benchmark only: 384 generated tokens total, short prompts, single process, no batching, no long-context evaluation, no serving engine, no acceptance-rate internals, no sampling or repetition-penalty exactness guarantee, and no 7B+ target.

## Claim scope

On a single GB10 worker, Transformers built-in assisted generation using Qwen3-0.6B as draft for Qwen2.5-3B-Instruct improved exact raw greedy single-prompt decoding throughput by 1.23x on 6 short prompts x 64 generated tokens when num_assistant_tokens was fixed at 2.

## Why it stopped

The result is a bounded local signal rather than publication-grade validation: the exact speedup holds only for raw greedy with num_assistant_tokens=2, while larger lookahead and model-default generation settings produce mismatches or slowdowns.

## Recommended next action

Stop this run as no-paper useful signal; next deepen with a medium exactness/throughput benchmark over longer prompts and a target-family matched draft before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium exactness and acceptance study for Qwen speculative decoding on GB10
- Success threshold: Mean exact-greedy throughput speedup >=1.2x with no output mismatches and no p95 latency regression versus target-only greedy.
- Stop condition: Stop if any exactness mismatch appears under the intended generation config or if mean speedup is below 1.1x after the first 20 prompts.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-tiny-draft-model-on-gb10-9fd291ce9426`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
