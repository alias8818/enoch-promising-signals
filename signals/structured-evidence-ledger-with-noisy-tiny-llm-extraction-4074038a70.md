# Structured Evidence Ledger with Noisy Tiny-LLM Extraction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `structured-evidence-ledger-with-noisy-tiny-llm-extraction-4074038a70`
Run ID: `structured-evidence-ledger-with-noisy-tiny-llm-extraction-4074038a70-20260523T232921225185+0000`

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

- Parent run decision: Structured Evidence Ledger for Tiny CPU Agents: enoch://control-plane/projects/structured-evidence-ledger-for-tiny-cpu-agents-0164eab1cdee/runs/structured-evidence-ledger-for-tiny-cpu-agents-0164eab1cdee-20260523T230648696549+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12311a2acc01

## What looked useful

Ledger consensus reached 0.8816 mean exact-record accuracy versus 0.3595 for single extraction, but plain majority voting reached 0.9899. Evidence grounding is useful relative to one pass but was not justified over self-consistency under independent noise.

## Boundaries and scale limits

The extractor is a controlled stochastic noise channel, not a real tiny LLM; the dataset is synthetic and small; noise is mostly independent across samples; no large-corpus, real-model, or human-labeled validation was performed.

## Claim scope

In a controlled 80-item synthetic evidence-extraction benchmark with 9 repeated stochastic noisy extractions per item over 100 replicates, an evidence-span-grounded structured ledger improves exact record accuracy over a single noisy extraction but does not beat ungrounded majority voting.

## Why it stopped

The predeclared controlled Tier 1 threshold failed: ledger exact accuracy exceeded single extraction by 0.5221 but trailed ungrounded majority vote by 0.1083, so the result is mixed rather than paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use a real tiny LLM on hand-labeled snippets with correlated hallucination or distractor cases and compare directly against majority vote.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-LLM evidence ledger test under correlated hallucination distractors
- Success threshold: Ledger exact-record accuracy is at least 10 percentage points higher than ungrounded majority vote with coverage no more than 5 percentage points lower, across at least three random seeds or prompt variants.
- Stop condition: Stop if majority vote is equal or better than the ledger on exact-record accuracy, or if the tiny LLM cannot produce parseable structured outputs above 70 percent validity after reasonable prompt calibration.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-with-noisy-tiny-llm-extraction-4074038a70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
