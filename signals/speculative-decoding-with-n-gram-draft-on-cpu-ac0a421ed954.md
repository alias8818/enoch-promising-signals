# Speculative Decoding with N-Gram Draft on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-n-gram-draft-on-cpu-ac0a421ed954`
Run ID: `speculative-decoding-with-n-gram-draft-on-cpu-ac0a421ed954-20260608T223432816079+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7b7a88ab66bb

## What looked useful

CPU n-gram drafting is very cheap and can approach draft_len+1 oracle target-call speedup on repetitive streams, but gives only about 1.15x oracle speedup on downloaded prose under this trace test.

## Boundaries and scale limits

No real transformer target, no end-to-end latency measurement, no GPU/model verification, no tokenizer-specific study, and only one downloaded prose corpus plus two synthetic repetitive corpora.

## Claim scope

Trace-level oracle simulation of a prior-context n-gram CPU drafter on 60k-token downloaded prose plus synthetic repeated code/log streams. The mechanism reduces target verification calls strongly only when generated tokens repeat earlier spans.

## Why it stopped

No-paper closure: this is a trace/proxy mechanism result, not full validation of real transformer speculative decoding latency.

## Recommended next action

Run a bounded direct small-transformer speculative decoding benchmark with real tokenizer IDs and wall-clock latency versus greedy decoding on prose and repetitive code/log prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-transformer latency test for CPU n-gram drafting
- Success threshold: At least 1.25x end-to-end latency speedup on repetitive code/log prompts with byte/token-identical output versus greedy decoding, and no claimed win on prose unless latency also exceeds 1.10x.
- Stop condition: Stop if verifier batching overhead removes the repetitive-stream speedup or if output equality cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-draft-on-cpu-ac0a421ed954`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
