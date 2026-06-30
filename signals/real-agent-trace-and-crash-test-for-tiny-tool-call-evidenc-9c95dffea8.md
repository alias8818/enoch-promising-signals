# Real Agent Trace and Crash Test for Tiny Tool-Call Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-trace-and-crash-test-for-tiny-tool-call-evidenc-9c95dffea8`
Run ID: `real-agent-trace-and-crash-test-for-tiny-tool-call-evidenc-9c95dffea8-20260528T200344160080+0000`

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

- Parent run decision: Tiny Agent Evidence Ledger for Tool Calls: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-calls-06c77b526a27/runs/tiny-agent-evidence-ledger-for-tool-calls-06c77b526a27-20260528T162823992974+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9ad70054129c

## What looked useful

The controlled direct test supports the mechanism that explicit length framing plus hash-chain validation gives auditable prefix recovery for tool-call evidence, while naive JSONL lacks an explicit commit marker and accepted 26 truncated-at-record-end cases as complete records.

## Boundaries and scale limits

Single local Codex trace, 26 command-execution events, deterministic byte-truncation model only; no live SIGKILL writer, filesystem reorder, concurrent writer, remote storage, or long-running multi-agent validation.

## Claim scope

A tiny framed SHA-256 hash-chain ledger recovered exactly the longest complete valid prefix for 26 real local Codex command-execution trace events under exhaustive byte-truncation crash modeling, and detected one injected byte corruption per record prefix.

## Why it stopped

Tier 1 direct crash-model test passed and produced useful mechanism evidence, but the result remains no-paper because it lacks live process-death, filesystem, concurrency, and scale validation.

## Recommended next action

Run a live crash/restart deepen test that kills a writer around append/fsync boundaries over larger real traces and verifies the same longest-valid-prefix invariant across at least 1000 randomized trials.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live SIGKILL Crash-Recovery Test for Tiny Tool-Call Evidence Ledger
- Success threshold: Zero cases where recovery returns a record beyond the last committed/fsynced append, zero hash-chain validation failures for committed prefixes, and at least one baseline failure or ambiguity under the same crash schedule.
- Stop condition: Stop on any ledger prefix violation or hash-chain mismatch; otherwise stop after 1000 successful randomized crash trials with complete logs and metrics.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-and-crash-test-for-tiny-tool-call-evidenc-9c95dffea8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
