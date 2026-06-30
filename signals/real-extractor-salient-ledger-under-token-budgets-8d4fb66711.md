# Real-Extractor Salient Ledger Under Token Budgets

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-extractor-salient-ledger-under-token-budgets-8d4fb66711`
Run ID: `real-extractor-salient-ledger-under-token-budgets-8d4fb66711-20260527T015702524305+0000`

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

- Parent run decision: Sliding Salient-Fact Ledger for Low-RAM Agents: enoch://control-plane/projects/sliding-salient-fact-ledger-for-low-ram-agents-790357fc211c/runs/sliding-salient-fact-ledger-for-low-ram-agents-790357fc211c-20260524T205150219526+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

The salient ledger improved mean F1 over the best non-ledger control by +0.2508 at 120 tokens, +0.2944 at 180 tokens, +0.3232 at 220 tokens, and +0.2997 at 250 tokens; it reached exact recovery once the compact ledger fit in budget.

## Boundaries and scale limits

80 generated documents, 120 records per document, 16 salient records per document; exact structured extractor; word-token budgets; no real PDFs, OCR noise, ambiguous salience labels, tokenizer-specific accounting, or LLM extraction variability.

## Claim scope

In a controlled generated ledger-document benchmark with explicit salience markers, a compact salient-ledger intermediate representation preserved more salient transaction facts under 120-250 word-token budgets than prefix truncation, prefix/suffix windows, or paragraph salience retrieval.

## Why it stopped

Tier 1 controlled direct test completed; mechanism supported locally, but evidence is synthetic and not publication-grade.

## Recommended next action

Run a bounded deepen test on real public financial or audit-style documents with implicit salience and a real LLM or trained IE extractor before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Document Salient Ledger Extraction Under Fixed LLM Context Budgets
- Success threshold: Mean F1 improvement of at least +0.10 over the best non-ledger control at one or more budgets below 30 percent of the full document length, with no precision drop below 0.95.
- Stop condition: Stop if the ledger extraction step fails to identify salient records with at least 0.90 recall on the validation set or if the best retrieval control matches ledger F1 within 0.03 at all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/real-extractor-salient-ledger-under-token-budgets-8d4fb66711`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
