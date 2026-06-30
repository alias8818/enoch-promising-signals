# Early-Exit Speculative Decoding for VRAM-Constrained GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-speculative-decoding-for-vram-constrained-gpus-c875a29a198a`
Run ID: `early-exit-speculative-decoding-for-vram-constrained-gpus-c875a29a198a-20260523T052304360597+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e926d567412a

## What looked useful

Distilgpt2 accepted up to 75.0% of draft tokens but reached only 0.596x baseline throughput. GPT-2-small FP32 was exact but accepted only 35.9% at the best configuration and reached 0.438x baseline throughput. GPT-2-small FP16 was slower and had one prompt mismatch, indicating exact greedy reproduction can be numerically fragile.

## Boundaries and scale limits

Tested only 4 prompts, 32 generated tokens each, distilgpt2 and GPT-2-small, single-process single-stream decoding. The harness does not include paged KV-cache reuse, fused kernels, concurrent serving, or 7B+ production models.

## Claim scope

On a GB10 CUDA GPU, a straightforward Hugging Face GPT-2-family implementation of early-exit self-speculative greedy decoding is feasible and can be exact under FP32, but it was slower than vanilla greedy decoding for distilgpt2 and GPT-2-small single-stream generation.

## Why it stopped

Bounded direct GPU evidence falsified the straightforward speedup hypothesis: every exact configuration was slower than vanilla greedy decoding, and FP16 GPT-2-small showed a correctness caveat.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit with a KV-cache integrated implementation that reuses early-layer work and must exceed 1.05x greedy throughput while preserving exact output equality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache integrated early-exit self-speculative decoding
- Success threshold: At least 1.05x aggregate tokens/sec over vanilla greedy with exact output equality across all prompts, and no more than 1.10x CUDA peak allocated memory versus vanilla greedy for the single-model path.
- Stop condition: Stop if KV-cache reuse still remains below 0.95x greedy throughput or if exact equality fails under the intended inference dtype after deterministic controls.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-speculative-decoding-for-vram-constrained-gpus-c875a29a198a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
