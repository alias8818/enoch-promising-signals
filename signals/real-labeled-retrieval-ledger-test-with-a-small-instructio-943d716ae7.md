# Real labeled retrieval ledger test with a small instruction model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-labeled-retrieval-ledger-test-with-a-small-instructio-943d716ae7`
Run ID: `real-labeled-retrieval-ledger-test-with-a-small-instructio-943d716ae7-20260524T074313059090+0000`

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

- Parent run decision: Small-Agent Evidence Ledger: enoch://control-plane/projects/small-agent-evidence-ledger-339c9bb6b39b/runs/small-agent-evidence-ledger-339c9bb6b39b-20260524T070832042830+0000
- Parent run decision: LLM Small-Agent Evidence Ledger on Labeled Retrieval Tasks: enoch://control-plane/projects/llm-small-agent-evidence-ledger-on-labeled-retrieval-tasks-dd12f1d09c/runs/llm-small-agent-evidence-ledger-on-labeled-retrieval-tasks-dd12f1d09c-20260524T072713026673+0000

## What looked useful

A combined ledger-plus-answer prompt caused a tradeoff: answer F1 rose versus labels-only (+0.2748) and exceeded the no-gold control (+0.1668), but it was worse than the unlabeled baseline (-0.1774 answer F1) and much worse than labels-only on citation F1 (-0.2720).

## Boundaries and scale limits

Single small instruction model, HotpotQA distractor dev contexts, greedy decoding, 3 fixed seeds with 100 sampled examples per seed. Does not cover larger instruction models, learned retrievers, human ratings, or production RAG workloads.

## Claim scope

On 299 usable seeded HotpotQA distractor-dev examples evaluated with google/flan-t5-base, an explicit evidence-ledger prompt improved answer F1 over a brittle labels-only citation prompt but underperformed a standard unlabeled context baseline and substantially reduced citation quality.

## Why it stopped

Tier 2 direct metrics failed the success threshold: the ledger did not beat the real unlabeled answer baseline and did not improve citation F1 or recall over the labels-only ablation.

## Recommended next action

Stop this run as no-paper evidence; the concrete next bounded test is a decoupled two-step support-selection then answer-generation protocol on the same HotpotQA setup.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Decoupled support-selection ledger for small instruction RAG
- Success threshold: Two-step protocol improves answer F1 by at least +0.03 over baseline_unlabeled and citation F1 by at least +0.05 over labels_only, while staying at least +0.10 answer F1 above the no-gold control.
- Stop condition: Stop if the two-step protocol fails either the answer baseline threshold or the citation threshold on the fixed seeded HotpotQA protocol.

## Evidence references

- Artifact root: `<local-path>/projects/real-labeled-retrieval-ledger-test-with-a-small-instructio-943d716ae7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
