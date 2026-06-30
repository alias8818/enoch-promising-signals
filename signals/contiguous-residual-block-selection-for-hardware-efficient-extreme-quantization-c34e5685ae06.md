# Contiguous Residual Block Selection for Hardware-Efficient Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `contiguous-residual-block-selection-for-hardware-efficient-extreme-quantization-c34e5685ae06`
Run ID: `contiguous-residual-block-selection-for-hardware-efficient-extreme-quantization-c34e5685ae06-20260529T142613357364+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f7118403712

## What looked useful

Across 9 synthetic sweep configurations, contiguous greedy blocks recovered a mean 67.8% of unstructured top-k's error reduction, improved over random contiguous selection by 3.15 percentage points, reduced row segment count by 92.1%, and showed a 15.16x mean CPU residual-application proxy speedup.

## Boundaries and scale limits

No real transformer weight matrices, perplexity, downstream task metrics, GPU kernels, accelerator kernels, or full serving benchmarks were validated. Hardware efficiency is represented only by segment count and a CPU residual-application proxy.

## Claim scope

Synthetic 512x512 matrix probes under rowwise 2-bit quantization show that greedy contiguous residual blocks are a reproducible middle point: they recover more quantization error than random contiguous blocks and use far fewer row segments than unstructured top-k, but recover less error than top-k.

## Why it stopped

Synthetic/proxy evidence supports a useful mechanism signal but is not direct or broad enough for a paper-positive hardware-efficient quantization claim.

## Recommended next action

Run a bounded direct follow-up on real GPT-2-small-class or comparable open transformer weight matrices with perplexity and a kernel-aware residual application benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer Contiguous Residual Block Validation
- Success threshold: Contiguous residual blocks retain at least 60% of top-k reconstruction error reduction, reduce row segments by at least 85%, beat random contiguous controls, and keep perplexity degradation within a predeclared acceptable bound versus top-k residuals.
- Stop condition: Stop if real-weight contiguous blocks fall below 50% of top-k reconstruction benefit or fail to beat random contiguous controls on most evaluated layers at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/contiguous-residual-block-selection-for-hardware-efficient-extreme-quantization-c34e5685ae06`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
