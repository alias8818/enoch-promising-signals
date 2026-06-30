# Largest GPT-2-class model trainable under 8GB VRAM cap across optimizers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `largest-gpt-2-class-model-trainable-under-8gb-vram-cap-across-optimizers-5080e1fcf866`
Run ID: `largest-gpt-2-class-model-trainable-under-8gb-vram-cap-across-optimizers-5080e1fcf866-20260614T100321955649+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8e64d1d89fb2

## What looked useful

Optimizer state materially changes the largest GPT-2-class model that can complete a one-step update under an 8 GiB allocator cap: AdamW was limited to about 977M parameters, while Adafactor and SGD-family optimizers crossed 1B parameters, with plain SGD reaching 1.766B parameters in this scoped setup.

## Boundaries and scale limits

This was a one-step synthetic memory feasibility sweep on GB10 UMA-style memory, not a discrete 8GB GPU validation or a real-data convergence study. It did not test multi-step stability, throughput, checkpointing, no-gradient-checkpointing mode, larger batches, other sequence lengths, fused optimizers, 8-bit optimizers, ZeRO/offload, or optimizer quality.

## Claim scope

On NVIDIA GB10 with PyTorch 2.12.0+cu130 and Transformers 4.57.6, a synthetic one-step bf16 GPT-2-shaped 12-layer causal LM training update with batch size 1, sequence length 1024, gradient checkpointing, and an 8 GiB PyTorch CUDA allocator cap passed up to 976.9M parameters for AdamW, 1.400B for Adafactor, 1.287B for SGD with momentum, and 1.766B for plain SGD.

## Why it stopped

The result is a bounded synthetic one-step memory feasibility signal rather than full validation of trainability or convergence under a general 8GB VRAM claim.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is a short real-data multi-step repeat on the boundary candidates and first-failing neighbors, preferably on both GB10 and a discrete 8GB NVIDIA GPU.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data multi-step validation of 8 GiB GPT-2-class optimizer boundaries
- Success threshold: Each best boundary candidate completes the planned multi-step run with peak allocated memory <= 8 GiB, no OOM, finite loss, and successful checkpoint save/load; each first-failing neighbor either fails under the cap or is documented as overturning the one-step boundary.
- Stop condition: Stop if any optimizer's best boundary candidate cannot complete 100 real-data steps under the 8 GiB cap, or if discrete-GPU telemetry contradicts the GB10 UMA allocator-based ranking.

## Evidence references

- Artifact root: `<local-path>/projects/largest-gpt-2-class-model-trainable-under-8gb-vram-cap-across-optimizers-5080e1fcf866`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
