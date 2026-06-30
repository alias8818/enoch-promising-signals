# Exact-Anchor Quantized KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-quantized-kv-cache-73850c695f50`
Run ID: `exact-anchor-quantized-kv-cache-73850c695f50-20260604T143723684029+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c108e0d23655

## What looked useful

Exact anchors can fully rescue attention-output error when anchor tokens truly dominate attention and value quantization error, at 0.2734 fp16 KV memory ratio versus 0.2500 for all-int4. In generic synthetic cases the same anchor budget produced only small NMSE reductions, so the main open question is anchor selection on real KV traces rather than whether exact preservation can help in principle.

## Boundaries and scale limits

No real model activations, perplexity, generation quality, serving throughput, latency, or integrated cache-memory measurements were tested. Oracle attention selection is an upper-bound diagnostic and not deployable. The result should not be generalized to real LLM decoding without a trace replay or model-level validation.

## Claim scope

Synthetic PyTorch attention-error probe for per-token int4 quantized KV cache with a small exact-fp16 anchor subset. At a matched 3.125% exact-anchor budget on seq=4096, heads=16, dim=128 synthetic tensors, exact anchors eliminate error only when the selected anchors contain all attention-dominant/high-error tokens; on random and weakly anchor-biased tensors they reduce all-int4 attention-output NMSE by about 3.0% to 4.3%.

## Why it stopped

No-paper bounded synthetic result: mechanism supported under constructed anchor-dominant conditions, but generic synthetic gains are small and real-model evidence is absent.

## Recommended next action

Run a bounded real-model trace replay on GPT-2-small-class decoding: capture KV tensors and attention distributions, compare all-int4 against cheap exact-anchor selectors, and require quality/error gain per added byte before considering larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace replay for exact-anchor KV quantization
- Success threshold: At least one deployable selector achieves >=10% reduction in attention-output NMSE or model-level degradation versus all-int4 while keeping KV storage <=0.28 of fp16 and adding negligible selector overhead on the bounded run.
- Stop condition: Stop if deployable selectors fail to beat all-int4 by 5% relative error reduction at <=0.28 fp16 KV storage on real traces, or if selector overhead dominates the saved cache cost.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-quantized-kv-cache-73850c695f50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
