# Natural Corpus Paraphrase Memory Grounding With Equal-Budget Controls

Status: `useful_signal`
Project ID: `natural-corpus-paraphrase-memory-grounding-with-equal-budg-d480d2d7bc`
Run ID: `natural-corpus-paraphrase-memory-grounding-with-equal-budg-d480d2d7bc-20260519T125746791436+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Natural Corpus Paraphrase Memory Grounding With Equal-Budget Controls: internal_generated:natural-corpus-paraphrase-memory-grounding-with-equal-budg-d480d2d7bc

## What looked useful

Natural paraphrase grounding improved top-1 by +0.0855 to +0.1297 over canonical-only and by +0.1417 to +0.4563 over equal-budget random controls across Quora and StackExchange, k=1 and k=2. Random equal-budget augmentation degraded accuracy, indicating the gain depends on semantically grounded paraphrases rather than extra index entries.

## Boundaries and scale limits

Lexical BM25 retrieval only; duplicate-question components only; no neural retriever, LLM memory module, downstream QA task, human relevance audit, or web-scale memory bank. Quora k=2 eligibility limited the equal-size main run to 3,000 memories per corpus.

## Claim scope

On two natural duplicate-question corpora, adding same-component natural paraphrase entries to a BM25 memory index improves held-out paraphrase retrieval over canonical-only BM25 and over equal-budget random natural-text augmentation for 3,000 memory items across five fixed seeds.

## Why it stopped

Moderate direct BM25 retrieval evidence supports the mechanism in a bounded setting, but the Tier 4 paper-readiness threshold is not met because neural/end-to-end memory baselines, audited relevance, larger memory banks, and downstream metrics were not tested.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; do not chain another follow-up from this branch under the controller cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/natural-corpus-paraphrase-memory-grounding-with-equal-budg-d480d2d7bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
