# Real Trace Persistence Test for Anchored Tool-Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-persistence-test-for-anchored-tool-agent-eviden-08de1668ec`
Run ID: `real-trace-persistence-test-for-anchored-tool-agent-eviden-08de1668ec-20260529T081203923377+0000`

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

- Parent run decision: Tamper-Evident Evidence Ledger for Small Tool Agents: enoch://control-plane/projects/tamper-evident-evidence-ledger-for-small-tool-agents-ea814a10fc40/runs/tamper-evident-evidence-ledger-for-small-tool-agents-ea814a10fc40-20260529T040413314394+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f91fc069d69e

## What looked useful

The Tier 1 direct test met its stated threshold: 100% clean recovery, 100% payload tamper detection, 100% anchor tamper detection, and 100% truncation detection for local real tool-command traces.

## Boundaries and scale limits

Only 20 trials and 500 clean events were tested. The run did not test power-loss writes, kernel crashes, concurrent multi-agent writers, external immutable anchoring, or an adversary able to rewrite ledger, anchors, and manifest consistently.

## Claim scope

In a controlled local filesystem test, a hash-chained JSONL evidence ledger with periodic anchor records and a manifest persisted 500 real subprocess tool-command events across process reopen cycles and detected payload mutation, anchor mutation, and truncation in all 20 trials.

## Why it stopped

No-paper useful signal: the mechanism worked in a controlled small direct test, but the evidence is not publication-grade without crash-injection, baseline comparison, concurrency, and external anchoring controls.

## Recommended next action

Run a bounded deepen follow-up with child-process kill/crash injection at write boundaries and a plain JSONL baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-Injection Baseline Test for Anchored Tool-Agent Evidence Ledgers
- Success threshold: Across at least 100 crash-injection trials, anchored logging must show 0 undetected corruptions, at least 99% verifier correctness, and a strictly longer median verifiable recovery prefix than the plain JSONL baseline.
- Stop condition: Stop as negative if any undetected corruption appears in the anchored verifier or if anchored logging does not improve median verifiable recovery prefix over the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-persistence-test-for-anchored-tool-agent-eviden-08de1668ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
