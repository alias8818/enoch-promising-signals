# Suffix-Array Speculative Draft for GPT-2

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `suffix-array-speculative-draft-for-gpt-2-8fdf2bfb7239`
Run ID: `suffix-array-speculative-draft-for-gpt-2-8fdf2bfb7239-20260607T043935298690+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2342148c1368

## What looked useful

The suffix-array policy retrieved candidates and beat random continuation, but accepted only 0.137 tokens per position at min-match 1, fell to 0.080 and 0.039 at min-match 2 and 3 as coverage dropped, and accepted zero full 4-token drafts across 1,000 held-out positions. This is below the acceptance needed to amortize GPT-2 verification overhead for the naive method.

## Boundaries and scale limits

This tested GPT-2-small, WikiText-2, a 120k-token corpus, exact suffix matching with min-match 1-3, lexicographically first matching occurrence, and 4-token greedy drafts. It did not test larger corpora, reranking across multiple suffix hits, sampling acceptance, or full batched speculative decoding wall-clock speed.

## Claim scope

Naive exact suffix-array retrieval over 120k GPT-2 WikiText-2 training tokens is not a practically useful speculative draft source for GPT-2-small greedy decoding on 1,000 held-out WikiText-2 validation positions.

## Why it stopped

Proxy-scale but direct target-acceptance evidence early-falsified the naive method: retrieval coverage exists, but accepted draft length is too low and no full 4-token drafts were accepted in the 1,000-position confirmation.

## Recommended next action

Stop this naive suffix-array draft line unless a future bounded variant adds multi-hit reranking or model-assisted filtering and first demonstrates at least 0.5 accepted GPT-2-small greedy tokens per held-out position.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-draft-for-gpt-2-8fdf2bfb7239`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
