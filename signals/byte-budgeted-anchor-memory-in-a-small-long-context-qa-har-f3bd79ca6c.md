# Byte-Budgeted Anchor Memory in a Small Long-Context QA Harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `byte-budgeted-anchor-memory-in-a-small-long-context-qa-har-f3bd79ca6c`
Run ID: `byte-budgeted-anchor-memory-in-a-small-long-context-qa-har-f3bd79ca6c-20260628T232808539992+0000`

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

- Parent run decision: Anchor-Addressed Compressed Memory for Long Context: enoch://control-plane/projects/anchor-addressed-compressed-memory-for-long-context-cf6693553ac5/runs/anchor-addressed-compressed-memory-for-long-context-cf6693553ac5-20260628T231612026279+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aa15f41a92c5

## What looked useful

Anchor memory achieved 52.5% mean answer availability at 4096 bytes versus 1.4% tail and 1.8% head-tail truncation; at 8192 bytes compact anchors reached 100% while truncation stayed near 3%. Ordered anchor packing is position-biased, while position-balanced packing preserves the same mean accuracy with uniform early/middle/late coverage.

## Boundaries and scale limits

No neural model, real dataset, learned anchor extractor, tokenizer budget, latency benchmark, or multi-hop/natural-language QA was tested. The result is a retrieval-memory proxy over synthetic exact-match anchors.

## Claim scope

In a deterministic synthetic long-context QA harness with 100 contexts, 120 anchors per context, and byte budgets from 512 to 8192 bytes, compact anchor records preserve answer availability far better than tail or head-tail truncation under the same byte budget.

## Why it stopped

Closed as a no-paper useful signal because the current evidence is synthetic and proxy-only, despite supporting the byte-budgeted anchor-memory mechanism in the local harness.

## Recommended next action

Run a bounded deepen follow-up with a small local QA model and real tokenizer accounting to test whether generated or extracted anchors improve model answer accuracy over truncation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop byte-budgeted anchor memory on small QA tasks
- Success threshold: At least a 10 percentage point absolute answer-accuracy gain over the best truncation baseline at one or more matched sequence-item budgets, with no more than a 5 percentage point drop in worst-position accuracy relative to mean accuracy.
- Stop condition: Stop if anchor prompts fail to beat the best truncation baseline by 5 percentage points on a 50-example smoke set or if generated anchors routinely omit answer-bearing evidence.

## Evidence references

- Artifact root: `<local-path>/projects/byte-budgeted-anchor-memory-in-a-small-long-context-qa-har-f3bd79ca6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
