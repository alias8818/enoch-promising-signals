# Anchor-Preserved KV Eviction for Long-Context Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserved-kv-eviction-for-long-context-inference-d908c8d89e9e`
Run ID: `anchor-preserved-kv-eviction-for-long-context-inference-d908c8d89e9e-20260603T182844653517+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f0f7bab3ad5a

## What looked useful

Anchor+recent retention improved selected-anchor retrieval MSE in all 12 positive-affinity cases, with best retrieval MSE ratio 0.178x versus recent-only. However, it worsened MSE to the full-attention output in all 12 positive-affinity cases, with worst full-output MSE ratio 7.139x. The zero-affinity control stayed near parity, with full-output MSE ratio 0.982-1.017.

## Boundaries and scale limits

No pretrained language model, tokenizer, multi-layer cache dynamics, real long-context benchmark, production serving latency, or 7B+ validation was tested. The result is a mechanism probe, not an end-to-end inference result.

## Claim scope

Synthetic single-layer attention benchmark with sequence length 4096, 512 decode queries, dimension 64, 64 fixed prefix anchors, budgets 128-1024, and controlled query affinity to anchor keys. Anchor+recent KV retention was compared against same-budget recent-only and random-old+recent controls.

## Why it stopped

Bounded synthetic evidence supports the retrieval mechanism but falsifies the unqualified naive hypothesis that fixed anchor preservation is a drop-in full-attention approximation; this is a proxy mechanism result, not full validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded test should evaluate calibration-aware anchor eviction in a small pretrained transformer on real retrieval and non-retrieval long-context prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibration-Aware Anchor KV Eviction in a Small Pretrained Transformer
- Success threshold: Calibration-aware anchor eviction must retain at least 80% of the retrieval gain of naive anchor+recent while reducing full-KV output divergence by at least 30% versus naive anchor+recent at the same cache budget, without degrading non-retrieval controls by more than 2%.
- Stop condition: Stop if calibration-aware eviction does not improve full-KV divergence over naive anchor+recent on the synthetic reproduction and at least one small pretrained-model prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-kv-eviction-for-long-context-inference-d908c8d89e9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
