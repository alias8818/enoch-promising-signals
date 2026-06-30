# Speculative decoding gated by evidence-ledger consistency on tool plans

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-gated-by-evidence-ledger-consistency-on-tool-plans-8e2a6d117ecf`
Run ID: `speculative-decoding-gated-by-evidence-ledger-consistency-on-tool-plans-8e2a6d117ecf-20260629T154930087198+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/237047725527

## What looked useful

Across 5,000-task scenarios, ledger gating produced 1.30x, 1.50x, and 1.74x simulated speedups at draft correctness 0.35, 0.55, and 0.75, versus exact-prefix speculation at 0.84x, 1.02x, and 1.23x. It prevented 25,583, 12,468, and 5,395 invalid actions respectively, but accepted irrelevant locally consistent searches in lower-quality settings.

## Boundaries and scale limits

Synthetic tasks only; hand-coded draft planner; parameterized latency model; no real LLM target, no real tools, no side-effectful operations, no production agent traces.

## Claim scope

In a deterministic synthetic evidence-gathering tool-plan benchmark, a ledger-consistency gate accepted more valid speculative plan actions than exact-prefix verification and reduced simulated target-planner calls while preventing invalid precondition-violating tool actions.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct enough for a paper; consistency-only gating also admits irrelevant locally consistent work.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay the gate on real or realistic agent traces with sandboxed/no-op tools and measured runtime latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay evidence-ledger gated speculative tool plans on real agent traces
- Success threshold: At least 1.2x measured end-to-end latency improvement versus no speculation, at least 25% fewer target planner calls, 100% task completion under fallback, and unsafe accepted tool actions below 0.1%.
- Stop condition: Stop if measured speedup is below 1.05x, unsafe accepted actions exceed 0.1%, or irrelevant accepted work exceeds the latency saved by reduced target calls.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-gated-by-evidence-ledger-consistency-on-tool-plans-8e2a6d117ecf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
