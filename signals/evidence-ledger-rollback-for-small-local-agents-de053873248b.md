# Evidence-Ledger Rollback for Small Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-small-local-agents-de053873248b`
Run ID: `evidence-ledger-rollback-for-small-local-agents-de053873248b-20260605T021944513018+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47a251bb1026

## What looked useful

Rollback improved audited-poisoned accuracy from 0.777925 to 0.996363 and removed all stale poisoned derived beliefs after audit; no-rollback and blacklist-future baselines retained 18659 stale poisoned beliefs.

## Boundaries and scale limits

Tested only on a deterministic synthetic scoring agent: 30 trials of 2000 episodes. Not tested on local LLM agents, natural-language evidence extraction, multi-step tool traces, persistent vector stores, or production workloads.

## Claim scope

In a synthetic small-agent endpoint selection task with source-tagged evidence, adversarial poisoned evidence, and later source invalidation, dependency-aware evidence-ledger rollback improves audited-poisoned decision accuracy versus no rollback or future-only blacklisting.

## Why it stopped

The result is a bounded synthetic mechanism validation, not direct full validation on real local agents or production-like evidence ledgers.

## Recommended next action

Run a bounded real-agent follow-up using a small local LLM/tool agent with logged evidence dependencies and controlled source invalidations; stop this run as no-paper useful synthetic evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback on real small local tool-agent traces
- Success threshold: Across at least 300 controlled real-agent episodes, rollback improves audited-poisoned task success by at least 10 percentage points over both baselines, eliminates at least 95% of stale poisoned derived beliefs, and adds less than 20% median decision latency.
- Stop condition: Stop if rollback improves audited-poisoned task success by less than 5 percentage points over both baselines, cannot eliminate stale dependent beliefs, or requires manual/private evidence unavailable to the worker.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-small-local-agents-de053873248b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
