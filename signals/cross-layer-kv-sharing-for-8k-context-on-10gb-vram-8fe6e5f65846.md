# Cross-Layer KV Sharing for 8k Context on 10GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-kv-sharing-for-8k-context-on-10gb-vram-8fe6e5f65846`
Run ID: `cross-layer-kv-sharing-for-8k-context-on-10gb-vram-8fe6e5f65846-20260531T235140936571+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4b1cd1e04538

## What looked useful

KV memory at 8k context fell from 1.568 GiB CUDA peak in the 24-layer synthetic baseline to 0.811 GiB for share2, 0.430 GiB for share4, and 0.242 GiB for share8. Median decode throughput improved modestly from 91.70 tok/s to 100.28 tok/s at share8, indicating the primary benefit is memory capacity rather than speed.

## Boundaries and scale limits

No pretrained or trained language model was evaluated; no perplexity, retrieval accuracy, or end-to-end serving benchmark was measured. The throughput probe uses synthetic tensors and small projection weights, so it should not be read as full model performance.

## Claim scope

On GB10 with PyTorch CUDA, a synthetic 24-layer 8k decode probe shows that cross-layer KV sharing reduces KV-cache allocation by the expected group factor and remains runnable; analytical accounting shows similar cache savings for common MHA/GQA 8k layouts.

## Why it stopped

No-paper closure: the systems mechanism is supported by direct synthetic 8k CUDA evidence, but trained-model quality is only proxied and remains the decisive risk.

## Recommended next action

Run a bounded trained-model follow-up on a small rotary decoder with a synthetic long-context retrieval/copy task, comparing baseline, share2, and share4 for accuracy/perplexity and KV memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train Small Rotary Decoders With Cross-Layer KV Sharing on Long-Context Retrieval
- Success threshold: Share2 reaches at least 95% of baseline held-out long-context task accuracy or no more than 5% relative perplexity degradation while saving at least 50% KV memory at 8k.
- Stop condition: Stop if share2 fails to reach 90% of baseline accuracy after the same training budget, diverges repeatedly, or shows no KV-memory advantage in the measured decode path.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-sharing-for-8k-context-on-10gb-vram-8fe6e5f65846`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
