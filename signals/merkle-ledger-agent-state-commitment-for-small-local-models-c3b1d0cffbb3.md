# Merkle-ledger agent state commitment for small local models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-ledger-agent-state-commitment-for-small-local-models-c3b1d0cffbb3`
Run ID: `merkle-ledger-agent-state-commitment-for-small-local-models-c3b1d0cffbb3-20260604T073333905585+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a88e0eff45b3

## What looked useful

The mechanism is feasible and cheap at toy/local protocol scale, but external final-head anchoring is required to detect valid-prefix truncation. The result is useful engineering evidence rather than a paper-ready validation.

## Boundaries and scale limits

Synthetic state only; no real local LLM agent integration, no crash recovery, no multi-writer concurrency, no persistent private blob store, no adversarial replay campaign, and no long-running production trace.

## Claim scope

A stdlib Python prototype using canonical JSON, Merkle roots over top-level agent-state fields, and a hash-chained ledger detected state, metadata, deletion, reorder, and anchored truncation tampering on synthetic small-agent snapshots while keeping median commit latency below 0.4 ms for tested states up to about 77 KiB.

## Why it stopped

Synthetic protocol benchmark supports feasibility but is not direct/full validation of deployed small local model agents.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate the ledger into a real small local model agent loop with persisted state blobs and crash/replay tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-agent Merkle ledger persistence and replay test
- Success threshold: Median commit latency below 5 ms and p95 below 20 ms for real agent states, verification below 2 ms per step, and detection of all injected tampering scenarios except explicitly unanchored valid-prefix truncation.
- Stop condition: Stop if real-agent integration exceeds 5 ms median commit latency, misses any anchored tamper scenario, or requires non-local infrastructure to produce the evidence.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-ledger-agent-state-commitment-for-small-local-models-c3b1d0cffbb3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
