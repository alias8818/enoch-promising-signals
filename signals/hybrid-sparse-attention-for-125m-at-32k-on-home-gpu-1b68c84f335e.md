# Hybrid Sparse Attention for 125M at 32K on Home GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-sparse-attention-for-125m-at-32k-on-home-gpu-1b68c84f335e`
Run ID: `hybrid-sparse-attention-for-125m-at-32k-on-home-gpu-1b68c84f335e-20260527T211202185902+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8e6317e9d84d

## What looked useful

At 32K, the hybrid pattern reduced theoretical attention pairs by 96.13%, but the straightforward blockwise sparse prototype took 0.03675 s median versus 0.01754 s for dense fused causal SDPA, with similar peak CUDA allocation. Dense SDPA fit and ran at the target single-layer shape on GB10.

## Boundaries and scale limits

No full 125M model, no training/backward pass, no language-model quality metrics, and no fused block-sparse kernel were tested. Results cover attention mechanics only, not end-to-end model viability.

## Claim scope

Synthetic single-forward attention-layer benchmark on GB10 for GPT-2-small-class attention shape [1, 12, 32768, 64] in BF16, comparing PyTorch dense causal SDPA against a Python/PyTorch blockwise hybrid local-window-plus-global-prefix sparse prototype.

## Why it stopped

Proxy attention-only evidence falsified the practical benefit of a straightforward hybrid sparse prototype at 32K; this is not a full model validation.

## Recommended next action

Stop this run as no-paper useful evidence; only continue via a bounded fused block-sparse kernel/end-to-end transformer-block follow-up with dense SDPA as the control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused Block-Sparse Hybrid Attention vs Dense SDPA at 32K
- Success threshold: At 32K, fused hybrid sparse attention or a full transformer block using it is at least 1.25x faster or uses at least 25% less peak memory than dense SDPA while passing correctness and a small quality proxy.
- Stop condition: Stop if the fused sparse path is slower than dense SDPA, fails correctness, or shows severe quality-proxy degradation at the target 32K shape.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-sparse-attention-for-125m-at-32k-on-home-gpu-1b68c84f335e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
