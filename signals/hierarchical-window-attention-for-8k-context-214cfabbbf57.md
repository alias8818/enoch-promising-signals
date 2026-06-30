# Hierarchical Window Attention for 8K Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-window-attention-for-8k-context-214cfabbbf57`
Run ID: `hierarchical-window-attention-for-8k-context-214cfabbbf57-20260522T172934372955+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/79d3f7dbc52f

## What looked useful

At 8K tokens the hierarchical pattern reduced logical attention edges to 6.53% of dense and gave the final token 287 keys, but measured 3.188 ms mean versus 0.894 ms for dense SDPA and used 85.3 MB peak allocated versus 75.8 MB. Edge sparsity did not translate into performance with a naive blockwise implementation.

## Boundaries and scale limits

No training quality, backward-pass, fused-kernel, multi-batch, or 7B+ model evidence was produced. Summary tokens were mean key/value block summaries, and Python block loops likely understate the potential of a fused sparse kernel.

## Claim scope

A straightforward PyTorch blockwise hierarchical-window attention implementation for 8K causal forward passes on NVIDIA GB10 is functionally valid but slower and slightly higher in peak allocated memory than optimized dense causal SDPA at batch=1, heads=8, head_dim=64, fp16, window/block=256.

## Why it stopped

Proxy implementation-level falsification: the tested naive hierarchical-window attention did not beat dense SDPA at 8K, so this run is not paper-ready and should not claim architectural quality or full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next meaningful bounded test is a fused CUDA/Triton hierarchical-window kernel benchmark with forward and backward latency against dense SDPA.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused Hierarchical Window Attention Kernel for 8K Forward/Backward
- Success threshold: Fused hierarchical attention is at least 1.5x faster than dense SDPA for 8K forward+backward and uses at least 25% less peak memory while passing correctness checks within fp16 tolerance.
- Stop condition: Stop if a fused implementation cannot beat dense SDPA on both latency and memory at 8K after validating correctness, or if kernel development becomes the dominant blocker without benchmarkable results.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-window-attention-for-8k-context-214cfabbbf57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
