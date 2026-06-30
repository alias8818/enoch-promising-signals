# Real-model fixed-window KV serving under GB10 memory pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-fixed-window-kv-serving-under-gb10-memory-press-39d3736649`
Run ID: `real-model-fixed-window-kv-serving-under-gb10-memory-press-39d3736649-20260610T190441445218+0000`

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

- Parent run decision: Bounded KV-Cache Pressure for Memory-Constrained GPU Workers: enoch://control-plane/projects/bounded-kv-cache-pressure-for-memory-constrained-gpu-workers-fb2cbe81ca54/runs/bounded-kv-cache-pressure-for-memory-constrained-gpu-workers-fb2cbe81ca54-20260610T184427769184+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f040bdbdf971

## What looked useful

The bounded direct test supports the mechanism: fixed-window KV retained the configured cache length, delivered a 4.0x measured final KV byte reduction at 512 tokens, and ran at 1.48x the full-prefix decode throughput in this small GB10 run. This is useful engineering evidence but not a paper-ready result.

## Boundaries and scale limits

Single process, GPT-2 small, 128-token fixed window, 384-token decode after 128-token prefill, 4 GiB host-memory ballast, no high-concurrency serving engine, no near-OOM pressure, no 7B+ model, and no quality/perplexity evaluation.

## Claim scope

On NVIDIA GB10 with a real GPT-2 causal LM in a direct Hugging Face decode loop, cropping past_key_values to a fixed 128-token window bounded measured KV cache memory at 4.5 MiB while the full-prefix cache grew to 18.0 MiB over a 512-token effective context under modest no-swap memory pressure.

## Why it stopped

The Tier 1 direct test met the minimum validation target and produced useful mechanism support, but it is too narrow for publication-grade evidence.

## Recommended next action

Run a medium direct serving confirmation with a larger local model or production serving stack, concurrent requests, longer contexts, and a quality/perplexity guardrail before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium concurrency fixed-window KV serving on GB10 with quality guardrails
- Success threshold: At 4096-token effective context with concurrent active sequences, fixed-window KV shows at least 4x measured KV or allocator memory reduction, no throughput below 90% of full-prefix, and no severe degradation on the selected quality guardrail.
- Stop condition: Stop if fixed-window memory reduction is below 2x at 4096 tokens, throughput drops below 70% of full-prefix, the serving stack cannot expose a real fixed-window cache mode, or quality guardrails fail catastrophically.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-fixed-window-kv-serving-under-gb10-memory-press-39d3736649`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
