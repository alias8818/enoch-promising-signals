# Sparse Anchor-Retrieval Attention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-anchor-retrieval-attention-2be3e53d9097`
Run ID: `sparse-anchor-retrieval-attention-2be3e53d9097-20260531T153331065583+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a71920fc2d04

## What looked useful

The mechanism is viable only when important tokens are reliably anchored and retrievable. Local, fixed-stride, and random sparse controls failed at comparable fanout, but exact anchor scoring shifts dense work into the retrieval stage.

## Boundaries and scale limits

No trained transformer, no learned anchor formation, no natural-language benchmark, and no proof of end-to-end speedup; the tested sparse method still scored all 512 typed anchors before selecting top-k.

## Claim scope

On a synthetic associative-recall proxy with explicit typed key anchors, sparse anchor retrieval matched dense retrieval accuracy while reducing final query attention fanout from 1025 edges to 1 edge.

## Why it stopped

Proxy evidence supports the typed-anchor mechanism but does not validate learned anchors, sublinear retrieval, real-model quality, or end-to-end efficiency.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should replace exact all-anchor scoring with an approximate or hierarchical anchor index and measure recall versus score-count/runtime.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Approximate Indexed Sparse Anchor Retrieval
- Success threshold: At 2048 and 8192 anchors, approximate indexed retrieval retains at least 98% of exact-retrieval accuracy while scoring no more than 10% of anchors and improving wall-clock query time versus exact scoring.
- Stop condition: Stop if approximate retrieval drops below 95% of exact accuracy at 2048 anchors or fails to reduce measured query time despite scoring fewer anchors.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-anchor-retrieval-attention-2be3e53d9097`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
