# Constrained model-authored evidence ledgers for sub-1B QA generation

Status: `useful_signal`
Project ID: `constrained-model-authored-evidence-ledgers-for-sub-1b-qa-9b15f7fcd3`
Run ID: `constrained-model-authored-evidence-ledgers-for-sub-1b-qa-9b15f7fcd3-20260516T101223206933+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Constrained model-authored evidence ledgers for sub-1B QA generation: internal_generated:constrained-model-authored-evidence-ledgers-for-sub-1b-qa-9b15f7fcd3

## What looked useful

The ledger prompt sometimes produced real copied evidence and successful parsed ledger outputs were cleaner conditionally, but end-to-end reliability was poor: parse OK fell from 0.956 baseline to 0.717 ledger, verifier F1 fell from 0.329 to 0.294, and only 0.050 of ledger outputs satisfied parse plus answer-in-context plus verifier F1 >= 0.5 plus valid evidence binding.

## Boundaries and scale limits

Single 0.5B instruction model, one extractive QA dataset, prompt-only generation, 1,080 total generations, no fine-tuning, no constrained decoding, no human evaluation, and no larger sub-1B model sweep.

## Claim scope

On 120 SQuAD validation passages with Qwen2.5-0.5B-Instruct, a free-form pre-answer model-authored evidence ledger prompt did not improve end-to-end grounded QA generation over a direct QA baseline; it reduced parse success and verifier F1 while producing a small conditional quality signal among successfully parsed outputs.

## Why it stopped

Bounded direct validation produced a no-paper mixed/negative result for the tested free-form ledger mechanism; the evidence supports a narrow implementation follow-up, not publication readiness.

## Recommended next action

Run one bounded deepen test replacing free-form evidence copying with programmatic span candidates or constrained decoding, using the same paired SQuAD metrics and stopping if ledger-valid supported QA remains below 15% or fails to beat the posthoc-evidence control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained span-candidate evidence ledgers for sub-1B QA generation
- Success threshold: Ledger-valid supported QA rate >= 0.15 and at least +0.03 absolute over posthoc evidence, with no more than -0.05 parse success loss versus baseline.
- Stop condition: Stop as negative if ledger-valid supported QA is below 0.15, if it does not beat posthoc evidence by 0.03 absolute, or if parse success remains more than 0.05 below baseline after constrained decoding.

## Evidence references

- Artifact root: `<local-path>/projects/constrained-model-authored-evidence-ledgers-for-sub-1b-qa-9b15f7fcd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
