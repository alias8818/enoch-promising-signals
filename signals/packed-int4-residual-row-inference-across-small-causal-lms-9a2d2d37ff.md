# Packed INT4 residual-row inference across small causal LMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `packed-int4-residual-row-inference-across-small-causal-lms-9a2d2d37ff`
Run ID: `packed-int4-residual-row-inference-across-small-causal-lms-9a2d2d37ff-20260614T022758657718+0000`

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

- Parent run decision: INT4 Extreme Quantization with Residual Channel Preservation: enoch://control-plane/projects/int4-extreme-quantization-with-residual-channel-preservation-9a88f9a4ed6d/runs/int4-extreme-quantization-with-residual-channel-preservation-9a88f9a4ed6d-20260614T020522825021+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

At 10% residual rows, storage was about 0.351x dense FP16 and median relative RMSE improved on real checkpoints, but packed-path latency was only 0.066x-0.078x dense FP16 median. The idea has a compression/error mechanism signal but no practical latency support without a fused kernel.

## Boundaries and scale limits

Tested only 2D linear/embedding matrices from gpt2 and distilgpt2 plus synthetic GPT-2-shaped matrices; no full generation benchmark, custom fused INT4 kernel, perplexity evaluation, or larger-model validation.

## Claim scope

Direct Tier 1 CUDA benchmark on GPT-2-small-class causal LM matrices shows packed INT4 plus exact residual output rows reduces storage and relative output RMSE versus plain INT4, but a generic packed unpack/dequant PyTorch inference path is much slower than dense FP16.

## Why it stopped

Direct Tier 1 evidence supports the residual-row error/storage mechanism but falsifies the practical inference-speed claim for the available packed PyTorch path; this is not full validation or paper-positive evidence.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded fused CUDA/Triton packed INT4 residual-row kernel test on the same gpt2 and distilgpt2 matrices.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused packed INT4 residual-row kernel for GPT-2 projection matrices
- Success threshold: At 10% residual rows, fused packed INT4 residual-row inference is at least 1.10x dense FP16 median latency for token=1 and token=128 on gpt2 and distilgpt2 projection matrices, with storage <=0.36x dense and relative RMSE no worse than the current 10% residual-row reference.
- Stop condition: Stop if the fused kernel is below 0.95x dense FP16 median latency on either token=1 or token=128 after a correct implementation, or if residual correction cannot be fused without exceeding 0.36x dense storage.

## Evidence references

- Artifact root: `<local-path>/projects/packed-int4-residual-row-inference-across-small-causal-lms-9a2d2d37ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
