# Anchor-Preserved Semantic Memory for Long-Horizon Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-preserved-semantic-memory-for-long-horizon-agent-tasks-dd76e8cb20c3`
Run ID: `anchor-preserved-semantic-memory-for-long-horizon-agent-tasks-dd76e8cb20c3-20260629T020214491757+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed224b707225

## What looked useful

Anchor identity and active-status preservation was the decisive mechanism: flat semantic memory matched the anchor method on long no-noise controls but failed under moderate unanchored semantic noise, while anchor-preserved memory stayed at 1.000 exact match.

## Boundaries and scale limits

Synthetic CPU-only proxy; no real LLM agent loop, no learned embedding retriever, no real repository/operator traces, no adversarial anchor corruption, and no large-scale or overnight validation.

## Claim scope

In a deterministic synthetic replay benchmark with 240 long-horizon tasks, 96 events per task, and unanchored draft/stale semantic distractors, anchor-preserved memory recovered committed active facts keyed by stable anchors while no-memory, recent transcript window, and flat semantic memory baselines failed.

## Why it stopped

Proxy-only synthetic mechanism evidence is useful but insufficient for paper-positive closure or broad validation.

## Recommended next action

Stop this run as proxy-only useful signal; next run should replay real or LLM-generated long-horizon agent traces through an actual retriever/summarizer with anchor-preservation ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic agent-trace validation of anchor-preserved memory under noisy writes
- Success threshold: Anchor-preserved memory improves exact-match recall by at least 20 percentage points over flat semantic retrieval and reduces stale/draft value errors by at least 50 percent on the held-out replay set.
- Stop condition: Stop if the anchor-preserved variant fails to beat flat semantic retrieval by 10 percentage points, or if most errors come from anchor extraction/corruption rather than retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-semantic-memory-for-long-horizon-agent-tasks-dd76e8cb20c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
