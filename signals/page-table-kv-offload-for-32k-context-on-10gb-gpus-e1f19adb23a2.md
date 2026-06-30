# Page-Table KV Offload for 32k Context on 10GB GPUs

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `page-table-kv-offload-for-32k-context-on-10gb-gpus-e1f19adb23a2`
Run ID: `page-table-kv-offload-for-32k-context-on-10gb-gpus-e1f19adb23a2-20260530T023002108077+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/36b9f72c1481

## What looked useful

For 32k MHA with a model-aligned 9,216-token resident tail, resident one-layer attention was 2.49 ms median and page-staged offload was 13.91 ms median while copying 368 MiB per layer per decode, a 5.59x slowdown. GQA resident attention was 0.65 ms median and offload was 5.11 ms median despite the modeled 32k KV fitting in 10 GiB.

## Boundaries and scale limits

Synthetic one-layer attention and host-to-CUDA staging on GB10 unified-memory hardware; not a full 7B/8B serving stack, not an optimized paged-attention kernel, and not a direct measurement on a discrete 10 GiB PCIe GPU.

## Claim scope

Bounded GB10/PyTorch proxy: page-wise KV offload for 32k decode is numerically correct and reduces MHA KV residency, but fp16 page-table offload alone imposes a large bandwidth/latency penalty. In the modeled 10 GiB budget, Llama2-class MHA must offload 11.5 GiB of KV per generated token, while Llama3-class GQA fits 32k fp16 KV without offload.

## Why it stopped

Proxy evidence shows the mechanism is correct but bandwidth-bound and not paper-worthy by itself: MHA streams too much KV per token, and modern GQA shapes can fit the 32k KV budget without offload.

## Recommended next action

Stop pursuing plain fp16 page-table KV offload as a standalone paper idea; only revisit with a direct serving-stack experiment that also reduces or hides offloaded bytes through compression, sparsity, retrieval, or asynchronous prefetch.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/page-table-kv-offload-for-32k-context-on-10gb-gpus-e1f19adb23a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
