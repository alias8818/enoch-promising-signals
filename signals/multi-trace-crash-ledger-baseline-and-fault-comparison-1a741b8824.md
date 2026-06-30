# Multi-trace crash ledger baseline and fault comparison

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-trace-crash-ledger-baseline-and-fault-comparison-1a741b8824`
Run ID: `multi-trace-crash-ledger-baseline-and-fault-comparison-1a741b8824-20260608T011112891262+0000`

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

- Parent run decision: Real-trace crash-safe evidence ledger for small agents: enoch://control-plane/projects/real-trace-crash-safe-evidence-ledger-for-small-agents-f0bf7440ee/runs/real-trace-crash-safe-evidence-ledger-for-small-agents-f0bf7440ee-20260607T190405353783+0000
- Parent run decision: Cryptographic Evidence Ledger for Small Agents: enoch://control-plane/projects/cryptographic-evidence-ledger-for-small-agents-f8f165d73c81/runs/cryptographic-evidence-ledger-for-small-agents-f8f165d73c81-20260607T135205367284+0000

## What looked useful

Multi-trace anomaly normalization appears useful under low fault prevalence and high noise, but the full downstream-transition discount is harmful in the stress condition. The no-transition ablation reached top1 0.869 and MRR 0.933 versus full ledger top1 0.619 and MRR 0.807, and versus frequency baseline top1 0.478 and MRR 0.728.

## Boundaries and scale limits

Synthetic traces only; no production incident traces, real topology, real crash dumps, deployed overhead measurement, or comparison against mature observability/RCA systems. CPU-only local evaluation, 360 cases per medium condition.

## Claim scope

On deterministic synthetic multi-trace crash-localization workloads with 240 traces per case, 5 fixed seeds, 24 replicates per seed, and crash/timeout/resource faults, the full multi-trace crash ledger does not improve over a simple frequency baseline in standard or moderately confounded settings. Under a harder low-fault/high-noise confounded stress setting, it improves over frequency ranking but is outperformed by its own no-transition-discount ablation.

## Why it stopped

Tier 2 synthetic evidence is mixed: the full method ties trivial baselines in medium standard/confounded tests and is worse than a simpler ablation in the stress test, so this is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Stop paper progression for the full ledger; run a bounded deepen follow-up focused on the no-transition anomaly-normalized variant against real or benchmark incident traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: No-transition anomaly-normalized crash ledger on benchmark incident traces
- Success threshold: No-transition anomaly-normalized ledger improves MRR by at least 0.05 and top1 by at least 0.05 over the best non-ledger baseline with paired 95% confidence intervals excluding zero, while keeping overhead below 2x the frequency baseline.
- Stop condition: Stop if the variant fails to beat the best baseline on MRR/top1, if confidence intervals include zero on the primary metric, or if overhead exceeds 2x without a compensating accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-crash-ledger-baseline-and-fault-comparison-1a741b8824`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
