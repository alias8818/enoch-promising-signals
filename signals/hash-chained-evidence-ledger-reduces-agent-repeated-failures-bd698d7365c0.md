# Hash-Chained Evidence Ledger Reduces Agent Repeated Failures

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-evidence-ledger-reduces-agent-repeated-failures-bd698d7365c0`
Run ID: `hash-chained-evidence-ledger-reduces-agent-repeated-failures-bd698d7365c0-20260630T121112102802+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6535d1d4d6f9

## What looked useful

Persistent structured failure evidence eliminated repeated failures in the clean benchmark, while hash-chained verification reduced repeated failures under 5% retrieval corruption from 0.2439 to 0.0855 versus corruptible plain evidence. Hash chaining added about 28x per-trial overhead versus plain evidence in the naive implementation.

## Boundaries and scale limits

60 trials x 800 synthetic episodes only; no real LLM agent traces, no live coding tasks, no token-cost measurement, and a naive full-chain verification implementation with high overhead.

## Claim scope

In a local synthetic recurring-task benchmark, structured evidence ledgers reduced repeated task/action failures versus no memory; hash chaining specifically improved robustness under injected evidence corruption but did not improve over plain structured evidence in the clean setting.

## Why it stopped

Closed as no-paper useful signal because current evidence is synthetic/proxy and shows the main repeat-failure reduction comes from structured evidence; hash chaining helps only under integrity stress in this run.

## Recommended next action

Run a bounded direct benchmark on real agent/tool traces with equalized retrieval quality and checkpointed hash verification before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Trace Benchmark for Hash-Chained Failure Evidence
- Success threshold: At least 25% relative reduction in repeated failures versus the strongest non-hash baseline under integrity stress, with less than 10% wall-clock overhead from checkpointed verification.
- Stop condition: Stop if hash chaining does not beat plain structured evidence under integrity stress or if verification overhead exceeds 10% after checkpointing/indexing.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-reduces-agent-repeated-failures-bd698d7365c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
