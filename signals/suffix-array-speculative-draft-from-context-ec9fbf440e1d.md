# Suffix-Array Speculative Draft from Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-draft-from-context-ec9fbf440e1d`
Run ID: `suffix-array-speculative-draft-from-context-ec9fbf440e1d-20260529T132243273815+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/277f7d0bf68a

## What looked useful

On tiny_shakespeare and Alice, longest suffix-copy drafting covered about 92-94% of query positions but accepted only 0.17-0.32 tokens/query and 2.3-4.3% of proposed tokens. A repeated-span positive control accepted 7.81 tokens/query and 97.6% of proposed tokens, showing the implementation detects the mechanism when repetition exists.

## Boundaries and scale limits

Tested only small public-domain prose corpora and a synthetic repeated-span positive control; no production tokenizer, target model verifier, GPU decode loop, code/log/RAG prompt corpus, or end-to-end latency measurement was run.

## Claim scope

A local causal suffix-array benchmark over word/punctuation token streams found that naive longest prior-context suffix continuation copying is effective on deliberately repeated spans but weak on two natural prose corpora.

## Why it stopped

This is a proxy/mechanism benchmark, not full end-to-end validation; it early-falsifies naive suffix-array copying for ordinary natural prose because accepted draft length is far below a likely useful speculative-decoding threshold.

## Recommended next action

Run a bounded deepen test on code/log/RAG-style prompt traces with a real tokenizer and target-model verifier; stop treating natural prose suffix-copy alone as paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-and-verifier suffix drafts on repeated-context domains
- Success threshold: At least 1.0 accepted token per query and a measured net wall-clock speedup over no-draft decoding on a bounded repeated-context corpus.
- Stop condition: Stop if accepted tokens/query remains below 0.5 or lookup overhead erases speedup on two repeated-context domains.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-draft-from-context-ec9fbf440e1d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
