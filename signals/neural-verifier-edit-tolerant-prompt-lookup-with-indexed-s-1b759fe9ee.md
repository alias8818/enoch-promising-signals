# Neural-verifier edit-tolerant prompt lookup with indexed search

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `neural-verifier-edit-tolerant-prompt-lookup-with-indexed-s-1b759fe9ee`
Run ID: `neural-verifier-edit-tolerant-prompt-lookup-with-indexed-s-1b759fe9ee-20260601T100041377139+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Edit-tolerant prompt-lookup speculative decoding on 10GB: enoch://control-plane/projects/edit-tolerant-prompt-lookup-speculative-decoding-on-10gb-b85b447f23f5/runs/edit-tolerant-prompt-lookup-speculative-decoding-on-10gb-b85b447f23f5-20260601T050638566302+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e2ed0cb03f27

## What looked useful

Indexed character n-gram search alone was strong for edit-tolerant prompt lookup; in two direct controlled runs the learned verifier recovered 0 indexed top-1 errors despite the correct prompt always appearing in the top-25 candidate set.

## Boundaries and scale limits

The corpus and query distribution are synthetic, English-only, and small compared with production prompt stores. The verifier is a compact feature-based MLP, not a transformer cross-encoder or contrastive neural retriever. Real prompt logs, multilingual text, much larger corpora, and stronger verifier architectures were not tested.

## Claim scope

In a controlled synthetic prompt-library lookup benchmark with 600-1200 canonical prompts, substantial character edits, word drops, punctuation/case changes, synonym substitutions, and near-duplicate prompt templates, TF-IDF character n-gram indexed search achieved 97.8-98.96% top-1 accuracy and 100% top-25 recall, while the tested PyTorch MLP neural verifier/reranker provided no top-1 improvement.

## Why it stopped

Controlled direct Tier 1 evidence did not support the core improvement threshold: verifier top-1 accuracy equaled indexed top-1 accuracy and recovered 0 indexed errors in both main and stress runs.

## Recommended next action

Stop this run as a no-paper useful negative for the tested neural-verifier design; a bounded follow-up should test a stronger cross-encoder or character-CNN verifier only on hard top-k ambiguity cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-encoder verifier for hard prompt-lookup ambiguities
- Success threshold: Verifier reranking improves top-1 accuracy by at least 1 absolute percentage point and recovers at least 25% of indexed top-1 errors, with top-k recall unchanged and no more than 1% loss on index-correct cases.
- Stop condition: Stop if the stronger verifier recovers fewer than 10% of indexed top-1 errors or loses more correct index top-1 cases than it recovers on a controlled 1000-query benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/neural-verifier-edit-tolerant-prompt-lookup-with-indexed-s-1b759fe9ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
