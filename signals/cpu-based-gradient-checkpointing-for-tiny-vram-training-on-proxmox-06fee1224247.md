# CPU-based gradient checkpointing for tiny-VRAM training on Proxmox

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-based-gradient-checkpointing-for-tiny-vram-training-on-proxmox-06fee1224247`
Run ID: `cpu-based-gradient-checkpointing-for-tiny-vram-training-on-proxmox-06fee1224247-20260605T223038834666+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/05217060f36f

## What looked useful

Checkpointing gave an 84.4% saved-tensor reduction in the bounded CPU benchmark while keeping the loss identical, suggesting a direct tiny-VRAM GPU follow-up is worth a small controlled test. The CPU clone/offload proxy did not validate GPU offload cost.

## Boundaries and scale limits

No GPU was available. The run did not measure real VRAM, CUDA allocator behavior, CPU pinned-memory offload, PCIe transfer cost, Proxmox GPU passthrough overhead, optimizer-state placement, or OOM boundaries on an actual tiny-VRAM GPU.

## Claim scope

On a CPU-only Proxmox worker, PyTorch gradient checkpointing reduced measured saved-for-backward tensor residency for a synthetic 18-block MLP training step from 512.21 MiB to 80.02 MiB at 9 checkpoint segments, with 1.189x median step-time overhead and identical losses. This supports the local activation-memory mechanism only.

## Why it stopped

No-paper closure: this is a CPU-only proxy/useful-signal result, not a full validation of tiny-VRAM GPU training on Proxmox.

## Recommended next action

Run a bounded direct-GPU follow-up on a 2-4 GiB VRAM Proxmox passthrough VM measuring CUDA peak memory, host RSS, transfer time, step time, and OOM boundaries for baseline versus checkpointed CPU-offload modes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-VRAM GPU Proxmox checkpoint/offload validation
- Success threshold: Checkpoint+offload trains at least one target shape that baseline OOMs under the same VRAM cap, with matching loss on fit-capable shapes and median step-time overhead below 2x versus checkpoint-only or the largest fitting baseline.
- Stop condition: Stop if CPU offload plus checkpointing still OOMs at the target tiny-VRAM shape, or if it only avoids OOM with median step-time overhead at or above 2x and no larger feasible batch/sequence setting.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-based-gradient-checkpointing-for-tiny-vram-training-on-proxmox-06fee1224247`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
