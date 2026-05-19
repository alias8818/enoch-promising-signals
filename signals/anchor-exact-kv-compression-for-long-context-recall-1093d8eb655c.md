# Anchor-Exact KV Compression for Long Context Recall

Status: `useful_signal`
Project ID: `anchor-exact-kv-compression-for-long-context-recall-1093d8eb655c`
Run ID: `anchor-exact-kv-compression-for-long-context-recall-1093d8eb655c-20260519T102359928113+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6c11686cef8e

## What looked useful

Anchor-exact compression matched the full-cache synthetic retrieval upper bound at 0.9258-0.9297 accuracy while same-budget pooled and uniform exact controls were near chance; recall degraded when anchors were missed or the anchor budget covered only half of the anchors.

## Boundaries and scale limits

No pretrained LLM KV states, no natural-language benchmark, no learned or heuristic anchor detector, no decoder-loop latency measurement, and no multi-layer model interaction were evaluated.

## Claim scope

Synthetic attention retrieval with oracle-known sparse answer anchors: preserving exact KV entries for all anchors while pooling only non-anchor background preserved full-cache answer accuracy out to 32,768 tokens at 96-entry budgets.

## Why it stopped

No-paper closure: the mechanism is supported in a synthetic oracle-anchor proxy, but direct real-LLM long-context recall evidence is missing.

## Recommended next action

Run a bounded real-model follow-up on a small open transformer using actual KV tensors, a practical anchor-selection rule, and Needle/RULER-style recall at matched cache budgets; stop this run because current evidence is synthetic mechanism-only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV Anchor Selection for Long-Context Recall
- Success threshold: At 8k-32k context on at least one real long-context recall benchmark, anchor-exact should recover at least 90% of full-cache recall and exceed every same-budget compression baseline by at least 20 percentage points.
- Stop condition: Stop if practical anchor selection fails to recover at least 70% of full-cache recall or does not beat same-budget baselines on two independent prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-compression-for-long-context-recall-1093d8eb655c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
