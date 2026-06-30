# CPU N-Gram Suffix Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-n-gram-suffix-speculative-decoding-32a867f96f3a`
Run ID: `cpu-n-gram-suffix-speculative-decoding-32a867f96f3a-20260525T225601013275+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/239c7a000d18

## What looked useful

On 24 local Python documents, best regex-token configuration reached 1.861x ideal target-call speedup with 0.872 accepted tokens per target call and about 12.5 us CPU lookup per call; byte tokens reached 3.198x. Local docs reached 1.649x regex and 2.178x byte. Synthetic repeated code approached the draft-length ceiling at about 15.4-15.9x for draft_len=16.

## Boundaries and scale limits

No real LLM verifier, production tokenizer, GPU/KV-cache measurement, or end-to-end wall-clock speculative decoding test was run; corpora were local system files plus a synthetic repeated-code control.

## Claim scope

Bounded local proxy benchmark shows that CPU n-gram suffix lookup can reduce ideal verifier target calls on repetitive/code-like token streams when exact held-out continuations are used as the acceptance oracle.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported by a bounded acceptance proxy, but verifier-free/tokenization-proxy evidence is insufficient for a paper or production speedup claim.

## Recommended next action

Run a direct small-model speculative decoding experiment with a production tokenizer and exact-output preservation, using code/document prompts and reporting wall-clock speedup versus standard decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Direct Verification of CPU N-Gram Suffix Drafting
- Success threshold: At least 1.25x median wall-clock speedup on repetitive code/document prompts with exact output preservation and no more than 5% median slowdown on low-repeat controls.
- Stop condition: Stop if exact-output preservation fails, if CPU lookup overhead eliminates speedup at draft_len<=16, or if median wall-clock speedup remains below 1.10x on repetitive prompts after tuning n-gram length and occurrence cap.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-suffix-speculative-decoding-32a867f96f3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
