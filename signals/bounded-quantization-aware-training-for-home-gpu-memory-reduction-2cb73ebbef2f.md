# Bounded Quantization-Aware Training for Home GPU Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-quantization-aware-training-for-home-gpu-memory-reduction-2cb73ebbef2f`
Run ID: `bounded-quantization-aware-training-for-home-gpu-memory-reduction-2cb73ebbef2f-20260607T191415256298+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3b3ec81cde58

## What looked useful

The memory-saving mechanism is not ordinary fake quantization-aware training. Memory reduction requires compressing resident training state. In this probe, fake-QAT Adam had 1.0x persistent memory and 1.31x peak algorithmic memory versus fp32 Adam, while int8-state SGD had 0.065x persistent and 0.565x peak memory but lower validation accuracy: 0.580 versus 0.656 for fp32 Adam.

## Boundaries and scale limits

CPU-only small MLP proxy; no CUDA/PyTorch stack available; no transformer, GPT-2-small-class, real home-GPU allocator telemetry, long token budget, or production quantized kernels were tested.

## Claim scope

On a deterministic NumPy MLP synthetic classification probe, standard fake-QAT Adam did not reduce persistent training memory versus fp32 Adam because fp32 master weights, gradients, and Adam moments remained resident; a distinct int8 resident-state SGD variant reduced explicit training-state memory but degraded validation accuracy.

## Why it stopped

Proxy early falsification of the broad QAT-memory claim: standard fake-QAT did not reduce training memory in explicit state accounting, and the compressed-state variant that did reduce memory is a different algorithm with observed quality loss.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded direct test should run on a real home GPU with PyTorch allocator telemetry and a GPT-2-small-class or parameter-matched transformer baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Home-GPU Transformer Test of Fake-QAT Versus Compressed-State Low-Bit Training
- Success threshold: At least 35% measured CUDA peak-memory reduction versus fp32 AdamW with no more than 5% relative validation-loss degradation at the same token budget.
- Stop condition: Stop if fake-QAT AdamW reports peak memory within 10% of fp32 AdamW and the compressed-state optimizer either fails to run reproducibly or exceeds 5% relative validation-loss degradation after the fixed sequence-item budget.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-quantization-aware-training-for-home-gpu-memory-reduction-2cb73ebbef2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
