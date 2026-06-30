# Exact Anchor Rolling Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-rolling-memory-1794315c31e5`
Run ID: `exact-anchor-rolling-memory-1794315c31e5-20260604T204824413689+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e92de2eb0aa4

## What looked useful

Exact retention is useful only with sufficient anchor budget or a strong admission/eviction policy. Exactness alone is not robust: FIFO exact-anchor memory lost to an equal-budget reservoir anchor control by about 2x in over-budget old-query scenarios.

## Boundaries and scale limits

No LLMs, no real documents, no learned anchor detector, no training or serving benchmark; single-process CPU proxy over synthetic streams with 8 seeds and three scenarios.

## Claim scope

Synthetic keyed-anchor streams under equal token budgets: exact-anchor rolling memory gives perfect retrieval when marked anchors fit in the reserved exact budget, but FIFO exact-anchor retention degrades sharply and underperforms reservoir sampling when anchors exceed budget and queries target older anchors.

## Why it stopped

Proxy evidence supports the narrow mechanism but falsifies the stronger naive FIFO exact-anchor claim; this is not direct/full validation and is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should compare FIFO, reservoir, priority, and oracle exact-anchor admission on semi-real long-document retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact Anchor Admission Policies on Semi-Real Long-Document Retrieval
- Success threshold: Priority exact-anchor memory improves old-anchor exact-match recall by at least 20 percentage points over reservoir and FIFO controls at the same memory budget in saturated-anchor scenarios.
- Stop condition: Stop if priority admission fails to beat reservoir by at least 5 percentage points on old-anchor recall or only wins on synthetic marker artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-rolling-memory-1794315c31e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
