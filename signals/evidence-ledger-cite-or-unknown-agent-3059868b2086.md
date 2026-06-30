# Evidence-Ledger Cite-or-Unknown Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-cite-or-unknown-agent-3059868b2086`
Run ID: `evidence-ledger-cite-or-unknown-agent-3059868b2086-20260611T051059463964+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb94e1342f57

## What looked useful

The ledger mechanism eliminated unsupported answers in the toy benchmark by abstaining on unsupported or unmatched evidence, improving overall accuracy from 0.389 to 0.833 at the cost of answering only 7 of 18 questions.

## Boundaries and scale limits

Synthetic data, small corpus, lexical retrieval, rule-based extraction, no real LLM generation, no public benchmark, and threshold selected on the same benchmark; not publication-grade broad validation.

## Claim scope

On a deterministic synthetic QA harness with 7 documents and 18 questions, an evidence-ledger cite-or-unknown policy reduced unsupported answer rate from 0.611 for a naive always-answer retriever to 0.000 while preserving 0.700 answerable accuracy.

## Why it stopped

Useful bounded synthetic signal, but not paper-ready because the run is proxy-only and does not validate behavior with real LLM generation or realistic retrieval.

## Recommended next action

Run a bounded deepen follow-up on a public unanswerable-QA benchmark with a real LLM/retriever wrapped by the same evidence-ledger contract and audit citations against gold support.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public QA validation of evidence-ledger cite-or-unknown behavior
- Success threshold: Unsupported answer rate at least 50% lower than baseline and no more than 25% relative loss in answerable accuracy on the evaluated subset.
- Stop condition: Stop if unsupported answer rate is not materially reduced, or if answerable accuracy drops below half of the baseline on the same evaluated subset.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-cite-or-unknown-agent-3059868b2086`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
