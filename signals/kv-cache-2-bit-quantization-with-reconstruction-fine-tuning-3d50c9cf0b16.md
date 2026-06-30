# KV cache 2-bit quantization with reconstruction fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-2-bit-quantization-with-reconstruction-fine-tuning-3d50c9cf0b16`
Run ID: `kv-cache-2-bit-quantization-with-reconstruction-fine-tuning-3d50c9cf0b16-20260610T230427548468+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6e35676d305a

## What looked useful

MSE-based reconstruction calibration reduced K/V cache MSE by 21-24% but worsened NLL versus raw 2-bit cache by +1.21 to +1.51, indicating standalone cache reconstruction error was misaligned with autoregressive language-model quality in this setup.

## Boundaries and scale limits

Small model, short-context WikiText-2 probe; int2 numerics are simulated with dequantized PyTorch tensors, so packed-kernel memory/latency and 7B+ long-context behavior were not validated. Reconstruction was closed-form affine calibration, not full task-loss fine-tuning.

## Claim scope

On distilgpt2 with 128-token WikiText-2 chunks, raw per-token/per-head 2-bit min/max KV-cache quantization moderately degrades next-token NLL, while scalar and per-channel affine cache reconstruction calibrated to K/V MSE further worsens task loss despite reducing cache MSE.

## Why it stopped

Proxy/early falsification of MSE-based affine reconstruction calibration, not a full validation or full disproof of task-loss fine-tuned 2-bit KV-cache reconstruction.

## Recommended next action

Stop this MSE-calibrated reconstruction path; a bounded follow-up should optimize reconstruction adapters against next-token or attention-output loss before any larger-scale packed int2 validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Task-loss-optimized 2-bit KV-cache reconstruction adapters
- Success threshold: Held-out NLL for task-loss-trained reconstruction is at least 50% closer to fp-cache NLL than raw 2-bit cache and does not regress perplexity on a second held-out text sample.
- Stop condition: Stop if task-loss-trained reconstruction fails to beat raw 2-bit NLL by at least 0.10 after a bounded GPU run under 2 hours or if gains require storing per-token metadata that erases most of the nominal 8x KV-cache compression.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-2-bit-quantization-with-reconstruction-fine-tuning-3d50c9cf0b16`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
