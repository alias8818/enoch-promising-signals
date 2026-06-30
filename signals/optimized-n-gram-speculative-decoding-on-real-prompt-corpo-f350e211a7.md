# Optimized n-gram speculative decoding on real prompt corpora

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `optimized-n-gram-speculative-decoding-on-real-prompt-corpo-f350e211a7`
Run ID: `optimized-n-gram-speculative-decoding-on-real-prompt-corpo-f350e211a7-20260605T031814020971+0000`

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

- Parent run decision: N-gram Draft Speculative Decode: enoch://control-plane/projects/n-gram-draft-speculative-decode-0ce27366b8bf/runs/n-gram-draft-speculative-decode-0ce27366b8bf-20260604T222103992367+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5938b088e934

## What looked useful

Prompt-local n-gram lookup was the dominant source of gains, reaching 56.4% target-call reduction at draft cap 32. Corpus-only lookup was weak at about 13.5% reduction and 1.3% token acceptance; combined lookup improved over prompt-local by only about 1.15 percentage points at draft cap 32.

## Boundaries and scale limits

Small prompt corpus sample, distilgpt2 target model, greedy continuation replay, target-call accounting only; no end-to-end serving latency, no 7B+ model, no multi-corpus robustness, no batching or KV-cache cost measurement.

## Claim scope

Tier 1 replay evidence on 96 held-out prompts from f/awesome-chatgpt-prompts using distilgpt2 greedy continuations supports prompt-local n-gram speculative drafting as a target-call reduction mechanism; best tested combined setting reduced target verification calls by 57.5% in the replay.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported by a direct small replay, but publication readiness requires live latency evidence and broader model/corpus validation.

## Recommended next action

Run a bounded live speculative-decoding microbenchmark on the same prompt split to measure wall-clock latency and tokens/sec for prompt-local versus combined lookup under real target forward-pass costs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live latency microbenchmark for prompt-local n-gram speculative decoding
- Success threshold: At least 20% end-to-end tokens/sec improvement over greedy baseline on 96 or more real prompts without changing generated greedy outputs; prompt-local must explain most of the improvement.
- Stop condition: Stop if live speculative decoding improves tokens/sec by less than 10% or if verification sequence overhead erases the replay target-call advantage.

## Evidence references

- Artifact root: `<local-path>/projects/optimized-n-gram-speculative-decoding-on-real-prompt-corpo-f350e211a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
