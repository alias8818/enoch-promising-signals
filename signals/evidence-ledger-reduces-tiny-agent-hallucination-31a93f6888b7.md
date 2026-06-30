# Evidence ledger reduces tiny agent hallucination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reduces-tiny-agent-hallucination-31a93f6888b7`
Run ID: `evidence-ledger-reduces-tiny-agent-hallucination-31a93f6888b7-20260529T080133385441+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/eddb43fb175d

## What looked useful

Main run: baseline hallucination rate 0.31076 vs ledger 0.00000 across 50 seeds x 500 questions, with ledger abstention 0.29676. Answerable-only stress check: baseline hallucination 0.04200 vs ledger 0.00000 across 10 seeds x 300 questions, with ledger abstention 0.00133.

## Boundaries and scale limits

No real LLM was run; the corpus and questions are synthetic and templated; the ledger verifier uses structured metadata; the main evidence covers 25,000 generated QA cases plus a 3,000-case answerable-only stress check, not naturalistic multi-step agent tasks.

## Claim scope

In a deterministic synthetic tiny retrieval-agent benchmark with generated entity facts, adversarial distractor passages, and unknown-entity questions, requiring an explicit evidence ledger before answering reduced unsupported answers relative to an always-answer retrieval baseline.

## Why it stopped

Closed as no-paper useful signal because the local result is a synthetic proxy mechanism test, not direct publication-grade evidence for real tiny LLM agents.

## Recommended next action

Run a bounded direct small-LLM follow-up comparing prompt-only, retrieval-only, and evidence-ledger-gated conditions on the same adversarial QA design.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM evidence ledger test on adversarial synthetic QA
- Success threshold: Ledger condition reduces hallucination by at least 30% relative to the strongest non-ledger control with no more than 15 percentage points additional abstention on answerable questions.
- Stop condition: Stop if the small LLM cannot be run locally/API-free within the controller budget, or if ledger prompting fails to produce parseable evidence entries in more than 20% of answer attempts after one formatting retry.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-tiny-agent-hallucination-31a93f6888b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
