# Extreme INT4 Residual Channel Quantization for gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int4-residual-channel-quantization-for-gb10-1e51b952ae12`
Run ID: `extreme-int4-residual-channel-quantization-for-gb10-1e51b952ae12-20260610T201149316780+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fb7c04855f43

## What looked useful

Importance-selected residual channels are only worthwhile when quantization error is channel-concentrated. In no-tail synthetic layers, importance selection was indistinguishable from random residual storage; in heavy-tail settings it clearly outperformed random and magnitude controls, but at a storage cost that reduced compression from 3.88x to about 3.36x versus FP16 for 4% residual channels.

## Boundaries and scale limits

No packed INT4 kernel, no fused sparse residual kernel, no real pretrained model perplexity or downstream quality evaluation, no comparison against GPTQ/AWQ/NF4-style baselines, and no end-to-end serving throughput evidence. Timing is only a dequantized FP16 matmul proxy on GB10.

## Claim scope

On synthetic GB10 CUDA tensor tests for GPT-2-small and LLaMA-like linear layer shapes, preserving 4% importance-selected residual input channels in FP16 reduced per-layer INT4 output relative MSE by 5.65% to 12.21% versus plain group-128 INT4 under the default heavy-tailed setting, and by 23.31% on a stronger tail-sensitivity case.

## Why it stopped

The result supports a bounded mechanism but remains synthetic/proxy-only and does not establish production viability or paper-ready model-quality and throughput claims.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should implement a fused packed INT4 plus residual-channel CUDA kernel and compare end-to-end quality on a real small pretrained transformer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused GB10 INT4 plus residual-channel kernel on a real small transformer
- Success threshold: At matched or lower memory than a strong 4-bit baseline, recover at least half of the observed residual-channel layerwise MSE reduction, keep perplexity degradation within an agreed small-model threshold, and show non-negative GB10 latency or throughput impact versus the relevant baseline.
- Stop condition: Stop if the fused residual correction erases INT4 throughput gains, if real-model quality does not improve over plain INT4 at matched memory, or if established baselines dominate both quality and runtime.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-residual-channel-quantization-for-gb10-1e51b952ae12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
