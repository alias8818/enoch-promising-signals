# Evidence Ledger for Tiny Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-local-agents-2b587e5d0911`
Run ID: `evidence-ledger-for-tiny-local-agents-2b587e5d0911-20260529T152810937385+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9c7d9b00b62d

## What looked useful

Main 500-trial run: evidence ledger reached 1.000 value+source accuracy with 0.000 unsupported citation rate, versus best baseline 0.139 value+source accuracy. Sweep showed no advantage when context was large and noise-free, but +0.392 to +0.947 advantage under smaller context or distractors.

## Boundaries and scale limits

Test used synthetic structured facts, updates, and distractors only; no natural-language extraction, no real local LLM loop, no adversarial evidence, and no long-running deployment overhead measurement.

## Claim scope

In a synthetic structured-observation benchmark with perfect extraction, a normalized evidence ledger preserved latest trusted facts and source ids for tiny context-limited agents better than rolling context or naive note retrieval.

## Why it stopped

Closed as no-paper useful signal because the mechanism was supported only under synthetic perfect-extraction assumptions, not real local-agent operation.

## Recommended next action

Run a bounded end-to-end follow-up where a small local model extracts ledger entries from natural-language notes and is compared against rolling-context and retrieval baselines on the same value+source metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language extraction test for evidence-ledger tiny agents
- Success threshold: Ledger agent improves value+source accuracy by at least 0.20 over the best baseline and reduces unsupported citation rate by at least 0.10 absolute across at least 200 randomized trials.
- Stop condition: Stop if extraction F1 is below 0.80 or if ledger value+source accuracy fails to beat the best baseline by 0.05 in an initial 50-trial smoke run.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-local-agents-2b587e5d0911`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
