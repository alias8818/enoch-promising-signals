# Suffix-tree n-gram speculative CPU decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-speculative-cpu-decoding-86fd84267092`
Run ID: `suffix-tree-n-gram-speculative-cpu-decoding-86fd84267092-20260524T081412937233+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e35c100a1357

## What looked useful

A short suffix cache can be a useful local repetition proposer for byte-level streams, but the evidence argues against deeper uncompressed suffix-tree n-gram contexts as a standalone CPU decoding win. On 80k-token byte runs, suffix_2_8 reached 1.428 tokens/call on Shakespeare and 1.631 on Alice, versus fixed_4 at 1.392 and 1.545. Word-token Shakespeare was effectively negative at 1.006 tokens/call.

## Boundaries and scale limits

No real transformer verifier, no CPU decoder integration, no tokenizer/model KV-cache measurement, and only small text corpora. The result measures proposer acceptance and overhead, not end-to-end LLM tokens/second.

## Claim scope

Bounded proxy benchmark of suffix-style variable-order n-gram speculative proposals on small real text streams. Byte-level suffix_2_8 slightly improves idealized verifier-call reduction over fixed_4 on Shakespeare and Alice, but deeper suffix contexts add memory/runtime without acceptance gains and word-token results are negative.

## Why it stopped

Proxy evidence is mixed and insufficient for a paper: byte-level acceptance improves modestly, but deeper suffix contexts do not help and word-token behavior is negative. This is an early bounded falsification of the broad suffix-tree n-gram CPU decoding claim, not a full validation.

## Recommended next action

Stop this no-paper proxy run; a bounded deepen follow-up should integrate suffix_2_8 and fixed_4 into a real CPU greedy decoder and require wall-clock speedup plus output identity before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU decoder validation of short suffix n-gram drafting
- Success threshold: At least 10% median wall-clock tokens/second improvement over greedy baseline on repetitive prompts, no regression larger than 5% on non-repetitive controls, and exact output identity.
- Stop condition: Stop if accepted draft tokens do not translate into at least 10% wall-clock speedup, if verifier batching cost erases the call reduction, or if exact greedy output identity fails.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-cpu-decoding-86fd84267092`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
