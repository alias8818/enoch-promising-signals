# EvidenceLedgerToolHallucination

Status: `useful_signal`
Project ID: `evidenceledgertoolhallucination-68bf0a21e3b8`
Run ID: `evidenceledgertoolhallucination-68bf0a21e3b8-20260519T011914011258+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fce03dab0611

## What looked useful

Across five 2,000-case seeds, citation-only rejected a mean 25.36% of unsupported claims, exact ledger 70.14%, and normalized ledger 98.84%, all with 100% supported-claim recall in this synthetic distribution.

## Boundaries and scale limits

Synthetic claims only; no live LLM generations, real tool APIs, human labels, retrieval noise, or production traces. The verifier is lexical/structured and hand-built for the benchmark templates.

## Claim scope

On a seeded synthetic benchmark of structured tool observations and controlled answer claims, a normalized evidence-ledger verifier rejected unsupported tool-output claims much more often than a citation-presence baseline while preserving supported-claim recall.

## Why it stopped

No-paper closure: this is useful synthetic verifier evidence, not direct live-agent evidence or publication-grade validation.

## Recommended next action

Run a bounded live LLM trace experiment comparing ungated, citation-only, and evidence-ledger-gated agents on labeled tool-grounded QA tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Tool-Trace Evidence Ledger Hallucination Test
- Success threshold: Evidence-ledger-gated variant reduces unsupported claim rate by at least 50% relative to citation-only while keeping supported-claim recall at or above 90% on at least 200 labeled live-model claims.
- Stop condition: Stop if the ledger gate fails to reduce unsupported claims by at least 25% relative to citation-only or if supported-claim recall falls below 80%.

## Evidence references

- Artifact root: `<local-path>/projects/evidenceledgertoolhallucination-68bf0a21e3b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
