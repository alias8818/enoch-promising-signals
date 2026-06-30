# Anchor-Preserving Compressed Memory for Long-Context Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-preserving-compressed-memory-for-long-context-agents-36f805127f4e`
Run ID: `anchor-preserving-compressed-memory-for-long-context-agents-36f805127f4e-20260613T204001598376+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffda7f9aacb9

## What looked useful

Main run: anchor-preserving compressed memory reached 2400/2400 recall at 680 mean stored chars, matching transcript_search at 17629.9 mean stored chars and outperforming flat_retrieval by 0.8287 accuracy. Sensitivity showed a clear budget boundary: 0.6667 mean anchor accuracy at 240 chars and 1.0 at 360+ chars.

## Boundaries and scale limits

Synthetic replay only; no LLM extraction, real agent traces, semantic retrieval baseline, or end-to-end task execution. Main evidence is 200 tasks at 700 chars plus a 5-seed x 5-budget sensitivity sweep.

## Claim scope

In deterministic synthetic repeated-agent replay tasks with explicit canonical anchors and a fixed compressed memory budget, preserving anchor key/value pairs retains long-horizon facts much better than lossy flat or layered recency compression, matching transcript-search recall when the anchor budget is sufficient.

## Why it stopped

No-paper closure: this is a bounded synthetic mechanism signal, not direct full validation of long-context agents.

## Recommended next action

Run a bounded direct follow-up on real or LLM-generated repeated-agent traces with noisy anchor extraction and end-to-end task success metrics before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Anchor Extraction Replay for Compressed Agent Memory
- Success threshold: At equal compressed storage budget, anchor-preserving memory improves final recall or downstream task success by at least 20 percentage points over the best compressed baseline across at least 3 seeds, while retaining at least 90% of transcript-search performance.
- Stop condition: Stop as negative if noisy extraction reduces anchor-preserving recall below the best compressed baseline or below 70% of transcript-search performance across 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-compressed-memory-for-long-context-agents-36f805127f4e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
