# Suffix-Trie Speculative Decoding with Sliding Output Window

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-trie-speculative-decoding-with-sliding-output-window-4d54ea8ce2d3`
Run ID: `suffix-trie-speculative-decoding-with-sliding-output-window-4d54ea8ce2d3-20260610T161208072923+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b835979da057

## What looked useful

The mechanism is real but repetition-sensitive. Best byte-token real-corpus settings reached 1.77 tokens/verify on Tiny Shakespeare and 2.26 on War and Peace at window 32768 and draft length 16. Word-token checks reached only 1.05 and 1.08 tokens/verify, making the broad paper claim unsupported without BPE/model-serving evidence.

## Boundaries and scale limits

No learned target model, no BPE tokenizer, no GPU serving loop, no stochastic decoding, and no end-to-end latency measurement. Byte-level acceptance likely overstates usefulness relative to production LLM tokenization.

## Claim scope

Offline exact-replay proxy over 200k byte-token streams and 120k word-token streams: a sliding-window suffix index can draft accepted continuations when exact local repetition exists, with strong gains on byte/copy-heavy streams but weak gains on word-token streams.

## Why it stopped

Useful proxy evidence was produced, but it is not full validation: exact-replay byte metrics are promising, word-token metrics are weak, and no live target-model verifier or latency baseline was tested.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with a real BPE tokenizer and target-model greedy decoding traces before any serving-latency claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE Trace Validation for Sliding-Window Suffix Speculation
- Success threshold: Mean end-to-end tokens per verifier call >= 1.15 and measured latency improvement >= 10% on a repetitive/code-like subset without >5% regression on prose.
- Stop condition: Stop if BPE trace acceptance stays below 1.05 tokens per verifier call or lookup overhead eliminates measured latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-trie-speculative-decoding-with-sliding-output-window-4d54ea8ce2d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
