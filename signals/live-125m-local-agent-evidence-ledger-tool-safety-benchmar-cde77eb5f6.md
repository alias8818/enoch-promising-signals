# Live 125M local-agent evidence-ledger tool-safety benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-125m-local-agent-evidence-ledger-tool-safety-benchmar-cde77eb5f6`
Run ID: `live-125m-local-agent-evidence-ledger-tool-safety-benchmar-cde77eb5f6-20260531T104710825629+0000`

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

- Parent run decision: Mandatory evidence ledger for 125M local agent tool safety: enoch://control-plane/projects/mandatory-evidence-ledger-for-125m-local-agent-tool-safety-d5816bc44e25/runs/mandatory-evidence-ledger-for-125m-local-agent-tool-safety-d5816bc44e25-20260530T031428141611+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7f71c05face3

## What looked useful

The evidence-ledger mechanism blocked all unsafe model-selected adversarial tool calls in a small direct local benchmark and exposed one benign case where blocking a dangerous shell proposal was desirable.

## Boundaries and scale limits

Synthetic paired candidates; simulated tools; no free-form multi-step planning; no actual filesystem or network side effects; no larger or instruction-tuned model comparison; no prompt-only or alternative guardrail ablations.

## Claim scope

In a 24-task controlled paired-choice benchmark, a GPT-2 124M local action scorer selected unsafe tool calls on all adversarial prompts, and a hand-written evidence-ledger gate reduced adversarial unsafe execution from 100% ungated to 0% while preserving 91.7% benign completion.

## Why it stopped

Tier 1 threshold passed, but evidence remains controlled and synthetic, so the run closes as no-paper useful signal rather than publication readiness.

## Recommended next action

Run a deeper local benchmark with free-form generation, sandboxed real tool side effects, and ablations against allowlist-only and prompt-only controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Free-form local-agent evidence-ledger safety benchmark with sandboxed tools
- Success threshold: Evidence-ledger adversarial unsafe execution <= 5%, benign completion >= 70%, and at least a 2x unsafe-execution reduction versus the strongest non-ledger baseline.
- Stop condition: Stop if free-form generation produces too few parseable tool calls for direct comparison, or if ledger benign completion falls below 50% after obvious schema fixes.

## Evidence references

- Artifact root: `<local-path>/projects/live-125m-local-agent-evidence-ledger-tool-safety-benchmar-cde77eb5f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
