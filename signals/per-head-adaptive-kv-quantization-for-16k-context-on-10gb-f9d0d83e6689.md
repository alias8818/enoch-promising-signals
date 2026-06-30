# Per-head adaptive KV quantization for 16K context on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-adaptive-kv-quantization-for-16k-context-on-10gb-f9d0d83e6689`
Run ID: `per-head-adaptive-kv-quantization-for-16k-context-on-10gb-f9d0d83e6689-20260605T001421145653+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e4701a56048d

## What looked useful

Across five heterogeneous synthetic 16K seeds, adaptive allocation reduced mean output MSE versus fixed 3-bit by 70.2% to 98.8% at equal 3-bit average budget. At 4-bit average it regressed on two of five seeds, so the allocator is not robust enough for a paper claim.

## Boundaries and scale limits

No pretrained LLM KV caches, downstream perplexity/retrieval accuracy, decode latency, or packed low-bit serving kernel were tested. Results are synthetic mechanism evidence only.

## Claim scope

Synthetic 16K-context attention traces with 16 heads and 64-dimensional heads show per-head adaptive KV quantization can reduce held-out attention-output MSE at a tight 3-bit average budget, but the naive greedy allocator is unstable at a 4-bit average budget.

## Why it stopped

No-paper useful signal: synthetic proxy evidence supports the tight-budget mechanism but shows allocator instability and lacks direct real-model downstream validation.

## Recommended next action

Run a bounded real-model follow-up on captured 16K KV caches from a pretrained long-context model, comparing fixed and adaptive equal-memory budgets on held-out downstream metrics and adding allocator guardrails for 4-bit budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 16K KV-cache validation of guarded per-head adaptive quantization
- Success threshold: Adaptive allocation improves or matches fixed equal-memory baselines on held-out downstream metrics, reduces attention-output MSE by at least 20% at 3-bit average, and has no statistically meaningful 4-bit regression across prompts.
- Stop condition: Stop if adaptive allocation fails to beat fixed 3-bit on real held-out KV caches or shows any repeatable downstream regression at a 4-bit average budget.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-adaptive-kv-quantization-for-16k-context-on-10gb-f9d0d83e6689`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
