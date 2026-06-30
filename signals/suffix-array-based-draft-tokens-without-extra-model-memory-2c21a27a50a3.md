# Suffix-Array Based Draft Tokens Without Extra Model Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-based-draft-tokens-without-extra-model-memory-2c21a27a50a3`
Run ID: `suffix-array-based-draft-tokens-without-extra-model-memory-2c21a27a50a3-20260609T121109889845+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e2a380800d3b

## What looked useful

Suffix arrays are a plausible low-memory prompt-copy drafter, but local BPE acceptance is modest and word-token acceptance is very low, so practical speedup remains unproven.

## Boundaries and scale limits

No real LM verifier, no wall-clock speculative decoding integration, one natural-text corpus, single-threaded Python implementation, fixed prompt index only, and no dynamic indexing of generated tokens.

## Claim scope

On Tiny Shakespeare held-out continuation proxies, a fixed-prompt suffix array reproduces rightmost-longest prompt-copy draft quality with far less index memory than a naive all-n-grams hash table; GPT-2 BPE exact acceptance reached 0.3848-0.5155 tokens per position for 4-token drafts at 8k-16k prompt sizes.

## Why it stopped

Proxy-only evidence produced a useful mechanism signal but not direct publication-grade validation of model-serving speedup.

## Recommended next action

Run a bounded direct speculative-decoding test with GPT-2-small-class verification and an optimized suffix-array/FM-index drafter before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2 verifier test for suffix-array prompt-copy drafting
- Success threshold: At least 1.10x end-to-end wall-clock tokens/s over no-draft decoding on copy-heavy prompts, with no regression above 5% on general prose and less than 5 MB drafter index memory for 16k-token prompts.
- Stop condition: Stop if optimized direct-verifier runs show less than 1.05x speedup on copy-heavy prompts or drafter overhead exceeds the acceptance benefit.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-based-draft-tokens-without-extra-model-memory-2c21a27a50a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
