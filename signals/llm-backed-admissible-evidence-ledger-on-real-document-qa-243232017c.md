# LLM-backed admissible evidence ledger on real-document QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-backed-admissible-evidence-ledger-on-real-document-qa-243232017c`
Run ID: `llm-backed-admissible-evidence-ledger-on-real-document-qa-243232017c-20260523T065904642730+0000`

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

- Parent run decision: Constrained Evidence Ledger Agent: enoch://control-plane/projects/constrained-evidence-ledger-agent-5664a4c79317/runs/constrained-evidence-ledger-agent-5664a4c79317-20260523T045104370199+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb1f540afb65

## What looked useful

A provenance-only evidence ledger can record verifiable source hashes, offsets, and quotes, but this is not enough for answer admissibility: at min score 0.15 it falsely admitted 2/3 unsupported answers and only answered 1/6 supported questions correctly. Raising the score threshold to 0.50 eliminated unsupported false admissions on this tiny task but still left supported accuracy at 1/6, showing that confidence gating alone is not a viable paper-ready mechanism.

## Boundaries and scale limits

Small public-web sample only; no legal admissibility review, no human entailment labels beyond fixed expected answers, no scanned/OCR documents, no multi-hop questions, no production LLM, and no semantic verifier because the attempted local NLI model load exceeded the short-run budget.

## Claim scope

Tier 1 controlled small direct test: 3 public real web documents, 9 document questions, local extractive QA, top-3 chunk retrieval, and deterministic source-hash/offset/quote evidence-ledger admission.

## Why it stopped

Direct Tier 1 evidence was useful but no-paper: provenance-only ledger admissibility failed semantically, and threshold gating recovered unsupported abstention only by preserving very low supported-answer accuracy.

## Recommended next action

Do not write a paper from this run; run one bounded deepen test that adds semantic support verification over question-answer-quote triples and compares against the saved provenance-only threshold baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic support verifier for admissible evidence ledgers on real-document QA
- Success threshold: Semantic-verifier ledger achieves at least 70% supported-answer accuracy with 0 unsupported false admissions on the bounded real-document test, and beats the saved provenance-only threshold baseline by at least 30 percentage points in supported accuracy at the same false-admission rate.
- Stop condition: Stop as negative if semantic verification either admits any unsupported answer or fails to exceed 50% supported-answer accuracy on the bounded 20-question direct test.

## Evidence references

- Artifact root: `<local-path>/projects/llm-backed-admissible-evidence-ledger-on-real-document-qa-243232017c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
