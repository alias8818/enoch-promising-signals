# Trace-Based Consensus Ledger Evaluation for Smart-Home Agent Actions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-based-consensus-ledger-evaluation-for-smart-home-age-f8054ed932`
Run ID: `trace-based-consensus-ledger-evaluation-for-smart-home-age-f8054ed932-20260526T172301271866+0000`

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

- Parent run decision: Multi-Agent Consensus Ledger for Safe Home Actions: enoch://control-plane/projects/multi-agent-consensus-ledger-for-safe-home-actions-1cd7ecb2bf47/runs/multi-agent-consensus-ledger-for-safe-home-actions-1cd7ecb2bf47-20260525T203351264325+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/abf77b336ae1

## What looked useful

The mechanism is locally viable: compared with a single-agent direct-commit baseline that averaged 39 unsafe commits per 200-action run, the consensus ledger committed zero unsafe actions and kept safe-action false rejection below the 10% threshold in controlled runs.

## Boundaries and scale limits

Synthetic traces, local policy oracle labels, no real Home Assistant logs, no distributed network latency, no physical device actuation, and no adversarial agent collusion beyond bounded witness observation noise.

## Claim scope

In a controlled deterministic smart-home trace simulation with 3 witness agents, 2-of-3 quorum consensus plus invariant checks blocked all modeled unsafe actions across 6000 Tier 1 actions at 2% witness noise and 6000 robustness actions at 10% witness noise, while preserving hash-chain integrity.

## Why it stopped

No-paper useful signal: controlled direct Tier 1 evidence supports the mechanism, but synthetic traces and oracle labels are insufficient for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up replaying real or Home Assistant-style smart-home event traces through the same consensus ledger, with direct-commit and invariant-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Realistic Smart-Home Event Traces Through Trace Consensus Ledger
- Success threshold: Zero or <=5% unsafe ledger commits on labeled unsafe actions, safe-action false rejection <=10%, valid persisted hash chains, and lower unsafe commit rate than both direct-commit and invariant-only baselines.
- Stop condition: Stop if real/replay traces show unsafe commit rate above 5% or safe false rejection above 10% after policy calibration, or if no labeled realistic trace source is available.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-consensus-ledger-evaluation-for-smart-home-age-f8054ed932`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
