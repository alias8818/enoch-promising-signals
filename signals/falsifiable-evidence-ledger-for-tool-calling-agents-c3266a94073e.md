# Falsifiable Evidence Ledger for Tool-Calling Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-for-tool-calling-agents-c3266a94073e`
Run ID: `falsifiable-evidence-ledger-for-tool-calling-agents-c3266a94073e-20260531T113313505965+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d4231f33a1c

## What looked useful

Across a 10,000-case main run, ledger verification achieved 1.000 accuracy versus 0.894 for the stronger key-value transcript baseline and 0.680 for value-only matching; five additional 5,000-case seeds showed ledger accuracy delta over key-value matching between +0.0998 and +0.1098.

## Boundaries and scale limits

Evidence is synthetic and mechanism-level only. It does not validate real LLM tool-calling behavior, natural-language claim extraction, noisy tool outputs, adversarial agents, or user-facing task outcomes.

## Claim scope

On generated tool-calling traces with typed observations, explicit evidence references, and hash-chained ledger entries, a structured evidence-ledger verifier detected unsupported, contradicted, misattributed, and tampered claims more accurately than transcript-only string baselines.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only on synthetic traces generated from the verifier's own formal assumptions.

## Recommended next action

Run a bounded deepen test on real or model-generated tool-calling traces with independently labeled grounding errors and a stronger transcript/NLI baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger Verification on Model-Generated Tool Traces
- Success threshold: Ledger verifier improves invalid-claim detection precision or specificity by at least 20 percentage points over the strongest transcript baseline while maintaining at least 95% recall on valid claims.
- Stop condition: Stop if structured claims cannot be extracted with at least 90% parse success, if independent labels show no recurring evidence-reference failures, or if the ledger fails to outperform the strongest baseline by at least 5 percentage points on a 100-trace pilot.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-for-tool-calling-agents-c3266a94073e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
