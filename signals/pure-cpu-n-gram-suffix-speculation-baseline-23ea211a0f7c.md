# Pure-CPU N-Gram Suffix Speculation Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pure-cpu-n-gram-suffix-speculation-baseline-23ea211a0f7c`
Run ID: `pure-cpu-n-gram-suffix-speculation-baseline-23ea211a0f7c-20260614T060300659503+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/915e27ae2b3e

## What looked useful

The mechanism is cheap and sometimes helpful but weak: draft-4 produced only 1.068x-1.134x ideal emitted tokens per verification step with 1.9%-4.4% accepted/proposed token rates; draft-8 reduced accepted/proposed rates to 0.8%-2.0% and had near-zero full-draft accepts. Shakespeare failed the unigram top-1 baseline, showing corpus dependence.

## Boundaries and scale limits

No neural target model, model tokenizer, KV cache, sampling policy, or end-to-end serving latency was tested. Corpora were small public-domain/proxy texts capped at 500k characters, and all measurements were single-process CPU runs.

## Claim scope

A dependency-free CPU suffix n-gram table was tested as an oracle speculative drafting proxy on three small public text corpora using lowercase word/punctuation tokens, max_order 6, min_count 2, and draft lengths 4 and 8.

## Why it stopped

Proxy/early falsification rather than full validation: pure CPU suffix n-grams are fast, but acceptance is too low and corpus-dependent for a paper-ready or general positive claim.

## Recommended next action

Stop this proxy run; the concrete next action is a bounded direct validation using a real target-model tokenizer and greedy target-model verification, comparing suffix n-gram drafts against no-draft and simple one-token draft baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tokenizer-matched n-gram speculation against a small neural target
- Success threshold: At least 1.10x end-to-end tokens/sec over no speculation on two domains, with accepted/proposed token rate above 10% and CPU draft overhead below 10% of target verification time.
- Stop condition: Stop if tokenizer-matched suffix drafts still stay below 5% accepted/proposed tokens or fail to exceed 1.03x end-to-end speedup on both domains.

## Evidence references

- Artifact root: `<local-path>/projects/pure-cpu-n-gram-suffix-speculation-baseline-23ea211a0f7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
