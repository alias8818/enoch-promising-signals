# Suffix-Tree Speculative Draft from Compressed Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-draft-from-compressed-memory-d5d26b8eb8c3`
Run ID: `suffix-tree-speculative-draft-from-compressed-memory-d5d26b8eb8c3-20260604T040404144860+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/79f886d5213e

## What looked useful

Suffix drafting accepted 6.18 and 4.54 tokens/query on clean and 3%-mutated repeated synthetic memory, versus 0.43 and 0.40 for a last-token baseline. On Gutenberg Alice and Sherlock, it accepted only 0.23 and 0.16 tokens/query, approximately tied with the baseline. Position caps preserved synthetic quality, suggesting compressed storage can work when repeats exist.

## Boundaries and scale limits

Tested only with a CPU Python prototype, synthetic repetition, and two public-domain natural-text books up to 120k tokens. No transformer target model, end-to-end speculative decoding loop, production packed index, code workload, chat-history workload, or GPU-serving path was tested.

## Claim scope

A compressed suffix-key index can produce high-acceptance speculative drafts when the memory contains repeated or lightly mutated token spans; it is not useful as a broad natural-language draft source in the tested Gutenberg proxy.

## Why it stopped

Proxy early falsification of the broad claim: suffix-memory drafting works on repeated spans but is near-baseline on ordinary natural text and lacks direct end-to-end model-serving evidence.

## Recommended next action

Stop this run as a useful no-paper proxy result; the next bounded test should integrate the suffix draft index into a small target-model speculative decoding harness on repeated-memory workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM speculative decoding with compressed suffix-memory drafts on repeated-context workloads
- Success threshold: At least 1.25x end-to-end decode tokens/second over no-draft and at least 15% over an ngram/prompt-lookup baseline on a repeated-memory workload, with accepted draft tokens per query above 1.0 and index memory below 20% of model weights for the tested setup.
- Stop condition: Stop if accepted draft tokens/query stays below 0.5 or end-to-end decode speed is not improved by at least 5% on the repeated-memory workload after basic implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-draft-from-compressed-memory-d5d26b8eb8c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
