# Signed Recorder on Real Multi-Step Agent Tool Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `signed-recorder-on-real-multi-step-agent-tool-traces-3d0cea7dba`
Run ID: `signed-recorder-on-real-multi-step-agent-tool-traces-3d0cea7dba-20260518T120404719724+0000`

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

- Internal Enoch project: Signed Recorder on Real Multi-Step Agent Tool Traces: internal_generated:signed-recorder-on-real-multi-step-agent-tool-traces-3d0cea7dba

## What looked useful

Signed-chain trace recording is mechanically viable and low-overhead enough for local agent logs, with clear authenticity benefit over plain JSONL and unsigned hash-chain baselines under the tested tamper attacks.

## Boundaries and scale limits

The recorder was evaluated on local replayed trace files, not integrated into a live multi-step agent runtime. It does not cover concurrent writers, crash recovery, key rotation, external timestamping, verifier UX, remote storage, or signing-key compromise.

## Claim scope

Post-hoc replay validation on 16,906 real local Enoch/OMX agent trace events shows an Ed25519 signed hash-chain recorder detects fixed-seed payload edits, deletions, swaps, and truncations that plain JSONL misses, and resists an adaptive unsigned-hash-chain recomputation control while recording about 51k events/s.

## Why it stopped

Medium local replay evidence supports the mechanism but is not paper-positive because the recorder was not validated inside a live agent runtime or under operational failure modes.

## Recommended next action

Run a live-instrumentation follow-up that places the signed-chain recorder in the agent tool-call path for at least 20 multi-step tasks, including concurrent writes and crash/restart cases, then repeat the tamper suite and measure end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Agent Tool-Path Signed Recorder With Crash and Concurrency Checks
- Success threshold: Signed-chain detects 100% of tested tamper attacks across live traces, adds less than 5% median end-to-end latency versus no recorder, and produces no unverifiable gaps in crash/restart or concurrent-write tests.
- Stop condition: Stop if live insertion loses events, creates unverifiable gaps after crash/restart, or exceeds 10% median end-to-end latency overhead on the 20-task suite.

## Evidence references

- Artifact root: `<local-path>/projects/signed-recorder-on-real-multi-step-agent-tool-traces-3d0cea7dba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
