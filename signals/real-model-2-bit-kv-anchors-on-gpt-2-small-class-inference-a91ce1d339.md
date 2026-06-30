# Real-model 2-bit KV anchors on GPT-2-small-class inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-2-bit-kv-anchors-on-gpt-2-small-class-inference-a91ce1d339`
Run ID: `real-model-2-bit-kv-anchors-on-gpt-2-small-class-inference-a91ce1d339-20260528T081929456068+0000`

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

- Parent run decision: 2-bit KV Cache with Residual Attention Anchors: enoch://control-plane/projects/2-bit-kv-cache-with-residual-attention-anchors-e136963a2949/runs/2-bit-kv-cache-with-residual-attention-anchors-e136963a2949-20260528T022613333519+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d16359ce1dba

## What looked useful

On GPT-2 small, unanchored 2-bit KV raised loss from 4.1015 to 6.1733. Exact anchor positions improved loss monotonically with density: stride 32 6.0861, stride 16 6.0267, stride 8 5.9685, stride 4 5.8879. Best stride-4 anchoring recovered about 13.8% of the 2-bit loss penalty, but still left perplexity 5.97x the FP cache; 4-bit KV was near baseline at loss 4.1380.

## Boundaries and scale limits

One GPT-2-small-class model, WikiText-2 test text, 4,064 evaluated next-token targets, sequence length 128, simulated cache quantization rather than optimized compressed kernels, no long-context serving or generation-quality evaluation.

## Claim scope

Controlled small direct GPT-2 inference test: per-token-vector symmetric 2-bit quantized KV cache with periodic exact anchors on WikiText-2 128-token windows. Anchors monotonically reduce the 2-bit loss penalty, but do not make this 2-bit scheme practically competitive with FP or 4-bit KV.

## Why it stopped

The controlled direct test supports the anchor mechanism but early-falsifies the practical naive 2-bit anchored KV scheme: even dense stride-4 anchors leave a large quality gap versus FP and are much worse than the 4-bit control.

## Recommended next action

Do not write a paper from this result; run one bounded deepen test of improved sub-4-bit KV such as 3-bit or residual/asymmetric 2-bit anchors, requiring delta loss <= 0.15 versus FP and memory materially below 4-bit before further escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sub-4-bit GPT-2 KV anchors with stronger quantization
- Success threshold: Anchored sub-4-bit KV achieves delta loss <= 0.15 versus FP cache, recovers at least 70% of the unanchored sub-4-bit loss penalty, and uses at least 20% less effective KV memory than a 4-bit KV cache.
- Stop condition: Stop if the best anchored sub-4-bit variant has delta loss > 0.50 versus FP or fails to beat the 4-bit memory-quality tradeoff after the direct 16k-token GPT-2-small-class test.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-2-bit-kv-anchors-on-gpt-2-small-class-inference-a91ce1d339`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
