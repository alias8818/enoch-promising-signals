# Evidence Ledger vs Flat Transcript for Repeat Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-vs-flat-transcript-for-repeat-agent-tasks-0122d1d2564e`
Run ID: `evidence-ledger-vs-flat-transcript-for-repeat-agent-tasks-0122d1d2564e-20260629T214431907785+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6c14b3140ece

## What looked useful

Evidence ledgers can compact repeated-task current state much better than chronological transcript truncation, but the advantage is not established over query-aware retrieval; future work should compare ledger maintenance against retrieval in real LLM repeat-agent loops.

## Boundaries and scale limits

CPU-only synthetic benchmark, 300 generated cases, 28,800 exact-match slot queries per budget, approximate whitespace token budgets, deterministic extractor rather than an LLM agent, no natural transcripts or live tool-use tasks.

## Claim scope

In a deterministic synthetic repeat-task memory benchmark with superseding updates and distractor notes, a structured current-state evidence ledger outperformed a naive chronological recent flat transcript once the ledger fit within the context budget, but did not outperform a simple query-aware retrieval control over the same flat events.

## Why it stopped

Synthetic evidence supports a narrow mechanism but the query-aware flat retrieval control achieved perfect accuracy, so the broad ledger-vs-flat claim is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next run should deepen with an LLM repeat-agent benchmark that includes ledger, chronological transcript, and query-aware retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Repeat-Agent Memory Benchmark for Ledger vs Retrieval
- Success threshold: Ledger condition improves task success by at least 10 percentage points or reduces context tokens by at least 40% at matched success versus both chronological transcript and query-aware retrieval on the natural repeat-agent suite.
- Stop condition: Stop if query-aware retrieval matches ledger within 3 percentage points at equal or lower token cost, or if ledger maintenance errors exceed the stale-fact errors it prevents.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-vs-flat-transcript-for-repeat-agent-tasks-0122d1d2564e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
