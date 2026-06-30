# Shared Residual Projection for LM Head and Embedding Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `shared-residual-projection-for-lm-head-and-embedding-quantization-121740abc8fd`
Run ID: `shared-residual-projection-for-lm-head-and-embedding-quantization-121740abc8fd-20260628T131242050531+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/87c0c852268e

## What looked useful

The shared residual mechanism recovers some int4 error, but its storage overhead is a poor trade versus spending the same bits on scalar precision. This is a useful early negative control for the simple shared-residual formulation.

## Boundaries and scale limits

Synthetic matrices only; no real pretrained model weights, perplexity, downstream tasks, activation quantization, or GPU inference throughput were tested. Matrix size was 8192x256 with 512 sampled hidden states.

## Claim scope

In a bounded NumPy proxy over synthetic tied embedding/LM-head matrices, int4 plus a shared SVD low-rank residual improves plain int4 but is dominated by rowwise int5/int6 at comparable effective bits per weight.

## Why it stopped

Early proxy falsification: the proposed simple shared residual improves int4 but loses decisively to bit-matched higher precision controls, so current evidence is not paper-worthy or storage-efficient.

## Recommended next action

Stop this run as a proxy negative; if continuing, run a real GPT-2-small-class tied-weight perplexity test with matched-bpw int5/int6 and modern low-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tied-weight perplexity test for shared residual quantization
- Success threshold: At matched effective bits per weight, int4 plus shared residual improves perplexity/logit RMSE over int5 at rank16-class storage or over int6 at rank32-class storage without worse top-k agreement.
- Stop condition: Stop if real-model int4 plus shared residual again trails bit-matched int5/int6 on perplexity and logit metrics, or if dependency/runtime constraints prevent loading a real tied-weight model locally.

## Evidence references

- Artifact root: `<local-path>/projects/shared-residual-projection-for-lm-head-and-embedding-quantization-121740abc8fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
