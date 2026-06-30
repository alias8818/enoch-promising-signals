# Evidence-Ledger Hallucination Detection in Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-hallucination-detection-in-small-agents-535a284e7eb7`
Run ID: `evidence-ledger-hallucination-detection-in-small-agents-535a284e7eb7-20260525T074151333631+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a3a61c76de48

## What looked useful

Evidence ledgers are useful when the detector validates citation identity, structured claim triples, and rendered-answer consistency. Simple citation or value-overlap checks miss fabricated-subject and answer-ledger-mismatch cases in this benchmark.

## Boundaries and scale limits

Synthetic-only evidence; no LLM-generated traces, human labels, open-domain retrieval, paraphrase stress test, or large-scale deployment evidence. The verifier and generator share a schema, so this is a mechanism probe rather than external validation.

## Claim scope

In a deterministic synthetic benchmark of 1,200 small-agent traces with structured claim ledgers and known evidence IDs, a ledger verifier detected missing citations, wrong values, irrelevant citations, fabricated subjects, and answer-ledger mismatches better than citation-presence, lexical, and cited-value baselines.

## Why it stopped

Synthetic mechanism evidence supports the idea locally, but direct real-agent evidence is required before any paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to evaluate the same verifier on a labeled set of real small-agent traces with claim-level ledgers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Agent Evidence-Ledger Hallucination Benchmark
- Success threshold: Ledger verifier improves F1 by at least 0.10 over the strongest non-ledger baseline while maintaining precision at or above 0.90 on real traces.
- Stop condition: Stop if real traces lack reliable claim-level ledgers or if the ledger verifier fails to beat the strongest baseline by 0.05 F1 on the first 200 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-hallucination-detection-in-small-agents-535a284e7eb7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
