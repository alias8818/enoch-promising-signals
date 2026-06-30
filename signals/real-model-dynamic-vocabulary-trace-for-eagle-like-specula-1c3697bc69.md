# Real-model dynamic vocabulary trace for EAGLE-like speculative heads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-dynamic-vocabulary-trace-for-eagle-like-specula-1c3697bc69`
Run ID: `real-model-dynamic-vocabulary-trace-for-eagle-like-specula-1c3697bc69-20260520T003942830919+0000`

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

- Parent run decision: Dynamic Speculative Vocabulary for DFlash and EAGLE Heads: enoch://control-plane/projects/dynamic-speculative-vocabulary-for-dflash-and-eagle-heads-e1fa6de4b6a2/runs/dynamic-speculative-vocabulary-for-dflash-and-eagle-heads-e1fa6de4b6a2-20260519T234516956601+0000
- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Dynamic vocabularies around K=256-K=512 can preserve most draft-proxy top-1 decisions in a real model trace, but reference-token coverage remains too incomplete for an aggressive small-vocabulary claim and the selector tested is not a cheap deployable mechanism.

## Boundaries and scale limits

Single pretrained GPT-2 small model, 20 local text snippets, logit-lens proxy rather than a trained EAGLE head, optimistic selector derived from full teacher logits, no speculative decoding acceptance loop, no serving speed measurement.

## Claim scope

On 396 GPT-2 token positions from 20 short snippets, an optimistic teacher-logit top-K dynamic vocabulary retained a penultimate-hidden EAGLE-like draft proxy top-1 token 93.4% at K=256 and 97.7% at K=512, while actual reference next-token coverage was only 75.3% and 81.1% respectively.

## Why it stopped

No-paper useful signal: this Tier 1 direct trace supports the coverage mechanism partly, but it is a trace-only proxy without a trained speculative head, cheap selector, acceptance-rate baseline, or serving-speed result.

## Recommended next action

Run a bounded trained EAGLE-style head plus cheap dynamic selector evaluation on GPT-2 small, comparing full-vocabulary draft scoring against K=256 and K=512 restricted scoring on multi-token acceptance rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained GPT-2-small EAGLE head with cheap K=256/K=512 dynamic selector
- Success threshold: At K=512, restricted scoring retains >=95% of full-vocabulary draft top-1 decisions and >=90% of multi-token verifier acceptance, with a documented selector cost below full LM-head scoring.
- Stop condition: Stop if K=512 loses more than 10% relative verifier acceptance versus full-vocabulary draft scoring or if the cheap selector cost approaches full-vocabulary LM-head scoring.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-dynamic-vocabulary-trace-for-eagle-like-specula-1c3697bc69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
