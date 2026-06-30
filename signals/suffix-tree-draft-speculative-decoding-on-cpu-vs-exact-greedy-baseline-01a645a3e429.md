# Suffix-Tree Draft Speculative Decoding on CPU vs Exact Greedy Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-draft-speculative-decoding-on-cpu-vs-exact-greedy-baseline-01a645a3e429`
Run ID: `suffix-tree-draft-speculative-decoding-on-cpu-vs-exact-greedy-baseline-01a645a3e429-20260621T113001229239+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db62ea746c91

## What looked useful

Across 9 trials, exact match held for all outputs. Mean verifier-call reduction was 5.235x overall, with 6.170x on repetitive logs, 7.604x on periodic code, and 1.931x on local project text. Mean draft-token acceptance was 0.535.

## Boundaries and scale limits

No transformer model was run; verifier was a target-trace oracle. Results do not measure end-to-end CPU LLM throughput, tokenizer effects, KV-cache behavior, or real multi-token forward-pass latency.

## Claim scope

On bounded CPU byte-token traces, an online suffix-index drafter preserved exact greedy output identity and reduced verifier-call counts, with strongest results on repetitive logs and periodic code.

## Why it stopped

Bounded trace proxy supports the mechanism but is not full validation of CPU LLM speculative decoding speedup.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should wrap the same suffix-index drafter around a small CPU transformer greedy decoder and measure end-to-end tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small CPU Transformer Verification for Suffix-Index Draft Decoding
- Success threshold: Exact output match on all examples and at least 1.25x end-to-end tokens/s improvement on a code/log-like corpus without more than 10% regression on natural-language text.
- Stop condition: Stop if exact identity fails, if acceptance stays below 0.25 on all corpora, or if end-to-end CPU tokens/s is not improved on the repetitive/code-like corpus.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-speculative-decoding-on-cpu-vs-exact-greedy-baseline-01a645a3e429`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
