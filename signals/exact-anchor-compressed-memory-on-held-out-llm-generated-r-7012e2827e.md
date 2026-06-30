# Exact-anchor compressed memory on held-out LLM-generated repeated-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-compressed-memory-on-held-out-llm-generated-r-7012e2827e`
Run ID: `exact-anchor-compressed-memory-on-held-out-llm-generated-r-7012e2827e-20260619T021649426993+0000`

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

- Parent run decision: Compressed-State Agent Memory with Exact Anchors: enoch://control-plane/projects/compressed-state-agent-memory-with-exact-anchors-dc9601f4b701/runs/compressed-state-agent-memory-with-exact-anchors-dc9601f4b701-20260614T114343910552+0000
- Parent run decision: Exact-anchor compressed memory on real or LLM-generated repeated-agent traces: enoch://control-plane/projects/exact-anchor-compressed-memory-on-real-or-llm-generated-re-ac330ec9fa/runs/exact-anchor-compressed-memory-on-real-or-llm-generated-re-ac330ec9fa-20260614T121020689869+0000

## What looked useful

Exact per-agent source anchors appear necessary when compressed memory must answer source-faithful repeated-agent recall queries; summary-only compression can preserve values while losing the exact-anchor target.

## Boundaries and scale limits

No external held-out LLM trace corpus was available; traces were locally generated from deterministic templates, extraction was pattern-based, and no LLM/judged natural-language robustness baseline was run.

## Claim scope

On deterministic LLM-style synthetic repeated-agent traces with fixed held-out seeds, exact-anchor compressed memory recovered both current durable values and exact source anchors under the tested memory budget, outperforming transcript search, flat retrieval, summary-only compression, and wrong-agent-anchor ablation.

## Why it stopped

Mechanism threshold was met on a bounded synthetic benchmark, but evidence is not publication-grade because the traces and extractor are template-constrained rather than real held-out LLM traces.

## Recommended next action

Stop this run as no-paper useful-signal evidence; deepen with a real held-out LLM-generated trace corpus and paraphrase-robust extraction before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor compressed memory on real held-out LLM-generated repeated-agent traces
- Success threshold: Full exact-anchor accuracy >= 0.85 and >= +0.15 absolute margin over the best non-exact-anchor control, with extraction failure rate <= 0.10.
- Stop condition: Stop as unsupported if exact-anchor compressed memory falls below 0.75 full exact-anchor accuracy or fails to beat the best control by at least +0.05 on two fixed held-out shards.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-compressed-memory-on-held-out-llm-generated-r-7012e2827e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
