# Anchor-compressed memory on LLM-generated agent traces with lossy summaries

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-compressed-memory-on-llm-generated-agent-traces-wit-ca9373ed8f`
Run ID: `anchor-compressed-memory-on-llm-generated-agent-traces-wit-ca9373ed8f-20260629T193239779869+0000`

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

- Parent run decision: Anchor-compressed agent memory vs flat-vector and full-transcript: enoch://control-plane/projects/anchor-compressed-agent-memory-vs-flat-vector-and-full-transcript-ba4e30b0d89d/runs/anchor-compressed-agent-memory-vs-flat-vector-and-full-transcript-ba4e30b0d89d-20260629T191222120781+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cdcc5f8089e1

## What looked useful

Across 500 main-run cases and 1500 queried anchors at budget 180, anchor_compressed recovered 100.0% of queried values versus 1.4% for centrality summary, 15.5% for recency summary, and 19.7% for a corrupted-value anchor-shaped control. A 300-case budget sweep from 60 to 240 tokens kept anchor_compressed at 100.0% while the best non-anchor generic summary stayed below 18.9%.

## Boundaries and scale limits

Synthetic/proxy-only evidence: no live LLM-generated traces, no LLM summarizer baseline, no learned or noisy anchor extractor, no downstream LLM reader, and no real production agent trace distribution.

## Claim scope

In deterministic synthetic agent-like traces with sparse explicit anchors and regex extraction, a budget-matched anchor-table-plus-summary memory preserves queried anchor facts far better than generic extractive lossy summaries or recency summaries.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the anchor-preservation mechanism only in a deterministic synthetic proxy, not in real LLM trace and summary conditions.

## Recommended next action

Run a bounded local follow-up using small LLM-generated traces and LLM-produced lossy summaries, then score anchor recovery through a model reader rather than regex extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-summary validation of anchor-compressed memory on generated agent traces
- Success threshold: Anchor-table memory improves exact answer accuracy by at least 0.25 absolute over the best non-anchor summary baseline with non-overlapping or clearly separated bootstrap confidence intervals.
- Stop condition: Stop if anchor-table accuracy is within 0.10 absolute of the best non-anchor baseline or if noisy anchor extraction causes more than 10% false-value answers.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-compressed-memory-on-llm-generated-agent-traces-wit-ca9373ed8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
