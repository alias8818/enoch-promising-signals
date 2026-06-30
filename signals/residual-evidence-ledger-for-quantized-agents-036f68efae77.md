# Residual Evidence Ledger for Quantized Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-evidence-ledger-for-quantized-agents-036f68efae77`
Run ID: `residual-evidence-ledger-for-quantized-agents-036f68efae77-20260604T152151998686+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/52d33b61574f

## What looked useful

Residual ledgers reduced MSE by 56.36% versus deterministic quantization in the medium run, but were 7.03% worse than stochastic rounding. In a clip sweep, ledgers were 6199% worse than naive at 28.37% saturation, but about 91% better than stochastic rounding when saturation was near zero.

## Boundaries and scale limits

Tested only synthetic numeric agents on convex stationary objectives: up to 8 seeds, 2048 runs per seed, 32 agents, 128 dimensions, and 240 steps on one GB10. Not tested on LLM agents, semantic evidence, tool-use traces, nonstationary tasks, or production quantization stacks.

## Claim scope

In a synthetic repeated multi-agent quadratic optimization loop with 3-bit quantized numeric messages, a per-agent residual evidence ledger improves final MSE when quantizer saturation is near zero, but can underperform or catastrophically fail when clipping prevents residual evidence from being transmitted.

## Why it stopped

The evidence is a bounded synthetic proxy with mixed support: it identifies a real low-saturation mechanism and a clear saturation failure mode, but does not validate residual ledgers for quantized LLM agents.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test residual clipping/decay or adaptive quantizer range on a bounded real-agent trace benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Saturation-Controlled Residual Ledgers on Small Agent Traces
- Success threshold: A saturation-controlled ledger beats stochastic rounding by at least 10% on the primary task metric across at least 5 seeds while keeping catastrophic saturated-regime failures absent.
- Stop condition: Stop if saturation-controlled ledgers do not beat stochastic rounding on the primary metric or if residual diagnostics show recurring instability under realistic trace distributions.

## Evidence references

- Artifact root: `<local-path>/projects/residual-evidence-ledger-for-quantized-agents-036f68efae77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
