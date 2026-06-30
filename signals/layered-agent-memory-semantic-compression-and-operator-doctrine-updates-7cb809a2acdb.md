# Layered Agent Memory: Semantic Compression and Operator Doctrine Updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-semantic-compression-and-operator-doctrine-updates-7cb809a2acdb`
Run ID: `layered-agent-memory-semantic-compression-and-operator-doctrine-updates-7cb809a2acdb-20260619T163354523806+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b455a7205b0

## What looked useful

Typed layered memory is a plausible mechanism for aggressive semantic compression when doctrine updates must remain current. The benchmark shows the failure mode of raw/recent and rolling-summary memory: they lose long-distance facts and older doctrine under small budgets, while full-archive retrieval preserves accuracy only by retaining the full archive.

## Boundaries and scale limits

Synthetic traces only; perfect regex extraction; no LLM-mediated summarization; no real operator logs; no ambiguous or conflicting doctrine; no downstream agent task evaluation.

## Claim scope

In deterministic synthetic agent traces with schema-extractable FACT and versioned DOCTRINE events, a layered latest-state memory preserving semantic facts separately from current operator doctrine maintained 100% query accuracy at about 1.1% retained-token cost, outperforming raw recent-context and rolling-summary truncation baselines and matching full-archive keyword retrieval without retaining the full archive.

## Why it stopped

Closed as a useful proxy signal rather than a full validation; direct evidence with realistic traces and imperfect extraction is required before any paper claim.

## Recommended next action

Run a bounded deepen follow-up using real or model-generated agent traces with an LLM extractor and human/gold doctrine labels; stop this run because current evidence is synthetic/proxy-only and not publication-grade.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Layered Memory Doctrine Extraction Benchmark
- Success threshold: Layered memory reaches at least 95% current-doctrine accuracy, at least 90% fact accuracy, stale doctrine error rate below 2%, and retained-token cost at least 5x lower than full-archive retrieval on realistic traces.
- Stop condition: Stop if extraction fidelity stays below 90% current-doctrine accuracy after one bounded prompt/parser iteration, or if retained-token cost exceeds 25% of the raw trace while still failing to beat rolling summaries by at least 10 accuracy points.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-semantic-compression-and-operator-doctrine-updates-7cb809a2acdb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
