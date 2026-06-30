# Bounded CPU n-gram draft generation for VRAM-light speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-cpu-n-gram-draft-generation-for-vram-light-speculative-decoding-3e653ccb9353`
Run ID: `bounded-cpu-n-gram-draft-generation-for-vram-light-speculative-decoding-3e653ccb9353-20260608T231025322466+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/38c857bbbb9c

## What looked useful

A 27-configuration sweep over 726,947 byte tokens found that larger bounded tables improved proxy call reduction. The best setting, max_order=8, draft_len=16, max_entries=131072, emitted 250,000 tokens using 127,694 verifier-call proxies: 1.958 tokens/call, 48.9% proxy call reduction, 39.9% nonzero accepted calls, 52.2 us mean CPU draft latency, and 88.4 MiB RSS. A max_order=4, draft_len=16 table was nearly tied at 1.956 tokens/call with 21.7 us mean draft latency.

## Boundaries and scale limits

Evidence is trace-level and byte-token based. It does not include a real LLM tokenizer, target-model greedy or sampled output, KV-cache verifier integration, GPU serving latency, or comparison against a neural draft model.

## Claim scope

On a public-domain byte-token text trace, a bounded CPU-resident n-gram table can draft exact future-token prefixes with low CPU latency and small memory footprint, improving an oracle verifier-call proxy from 1.0 to as much as 1.958 emitted tokens per call.

## Why it stopped

No-paper closure: this run produced useful scoped trace-level evidence, but the result is proxy-only and cannot validate real LLM speculative decoding or serving speedup.

## Recommended next action

Run a bounded deepen experiment with a real tokenizer and small target model output/verifier traces to measure actual speculative acceptance and wall-clock tokens/s versus no-draft decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer and small-model verifier test for bounded CPU n-gram speculative drafts
- Success threshold: At least 15% wall-clock tokens/s improvement on the repetitive workload, no regression worse than 5% on the low-repetition control, CPU RSS under 256 MiB, and unchanged target-model VRAM allocation.
- Stop condition: Stop as unsupported if actual model-token acceptance yields under 1.15 emitted tokens per verifier call or if CPU drafting overhead erases throughput gains on the repetitive workload.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-cpu-n-gram-draft-generation-for-vram-light-speculative-decoding-3e653ccb9353`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
