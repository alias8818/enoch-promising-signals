# Exact-anchor ledger on real small-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-ledger-on-real-small-agent-traces-062e6318fb`
Run ID: `exact-anchor-ledger-on-real-small-agent-traces-062e6318fb-20260528T034503278129+0000`

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

- Parent run decision: Exact-Anchor Ledger for Small-Agent Tool Calls: enoch://control-plane/projects/exact-anchor-ledger-for-small-agent-tool-calls-ad63afd98676/runs/exact-anchor-ledger-for-small-agent-tool-calls-ad63afd98676-20260528T012713250114+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9bff071dd906

## What looked useful

120 exact anchors from 30 real trace logs had 1.000 original validation rate and 1.000 corrupted-span rejection rate. Quote-only and item-id-only controls had 1.000 false-accept rates under decoy quote injection or stale item ids.

## Boundaries and scale limits

Local Enoch/Codex traces only; command_execution aggregated_output events only; deterministic mutation rather than live adversarial writers; no public corpus, all-tool coverage, signing, external timestamping, concurrent tailing, or semantic claim audit.

## Claim scope

On 30 real local Codex/Enoch small-agent JSONL traces, exact line/hash/span anchors for command-output evidence resolve on original logs and reject deterministic anchored-span corruption with decoy quote injection, while quote-only and item-id-only controls falsely accept stale rows.

## Why it stopped

Useful Tier 1 mechanism signal, but not paper-positive because validation is local, offline, command-output-only, and uses deterministic mutation rather than broad live trace conditions.

## Recommended next action

Run a bounded online tailer validation during live small-agent sessions, extending exact anchors beyond command outputs to command, file, browser, and connector events.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online exact-anchor ledger tailing across live small-agent tool events
- Success threshold: At least 100 live-generated anchors across at least 10 sessions, original validation rate >= 0.99, stale/tamper rejection rate = 1.0, no more than 1% anchor loss from tailing/replay, and weaker controls false-accept at least 50% of decoy stale rows.
- Stop condition: Stop if online tailing loses or misanchors more than 1% of events, if exact anchors fail to reject any corrupted anchored span, or if fewer than 100 anchors can be gathered from live sessions within the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-ledger-on-real-small-agent-traces-062e6318fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
