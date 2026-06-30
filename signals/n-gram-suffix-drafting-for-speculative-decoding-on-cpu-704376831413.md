# N-Gram Suffix Drafting for Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-suffix-drafting-for-speculative-decoding-on-cpu-704376831413`
Run ID: `n-gram-suffix-drafting-for-speculative-decoding-on-cpu-704376831413-20260619T073122500385+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

Best full replay reduced simulated target calls by 65.39% on Python stdlib bytes and 49.34% on TinyShakespeare bytes with mean draft overhead of 18.90 us and 25.46 us per call respectively. Wordish tokenization also reduced calls but was weaker.

## Boundaries and scale limits

No real transformer verifier, BPE tokenizer, KV-cache integration, stochastic sampling, or end-to-end CPU decode throughput was tested. Streams were capped to 600k byte tokens or 240k wordish tokens per dataset.

## Claim scope

Bounded offline replay shows that an online n-gram suffix table can reduce simulated target verification calls on exact-match text/code streams with microsecond-scale CPU overhead.

## Why it stopped

Closed as no-paper useful signal because this run is a proxy replay rather than direct model evidence.

## Recommended next action

Run a bounded direct CPU LLM decode integration with BPE tokens and compare end-to-end tokens/sec against greedy decoding and no-draft verification baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Integration for N-Gram Suffix Drafting
- Success threshold: At least 10% end-to-end tokens/sec improvement over greedy/no-draft baselines with no quality regression under deterministic decoding on both code and natural-language prompt sets.
- Stop condition: Stop if integrated suffix-table overhead exceeds saved verification time or if end-to-end throughput gain is below 5% on both code and natural-language prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-drafting-for-speculative-decoding-on-cpu-704376831413`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
