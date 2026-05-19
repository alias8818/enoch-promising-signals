# Multi-Model Semi-Real Evidence Ledger Hallucination Eval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-model-semi-real-evidence-ledger-hallucination-eval-36c7076304`
Run ID: `multi-model-semi-real-evidence-ledger-hallucination-eval-36c7076304-20260519T013704184628+0000`

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

- Internal Enoch project: Multi-Model Semi-Real Evidence Ledger Hallucination Eval: internal_generated:multi-model-semi-real-evidence-ledger-hallucination-eval-36c7076304

## What looked useful

Relevant ledger evidence mattered in the distractor-only ablation, and the ledger reduced unsupported answers for one small seq2seq model, but the effect was not robust across models and introduced an answer-utility cost versus raw RAG.

## Boundaries and scale limits

The run used 2,880 local generations over SQuAD-derived answerable and synthetically unanswerable examples. It did not test natural SQuAD-v2 unanswerables, production retrieval logs, human citation grading, multi-hop ledgers, frontier models, or larger 7B+ instruction models.

## Claim scope

On a local semi-real SQuAD-derived evaluation with 3 fixed seeds, 3 cached models, and a raw-RAG baseline, a deterministic extractive evidence ledger was not robustly better than raw RAG: it improved unsupported-answer rate for FLAN-T5-small, was neutral/slightly worse for FLAN-T5-base, worsened Qwen2.5-0.5B-Instruct, and reduced average answer F1.

## Why it stopped

Tier 2 threshold was not met: ledger averaged only a 1.94 percentage point unsupported-answer improvement versus raw RAG, reduced answer F1 by 6.79 points, helped only FLAN-T5-small, and worsened Qwen.

## Recommended next action

Stop this claim as no-paper evidence; the next bounded test should evaluate a hybrid raw-context-plus-ledger prompt that preserves answer F1 while using ledger rows only for abstention/citation gating.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Raw Context plus Evidence Ledger Abstention Gate
- Success threshold: Hybrid ledger improves unsupported false-answer rate by at least 10 percentage points versus raw RAG for at least two of three model families while keeping answer F1 within 2 percentage points of raw RAG and answerable abstention below 10%.
- Stop condition: Stop as negative if the hybrid still worsens unsupported answers for any model family or drops answer F1 by more than 2 percentage points on average.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-semi-real-evidence-ledger-hallucination-eval-36c7076304`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
