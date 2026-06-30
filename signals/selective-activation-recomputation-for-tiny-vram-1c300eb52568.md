# Selective Activation Recomputation for Tiny VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `selective-activation-recomputation-for-tiny-vram-1c300eb52568`
Run ID: `selective-activation-recomputation-for-tiny-vram-1c300eb52568-20260525T193251942323+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/830068e89f03

## What looked useful

FFN-only recomputation recovered 57% of full-checkpoint memory savings at FFN expansion 4 and 71% at expansion 8, with lower overhead than full checkpointing. Under a 1900 MiB cap, FFN-only and full checkpointing completed while no-checkpoint and attention-only variants OOMed.

## Boundaries and scale limits

Evidence is limited to synthetic tokens, one GB10 host, PyTorch 2.12 BF16 training steps, compact 8-layer GPT-style models, and short runs. It does not validate convergence, model quality, GPT-2-small-class scale, production training pipelines, or larger model families.

## Claim scope

On a compact synthetic GPT-style CUDA training benchmark, selective FFN-only activation recomputation reduced peak memory enough to pass a 1900 MiB allocator cap where no checkpointing and attention-only recomputation failed, while running faster than full-block checkpointing.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported by direct local memory and throughput evidence, but the run used synthetic short benchmarks rather than publication-grade real training validation.

## Recommended next action

Run a bounded GPT-2-small-class real-corpus follow-up that compares no checkpointing, FFN-only, attention-only, and full checkpointing under fixed memory caps, reporting max feasible batch/sequence, tokens/sec, and convergence parity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class fixed-memory validation of selective FFN recomputation
- Success threshold: FFN-only recomputation must fit at least one batch/sequence configuration that no checkpointing cannot fit, recover at least 60% of full-checkpoint memory savings, run at least 5% faster than full checkpointing, and match full/no-checkpoint short-run loss within normal seed noise.
- Stop condition: Stop if FFN-only fails to improve the feasible batch/sequence frontier over no checkpointing or if its throughput is not meaningfully better than full checkpointing at matched feasible settings.

## Evidence references

- Artifact root: `<local-path>/projects/selective-activation-recomputation-for-tiny-vram-1c300eb52568`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
