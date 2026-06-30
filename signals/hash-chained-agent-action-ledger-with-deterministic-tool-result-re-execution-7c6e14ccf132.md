# Hash-Chained Agent Action Ledger With Deterministic Tool-Result Re-Execution

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-agent-action-ledger-with-deterministic-tool-result-re-execution-7c6e14ccf132`
Run ID: `hash-chained-agent-action-ledger-with-deterministic-tool-result-re-execution-7c6e14ccf132-20260609T085100812951+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3ea99510e448

## What looked useful

The ledger detected 36/36 tested tamper mutations across six positions and replayed 100,000/100,000 deterministic entries, but uncontrolled nondeterministic tools failed replay at the first random/time-dependent call. Controlled seeding/frozen time restored 100,000/100,000 replay, showing replay contracts are mandatory.

## Boundaries and scale limits

Tested only synthetic local tools up to 100,000 ledger entries on one Python process; no real LLM agent traces, network APIs, mutable filesystem tools, shell side effects, concurrent writers, persistence recovery, or adversarial cryptanalysis were tested.

## Claim scope

A Python prototype hash-chained ledger over canonical JSON records can verify integrity and deterministically replay synthetic local tool calls when each tool has deterministic replay semantics or an explicitly controlled harness.

## Why it stopped

No-paper useful signal: local deterministic mechanism is supported, but the evidence is synthetic/prototype-only and directly shows uncontrolled nondeterministic tools break deterministic re-execution.

## Recommended next action

Run a bounded deepen follow-up on real captured agent traces with explicit replay contracts for time, random, filesystem, shell, and HTTP-like tools; stop if more than 1 percent of replay mismatches cannot be classified and controlled.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Contracts for Real Agent Tool Traces
- Success threshold: At least 99 percent exact result-hash agreement on replay across 1,000 or more real tool calls, 100 percent detection of tested ledger tamper mutations, and every remaining mismatch assigned to a documented replay-contract gap.
- Stop condition: Stop as a negative if uncontrolled external state causes more than 1 percent unclassified replay mismatches after implementing explicit replay contracts for the tested tool classes.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-agent-action-ledger-with-deterministic-tool-result-re-execution-7c6e14ccf132`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
