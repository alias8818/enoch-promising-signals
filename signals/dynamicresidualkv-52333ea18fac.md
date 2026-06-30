# DynamicResidualKV

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `dynamicresidualkv-52333ea18fac`
Run ID: `dynamicresidualkv-52333ea18fac-20260525T160941642318+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27448e2fdc40

## What looked useful

Dynamic residual allocation failed to beat the best static baseline in all tested regimes. It was near-tied on pure recency but lost about 0.047 mean retained attention mass and had about 5x higher miss rate than heavy-hitter retention on sink/anchor and mixed-shift traces.

## Boundaries and scale limits

No real transformer perplexity, downstream task accuracy, decoding throughput, memory bandwidth, or 7B+ model evidence was produced. The result should be read as an early mechanism falsification, not a full model validation.

## Claim scope

Synthetic attention-trace proxy for KV cache retention at sequence length 2048, 8 heads, and KV budget 256; dynamic residual was compared with sliding, sink+sliding, and heavy-hitter baselines using retained attention mass.

## Why it stopped

Proxy evidence did not support the mechanism: dynamic residual spent too much cache budget on recent tokens when older high-attention keys mattered, underperforming heavy-hitter baselines in the target mixed and sink/anchor regimes.

## Recommended next action

Stop this run as a proxy early falsification; the only worthwhile deepen test is a bounded real-transformer perplexity/long-context evaluation against the same baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer KV eviction check for DynamicResidualKV
- Success threshold: Confirm unsupported status if DynamicResidualKV fails to improve mean loss or retrieval accuracy by at least 2% relative to heavy-hitter plus recent-floor at equal KV budget, while not improving retained attention mass.
- Stop condition: Stop after one reproducible small-model run if DynamicResidualKV is at or below the heavy-hitter baseline on both quality and attention-retention diagnostics.

## Evidence references

- Artifact root: `<local-path>/projects/dynamicresidualkv-52333ea18fac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
