# Multi-trace noisy-anchor replay validation for anchor-linked compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-trace-noisy-anchor-replay-validation-for-anchor-link-998276cdc2`
Run ID: `multi-trace-noisy-anchor-replay-validation-for-anchor-link-998276cdc2-20260614T004739910427+0000`

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

- Parent run decision: Real-trace anchor-linked compression replay validation: enoch://control-plane/projects/real-trace-anchor-linked-compression-replay-validation-4e06ba330f/runs/real-trace-anchor-linked-compression-replay-validation-4e06ba330f-20260614T001704566874+0000
- Parent run decision: Trace-Derived Semantic Compression with Anchor-Linked Retrieval: enoch://control-plane/projects/trace-derived-semantic-compression-with-anchor-linked-retrieval-e0259426ab2f/runs/trace-derived-semantic-compression-with-anchor-linked-retrieval-e0259426ab2f-20260613T212251779085+0000

## What looked useful

Anchor-linked compression averaged 0.7934 answer accuracy at 0.1306 memory/full-events. Full transcript search averaged 0.4386 accuracy at 1.0000 memory/full-events; flat alias retrieval and the no-alias-link ablation averaged 0.4388 accuracy at about 0.8702 memory/full-events. Latest-trace-only anchor memory averaged 0.1938 accuracy, supporting the need for multi-trace persistence.

## Boundaries and scale limits

Synthetic structured facts only; no LLM extraction, no naturalistic operator traces, no learned retriever baseline, and no production-scale memory store.

## Claim scope

In a deterministic synthetic replay benchmark with 6 fixed seeds, 4 alias-noise levels, 8 traces, 48 anchors, and distractor events, anchor-linked compression improved noisy-anchor fact replay accuracy over transcript and flat-alias baselines while using about 13% of full-event memory units.

## Why it stopped

Tier 2 synthetic evidence supports the mechanism, but this is no-paper evidence because real agent traces, LLM extraction behavior, and stronger retrieval baselines were not tested.

## Recommended next action

Run a bounded deepen follow-up on naturalistic or LLM-generated replay traces with an equal-budget embedding/learned retriever baseline and measured entity-link precision/recall before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic noisy-anchor replay with equal-budget retriever baseline
- Success threshold: Across at least 5 fixed seeds and 3 noise levels, anchor-linked compression must exceed the strongest equal-budget retriever baseline by at least 15 absolute accuracy points, maintain at least 0.70 answer accuracy, and use no more than 20% of full-transcript memory units.
- Stop condition: Stop as unsupported if the equal-budget retriever closes the accuracy gap below 5 absolute points, if anchor-link precision falls below 0.80 on naturalistic aliases, or if compression rises above 20% of full-transcript memory units.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-noisy-anchor-replay-validation-for-anchor-link-998276cdc2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
