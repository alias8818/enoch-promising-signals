# Evidence-Ledger for Tiny Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-agent-tool-calls-51678a3e6e58`
Run ID: `evidence-ledger-for-tiny-agent-tool-calls-51678a3e6e58-20260528T012513536322+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/125b33f851bb

## What looked useful

The bounded benchmark showed 3/3 detection for each injected ledger attack class at 50,000 calls, while plain JSONL missed 0/3 middle content modifications and 0/3 tail truncations. Median ledger write slowdown was 4.964x, median storage overhead was 2.582x, and 50,000-call ledger verification took about 1.55 seconds.

## Boundaries and scale limits

Synthetic traces only; maximum 50,000 calls per trial, 12 trials total, one Python process, local filesystem, no real agent-framework integration, no concurrent writers, no remote timestamping, and no adversary with signing-key access.

## Claim scope

In a local single-writer synthetic tiny-tool-call benchmark, canonical JSON event hashing plus a per-record hash chain and HMAC root checkpoint detects content modification, deletion, reorder, and tail truncation that plain JSONL logging can miss, while preserving practical local throughput.

## Why it stopped

The result is a bounded synthetic/local useful signal, not publication-grade direct evidence for production agent systems.

## Recommended next action

Stop this run as no-paper useful evidence; next concrete action is a bounded integration test on real LangGraph or Codex tool-call traces with concurrent append and key-custody instrumentation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace Evidence-Ledger Integration
- Success threshold: All injected attacks are detected in real traces, p95 ledger append overhead is under 10 ms per call, storage overhead is under 4x plain JSONL, and independent verification of 10,000 records completes under 5 seconds.
- Stop condition: Stop if integration requires private credentials unavailable to the worker, if real-trace overhead exceeds the latency/storage thresholds by more than 2x, or if any mutation class is not detected under the stated key-custody assumptions.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-agent-tool-calls-51678a3e6e58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
