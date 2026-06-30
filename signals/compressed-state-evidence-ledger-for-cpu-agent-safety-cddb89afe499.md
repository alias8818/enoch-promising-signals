# Compressed State Evidence Ledger for CPU Agent Safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-evidence-ledger-for-cpu-agent-safety-cddb89afe499`
Run ID: `compressed-state-evidence-ledger-for-cpu-agent-safety-cddb89afe499-20260529T143610646387+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/770071bce95e

## What looked useful

The mechanism is locally viable as a compact audit substrate: 50,000 synthetic events compressed from 9,288,970 bytes to 515,613 bytes in the smallest tested configuration, retained 1.0 audit-term recall and 1.0 red-flag recall, and detected 250/250 random trace tampering trials. A decoy-query stress pass over 10,000 events and 256 absent probes measured near-zero Bloom false positives while retaining 13-18x compression.

## Boundaries and scale limits

Synthetic traces only; trusted ledger writer; no production agent traces, independent human labels, adversarial ledger-suppression model, reviewer workload study, or comparison against deployed agent observability systems.

## Claim scope

On deterministic synthetic CPU-agent event streams up to 50,000 events, a per-window compressed evidence ledger with counts, Bloom audit terms, red-flag stubs, event digest roots, and a hash chain preserved configured audit-term recall and red-flag recall while reducing retained JSON state by roughly 13-18x and detecting all tested presented-trace tampering.

## Why it stopped

No-paper useful signal: this is synthetic/proxy evidence for the ledger mechanism, not full validation of CPU-agent safety or adversarial robustness.

## Recommended next action

Run a bounded real-trace replay study with independently labeled safety incidents and compare incident-window recall plus reviewer workload against full logs and naive summaries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay evaluation for compressed agent evidence ledgers
- Success threshold: At least 0.98 incident-window recall, at least 8x retained-state reduction, no undetected presented-trace tampering in 500 trials, and lower median reviewer bytes inspected than full-log review.
- Stop condition: Stop as negative if real-trace incident-window recall is below 0.95, retained-state reduction is below 4x, or out-of-process persistence cannot detect ledger suppression/tampering in the bounded setup.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-evidence-ledger-for-cpu-agent-safety-cddb89afe499`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
