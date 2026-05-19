# Exact-Anchor KV Compression via Sparse Landmark Pooling

Status: `useful_signal`
Project ID: `exact-anchor-kv-compression-via-sparse-landmark-pooling-9567f71bb992`
Run ID: `exact-anchor-kv-compression-via-sparse-landmark-pooling-9567f71bb992-20260517T022305584812+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b9524683d7e6

## What looked useful

Exact anchors improved over landmark-only pooling in anchor-clustered synthetic attention, but the combined method did not robustly beat an equal-slot top-norm exact-retention baseline; pooling remained useful versus exact-drop baselines in diffuse settings.

## Boundaries and scale limits

No pretrained language model, no real KV activation traces, no perplexity/retrieval metric, no optimized streaming decoder implementation, and no long-context full-scale validation.

## Claim scope

Attention-level synthetic probe of exact top-norm anchors plus sparse landmark pooling for KV-cache compression at 5.3x to 32x compression on 1024-token synthetic caches.

## Why it stopped

No-paper closure: this was a synthetic attention-level mechanism probe, and the proposed combination was useful versus landmark-only in the favorable regime but matched or lost to a simpler equal-slot exact-token baseline.

## Recommended next action

Run a bounded direct LM-activation follow-up comparing exact-anchor SLP against equal-slot top-norm exact retention, landmark-only pooling, and recent-token retention on perplexity or retrieval accuracy before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Activation Test for Exact-Anchor Sparse Landmark Pooling
- Success threshold: At the same cache budget, exact-anchor SLP reduces perplexity increase or retrieval accuracy loss by at least 20% relative to the best simple baseline while adding no more than 10% decode/cache-update overhead in the bounded setup.
- Stop condition: Stop if exact-anchor SLP fails to beat the best simple baseline on the primary model-level metric in two matched-budget settings or if pooling overhead dominates the decode budget.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-via-sparse-landmark-pooling-9567f71bb992`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
