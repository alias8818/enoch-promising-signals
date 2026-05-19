# Real-model HAKV inference fidelity on small pretrained transformers

Status: `useful_signal`
Project ID: `real-model-hakv-inference-fidelity-on-small-pretrained-tra-d8a4514144`
Run ID: `real-model-hakv-inference-fidelity-on-small-pretrained-tra-d8a4514144-20260515T223852545243+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/908298541335

## What looked useful

HAKV is not a uniformly superior sparse-cache policy, but end-to-end logits show a real mechanism signal: it improves over recent-only caches and can exceed uniform anchors at larger retained fractions, unlike the prior attention-output proxy.

## Boundaries and scale limits

No production incremental KV-cache implementation, no latency or memory benchmark, one model family, one deterministic text fixture per sequence length, no downstream QA or retrieval accuracy, and no multi-seed or multi-model robustness.

## Claim scope

Tier 1 direct inference-fidelity test on distilgpt2 using sparse causal attention masks at 256 and 512 tokens; hierarchical anchor KV selection beat recent-only baselines broadly and beat uniform anchors only at the largest tested 512-token 25% retention setting.

## Why it stopped

No-paper closure: the direct Tier 1 evidence is mixed against the strong uniform baseline and supports only a bounded mechanism signal, not a publication-grade claim.

## Recommended next action

Run a bounded deepen follow-up across at least two small pretrained model families and multiple text/task sequences, requiring hierarchical anchors to beat both recent and uniform on KL and NLL delta at 25% retention without top-1 regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model HAKV inference fidelity robustness at 25% retention
- Success threshold: At 25% retention, hierarchical must beat both recent and uniform on mean KL and NLL delta in at least two model families, with top-1 agreement no worse than uniform by more than 0.01 absolute.
- Stop condition: Stop as negative if uniform matches or beats hierarchical on mean KL or NLL delta in a majority of model-family/task combinations.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-hakv-inference-fidelity-on-small-pretrained-tra-d8a4514144`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
