# Replay Verification on Real Agent Framework Trace Formats

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `replay-verification-on-real-agent-framework-trace-formats-4766929080`
Run ID: `replay-verification-on-real-agent-framework-trace-formats-4766929080-20260524T022333691784+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Replay Validation on Real Agent Workflow Ledgers: enoch://control-plane/projects/replay-validation-on-real-agent-workflow-ledgers-71a9e6e4a8/runs/replay-validation-on-real-agent-workflow-ledgers-71a9e6e4a8-20260524T014811214190+0000
- Parent run decision: Online Independent Replay Verification for Real Multi-Tool Agent Ledgers: enoch://control-plane/projects/online-independent-replay-verification-for-real-multi-tool-edb920ac25/runs/online-independent-replay-verification-for-real-multi-tool-edb920ac25-20260524T020315495607+0000

## What looked useful

Across 300 clean rerun comparisons and 1,200 injected faults, the canonical verifier accepted 300/300 clean reruns and 300/300 benign jitter traces while detecting 1200/1200 injected faults. Raw exact equality detected faults but rejected 300/300 clean reruns; schema-only and type-multiset baselines each detected only 600/1200 faults.

## Boundaries and scale limits

Validated only on deterministic local toy workloads: 100 seeds per framework, 600 trace files total, and 1,200 injected faults. It did not test production agents, external trace corpora, nondeterministic LLM/tool calls, concurrent branch races, cloud-hosted trace backends, partial traces, or schema evolution across framework versions.

## Claim scope

Canonical replay verification can separate volatile observer fields from replay-relevant semantics for locally generated deterministic traces emitted by LangGraph astream_events v2, AutoGen AgentChat run_stream, and OpenTelemetry SDK spans.

## Why it stopped

The run produced direct local evidence on real framework trace formats, but the workloads are toy/local and do not meet the requested Tier 4 paper-readiness replication and robustness threshold.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful signal; do not recommend another chained follow-up. A future independent project would need an external multi-application trace corpus with production-like nondeterminism before paper claims.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/replay-verification-on-real-agent-framework-trace-formats-4766929080`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
