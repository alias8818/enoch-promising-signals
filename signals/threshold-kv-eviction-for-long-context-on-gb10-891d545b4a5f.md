# Threshold KV-Eviction for Long Context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `threshold-kv-eviction-for-long-context-on-gb10-891d545b4a5f`
Run ID: `threshold-kv-eviction-for-long-context-on-gb10-891d545b4a5f-20260529T055940986152+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84537678186a

## What looked useful

Threshold-only KV eviction showed a clear fidelity/speed tradeoff. At 32k context, threshold 1e-4 reached 1.13x-1.18x speedup but reduced needle recall to 0.5 and dropped mean cosine to 0.578 in the needle scenario. At 4k context, fidelity-preserving settings retained about 95% of KV and ran about 6x slower than full attention due to dynamic indexing overhead.

## Boundaries and scale limits

No end-to-end LLM, no natural prompt benchmark, no perplexity/task accuracy measurement, and no fused production attention kernel were tested. The result is attention-level synthetic evidence only.

## Claim scope

On synthetic multi-head attention probes on GB10 at 4k and 32k context, a threshold-only KV eviction policy is not sufficient as a standalone long-context method: fidelity-preserving thresholds prune too little or run slower, while aggressive thresholds can speed up 32k attention but break delayed old-token retrieval.

## Why it stopped

Proxy attention-level early falsification, not full validation: the standalone threshold policy either preserves fidelity with little/no useful pruning or prunes enough to speed up while failing delayed retrieval.

## Recommended next action

Stop this threshold-only line as no-paper early falsification; run a bounded follow-up that adds retrieval-aware protection for old keys and tests it against full-cache and recent-window baselines on a small real transformer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retrieval-aware threshold KV eviction on a small transformer
- Success threshold: At least 25% KV reduction or 1.15x decode speedup at 16k+ context while preserving old-token retrieval within 2 percentage points of full-cache attention and keeping perplexity/task degradation within a predeclared tolerance.
- Stop condition: Stop if retrieval-aware protection cannot beat recent-window-only retention at matched KV budget, or if throughput remains slower than full-cache attention after bounded implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/threshold-kv-eviction-for-long-context-on-gb10-891d545b4a5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
