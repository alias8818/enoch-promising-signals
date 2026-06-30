# Cross-Layer Latent KV Bottleneck for Home Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-layer-latent-kv-bottleneck-for-home-inference-32ceaf8c6fa4`
Run ID: `cross-layer-latent-kv-bottleneck-for-home-inference-32ceaf8c6fa4-20260531T121457841771+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9589fd5d43ed

## What looked useful

Shared latent KV is not immediately falsified: rank 8 and rank 16 achieved 1.0 copy-token and exact copied-span accuracy versus a learned standard KV control, while rank 2 failed exact spans at 0.00024 and only reached 0.753 token accuracy. This suggests a real bottleneck-capacity threshold worth testing on natural text.

## Boundaries and scale limits

Evidence is limited to one seed, a toy random-prefix copy task, short-context length 16, small models under 0.5M parameters, and analytical KV byte accounting. It does not validate natural-text perplexity, pretrained-model compatibility, GPT-2-small or larger scale, real incremental decode kernels, quantization, or home-serving latency.

## Claim scope

In a small synthetic copy task with randomly initialized 4-layer 96-dim causal Transformers, a shared cross-layer latent KV source at rank 8 or 16 matched standard KV copy accuracy while reducing modeled fp16 decode KV bytes/token by 96x or 48x respectively.

## Why it stopped

Closed as no-paper useful-signal evidence because the result is synthetic/toy only and cannot support a home-inference or LLM-quality claim without natural-text and real decode validation.

## Recommended next action

Run a bounded natural-text deepen test with a 10-30M parameter GPT-style model, comparing standard KV against shared latent ranks 8/16/32 on validation perplexity, retrieval probes, and actual incremental decode memory/latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-text validation of shared cross-layer latent KV bottlenecks
- Success threshold: Rank 16 or 32 shared latent KV reaches validation perplexity within 10% of standard KV, passes incremental decode equivalence, and demonstrates at least 24x KV bytes/token reduction without worse than 20% tokens/sec regression on GB10.
- Stop condition: Stop if both rank 16 and rank 32 exceed 10% perplexity regression after matched training, fail retrieval diagnostics, or cannot implement numerically equivalent incremental decoding.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-latent-kv-bottleneck-for-home-inference-32ceaf8c6fa4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
