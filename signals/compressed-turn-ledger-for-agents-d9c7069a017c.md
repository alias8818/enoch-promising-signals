# Compressed Turn Ledger for Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-turn-ledger-for-agents-d9c7069a017c`
Run ID: `compressed-turn-ledger-for-agents-d9c7069a017c-20260604T101014466444+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2322373383a0

## What looked useful

Exact replay held in all 60 matrix runs. Ledger compression was mixed against gzip: low-reuse small observations lost in 10/10 runs with mean ratio 1.1398, while medium/high reuse large observations won in 20/20 runs with mean ratios 0.6821 and 0.4353.

## Boundaries and scale limits

Synthetic traces only; 60 CPU-only benchmark runs; no real agent logs, production runtime overhead, retrieval quality, privacy/security analysis, or long-horizon operational validation.

## Claim scope

On deterministic synthetic agent traces, a content-addressed turn ledger preserves exact replay and beats gzipped raw JSON only when traces contain medium/high reuse of large observations or workspace snapshots.

## Why it stopped

Bounded synthetic evidence supports a conditional mechanism but is not direct evidence on real agent workloads and is mixed against the gzip control.

## Recommended next action

Run the same replay and compression benchmark on real or archived agent traces before considering a paper; this run should stop as a synthetic useful signal, not a validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Validation for Content-Addressed Agent Turn Ledgers
- Success threshold: Across at least 100 real traces, exact replay succeeds for all traces and median gzipped ledger size is at least 20% smaller than gzipped raw JSON without more than 10% median replay-time overhead.
- Stop condition: Stop if exact replay fails on any valid trace class or if median gzipped ledger size is not at least 10% smaller than gzipped raw JSON after format tuning.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-turn-ledger-for-agents-d9c7069a017c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
