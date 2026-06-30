# Real-trace semantic compression versus embedding retrieval for repeated agent tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-trace-semantic-compression-versus-embedding-retrieval-24623a7f32`
Run ID: `real-trace-semantic-compression-versus-embedding-retrieval-24623a7f32-20260628T200901736461+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Layered agent memory: retrieval-only vs trace-derived semantic compression on repeated tasks: enoch://control-plane/projects/layered-agent-memory-retrieval-only-vs-trace-derived-semantic-compression-on-repeated-tasks-d68728863883/runs/layered-agent-memory-retrieval-only-vs-trace-derived-semantic-compression-on-repeated-tasks-d68728863883-20260628T194851920367+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7567edcb0a4

## What looked useful

Naive rolling semantic compression was brittle and failed to retain task-critical literals, paths, and enum values as reliably as retrieval. At 480 words, retrieval reached 0.893 mean recall and 0.867 exact query accuracy versus compression at 0.567 and 0.533.

## Boundaries and scale limits

Single local trace, 31 documents, 130 chunks, 8257 corpus words, deterministic span-recall evaluation only; embedding retrieval is a TF-IDF proxy, semantic compression is extractive rather than LLM-abstractive, and no human or LLM judge evaluated answer quality.

## Claim scope

On one frozen local Codex/Enoch trace with 15 literal repeated-task questions, query-specific TF-IDF cosine retrieval preserved operational facts better than a query-agnostic extractive semantic-compression baseline at 120, 240, and 480 word budgets.

## Why it stopped

Bounded local evidence is sufficient to reject the narrow naive-compression-beats-retrieval hypothesis for this trace, but it is a proxy/local result rather than full validation.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up on 20+ independent real agent traces comparing neural embedding retrieval, LLM compression with literal-preservation constraints, and a hybrid memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace neural retrieval versus literal-preserving LLM compression
- Success threshold: Hybrid memory improves exact query accuracy by at least 10 percentage points over the best single strategy at two of three token budgets, with no more than 5 percent latency overhead relative to retrieval.
- Stop condition: Stop if neural retrieval beats both compression variants by at least 10 percentage points exact accuracy at all tested budgets, or if fewer than 20 usable traces can be collected without private/human evidence.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-semantic-compression-versus-embedding-retrieval-24623a7f32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
