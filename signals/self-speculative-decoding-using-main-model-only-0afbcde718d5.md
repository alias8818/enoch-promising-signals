# Self-speculative decoding using main model only

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-using-main-model-only-0afbcde718d5`
Run ID: `self-speculative-decoding-using-main-model-only-0afbcde718d5-20260608T222906560408+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0547e56fa3bc

## What looked useful

Greedy main-model-only drafting accepted a second token in only 0.5076% of corpus rounds and netted 0.804x at verifier cost 1.25, an early negative. Exact sampling with k=8 emitted 2.222 output tokens per verification round in the corpus proxy, giving idealized net speedup 1.7777x at verifier cost 1.25 and 1.1110x at verifier cost 2.0, but full-draft acceptance was only 0.0034%.

## Boundaries and scale limits

No pretrained transformer, GPU kernel, KV-cache, or end-to-end serving latency was measured. The corpus model is a 6-character n-gram proxy, so claims do not extend to LLM wall-clock speedup or publication-grade quality preservation.

## Claim scope

Bounded proxy evidence for main-model-only self-speculative decoding using frozen current target distributions on synthetic Markov targets and a character n-gram target trained on Tiny Shakespeare. Greedy frozen-argmax drafting is unsupported in the natural-text proxy; exact frozen-distribution sampling shows a possible target-verification-round reduction under idealized verifier-cost assumptions.

## Why it stopped

Proxy evidence is sufficient to reject greedy frozen-argmax main-only speculation for this scope and to identify a sampling mechanism worth direct testing, but it is not full transformer validation.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded direct transformer follow-up measuring exact frozen-distribution sampling on a small pretrained model with real verifier latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-transformer latency test for frozen-distribution self-speculative sampling
- Success threshold: At least 1.2x end-to-end tokens/sec over ordinary sampling for k=4 or k=8 while matching baseline sampling distribution within a predeclared statistical tolerance.
- Stop condition: Stop if verifier latency factor is >= mean output tokens per verification round or if distribution-correctness tests fail.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-using-main-model-only-0afbcde718d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
