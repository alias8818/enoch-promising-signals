# Structured Evidence Ledger vs Bare Scratchpad on Agent Decision Reliability

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `structured-evidence-ledger-vs-bare-scratchpad-on-agent-decision-reliability-0392e22d82b4`
Run ID: `structured-evidence-ledger-vs-bare-scratchpad-on-agent-decision-reliability-0392e22d82b4-20260620T221734250908+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/330adaeef2cf

## What looked useful

A ledger-shaped prompt is not by itself a reliability mechanism. In the compact condition, ledger accuracy was 44% vs 63% for bare scratchpad over 100 paired cases; in an explicit emitted-ledger condition, ledger accuracy was 40% vs 42% over 50 paired cases and had more invalid outputs.

## Boundaries and scale limits

Local proxy only: one small instruction model, synthetic evidence packets, greedy decoding, no real agent tool traces, no human/private evidence, no larger-model robustness sweep.

## Claim scope

On a synthetic four-record evidence-selection benchmark using Qwen2.5-1.5B-Instruct, prompt-only structured evidence ledger scaffolds did not improve decision accuracy over a bare scratchpad and sometimes degraded it.

## Why it stopped

Proxy/local early falsification: prompt-only structured ledger scaffolding did not improve reliability in the tested setting, so the broad hypothesis is unsupported by this evidence.

## Recommended next action

Stop this run as no-paper useful negative evidence; the next bounded test should add mechanical ledger validation and compare against the same bare scratchpad on a stronger local model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validated Evidence Ledger vs Prompt-Only Ledger on Controlled Agent Decisions
- Success threshold: Validated ledger beats bare scratchpad by at least 10 percentage points in paired accuracy, reduces invalid outputs, and passes ledger-row validity checks on at least 95% of cases.
- Stop condition: Stop if validated ledger does not beat bare scratchpad by at least 5 percentage points on the synthetic set or if ledger-row validity remains below 90%.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-vs-bare-scratchpad-on-agent-decision-reliability-0392e22d82b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
