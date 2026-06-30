# Agent Memory Doctrine via Trace Semantic Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-doctrine-via-trace-semantic-compression-b581408c1aab`
Run ID: `agent-memory-doctrine-via-trace-semantic-compression-b581408c1aab-20260619T200702666506+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce09d176aa68

## What looked useful

Layered doctrine memory reached 1.0000 exact-action accuracy with 11.68 mean retained tokens, while transcript search reached 0.3825 accuracy with 33.28 mean retained tokens and flat retrieval reached 0.3850 accuracy with 15.86 mean retained tokens. The observed failure mode for baselines was selecting stale deprecated actions.

## Boundaries and scale limits

400 synthetic replay tasks, 1,600 strategy evaluations, one seed, no LLM/model-in-the-loop agent, no real production traces, no learned semantic extractor, and no long-horizon memory drift test.

## Claim scope

In a deterministic synthetic replay benchmark with structured active/deprecated doctrine markers, layered trace-semantic compression preserved active operator rules and selected the expected action more reliably than raw transcript search or flat retrieval under noisy traces.

## Why it stopped

Proxy-only mechanism result: useful signal but not direct/full validation and not paper-ready.

## Recommended next action

Run a bounded deepen follow-up on sanitized real or semi-real agent traces with human-labeled active doctrine targets and the same strategy matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace doctrine compression replay benchmark
- Success threshold: At least 100 labeled replay tasks, layered doctrine memory accuracy >= 0.75, and >= 20 percentage point absolute accuracy improvement over transcript_search without higher retained-token budget.
- Stop condition: Stop if layered doctrine memory improves accuracy by less than 10 percentage points over transcript_search or requires more retained tokens than transcript_search on the labeled corpus.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-doctrine-via-trace-semantic-compression-b581408c1aab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
