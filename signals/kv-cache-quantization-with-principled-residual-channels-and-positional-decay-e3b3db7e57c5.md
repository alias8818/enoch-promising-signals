# KV cache quantization with principled residual channels and positional decay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-quantization-with-principled-residual-channels-and-positional-decay-e3b3db7e57c5`
Run ID: `kv-cache-quantization-with-principled-residual-channels-and-positional-decay-e3b3db7e57c5-20260629T134736218606+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/507c09a4d15a

## What looked useful

Keeping eight sensitivity-selected key channels per head at higher precision across the full cache reduced relative attention-output error from about 1.07 to about 0.51 and improved top-1 attended-token agreement from about 0.38-0.40 to about 0.81-0.82 across recency, old-retrieval, and mixed synthetic scenarios. Age-decayed residual preservation stayed near failed baselines with top-1 agreement about 0.24-0.25.

## Boundaries and scale limits

No end-to-end transformer perplexity, task benchmark, RoPE-specific real-cache trace, compressed-kernel throughput, or metadata-inclusive memory measurement was run. Results are proxy evidence only and should not be treated as model-quality validation.

## Claim scope

Synthetic attention-level KV-cache quantization test at sequence length 4096, 8 heads, head dimension 64, and 6 seeds per scenario. Sensitivity-selected static residual key channels improved attention fidelity, but positional decay of those residual channels did not.

## Why it stopped

Proxy evidence is useful but mixed: static residual channels are supported, positional decay is unsupported, and no real-model quality or kernel measurement was produced.

## Recommended next action

Run a bounded deepen follow-up that implements static sensitivity-selected residual key channels in a small real decoder model and compares perplexity plus long-context retrieval against KIVI/KVQuant-style baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of static sensitivity-selected KV residual channels
- Success threshold: At comparable memory budget, static sensitivity-selected residual channels must reduce perplexity or retrieval degradation by at least 25% versus the best low-bit baseline and preserve the synthetic attention-error advantage on real KV traces.
- Stop condition: Stop if real KV traces do not show lower attention/logit error for selected residual channels than random residual channels, or if perplexity/retrieval degradation is not improved versus the best low-bit baseline.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-quantization-with-principled-residual-channels-and-positional-decay-e3b3db7e57c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
