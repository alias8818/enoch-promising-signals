# Real-trace coding-agent memory comparison with semantic cards versus flat session-window retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-coding-agent-memory-comparison-with-semantic-ca-b03b84dc9c`
Run ID: `real-trace-coding-agent-memory-comparison-with-semantic-ca-b03b84dc9c-20260628T033624124274+0000`

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

- Parent run decision: Agent memory architecture: trace-derived semantic compression vs flat retrieval on repeated coding tasks: enoch://control-plane/projects/agent-memory-architecture-trace-derived-semantic-compression-vs-flat-retrieval-on-repeated-codin-9b82f70c3ea6/runs/agent-memory-architecture-trace-derived-semantic-compression-vs-flat-retrieval-on-repeated-codin-9b82f70c3ea6-20260628T031702169372+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a959f9b7cbe6

## What looked useful

Semantic cards achieved 10/10 top-1 and top-3 hits versus 9/10 for 120-token flat windows on the canonical run; across flat window sizes 40-480, semantic cards stayed at 10/10 top-1 while flat windows ranged from 7/10 to 9/10.

## Boundaries and scale limits

Single trace, manually authored cards, lexical retrieval only, no automatic card extraction, no delayed coding-task execution, and no multi-trace or cross-project robustness.

## Claim scope

On one short local real Codex trace with ten trace-derived gold questions, deterministic semantic cards improved BM25 top-1 and top-3 retrieval over flat fixed session windows, while top-5 reached parity.

## Why it stopped

Tier 1 direct local test produced useful mechanism support, but the result is too small and manually carded for publication readiness.

## Recommended next action

Run a bounded deepen test on at least 5 independent real coding-agent traces with automatic card extraction and held-out delayed-memory questions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Automatic semantic-card extraction on multiple real coding-agent traces
- Success threshold: Semantic-card retrieval improves mean top-1 accuracy by at least 10 percentage points over the best flat-window baseline, with no worse than parity at top-5, across at least 50 total held-out questions.
- Stop condition: Stop if automatic cards fail to beat the best flat-window top-1 accuracy by 10 percentage points or if answer provenance cannot be established for the real traces.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-coding-agent-memory-comparison-with-semantic-ca-b03b84dc9c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
