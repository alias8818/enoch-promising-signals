# Suffix-N-gram Speculative Decoding vs Greedy and Tiny-Distilled Draft on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-n-gram-speculative-decoding-vs-greedy-and-tiny-distilled-draft-on-gb10-3f43d7d5837d`
Run ID: `suffix-n-gram-speculative-decoding-vs-greedy-and-tiny-distilled-draft-on-gb10-3f43d7d5837d-20260620T063642922816+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/09b091fae8ea

## What looked useful

Suffix-n-gram speculation produced 3.16-4.12x mean throughput over greedy with 0.977-0.986 acceptance on repeat/mixed traces, but only 0.40x greedy throughput and zero accepted proposals on random traces. Tiny bigram draft proxy was more robust in this synthetic setup.

## Boundaries and scale limits

Synthetic target and bigram draft proxy only; no real transformer checkpoint, KV-cache path, tokenizer/text corpus, or trained tiny neural draft model was tested. Timings are short bounded mechanism measurements, not production serving validation.

## Claim scope

In a synthetic GPU-backed oracle suffix-language benchmark on GB10, context-only suffix-n-gram speculative decoding exactly preserved greedy outputs and reduced target calls on repeat-heavy and mixed traces, but failed and slowed down on random low-repetition traces.

## Why it stopped

Bounded synthetic evidence supports a conditional mechanism but is not direct or broad enough for publication-grade validation.

## Recommended next action

Stop this worker run as a no-paper useful signal; the concrete next bounded test is a real small-model KV-cache benchmark with repetition-stratified prompts and a true tiny draft.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Model KV-Cache Benchmark for Gated Suffix-N-gram Speculation
- Success threshold: At least 1.5x throughput over greedy on high-repetition prompts with exact output match, no more than 5% slowdown on low-repetition prompts with the gate enabled, and credible comparison to a tiny draft baseline.
- Stop condition: Stop if suffix-n-gram acceptance remains below 0.3 on high-repetition prompts or if gated decoding cannot avoid slowdown on low-repetition prompts.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-speculative-decoding-vs-greedy-and-tiny-distilled-draft-on-gb10-3f43d7d5837d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
