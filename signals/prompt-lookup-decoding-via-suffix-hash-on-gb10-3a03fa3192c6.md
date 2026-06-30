# Prompt Lookup Decoding via Suffix Hash on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-decoding-via-suffix-hash-on-gb10-3a03fa3192c6`
Run ID: `prompt-lookup-decoding-via-suffix-hash-on-gb10-3a03fa3192c6-20260609T074335267937+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/84b358ff9516

## What looked useful

Corrected suffix-hash lookup had zero oracle mismatches on checked positions and 599x-2136x median lookup speedup versus brute-force scan. Local Python bytes produced 3.71-4.28 accepted tokens per position for k=4-16 with max_guess=16; random bytes produced no useful accepted continuations.

## Boundaries and scale limits

Tested only byte-token synthetic and local Python-source streams up to 1,000,000 tokens; no tokenizer-specific corpus, no transformer model, no GPU decode loop, and no end-to-end serving speed measurement.

## Claim scope

A CPU-side online suffix-hash table can reproduce latest-match prompt-lookup candidates much faster than brute-force scanning on byte-token streams, and repeated/local-code streams contain nonzero exact continuations under this proxy.

## Why it stopped

This run provides a bounded proxy/mechanism result but not full validation of model-serving speedup or output-equivalent decoding.

## Recommended next action

Run a bounded GPU decode follow-up with a real tokenizer and small local transformer, comparing greedy decoding, brute prompt lookup, and suffix-hash prompt lookup on repeated-document prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix-hash prompt lookup decoding on a small local transformer
- Success threshold: At least 1.15x end-to-end generated tokens/s over greedy decoding and at least 5x lower candidate lookup overhead than brute prompt lookup on repeated prompts, with identical accepted outputs for exact-match candidates.
- Stop condition: Stop if candidate lookup or CPU/GPU synchronization removes the speedup, if accepted draft tokens per generated token stay below 0.5 on repeated prompts, or if output equivalence cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-decoding-via-suffix-hash-on-gb10-3a03fa3192c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
