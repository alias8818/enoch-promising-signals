# Real-agent evidence ledger durability probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-evidence-ledger-durability-probe-d0c0d4c8e8`
Run ID: `real-agent-evidence-ledger-durability-probe-d0c0d4c8e8-20260607T133648776921+0000`

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

- Parent run decision: Evidence-Ledger CPU Agent: enoch://control-plane/projects/evidence-ledger-cpu-agent-f04c1a8e4fc7/runs/evidence-ledger-cpu-agent-f04c1a8e4fc7-20260607T063118526769+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bde5126b6812

## What looked useful

Durable ACK-after-fsync ledger recovered 1,995/1,995 ACKed pre-kill events with 50/50 valid hash chains, 50/50 matching manifests, and 50/50 successful restart appends. Naive ACK-before-flush baseline lost 656/2,031 ACKed events and recovered all ACKed events in only 1/50 trials.

## Boundaries and scale limits

Tested only on one local filesystem with deterministic subprocess agents, one writer at a time, small JSON events, and SIGKILL faults. Not tested for concurrent writers, actual machine reboot or power loss, network filesystems, object stores, disk-full behavior, partial sector writes, or production LLM-agent traces.

## Claim scope

Single-writer local JSONL evidence ledger with commit ACK after append, file fsync, atomic manifest replacement, and directory fsync recovered all ACKed subprocess-agent evidence events across SIGKILL and restart append in 50/50 controlled trials.

## Why it stopped

Tier 1 direct controlled test produced useful mechanism support, but evidence remains too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with concurrent multi-agent writers, sequence locking, and controlled reboot or crash injection before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent evidence ledger crash-recovery probe
- Success threshold: 100/100 crash trials recover all ACKed events, verify the global hash chain and manifest, and successfully append after restart; baseline must expose at least one missing ACKed event or ordering failure.
- Stop condition: Stop early if any durable trial loses an ACKed event, creates a duplicate or skipped sequence number, fails hash verification, or cannot append after restart.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-durability-probe-d0c0d4c8e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
