# Layered Memory Architecture with Trace-Derived Semantic Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-memory-architecture-with-trace-derived-semantic-compression-ca1b5a19f358`
Run ID: `layered-memory-architecture-with-trace-derived-semantic-compression-ca1b5a19f358-20260629T124637510219+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5a05e6a496ea

## What looked useful

Trace-derived semantic summaries can beat raw byte-matched memory when summary capacity spans the query lag distribution; undersized semantic layers can underperform reservoir raw memory. Payload retention was necessary in the ablation.

## Boundaries and scale limits

No real traces, no learned compressor, no LLM integration, no GPT-scale or production workload validation. The compressor used explicit task and payload fields emitted by the synthetic generator.

## Claim scope

Synthetic trace benchmark only: layered recent-raw plus semantic-summary memory improved long-lag payload query accuracy over raw FIFO/reservoir baselines at 8-16 KiB budgets, but failed at 4 KiB.

## Why it stopped

Proxy-only useful signal: the synthetic experiment supports the mechanism under calibrated budgets but is not a full validation and includes an early falsification at the smallest budget.

## Recommended next action

Run a bounded deepen test on real or semi-real execution traces with labeled long-lag questions and a non-oracle semantic extractor; stop if it fails to beat byte-matched raw retrieval by at least 5 percentage points at two budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of semantic summary memory under byte-matched budgets
- Success threshold: Layered semantic memory exceeds the best raw baseline by at least 5 absolute accuracy points at two or more budgets, with a positive payload/state ablation gap.
- Stop condition: Stop as negative if the semantic layer fails to beat the best raw baseline by 5 absolute points at all tested budgets or if non-oracle extraction removes the observed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-architecture-with-trace-derived-semantic-compression-ca1b5a19f358`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
