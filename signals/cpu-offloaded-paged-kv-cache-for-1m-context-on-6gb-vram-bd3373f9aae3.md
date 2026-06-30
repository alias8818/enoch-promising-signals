# CPU-offloaded paged KV cache for 1M context on 6GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-paged-kv-cache-for-1m-context-on-6gb-vram-bd3373f9aae3`
Run ID: `cpu-offloaded-paged-kv-cache-for-1m-context-on-6gb-vram-bd3373f9aae3-20260521T220254663177+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1d33469bb5d9

## What looked useful

Standard 32-layer fp16 MHA and 8-KV-head GQA are not practical with CPU-offloaded paged KV alone at 1M context on a 6 GiB VRAM target: KV sizes are 488.28 GiB and 122.07 GiB, and measured GB10 transfer bandwidth gives optimistic lower bounds of 8.85 s/token and 2.21 s/token with large coalesced copies, or 59.26 s/token and 14.82 s/token at 64 KiB page granularity. Extreme MQA/int8-KV variants look less impossible but require different architecture/quantization assumptions.

## Boundaries and scale limits

Not a discrete 6GB GPU implementation; no end-to-end paged-attention kernel or real model decode was run. GB10 unified memory and host-to-CUDA copy bandwidth were used as a proxy. Standard fp16 MHA/GQA results are bandwidth and memory lower bounds, not full serving measurements.

## Claim scope

Bounded GB10 proxy benchmark and analytical memory/bandwidth bounds for 1M-token CPU-offloaded KV cache under a 6 GiB VRAM working-set target.

## Why it stopped

Proxy/early falsification rather than full validation: measured bandwidth and KV-size bounds rule out practical 1M-context CPU-offloaded paged KV for standard fp16 MHA/GQA under a 6 GiB VRAM target without an additional sparsity, retrieval, MQA, or quantized-KV mechanism.

## Recommended next action

Stop this broad claim; a bounded follow-up should test an MQA plus int8-KV paged-attention implementation end to end on a true low-VRAM GPU, because only that variant crossed the optimistic bandwidth threshold in this proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end MQA int8-KV paged attention on a true low-VRAM GPU
- Success threshold: At least 1 generated token/s at 1M context with peak GPU memory <=6 GiB and no hidden full-KV residency on GPU, while preserving acceptable output quality on a long-context retrieval probe.
- Stop condition: Stop if 1M KV cannot fit in host memory with weights/runtime overhead, if page-transfer plus attention lower bound exceeds 1 s/token after coalescing, or if int8 KV quality fails the retrieval probe.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-paged-kv-cache-for-1m-context-on-6gb-vram-bd3373f9aae3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
