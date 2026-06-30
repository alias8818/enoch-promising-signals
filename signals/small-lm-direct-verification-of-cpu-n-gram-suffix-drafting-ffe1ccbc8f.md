# Small-LM Direct Verification of CPU N-Gram Suffix Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-lm-direct-verification-of-cpu-n-gram-suffix-drafting-ffe1ccbc8f`
Run ID: `small-lm-direct-verification-of-cpu-n-gram-suffix-drafting-ffe1ccbc8f-20260527T103913046721+0000`

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

- Parent run decision: CPU N-Gram Suffix Speculative Decoding: enoch://control-plane/projects/cpu-n-gram-suffix-speculative-decoding-32a867f96f3a/runs/cpu-n-gram-suffix-speculative-decoding-32a867f96f3a-20260525T225601013275+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/239c7a000d18

## What looked useful

Direct small-LM verification supports the mechanism in this bounded setting: GPT-2 small accepted enough suffix-copy draft tokens from natural-text histories to reduce target calls by 17.5% for max_draft=4 and 22.9% for max_draft=8, while the checked d8 run matched cached greedy output on all windows. The result is no-paper but useful because it identifies a concrete setting where CPU n-gram suffix drafting can beat the prior negative proxy threshold.

## Boundaries and scale limits

This was a Tier-1 controlled small direct test: one corpus, GPT-2 small only, greedy decoding only, 576 generated tokens total, CPU PyTorch verifier, and estimated speedup from measured call timings rather than an optimized end-to-end serving stack. It did not test sampling, batching, GPU verification, larger models, instruction-tuned models, or broad corpora.

## Claim scope

On 12 Tiny-Shakespeare natural-text windows using GPT-2 small greedy CPU verification, a CPU suffix n-gram drafter with 256-token visible histories, min_n=2, max_n=6, and max_draft=8 preserved exact greedy output and reduced target calls by 22.9%, with a conservative estimated speedup of 1.30x.

## Why it stopped

Tier-1 direct mechanism support was achieved, but evidence remains too narrow for a paper: one local corpus, one GPT-2 small verifier, short windows, and estimated rather than serving-integrated speedup.

## Recommended next action

Run a bounded deepen follow-up with an integrated cached serving benchmark on at least three corpora and two small LMs, requiring exact greedy equivalence and real wall-clock speedup above 1.10x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated Small-LM Serving Benchmark for CPU N-Gram Suffix Drafting
- Success threshold: Median real wall-clock speedup above 1.10x with no exact-match failures, plus target-call reduction above 10% on at least two corpora for each model.
- Stop condition: Stop as negative if exact-match failures occur, median speedup is at or below 1.05x, or target-call reduction falls below 10% on most corpus/model pairs.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-direct-verification-of-cpu-n-gram-suffix-drafting-ffe1ccbc8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
