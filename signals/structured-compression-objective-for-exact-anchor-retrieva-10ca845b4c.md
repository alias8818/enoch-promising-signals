# Structured Compression Objective for Exact Anchor Retrieval

Status: `useful_signal`
Project ID: `structured-compression-objective-for-exact-anchor-retrieva-10ca845b4c`
Run ID: `structured-compression-objective-for-exact-anchor-retrieva-10ca845b4c-20260518T023904371162+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/27b55e4499f7

## What looked useful

A structured anchor objective made exact anchor identity recoverable from compressed representations that reconstruction-only compression discarded. In the 16-dimensional stress check, structured compression reached 98.45% top-1 exact anchor retrieval versus 1.02% for reconstruction-only, with no MSE penalty.

## Boundaries and scale limits

No natural-language corpus, transformer model, long-context retrieval, adversarial distractors, real retrieval index, or large-scale training was tested.

## Claim scope

Controlled synthetic bag-of-token documents with one exact anchor id, 128 possible anchors, 512 content tokens, matched autoencoder compression baselines, and 8- or 16-dimensional bottlenecks.

## Why it stopped

No-paper closure: the Tier 1 synthetic direct test supports the mechanism, but publication-grade evidence would require realistic text/retrieval validation and broader ablations.

## Recommended next action

Run a bounded medium confirmation on real tokenized passages with exact entity or string anchors, matched compression baselines, and held-out anchor distributions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Text Exact Anchor Compression Confirmation
- Success threshold: Structured compression improves exact top-1 anchor retrieval by at least 20 percentage points over reconstruction-only and reaches at least 70% top-1 exact retrieval, with reconstruction or LM-loss degradation under 10%.
- Stop condition: Stop as unsupported if the structured objective improves exact top-1 by less than 10 percentage points or requires more than 10% reconstruction/LM-loss degradation in two reasonable bottleneck/weight settings.

## Evidence references

- Artifact root: `<local-path>/projects/structured-compression-objective-for-exact-anchor-retrieva-10ca845b4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
