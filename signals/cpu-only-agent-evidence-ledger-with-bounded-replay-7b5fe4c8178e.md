# CPU-Only Agent Evidence Ledger with Bounded Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-only-agent-evidence-ledger-with-bounded-replay-7b5fe4c8178e`
Run ID: `cpu-only-agent-evidence-ledger-with-bounded-replay-7b5fe4c8178e-20260605T102444602388+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/92a46d25a542

## What looked useful

Dependency-indexed evidence ledgers can make scoped claim audits much cheaper than full trace replay in sparse-to-moderate synthetic traces: 486/486 relevant corruptions detected, 486/486 unrelated corruptions ignored by scoped replay, mean bounded fraction 0.0697, mean speedup 28.33x.

## Boundaries and scale limits

Synthetic traces only; no real LLM/tool trajectories, no nondeterministic replay, no external hash-root anchoring test, no adversary capable of consistent ledger rewrite, and no comparison to production provenance systems.

## Claim scope

On deterministic synthetic CPU-only agent traces up to 4096 events, ancestor-cone bounded replay for audited claims detected every injected payload corruption inside the claim proof chain while replaying a mean 6.97% of events.

## Why it stopped

The result supports the bounded replay mechanism on a synthetic proxy, but it is not direct/full validation for real agent evidence ledgers.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay real recorded agent/tool trajectories with externally anchored ledger roots.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace Evidence Ledger with Anchored Bounded Replay
- Success threshold: At least 99% detection of in-chain injected tampering, zero accepted external-root mismatches, median bounded replay fraction under 25%, and no more than 1 scoped false miss across the replay corpus.
- Stop condition: Stop as negative if externally anchored bounded replay misses more than 1 in-chain corruption, if median replay fraction exceeds 50%, or if real tool nondeterminism prevents reproducible replay without manual intervention.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-only-agent-evidence-ledger-with-bounded-replay-7b5fe4c8178e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
