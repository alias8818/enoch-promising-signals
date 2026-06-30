# CPU Spec-Dec with 5-Gram Cache Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-spec-dec-with-5-gram-cache-draft-ff2ec7bcae18`
Run ID: `cpu-spec-dec-with-5-gram-cache-draft-ff2ec7bcae18-20260522T142844521296+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/04fb381aed47

## What looked useful

Corrected variable-backoff medium run on War and Peace found 5-gram mean accept probability 0.9997, sampled accept rate 0.9997, top-1 agreement 0.9967, and projected gamma=8 tokens per target call 8.9984 against a 6-gram target. The 4-gram control was already close at 0.9973 mean accept probability and 8.9790 projected gamma=8 tokens per target call, suggesting the mechanism is real in this proxy but the 5-gram order may not be uniquely justified without latency and memory tradeoff tests.

## Boundaries and scale limits

Single corpus, word/punctuation tokenizer, 120k-token bounded run, 20k sampled positions, n-gram target only, no neural model, no GPU target verification, no end-to-end latency benchmark.

## Claim scope

In a real-text n-gram proxy, a CPU 5-gram draft cache is highly compatible with a smoothed 6-gram target distribution and substantially outperforms unigram and 3-gram draft controls on speculative acceptance; this does not validate transformer-target speedup.

## Why it stopped

Proxy evidence supports the mechanism but is insufficient for a paper or for a direct speculative-decoding speedup claim.

## Recommended next action

Run a bounded transformer-target deepen test using a GPT-2-small-class model with BPE tokens, comparing 3/4/5-gram CPU cache drafts against no-draft on acceptance, target calls, wall-clock latency, and memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-target validation for CPU 5-gram speculative draft cache
- Success threshold: 5-gram draft improves end-to-end tokens/second by at least 15% over no-draft and at least 5% over 4-gram while staying under a documented memory budget, with transformer sampled accept rate at least 0.6 for gamma=4 or gamma=8.
- Stop condition: Stop as negative if transformer sampled accept rate is below 0.4, if wall-clock throughput is not better than no-draft, or if 4-gram matches 5-gram within 2% while using materially less memory.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-spec-dec-with-5-gram-cache-draft-ff2ec7bcae18`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
