# Dynamic KV-Cache Pruning for Long-Context Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-kv-cache-pruning-for-long-context-serving-174d8a19a4d4`
Run ID: `dynamic-kv-cache-pruning-for-long-context-serving-174d8a19a4d4-20260522T013834496230+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/097ee83fc7b8

## What looked useful

Dynamic attention-score pruning reduced mixed_sink mean relative output error from 0.177 to 0.000809 at budget 256 and raised anchor retention from 16.4% to 99.3%, but it was slower than sliding-window and gave weak or negative benefit on recent-only and rare periodic retrieval workloads.

## Boundaries and scale limits

No full LLM, tokenizer, natural prompt corpus, paged-attention kernel, batching scheduler, or end-to-end serving stack was tested. Metrics are synthetic attention-output error, anchor retention, and simulator throughput on one GB10 worker.

## Claim scope

Attention-level synthetic serving probe at sequence length 2048 and dimension 128: online attention-score KV retention can preserve repeatedly attended sink/anchor tokens under fixed cache budgets, but it is not a general improvement over sliding-window pruning across recent-only and rare-retrieval workloads.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic attention-level and mixed; it supports a mechanism in recurring-anchor workloads but does not validate dynamic KV pruning as a general long-context serving method.

## Recommended next action

Run a bounded model-level validation with a small causal LM, real long-context prompts containing recurring anchors and rare retrieval probes, and compare perplexity/task accuracy plus end-to-end decode latency against sliding-window and sink-token baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-level validation of dynamic KV retention for recurring-anchor long-context prompts
- Success threshold: Dynamic retention must improve recurring-anchor quality by at least 20% relative to sliding-window at the same KV budget, avoid degradation on recent-only controls, and keep decode throughput within 15% of sliding-window.
- Stop condition: Stop if dynamic retention fails to beat a fixed sink-token baseline on recurring-anchor quality or if decode throughput overhead exceeds 25% at all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-kv-cache-pruning-for-long-context-serving-174d8a19a4d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
