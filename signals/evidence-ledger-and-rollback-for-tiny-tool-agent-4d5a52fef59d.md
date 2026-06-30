# Evidence ledger and rollback for tiny tool agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-and-rollback-for-tiny-tool-agent-4d5a52fef59d`
Run ID: `evidence-ledger-and-rollback-for-tiny-tool-agent-4d5a52fef59d-20260601T001201722314+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6290d1416720

## What looked useful

Across 10,000 episodes per policy per error rate, ledger rollback/retry improved success by +14.08 to +39.28 percentage points and reduced harmful notification rate from 5.41-34.29% to 0.00%, with about 2.3x-2.6x simulated per-episode overhead.

## Boundaries and scale limits

Simulation-only evidence: no real LLM planner, no real external APIs, no concurrent side effects, no natural-language evidence extraction, and no long-horizon tasks. Timing is simulator overhead only and must not be interpreted as real agent latency.

## Claim scope

In a deterministic synthetic key-value tool-agent simulator with injected stochastic tool-call corruption, an evidence ledger with predicate checks, reversible rollback, one retry per step, and pre-execution gating for irreversible notification calls improved task success and eliminated harmful notifications versus naive execution across 0.05-0.35 error rates.

## Why it stopped

The result supports the mechanism only in a synthetic simulator and is not direct/full validation of real tool-agent behavior.

## Recommended next action

Stop this run as a no-paper synthetic useful signal; the next bounded test should wrap the ledger policy around a real tiny filesystem/subprocess or mock-HTTP tool agent with recorded planner outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger rollback on a real tiny filesystem tool agent
- Success threshold: Ledger rollback reduces unrecovered or harmful side effects by at least 75% relative to naive execution, keeps absolute harmful irreversible side effects below 2%, and maintains at least 90% of naive successful completions on the same task suite.
- Stop condition: Stop as negative if side-effect reduction is below 50%, harmful irreversible side effects exceed 5%, or success falls below 80% of naive completions under matched tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-and-rollback-for-tiny-tool-agent-4d5a52fef59d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
