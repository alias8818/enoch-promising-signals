# CPU-Resident LoRA Optimizer States

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-resident-lora-optimizer-states-aa0cef7da8b9`
Run ID: `cpu-resident-lora-optimizer-states-aa0cef7da8b9-20260524T171843316981+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7fced0aef310

## What looked useful

Moving fp32 Adam m/v states to CPU removes 8 bytes per trainable LoRA parameter from accelerator memory, a 66.7% reduction of the LoRA parameter+gradient+Adam-state footprint under bf16 parameter/gradient accounting. On this host, measured combined CPU update plus same-host copy time ranged from 0.0015s at 0.262M params to 5.42s at 67.1M params, making the naive CPU optimizer path plausible only for small/q-v LoRA settings without further optimization or overlap.

## Boundaries and scale limits

No GPU/CUDA device was visible, so accelerator residency, pinned memory, async transfer overlap, framework scheduling, convergence, and tokens/sec were not directly tested. Largest direct tensor benchmark was 67.1M trainable parameters; larger adapter scenarios are estimates from local measurements.

## Claim scope

CPU-only mechanism probe for CPU-resident Adam moments on LoRA-sized flat tensors, plus exact memory accounting for representative GPT-2-small, LLaMA-7B-class, and LLaMA-70B-class adapter shapes. The result supports accelerator memory reduction but not a broad low-overhead training claim.

## Why it stopped

Proxy/local mechanism evidence is sufficient to show memory savings and scale-sensitive CPU overhead, but direct GPU training evidence is required before any paper-positive claim.

## Recommended next action

Stop this worker run as no-paper useful signal; next concrete action is a GPU-integrated LoRA training-loop prototype with pinned CPU Adam states, async copies, and end-to-end peak-memory/tokens-per-second comparison against GPU-resident Adam.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU-integrated CPU-resident LoRA Adam states
- Success threshold: At rank 8 or 16 q/v LoRA, reduce accelerator LoRA optimizer-state memory by at least 60% while keeping median step-time regression at or below 10% over at least 200 training steps compared with GPU-resident Adam.
- Stop condition: Stop as negative if CPU-resident states cause more than 25% median step-time regression for q/v LoRA after pinned-memory/asynchronous-copy implementation, or if measured peak accelerator memory saving is below 50% of the expected LoRA optimizer-state saving.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-resident-lora-optimizer-states-aa0cef7da8b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
