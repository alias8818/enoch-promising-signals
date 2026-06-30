# Evidence Ledger Verification on Model-Generated Tool Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-verification-on-model-generated-tool-trace-42876f124a`
Run ID: `evidence-ledger-verification-on-model-generated-tool-trace-42876f124a-20260531T145301427186+0000`

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

- Parent run decision: Falsifiable Evidence Ledger for Tool-Calling Agents: enoch://control-plane/projects/falsifiable-evidence-ledger-for-tool-calling-agents-c3266a94073e/runs/falsifiable-evidence-ledger-for-tool-calling-agents-c3266a94073e-20260531T113313505965+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d4231f33a1c

## What looked useful

Field-level evidence ledger checks caught 94/94 corrupted ledgers with 0/1 valid-ledger false rejects, while a citation-only baseline accepted 62 invalid cases.

## Boundaries and scale limits

Single small trace, deterministic ledger construction, synthetic corruptions, explicit field/string/regex checks only; no large corpus, natural hallucination sample, human adjudication, or semantic entailment validation.

## Claim scope

On one live Codex model/tool JSONL trace, a deterministic field-level evidence ledger verifier accepted the valid trace ledger and rejected synthetic event-id, field, value, and no-evidence corruptions, outperforming a citation-only baseline.

## Why it stopped

Tier 1 direct test supports the mechanism but remains too small and partly synthetic for publication readiness.

## Recommended next action

Run a bounded deepen test on 10-20 independent model/tool traces with model-authored summaries converted into ledgers and human labels for ambiguous claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent Trace Corpus Test for Evidence Ledger Verification
- Success threshold: At least 95% invalid detection recall, at least 95% valid acceptance, and at least 30 percentage point invalid-recall improvement over citation-only baseline.
- Stop condition: Stop if the verifier accepts more than 10% of invalid claims or rejects more than 10% of valid claims on the independent trace corpus.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-verification-on-model-generated-tool-trace-42876f124a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
