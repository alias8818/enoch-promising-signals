# CascadeSpec: Adaptive Draft+Verify on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascadespec-adaptive-draft-verify-on-gb10-181722b0f265`
Run ID: `cascadespec-adaptive-draft-verify-on-gb10-181722b0f265-20260630T062217831343+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc6ddb85ba8b

## What looked useful

Adaptive scheduling improved synthetic accepted-token accounting (1.246x generated tokens/pass versus best static on bursty seeds) but did not produce robust wall-clock speedup (1.002x mean versus best static, stdev 0.0187). Real assisted generation was negative at small scale: 0.213x and 0.382x baseline throughput for the two tested model pairs.

## Boundaries and scale limits

Evidence is limited to a synthetic matrix-workload harness plus small Hugging Face model pairs (distilgpt2/tiny-gpt2 and gpt2/distilgpt2). It does not validate large LLMs, production KV-cache behavior, serving engines, multi-draft kernels, or publication-grade robustness.

## Claim scope

Synthetic GB10 CUDA draft+verify scheduling showed adaptive policies can improve generated tokens per verification pass under nonstationary acceptance, but wall-clock throughput was only roughly tied with the best fixed synthetic policy; two small real Transformers assisted-generation probes were slower than greedy baseline.

## Why it stopped

Proxy and small-model direct evidence do not support a robust CascadeSpec throughput claim on GB10; the useful mechanism signal is not enough for paper writing.

## Recommended next action

Stop this run as no-paper evidence; only deepen if testing real model pairs in a serving stack with adaptive and static speculative controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model adaptive speculative decoding control on GB10
- Success threshold: Adaptive cascade achieves at least 1.15x wall-clock new tokens/s over the best static speculative policy and at least 1.25x over target-only baseline, with matching outputs for greedy decoding across all prompt classes.
- Stop condition: Stop if adaptive is below 1.05x the best static policy after warmup on two model-pair sizes, or if assistant/tokenizer overhead dominates accepted-token gains.

## Evidence references

- Artifact root: `<local-path>/projects/cascadespec-adaptive-draft-verify-on-gb10-181722b0f265`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
