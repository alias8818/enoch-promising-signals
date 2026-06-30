# Real-Agent Merkle Ledger Anchoring and Crash-Recovery Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-merkle-ledger-anchoring-and-crash-recovery-test-e42c7a0664`
Run ID: `real-agent-merkle-ledger-anchoring-and-crash-recovery-test-e42c7a0664-20260524T021323841435+0000`

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

- Parent run decision: Merkle-Ledger Agent Tool-Call Integrity: enoch://control-plane/projects/merkle-ledger-agent-tool-call-integrity-f72fee77b0d4/runs/merkle-ledger-agent-tool-call-integrity-f72fee77b0d4-20260524T010404391720+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

Across 30 anchored and 30 baseline trials with 1,200 total injected SIGKILL crashes, both recovered all task artifacts with zero duplicate commits, while only the anchored ledger rejected an adversarially rehashed history rewrite. Local anchoring overhead was about 2.1% wall-clock and 10.0% persisted bytes in this small fsync-heavy harness.

## Boundaries and scale limits

Synthetic task workload; local filesystem ledger and local anchor file; one active agent process; 30 trials per condition; 64 operations per trial; no remote transparency log, no real LLM tool traces, no concurrent agents, no host power-loss testing, and no cross-machine recovery.

## Claim scope

In a local single-agent subprocess harness, a Merkle hash-chain ledger with periodic local anchors recovered exactly-once task completion after repeated SIGKILL crashes and detected a rehashed ledger-history rewrite that an unanchored hash chain accepted.

## Why it stopped

Controlled Tier 1 direct test produced a useful mechanism signal, but evidence is local, synthetic, and not paper-positive.

## Recommended next action

Run a Tier 2 real-agent trace test with a remote append-only anchor service and adversarial crash/tamper cases across concurrent workers before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Remote-Anchored Real-Agent Crash-Recovery Trace Test
- Success threshold: Zero lost committed operations, zero duplicate externally visible side effects, and 100% detection of anchored-history rewrites across at least 100 crash-injected real-agent runs.
- Stop condition: Stop if any anchored run loses a committed operation, duplicates an externally visible side effect, accepts a rewritten anchored history, or if remote anchoring overhead makes the real-agent workflow impractical under the declared latency budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-merkle-ledger-anchoring-and-crash-recovery-test-e42c7a0664`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
