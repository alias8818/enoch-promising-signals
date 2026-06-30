# Sliding-Window Sink Attention for 8k Local

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-sink-attention-for-8k-local-eb1f4c3b1fae`
Run ID: `sliding-window-sink-attention-for-8k-local-eb1f4c3b1fae-20260607T191110609592+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f3795769f29a

## What looked useful

At 8192 tokens, local+sinks used 3.20% of dense causal attention edges versus 3.10% for local-only and kept token 0 visible at the final position. On the prefix/header task, dense and local+sinks reached 1.000 accuracy while local-only was 0.531. The mask diagnostic also shows local+sinks cannot directly access arbitrary middle tokens outside the window unless information is summarized into the sink-visible prefix.

## Boundaries and scale limits

The run used toy transformers, synthetic binary tasks, dense masked PyTorch attention, short training, and no real language-model corpus or optimized sparse kernel. It does not validate production 8k local LLM perplexity, retrieval QA, or serving throughput.

## Claim scope

In a tiny synthetic CUDA probe up to 8192 tokens, adding 4 always-visible sink tokens to a 128-token sliding causal window preserves prefix-stored information at the final position while keeping attention connectivity near local-window sparsity.

## Why it stopped

Bounded synthetic evidence supports a narrow mechanism, but the result is proxy-scale and not a full validation of 8k local language modeling or sparse-kernel throughput.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should test a parameter-matched small LM or associative-recall model with explicit sink-summary routing and optimized local+sinks kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched local+sinks retrieval and LM validation
- Success threshold: Local+sinks improves long retrieval accuracy by at least 20 percentage points over local-only at matched compute, retains no worse than 5% relative perplexity degradation versus local-only, and demonstrates a measured memory or throughput advantage over dense causal attention at 8192 tokens.
- Stop condition: Stop if local+sinks fails to beat local-only retrieval by 10 percentage points in a reproducible medium run, or if optimized implementation overhead eliminates the expected memory/throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-sink-attention-for-8k-local-eb1f4c3b1fae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
