# Real-Trace Layered Memory Doctrine Extraction Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-layered-memory-doctrine-extraction-benchmark-3c2d573584`
Run ID: `real-trace-layered-memory-doctrine-extraction-benchmark-3c2d573584-20260619T173449968146+0000`

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

- Parent run decision: Layered Agent Memory: Semantic Compression and Operator Doctrine Updates: enoch://control-plane/projects/layered-agent-memory-semantic-compression-and-operator-doctrine-updates-7cb809a2acdb/runs/layered-agent-memory-semantic-compression-and-operator-doctrine-updates-7cb809a2acdb-20260619T163354523806+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b455a7205b0

## What looked useful

Layering improved precision from 0.8246 to 0.9574 and F1 from 0.8868 to 0.9375 while preserving 0.9184 recall, but the F1 delta was only +0.0507 versus the required +0.20.

## Boundaries and scale limits

Small manually labeled local corpus; deterministic regex/section extraction; not a broad public trace benchmark, not LLM-based extraction, and not publication-grade validation.

## Claim scope

On a six-case local real-trace benchmark, section/layer-aware doctrine extraction reduced false positives and improved aggregate F1 over flat keyword extraction, but did not meet the predeclared +0.20 F1 improvement threshold.

## Why it stopped

Tier 1 direct test produced a useful but below-threshold mechanism signal; this is no-paper evidence, not full validation.

## Recommended next action

Run a bounded deepen test of a hybrid high-recall layered extractor on an expanded real-trace corpus with independent doctrine labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid High-Recall Layered Doctrine Extraction on Expanded Real Traces
- Success threshold: Hybrid extractor recall >= 0.95, F1 >= 0.95, and false positives at least 50% lower than flat extraction on the expanded benchmark.
- Stop condition: Stop if hybrid recall remains below 0.90 or if false-positive reduction is under 25% after layer provenance is added.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-layered-memory-doctrine-extraction-benchmark-3c2d573584`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
