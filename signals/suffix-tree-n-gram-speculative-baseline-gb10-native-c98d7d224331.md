# Suffix-tree n-gram speculative baseline, GB10 native

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-speculative-baseline-gb10-native-c98d7d224331`
Run ID: `suffix-tree-n-gram-speculative-baseline-gb10-native-c98d7d224331-20260612T040250865003+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/13353fe01b83

## What looked useful

Suffix backoff improved the repetitive-trace speedup proxy from the best fixed n-gram 2.7435x to 3.0048x at max draft 8 and from 2.2351x to 2.4396x at max draft 4. On Tiny Shakespeare natural text it only reached 1.0353x, and at max draft 16 it was slightly below fixed 5-gram.

## Boundaries and scale limits

No real LLM target verification, no GPU serving path, no production tokenizer/model, no real agent benchmark traces, and no batch/concurrency measurement. Runs were single-process CPU proxy experiments on GB10 and completed in seconds.

## Claim scope

CPU trace-replay proxy on 20k-token evaluation windows: suffix-backoff n-gram drafting is useful on a synthetic repetitive agentic-style trace at max draft 4 and 8, but not meaningfully useful on natural text and not consistently better at max draft 16.

## Why it stopped

Proxy evidence is mixed: it supports the repetitive-trace mechanism but early-falsifies broad natural-text benefit and does not provide direct LLM serving evidence.

## Recommended next action

Stop this run as a no-paper useful signal; next run should integrate a real small target LLM verifier on GB10 with real agentic/code traces and compare suffix backoff against production n-gram speculation on end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-target GB10 suffix-backoff speculative decoding on agentic/code traces
- Success threshold: At least 10% end-to-end latency reduction over the best fixed n-gram baseline on real repetitive traces, with no more than 10% memory overhead and no regression versus no-speculation on natural/non-repetitive traces.
- Stop condition: Stop if real target verification shows less than 5% latency gain over fixed n-gram on two representative repetitive traces or if suffix-index memory/lookup overhead cancels the reduction in target passes.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-baseline-gb10-native-c98d7d224331`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
