# CPU N-gram Suffix-Trie Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-suffix-trie-speculative-decoding-cb256f4f0f05`
Run ID: `cpu-n-gram-suffix-trie-speculative-decoding-cb256f4f0f05-20260620T162425427908+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1adab9b823bd

## What looked useful

Suffix-trie drafting strongly reduced proxy target calls on copy-heavy repeated text, failed on random text, and produced only modest Tiny Shakespeare gains with zero full 6-token accepts.

## Boundaries and scale limits

No real language model, model tokenizer, GPU target verification, or end-to-end serving throughput was measured; the result is a bounded CPU proxy and should not be read as production speculative decoding validation.

## Claim scope

CPU suffix-trie n-gram drafting was tested as an exact-match held-out-token proxy on 60k-token repeated synthetic, random synthetic, and Tiny Shakespeare streams with draft length 6 and max orders 1, 2, 4, 8, and 16.

## Why it stopped

Closed as no-paper useful signal because the evidence is proxy-only: it supports the repeated-context mechanism but does not validate end-to-end model-serving speedup.

## Recommended next action

Run a bounded direct small-model speculative decoding test with a real tokenizer and wall-clock tokens/second before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-model CPU suffix-trie speculative decoding throughput test
- Success threshold: At least 10% end-to-end tokens/second improvement over greedy decoding on a repeated/code-like corpus with no throughput regression greater than 5% on the natural-language control.
- Stop condition: Stop if CPU draft overhead exceeds saved target time or if mean accepted draft tokens remain below 0.5 on the repeated/code-like direct model test.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-suffix-trie-speculative-decoding-cb256f4f0f05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
