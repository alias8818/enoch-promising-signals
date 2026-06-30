# Evaluate evidence-ledger gating on real LLM tool-call traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evaluate-evidence-ledger-gating-on-real-llm-tool-call-trac-500abf7944`
Run ID: `evaluate-evidence-ledger-gating-on-real-llm-tool-call-trac-500abf7944-20260607T093335233583+0000`

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

- Parent run decision: Tiny CPU Agent Evidence Ledger Reduces Hallucinated Actions: enoch://control-plane/projects/tiny-cpu-agent-evidence-ledger-reduces-hallucinated-actions-f7ae507e1f49/runs/tiny-cpu-agent-evidence-ledger-reduces-hallucinated-actions-f7ae507e1f49-20260607T070235512360+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/af1f0231b993

## What looked useful

Structured key/value evidence gating disambiguated field identity in real tool outputs and prevented same-output numeric false accepts that raw substring evidence could not prevent.

## Boundaries and scale limits

Numeric claims only; regex extractor; local Enoch/Codex trace corpus; controlled counterfactual swaps rather than naturally occurring unsupported claims; no broad scientific claim validation.

## Claim scope

On 100 deterministic local real Codex/Enoch tool-call traces, a structured evidence-ledger gate for numeric metric/resource claims accepted 33/34 natural claims and rejected 33/33 same-output counterfactual numeric swaps, while a substring gate false-accepted 33/33 swaps.

## Why it stopped

Tier 1 direct test passed for the scoped mechanism, but evidence is too narrow for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a frozen held-out corpus with blind labels for naturally unsupported numeric and nonnumeric claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blind held-out evidence-ledger gating on natural unsupported tool-trace claims
- Success threshold: At least 100 labeled claims, ledger false accept rate at least 50 percentage points lower than substring baseline, supported-claim accept rate at least 90%, and extractor miss rate reported separately.
- Stop condition: Stop if fewer than 100 labeled natural claims can be obtained locally, if supported-claim accept rate falls below 80%, or if false accept reduction versus substring is below 25 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evaluate-evidence-ledger-gating-on-real-llm-tool-call-trac-500abf7944`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
