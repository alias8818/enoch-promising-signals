# GPT-2-small perplexity and generation check for grouped 2-bit KV-cache quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gpt-2-small-perplexity-and-generation-check-for-grouped-2-058b1b29c9`
Run ID: `gpt-2-small-perplexity-and-generation-check-for-grouped-2-058b1b29c9-20260629T184153017672+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: KV-Cache 2-bit Grouped Quantization: Direct GPT-2-Small CPU Test: enoch://control-plane/projects/kv-cache-2-bit-grouped-quantization-direct-gpt-2-small-cpu-test-9dd24b3e62c2/runs/kv-cache-2-bit-grouped-quantization-direct-gpt-2-small-cpu-test-9dd24b3e62c2-20260629T181958455533+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0b7c62679c96

## What looked useful

The confirmation run increased cached perplexity from 73.4399 to 114.6755 (1.5615x relative perplexity, delta NLL 0.4456) and produced 0/4 exact greedy-generation matches, with first divergences at generated token indices 3, 7, 1, and 3.

## Boundaries and scale limits

Small fixed prompt set, 375 next-token positions, CPU-only simulation, no packed cache kernel, no real serving memory or throughput measurement, no large corpus, no group-size or residual-window sweep.

## Claim scope

For openai-community/gpt2 on 12 fixed natural-language snippets and 4 greedy-generation prompts, naive asymmetric grouped 2-bit quantize/dequantize of both key and value caches with group_size=32 substantially degrades cached next-token perplexity and changes every tested greedy continuation.

## Why it stopped

Early bounded falsification: direct GPT-2-small cached perplexity and generation checks showed a large quality hit for the tested naive grouped 2-bit KV-cache simulation, but this is not a full validation of all 2-bit KV-cache designs.

## Recommended next action

Stop this naive grouped 2-bit KV-cache variant as no-paper evidence; a bounded follow-up should test whether a small unquantized residual cache window or key-only/value-only quantization recovers perplexity before any larger serving work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small 2-bit KV-cache mitigation sweep with residual window and key/value ablations
- Success threshold: At least one variant reaches relative perplexity <= 1.10 versus the unquantized cached baseline on the same prompt set while retaining at least 3x idealized compression versus fp16 KV storage.
- Stop condition: Stop if all residual-window and key/value ablation variants remain above 1.20 relative perplexity or still diverge before generated token 8 on all prompts.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-perplexity-and-generation-check-for-grouped-2-058b1b29c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
