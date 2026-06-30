# Anchor-Addressed Compressed Memory for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-addressed-compressed-memory-for-long-context-cf6693553ac5`
Run ID: `anchor-addressed-compressed-memory-for-long-context-cf6693553ac5-20260628T231612026279+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aa15f41a92c5

## What looked useful

Addressing bytes can be a good trade when queries name stable anchors: with 64-bit anchors, exact lookup reached about 0.10, 0.21, 0.51, and 1.00 accuracy at 1%, 2%, 5%, and 10% of raw-context bytes across corpus sizes, versus about 0.01, 0.02, 0.05, and 0.10 for raw retention and about 0.03-0.08, 0.07-0.08, 0.18-0.19, and 0.36-0.37 for segment summaries. A 16-bit address ablation failed at 50,000 facts due to collisions, dropping anchor accuracy to 0.466 despite fitting all facts.

## Boundaries and scale limits

CPU-only synthetic retrieval probe; no trained transformer, KV-cache implementation, natural-language QA benchmark, or large-model inference was tested. Largest corpus was 50,000 facts, 8 seeds, and 1,000 queries per condition.

## Claim scope

In a deterministic synthetic exact-lookup task with 1,000 to 50,000 shuffled verbose key/value facts, anchor-addressed compact records preserve substantially higher retrieval accuracy than raw tail-window, raw reservoir-sample, and lossy segment-summary baselines at the same byte budget.

## Why it stopped

Bounded synthetic mechanism evidence is useful but not sufficient for a paper or architecture claim; the result is a proxy validation of exact anchor lookup rather than full long-context model validation.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should implement the same byte-budgeted anchor memory in a small transformer or LLM retrieval harness and measure direct long-context QA accuracy, latency, memory, and collision handling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Byte-Budgeted Anchor Memory in a Small Long-Context QA Harness
- Success threshold: At equal memory budget, anchor-addressed memory improves exact-answer accuracy by at least 2x over the best non-addressed compressed baseline on two or more context lengths while adding less than 20% retrieval latency and no unhandled collision errors.
- Stop condition: Stop if anchor memory fails to beat the best non-addressed compressed baseline by at least 25% relative on the smallest context length, or if collision handling consumes enough budget that accuracy advantage disappears.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-addressed-compressed-memory-for-long-context-cf6693553ac5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
