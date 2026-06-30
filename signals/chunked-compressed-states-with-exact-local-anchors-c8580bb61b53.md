# Chunked Compressed States with Exact Local Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `chunked-compressed-states-with-exact-local-anchors-c8580bb61b53`
Run ID: `chunked-compressed-states-with-exact-local-anchors-c8580bb61b53-20260530T022032435294+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/daf43b4f85d4

## What looked useful

Two exact anchors per chunk reduced anchor-window MSE to about 0.709x of chunked SVD and boundary-jump MSE to 0.0x, but increased total relative MSE to about 1.025x and linear-probe MSE to about 1.027x. More anchors worsened the tradeoff.

## Boundaries and scale limits

Tested only synthetic trajectories at length 2048, dimension 128, chunk size 128, budget ratio 0.22, five seeds, and three trajectory regimes. No real transformer KV-cache, perplexity, retrieval, or generation-quality experiment was run.

## Claim scope

Under a controlled hidden-state-like reconstruction proxy with equal scalar memory budget, exact local anchors in chunked compressed states guarantee selected local states and eliminate chunk-boundary jump error, but they do not improve overall state reconstruction or linear readout preservation.

## Why it stopped

Proxy evidence supports only local-fidelity benefits and shows an equal-budget global/readout cost, so this is not publication-grade support for the broad hypothesis.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test adaptive exact anchors on real small-transformer KV/cache states at fixed memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Exact Anchors for Small-Transformer KV Cache Compression
- Success threshold: Adaptive anchors improve anchor-proximal retrieval/copy accuracy by at least 10% relative or reduce local cache reconstruction error by at least 20% while keeping total perplexity or next-token loss degradation within 1% of chunked compression at the same memory budget.
- Stop condition: Stop if adaptive anchors still increase global reconstruction/readout or perplexity loss by more than 2% at matched memory, or if gains appear only at exact anchor positions with no downstream task benefit.

## Evidence references

- Artifact root: `<local-path>/projects/chunked-compressed-states-with-exact-local-anchors-c8580bb61b53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
