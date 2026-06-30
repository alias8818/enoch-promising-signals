# Structured Evidence Ledgers for Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `structured-evidence-ledgers-for-small-agents-7039f9293ac1`
Run ID: `structured-evidence-ledgers-for-small-agents-7039f9293ac1-20260607T085910002618+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14562d0f635d

## What looked useful

Structured claim-keyed compression produced large accuracy gains over unstructured bounded buffers, but source/provenance weighting added little when metadata was aligned and hurt badly when source reliability was adversarially inverted.

## Boundaries and scale limits

Synthetic/proxy-only evidence; no real LLM parsing, natural-language extraction, retrieval errors, tool-use side effects, or open-domain datasets were tested. The run used 5,000 tasks per condition and completed locally in about 23 seconds.

## Claim scope

In a deterministic synthetic evidence-stream benchmark with 64 snippets per task, 65% distractors, contradiction rates from 0.2 to 0.6, and memory budgets of 4, 8, or 16 entries, claim-keyed structured ledgers substantially outperformed unstructured recency and majority buffers for small context-limited agents.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy; it supports the ledger-compression mechanism but does not validate real small agents or publication-grade claims.

## Recommended next action

Run a bounded real-agent follow-up where a small LLM extracts ledger entries from natural-language evidence streams, with identical token budgets for ledger and scratchpad baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy LLM Extraction Test for Structured Evidence Ledgers
- Success threshold: Ledger agent improves answer accuracy by at least 10 percentage points over the strongest unstructured baseline while maintaining citation precision of at least 0.85 across at least 1,000 natural-language tasks.
- Stop condition: Stop if extraction precision falls below 0.70 or if the ledger advantage over the strongest unstructured baseline is under 3 percentage points after 1,000 tasks.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledgers-for-small-agents-7039f9293ac1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
