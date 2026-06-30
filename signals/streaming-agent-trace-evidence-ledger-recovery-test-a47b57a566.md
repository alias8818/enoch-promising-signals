# Streaming Agent Trace Evidence-Ledger Recovery Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `streaming-agent-trace-evidence-ledger-recovery-test-a47b57a566`
Run ID: `streaming-agent-trace-evidence-ledger-recovery-test-a47b57a566-20260529T011533891859+0000`

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

- Parent run decision: Evidence-Ledger for Tiny Agent Tool Calls: enoch://control-plane/projects/evidence-ledger-for-tiny-agent-tool-calls-51678a3e6e58/runs/evidence-ledger-for-tiny-agent-tool-calls-51678a3e6e58-20260528T012513536322+0000
- Parent run decision: Real Agent Trace Evidence-Ledger Integration: enoch://control-plane/projects/real-agent-trace-evidence-ledger-integration-495e12b923/runs/real-agent-trace-evidence-ledger-integration-495e12b923-20260528T150914016428+0000

## What looked useful

The ledger mechanism appears useful when recovery budgets are bounded: it achieved 1.000 exact recovery and citation accuracy across five fixed seeds, while the best real baseline reached 0.7336 and the first-write ablation reached 0.2650. A capacity-8 summary control matched the ledger, showing the effect is a structured-state and budget tradeoff rather than a universal advantage.

## Boundaries and scale limits

Synthetic symbolic traces only; no real LLM traces, production trace schemas, human labels, semantic extraction, concurrent sessions, or persistence-failure injection were tested.

## Claim scope

In a deterministic synthetic streaming-agent trace harness with fixed seeds, revisions, distractors, hard cutover, bounded summary/window baselines, and a first-write ablation, a latest-evidence ledger recovered task facts and provenance exactly and exceeded the best bounded real baseline by 26.64 percentage points.

## Why it stopped

No-paper closure because the current evidence is a synthetic Tier 2 mechanism confirmation, not direct production-agent validation.

## Recommended next action

Run a bounded deepen test on real recorded agent traces with labeled recovery facts and LLM summarization/retrieval baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Evidence-Ledger Recovery Validation
- Success threshold: Evidence ledger improves exact recovery and citation accuracy by at least 10 percentage points over the best matched-budget real baseline with non-overlapping or clearly favorable confidence intervals, while first-write/no-update ablations fail on revision-heavy traces.
- Stop condition: Stop if the ledger advantage over the best matched-budget real baseline is below 5 percentage points, if citation accuracy does not improve, or if real traces cannot be labeled reproducibly without private/human evidence.

## Evidence references

- Artifact root: `<local-path>/projects/streaming-agent-trace-evidence-ledger-recovery-test-a47b57a566`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
