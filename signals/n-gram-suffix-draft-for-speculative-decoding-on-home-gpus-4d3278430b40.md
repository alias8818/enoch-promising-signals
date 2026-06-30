# N-Gram Suffix Draft for Speculative Decoding on Home GPUs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-suffix-draft-for-speculative-decoding-on-home-gpus-4d3278430b40`
Run ID: `n-gram-suffix-draft-for-speculative-decoding-on-home-gpus-4d3278430b40-20260531T123900901537+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9589fd5d43ed

## What looked useful

The mechanism is viable enough for a bounded follow-up: Python suffix lookup overhead was 20-26 us per step and accepted/proposed draft rates were 66.8% on repetitive prompts and 41.6% on narrative prompts, with draft length trading acceptance quality for fewer verifier calls.

## Boundaries and scale limits

Small hand-built prompt set, distilgpt2 only, greedy decoding only, verifier-call proxy rather than optimized end-to-end decoder speed, no larger home-GPU model, no broad corpus, no batching or serving measurement.

## Claim scope

On eight short local prompts using distilgpt2 on CUDA, n-gram suffix prompt lookup produced draft tokens accepted by the target greedy verifier often enough to reduce verifier-call count by 80.7% on repetitive/code-like prompts and 62.5% on narrative prompts at draft length 8.

## Why it stopped

The run produced bounded local support for the mechanism but only via a small prompt suite and verifier-call proxy, not full end-to-end decoding validation.

## Recommended next action

Stop this run as no-paper useful signal; next implement a KV-cache real decoder benchmark on a 1B-3B local model and compare tokens/sec against greedy decoding and a no-draft baseline on a public prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram suffix speculative decoding on a 1B-3B home-GPU model
- Success threshold: At least 20% tokens/sec improvement on repetitive/code/copy-heavy prompts with no more than 5% slowdown on narrative prompts over at least 100 prompts total.
- Stop condition: Stop if verifier-call reduction does not translate to at least 10% wall-clock speedup in the first 30-prompt pilot or if KV-cache memory/copy overhead exceeds the saved verifier work.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-for-speculative-decoding-on-home-gpus-4d3278430b40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
