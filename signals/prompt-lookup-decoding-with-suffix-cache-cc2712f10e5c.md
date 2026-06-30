# Prompt Lookup Decoding with Suffix Cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-lookup-decoding-with-suffix-cache-cc2712f10e5c`
Run ID: `prompt-lookup-decoding-with-suffix-cache-cc2712f10e5c-20260605T045231100342+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2580c6b3cea7

## What looked useful

A suffix-to-last-position index removed repeated O(prompt_length) scans. Across synthetic repeated, copy, and no-hit controls, suffix-index lookup speedup excluding build ranged from about 100x to 17,225x; including build, end-to-end speedup ranged from 3.74x to 171.37x while preserving acceptance fractions.

## Boundaries and scale limits

No real language model, tokenizer, GPU decode loop, KV-cache implementation, batching, paged attention, or production serving workload was tested. Results are candidate-generation-only and synthetic.

## Claim scope

In a deterministic synthetic prompt-lookup candidate-generation harness with 1k-65k token prompts, an 8-token suffix index preserved naive prompt-lookup candidate acceptance while reducing lookup latency and remaining faster end-to-end after index build.

## Why it stopped

Synthetic candidate-generation evidence supports the mechanism, but it is proxy-only and not a full validation of model-serving speedup.

## Recommended next action

Stop this run as no-paper useful signal; next implement the suffix-index candidate generator in a real small-model decoding loop and measure end-to-end tokens/s and accepted speculative tokens versus naive prompt lookup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-model prompt lookup decoding with suffix index
- Success threshold: At least 10% end-to-end decode throughput improvement on repetitive prompts with no statistically meaningful drop in accepted speculative tokens and no more than 5% memory overhead for the tested context length.
- Stop condition: Stop if suffix-index build/memory overhead eliminates throughput gains on repetitive prompts or if candidate acceptance diverges from naive prompt lookup.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-decoding-with-suffix-cache-cc2712f10e5c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
