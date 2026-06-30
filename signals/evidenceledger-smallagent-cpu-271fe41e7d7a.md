# EvidenceLedger_SmallAgent_CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidenceledger-smallagent-cpu-271fe41e7d7a`
Run ID: `evidenceledger-smallagent-cpu-271fe41e7d7a-20260603T211251123169+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7dfe5b51a415

## What looked useful

The strongest control with full context but no conflict ledger reached 0.75 accuracy and 0.0 conflict detection; the evidence ledger reached 1.0 accuracy, 1.0 conflict detection, 0.0 unsupported answer rate, and 1.0 citation precision in 0.27 seconds wall-clock with about 20 MB RSS.

## Boundaries and scale limits

The run used 320 synthetic tasks and standard-library heuristic agents on one CPU process. It did not test a real LLM, real corpora, noisy extraction, adversarial paraphrase, large retrieval indexes, human citation judgments, or production latency.

## Claim scope

In a deterministic synthetic document-grounded QA harness with short structured records, an explicit evidence ledger that accumulates all subject-field evidence before answering eliminated unsupported answers and correctly abstained on all missing/conflicting evidence cases, outperforming retrieval-only and no-conflict controls.

## Why it stopped

Closed as a no-paper useful signal: the synthetic benchmark supports the mechanism but is not direct enough for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up using a small local LLM or semi-real QA corpus where evidence ledger entries must be extracted from noisy text, then compare against the same context without explicit ledger conflict accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: EvidenceLedger with Noisy Extraction on Semi-Real QA
- Success threshold: At least 50% relative reduction in unsupported conflict answers versus same-context no-ledger control, citation precision at least 0.9, and answerable accuracy drop no more than 5 percentage points.
- Stop condition: Stop if noisy extraction drives citation precision below 0.75 or answerable accuracy drops more than 10 percentage points relative to the no-ledger control.

## Evidence references

- Artifact root: `<local-path>/projects/evidenceledger-smallagent-cpu-271fe41e7d7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
