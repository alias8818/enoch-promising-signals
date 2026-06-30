# Byzantine Consensus for Small Agent Swarm on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `byzantine-consensus-for-small-agent-swarm-on-cpu-62cfadab35c9`
Run ID: `byzantine-consensus-for-small-agent-swarm-on-cpu-62cfadab35c9-20260608T020705248862+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/644b992a27af

## What looked useful

PBFT-style quorum rounds are computationally cheap for small CPU-hosted swarms and prevent the baseline's equivocation safety failure, but no-view-change PBFT-lite frequently loses liveness under a Byzantine leader.

## Boundaries and scale limits

Simulation only; no real network, process isolation, cryptographic signatures, view change, partial synchrony, crash recovery, or LLM-agent task execution. CPU benchmark is single-process Python and should not be read as deployment latency.

## Claim scope

In a synchronous authenticated simulator for n=3f+1 swarms with n=4..31, a PBFT-style pre-prepare/prepare/commit quorum protocol preserved agreement and honest-leader validity under tested Byzantine equivocation while a naive leader-following baseline produced divergent honest decisions.

## Why it stopped

Closed as no-paper useful signal: simulator evidence supports the safety mechanism but is not direct deployment or publication-grade validation.

## Recommended next action

Run a bounded local-process follow-up with authenticated messages and view change, measuring end-to-end safety, liveness, and decision latency under process-level Byzantine faults.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Local-process PBFT swarm with view change and authenticated messages
- Success threshold: Zero honest agreement violations, zero honest-leader validity violations, at least 99% decisions within 100 ms after at most one view change for n=4,7,10 on a CPU worker.
- Stop condition: Stop if any reproducible agreement violation occurs, or if view-change liveness stays below 95% after fixing implementation bugs, or if median decision latency exceeds 250 ms for n=10.

## Evidence references

- Artifact root: `<local-path>/projects/byzantine-consensus-for-small-agent-swarm-on-cpu-62cfadab35c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
