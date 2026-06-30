# Evidence-Ledger Agent: Falsifiable Claims with Counterexample Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-falsifiable-claims-with-counterexample-traces-b42178741090`
Run ID: `evidence-ledger-agent-falsifiable-claims-with-counterexample-traces-b42178741090-20260621T012643812159+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d322eaea04a2

## What looked useful

The evidence-ledger verifier achieved 1.0 exact verdict accuracy and 1.0 counterexample trace recall on the deterministic fixture, while citation-only gating falsely accepted 5 of 7 non-supported claims.

## Boundaries and scale limits

No real LLM/tool traces, no natural-language claim extraction, no retrieval completeness test, no adversarial robustness suite, and no large-scale benchmark.

## Claim scope

Structured synthetic evidence-ledger claims with explicit subject/predicate/comparator/value fields; 10 claims and 10 evidence records; citation-only baseline versus ledger counterexample checking.

## Why it stopped

Closed as no-paper useful signal: the result is synthetic structured-ledger evidence for the mechanism, not direct publication-grade validation on real agent traces.

## Recommended next action

Run a bounded deepen follow-up on recorded tool-agent traces with manually audited claim/evidence labels and retrieval completeness controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger counterexample traces on recorded tool-agent tasks
- Success threshold: Evidence-ledger false accept rate on non-supported claims at least 50 percent lower than citation-only gating, counterexample trace recall at least 0.8 on refuted claims, and supported-claim false reject rate no worse than 0.1.
- Stop condition: Stop if structured evidence cannot be audited for the trace set, or if ledger false accepts are not lower than citation-only false accepts on the first 50 audited claims.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-falsifiable-claims-with-counterexample-traces-b42178741090`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
