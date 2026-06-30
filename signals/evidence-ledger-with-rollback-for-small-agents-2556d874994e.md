# Evidence Ledger with Rollback for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-with-rollback-for-small-agents-2556d874994e`
Run ID: `evidence-ledger-with-rollback-for-small-agents-2556d874994e-20260608T172913564011+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/90c415cb3930

## What looked useful

Dependency-aware rollback matched a recompute-from-latest oracle on post-audit accuracy while retaining cached derived claims, and improved post-audit accuracy versus latest-direct/no-rollback memory by +0.0387 with 95% CI [0.0374, 0.0400] in the main run.

## Boundaries and scale limits

Structured numeric facts only; no LLM planner, natural-language evidence extraction, external tool latency, irreversible actions, long-horizon tasks, adversarial evidence, or production traces. Main evidence is 1000 synthetic paired episodes plus a six-condition robustness sweep.

## Claim scope

In a synthetic small-agent memory benchmark with noisy direct observations, later audit corrections, and memoized pair-sum derived claims, dependency-tracked evidence rollback improves post-correction answer consistency over append-only memory and latest-direct-fact memory without dependent invalidation.

## Why it stopped

Closed as no-paper useful signal because the current evidence supports the rollback mechanism only in a synthetic/proxy benchmark, not as direct full validation for real small agents.

## Recommended next action

Run a bounded real-agent trace benchmark with natural-language evidence records, reversible workspace edits, and contradictory tool evidence to test whether dependency rollback reduces stale claims and bad actions outside the synthetic numeric setting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent trace benchmark for evidence-ledger rollback
- Success threshold: Across at least 100 paired task traces, rollback reduces stale dependent claims by at least 25% and incorrect follow-on actions by at least 10% versus latest-memory/no-rollback, with no more than 20% latency overhead and no task-success regression.
- Stop condition: Stop if rollback fails to reduce stale dependent claims by 10% versus latest-memory/no-rollback or introduces more than 20% task-success regression in the paired trace benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-with-rollback-for-small-agents-2556d874994e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
