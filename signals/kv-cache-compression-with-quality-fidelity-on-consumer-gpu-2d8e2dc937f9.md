# KV-cache compression with quality fidelity on consumer GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-with-quality-fidelity-on-consumer-gpu-2d8e2dc937f9`
Run ID: `kv-cache-compression-with-quality-fidelity-on-consumer-gpu-2d8e2dc937f9-20260620T201732523612+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/56f71e69a40f

## What looked useful

Int8 KV-cache compression is a plausible consumer-GPU engineering target because distribution drift was tiny in this bounded direct cache-path test. Naive int4 needs more care because GPT-2 short-prompt top-1 agreement fell to 0.9499 and KL drift increased.

## Boundaries and scale limits

No packed KV attention kernel was implemented, so CUDA allocation and serving speed were not reduced. Models were distilgpt2 and gpt2 only; prompts were small hand-written probes plus a repeated-text long-context stress proxy capped at 384 prompt tokens. No standard long-context QA, summarization, code, or human-quality benchmark was run.

## Claim scope

On GB10, two small GPT-class pretrained causal LMs tolerated per-token/per-head int8 KV-cache quantize-dequantize injection over 24 short prompts x 64 decode steps, preserving top-1 next-token agreement above 0.996 and top-5 containment at 1.0 while implying about 0.516x fp16 KV bytes. Int4 was mixed: attractive theoretical size but lower fidelity on natural short prompts.

## Why it stopped

Closed as a no-paper useful signal because this run measured quantize-dequantize fidelity only; it did not demonstrate real compressed-cache residency, throughput gains, or broad quality preservation.

## Recommended next action

Implement or adapt a packed int8 KV-cache attention path and rerun the same fidelity harness plus real allocation/latency measurements on a 1B-class model with natural long-context tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed int8 KV-cache serving probe on a 1B-class model
- Success threshold: At least 35% measured KV-residency reduction, no more than 5% decode latency regression, top-1 agreement >= 0.99, top-5 containment >= 0.999, and mean KL(base||compressed) <= 0.002.
- Stop condition: Stop if packed int8 does not reduce measured KV residency by 25%, if decode latency regresses by more than 20%, or if top-1 agreement falls below 0.98 on natural long-context probes.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-with-quality-fidelity-on-consumer-gpu-2d8e2dc937f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
