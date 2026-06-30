# Suffix-tree speculative decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-cpu-ffc41f5815c1`
Run ID: `suffix-tree-speculative-decoding-on-cpu-ffc41f5815c1-20260524T202920545699+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5cef9dde20c1

## What looked useful

Suffix-index proposals reached 7.7 tokens per target step with 0.96 accepted/proposed on repetitive synthetic text, but only 1.42-1.63 tokens per target step and 0.09-0.12 accepted/proposed on natural text. Random control stayed at 1.0 tokens per step.

## Boundaries and scale limits

No real LLM target model, no tokenizer-level evaluation, no end-to-end CPU serving benchmark, and no comparison against neural draft models. Metrics use exact corpus replay as an oracle acceptance proxy.

## Claim scope

Trace-level byte-token benchmark of an online suffix-index speculative proposer on two natural text corpora plus repetitive and random controls. Evidence supports multi-token copying mainly when the stream contains repeated substrings.

## Why it stopped

Bounded proxy evidence found a niche mechanism under repetition but did not validate broad CPU LLM speedup or publication-grade end-to-end performance.

## Recommended next action

Stop this run as no-paper useful signal; next, test the same proposer inside a real small CPU LLM speculative decoding loop and require wall-clock tokens/sec improvement over greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LLM test for suffix-index speculative decoding
- Success threshold: At least 1.10x end-to-end tokens/sec over greedy decoding on a predeclared repetitive/code prompt set with no more than 5% regression on natural text prompts.
- Stop condition: Stop as negative if end-to-end CPU throughput is below 1.05x greedy on the repetitive/code set or if verification/KV overhead removes the trace-level target-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-cpu-ffc41f5815c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
