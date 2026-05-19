# Hybrid Raw Context plus Evidence Ledger Abstention Gate

Status: `useful_signal`
Project ID: `hybrid-raw-context-plus-evidence-ledger-abstention-gate-0d6d88f6a0`
Run ID: `hybrid-raw-context-plus-evidence-ledger-abstention-gate-0d6d88f6a0-20260519T015804380310+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Hybrid Raw Context plus Evidence Ledger Abstention Gate: internal_generated:hybrid-raw-context-plus-evidence-ledger-abstention-gate-0d6d88f6a0

## What looked useful

Across 10 seeds and 250,000 held-out test examples at k=8, raw_entity_attr hallucinated on 45.5% of unanswerable examples, while ledger_only and hybrid_full_gate reduced hallucination to 0.0029% with 99.998% answer accuracy on answerable cases. Retrieval-depth ablations at k=3,5,12 showed the same ordering, but hybrid_full_gate was identical to ledger_only.

## Boundaries and scale limits

The evidence is synthetic and parser-controlled. It does not include real open-domain corpora, LLM answer generation, noisy NLI extraction, human-written ambiguity, or production retrieval distributions. The hybrid-full method tied ledger-only, so this run does not establish a unique hybrid raw-context-plus-ledger advantage.

## Claim scope

On a deterministic synthetic retrieved-context QA benchmark with fixed seeds, validation-tuned thresholds, distractors, missing evidence, negative-only evidence, and contradictions, a conflict-aware evidence-ledger abstention gate sharply reduces unsafe answers compared with raw-context retrieval baselines.

## Why it stopped

Moderate synthetic evidence supports evidence-ledger contradiction accounting, but the central hybrid-specific novelty is not separated from ledger-only and the benchmark is not naturalistic enough for a paper claim.

## Recommended next action

Stop this run as no-paper synthetic mechanism evidence; the next bounded test should replace the regex ledger with an LLM or NLI extractor on a real selective QA/RAG abstention benchmark and require hybrid_full to beat ledger_only and raw-context verifier baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural selective-QA validation of evidence-ledger abstention with noisy extraction
- Success threshold: Hybrid raw-plus-ledger must reduce unanswerable hallucination by at least 30% relative to the strongest non-hybrid baseline while losing no more than 3 percentage points of answerable accuracy, and must outperform ledger-only by at least 5 percentage points utility.
- Stop condition: Stop as negative if hybrid_full does not beat ledger_only by at least 5 utility points or if hallucination reduction comes mainly from abstaining on answerable cases beyond the 3 point accuracy-loss cap.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-raw-context-plus-evidence-ledger-abstention-gate-0d6d88f6a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
