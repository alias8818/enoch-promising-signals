# Real KV Activation Test for Exact-Anchor Sparse Landmark Pooling

Status: `useful_signal`
Project ID: `real-kv-activation-test-for-exact-anchor-sparse-landmark-p-03f0f23aca`
Run ID: `real-kv-activation-test-for-exact-anchor-sparse-landmark-p-03f0f23aca-20260517T022924622251+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b9524683d7e6

## What looked useful

The practical regular-anchor scheme is not supported, but oracle anchors demonstrate that exact anchor selection can make landmark pooling close to dense attention at roughly 3.9x compression in some layers. Anchor selection, not just pooling, is the key bottleneck.

## Boundaries and scale limits

Tested one GPT-2-family pretrained model, 8 contiguous 256-token chunks, three layers, offline attention reconstruction only. Did not test long-context generation, downstream perplexity, learned anchor selection, larger models, or production kernels.

## Claim scope

A controlled small direct test on real distilgpt2 Q/K/V activations found that regular exact anchors plus contiguous landmark pooling achieved about 3.72x KV compression but failed the predefined fidelity threshold on layers 0, 2, and 5; oracle high-attention anchors showed an upper-bound mechanism signal in early and middle layers.

## Why it stopped

This Tier 1 direct real-KV test falsified the regular-anchor success threshold while leaving a useful oracle-anchor mechanism signal; it is not paper-positive evidence.

## Recommended next action

Run a bounded deepen test with a causal non-oracle anchor selector, then require the same >=3x compression, mean cosine >=0.98, p10 cosine >=0.95, top1 exact recall >=0.70, and anchor mass error <=0.05 across the same real-KV benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Causal Non-Oracle Anchor Selection for Real-KV Landmark Pooling
- Success threshold: At >=3x compression, a non-oracle selector must achieve mean cosine >=0.98, p10 cosine >=0.95, top1 exact recall >=0.70, and anchor mass absolute error <=0.05 on every tested layer, with no layer worse than the regular-anchor baseline.
- Stop condition: Stop if all causal non-oracle selectors fail either p10 cosine >=0.95 or anchor mass error <=0.05 on any tested layer, because that would indicate the oracle gap is not closed by cheap anchor heuristics.

## Evidence references

- Artifact root: `<local-path>/projects/real-kv-activation-test-for-exact-anchor-sparse-landmark-p-03f0f23aca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
