# Static KV-Cache Eviction via Cumulative Attention Mass on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `static-kv-cache-eviction-via-cumulative-attention-mass-on-cpu-0e0a8d2f7663`
Run ID: `static-kv-cache-eviction-via-cumulative-attention-mass-on-cpu-0e0a8d2f7663-20260608T004847983146+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c21b4dafbe61

## What looked useful

Standalone cumulative-attention-mass eviction preserved more required long-range tokens than recency in some regimes but lost about 0.65 retained attention-mass units versus recency across all medium scenarios. A recency-protected CAM comparator recovered much of the loss and strongly improved required-token recall, suggesting CAM is useful only with explicit freshness protection.

## Boundaries and scale limits

No real transformer weights, no perplexity or generation-quality measurement, no production serving throughput, and no full long-context benchmark. Metrics are retained synthetic full-attention mass and required-token recall.

## Claim scope

CPU-only NumPy synthetic causal-attention traces with seq_len=2048, KV budget=128, 20 trials per scenario, and scenarios for stationary anchors, phase shifts, and sink-heavy attention.

## Why it stopped

Bounded synthetic proxy evidence early-falsifies standalone static CAM as paper-ready because pure CAM consistently loses retained attention mass badly versus recency; this is not a full real-model validation.

## Recommended next action

Stop this standalone static-CAM run; run a bounded real-model follow-up testing recency-only, pure CAM, and recency-protected CAM on next-token negative log likelihood at equal KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model NLL test for recency-protected cumulative-attention KV eviction
- Success threshold: CAM+recent must improve long-range required-token retention or retrieval accuracy while keeping NLL/perplexity within 5% of recency-only and outperforming pure CAM at the same KV budget.
- Stop condition: Stop if CAM+recent is worse than recency-only by more than 5% NLL/perplexity or fails to improve any long-range retention diagnostic at equal budget.

## Evidence references

- Artifact root: `<local-path>/projects/static-kv-cache-eviction-via-cumulative-attention-mass-on-cpu-0e0a8d2f7663`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
