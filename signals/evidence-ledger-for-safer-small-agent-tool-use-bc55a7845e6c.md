# Evidence Ledger for Safer Small Agent Tool Use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-safer-small-agent-tool-use-bc55a7845e6c`
Run ID: `evidence-ledger-for-safer-small-agent-tool-use-bc55a7845e6c-20260531T122543662609+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9589fd5d43ed

## What looked useful

The evidence ledger k=2 gate reduced unsafe risky executions from 9.67% to 0.63% versus the prompt-weighted baseline, a 93.53% reduction, but authorized risky completion fell from 78.72% to 35.31%, missing the 80% utility threshold. Across the stress sweep, k=2 kept at least 90.98% unsafe reduction but never exceeded 51.72% authorized completion.

## Boundaries and scale limits

Synthetic hand-coded scenarios and policies only; no real LLM agent, human labels, live tools, production traces, or field deployment. Main evidence is 20,000 generated scenarios plus a 9-cell stress sweep of 10,000 scenarios per cell.

## Claim scope

In a deterministic synthetic benchmark of noisy authorization evidence for small-agent risky tool calls, a two-independent-trusted-source evidence ledger sharply reduced unauthorized risky executions but failed to preserve authorized risky-tool utility.

## Why it stopped

The pre-registered combined threshold failed in a proxy synthetic test: safety improved strongly, but authorized risky completion was far below target, so this is an early scoped falsification of the simple k=2 ledger gate rather than full validation.

## Recommended next action

Stop this run as no-paper useful synthetic evidence; run one bounded follow-up using actual small-LLM tool-use traces to test adaptive risk-tiered evidence-ledger gates against the same safety and utility metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Risk-Tiered Evidence Ledgers on Small-LLM Tool-Use Traces
- Success threshold: Adaptive ledger reduces unauthorized risky executions by at least 70% versus the small-LLM baseline while preserving at least 75% authorized risky completion, with confidence intervals excluding a trivial improvement.
- Stop condition: Stop if adaptive gating cannot exceed 60% authorized risky completion at the required safety reduction, or if source extraction from traces is too unreliable to support evidence-ledger decisions.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-safer-small-agent-tool-use-bc55a7845e6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
