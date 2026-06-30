# Volunteer CPU inference proof-of-work: determinism oracle catches shortcut cheats

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-cpu-inference-proof-of-work-determinism-oracle-catches-shortcut-cheats-1be0f4bbbf5c`
Run ID: `volunteer-cpu-inference-proof-of-work-determinism-oracle-catches-shortcut-cheats-1be0f4bbbf5c-20260619T052529878985+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9cd5010cb39

## What looked useful

Determinism oracles are effective against workers that broadly skip or replace deterministic inference, but small audit samples only probabilistically catch low-rate sparse cheating.

## Boundaries and scale limits

Test used 512 synthetic deterministic integer challenges on one CPU host, not real LLM inference, heterogeneous volunteer CPUs, networked workers, adaptive adversaries, or economic proof-of-work incentives.

## Claim scope

In a bounded toy deterministic CPU inference simulation, exact replay audits produced zero honest false rejects and detected broad shortcut strategies in every randomized audit; sparse shortcut detection followed audit coverage probability.

## Why it stopped

No-paper useful signal: local evidence supports the mechanism in a toy setting, but real-kernel and economic validation are required before any publication-grade claim.

## Recommended next action

Run a bounded follow-up over a real deterministic CPU model kernel with repeated-batch audits and an explicit sparse-cheat cost/slashing threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU model determinism oracle with repeated sparse-cheat audits
- Success threshold: Zero honest false rejects in the tested deterministic configurations and at least 99% cumulative detection of 5% sparse cheating under a documented repeated-audit budget.
- Stop condition: Stop if deterministic replay is not reproducible across the supported CPU/software configurations or if audit cost exceeds the honest work saved by the shortcut under the documented cost model.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-cpu-inference-proof-of-work-determinism-oracle-catches-shortcut-cheats-1be0f4bbbf5c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
