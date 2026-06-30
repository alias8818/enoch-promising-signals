# Sparse Anchor Highway Attention for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `sparse-anchor-highway-attention-for-long-context-6b0c524e2809`
Run ID: `sparse-anchor-highway-attention-for-long-context-6b0c524e2809-20260528T005453305413+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bac6899505f0

## What looked useful

The learnable 128-token task showed dense attention above chance on far retrieval (0.1966), local attention near chance on far retrieval (0.0595), and anchor_read/anchor_highway also near chance on far retrieval (0.0609-0.0613) despite using more attention edges.

## Boundaries and scale limits

Synthetic retrieval only; sequence lengths 128 and 256; 110k-378k parameter models; dense PyTorch masked attention rather than fused sparse kernels; no natural-language perplexity or GPT-2-small-class training.

## Claim scope

In a CUDA-trained tiny-transformer synthetic key-value retrieval benchmark, periodic anchor-read and anchor-highway causal masks did not improve far retrieval over a local sliding-window mask, even when anchor density increased from stride 16 to stride 8.

## Why it stopped

Proxy early falsification: in the bounded learnable synthetic task, the tested periodic anchor-highway masks failed to improve long-range retrieval over local attention, so the current mechanism is not worth paper escalation.

## Recommended next action

Stop this formulation as no-paper evidence; only revisit with explicit learned anchor tokens or an auxiliary anchor summarization objective and require a far-retrieval gain over local sparse attention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Explicit Learned Anchor Tokens for Sparse Long-Range Retrieval
- Success threshold: At <=0.45 allowed-edge fraction versus dense, explicit-anchor far accuracy improves by at least 5 absolute percentage points over local and is above 0.10 on the 16-value 128-token retrieval task across mean of three seeds.
- Stop condition: Stop if explicit-anchor variants remain within 2 absolute percentage points of local far accuracy after three seeds or require >0.60 dense edge fraction to exceed local.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-anchor-highway-attention-for-long-context-6b0c524e2809`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
