# EmbRes-Q: INT2 embeddings with frequency-aware residual channel

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embres-q-int2-embeddings-with-frequency-aware-residual-channel-86d2dfd1ae5f`
Run ID: `embres-q-int2-embeddings-with-frequency-aware-residual-channel-86d2dfd1ae5f-20260610T115130859962+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ff79ed4c30e8

## What looked useful

Frequency-aware residual row selection consistently beat random and rare-row residual policies on frequency-weighted MSE and frequent-row nearest-neighbor overlap across 5%, 10%, and 20% residual budgets on both tested embedding sources.

## Boundaries and scale limits

No downstream model training, no packed INT2 kernel, no real serving throughput, no large vocabulary LM/recommender validation, and no metadata/scale overhead accounting beyond the simple 2 + 8*residual_fraction bits/value payload estimate.

## Claim scope

In synthetic Zipf-structured embeddings and a Tiny Shakespeare PPMI/SVD word-embedding proxy, an INT2 embedding table plus an int8 residual channel assigned to the most frequent 5-20% of rows reduced frequency-weighted reconstruction error and improved frequent-row nearest-neighbor preservation compared with plain INT2 and equal-size random or rare-row residual allocation.

## Why it stopped

Closed as a proxy useful-signal result: the mechanism is supported for embedding reconstruction, but this is not full downstream validation or paper-ready evidence.

## Recommended next action

Run a bounded downstream validation with a small LM or recommender, comparing dense, INT2, INT3/INT4, and EmbRes-Q under equal training/evaluation conditions and measuring packed lookup memory and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small downstream validation of frequency-aware INT2 embedding residuals
- Success threshold: Frequency-residual INT2 must improve the downstream metric by at least 20% of the dense-vs-INT2 quality gap over plain INT2, beat random residual allocation at the same residual budget, and stay within 10% of the target packed-memory budget.
- Stop condition: Stop if frequency-residual allocation fails to beat random residual allocation on downstream quality at two residual budgets, or if metadata/latency overhead removes the intended memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/embres-q-int2-embeddings-with-frequency-aware-residual-channel-86d2dfd1ae5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
