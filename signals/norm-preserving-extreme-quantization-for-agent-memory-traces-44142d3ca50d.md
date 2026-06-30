# Norm-preserving extreme quantization for agent memory traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `norm-preserving-extreme-quantization-for-agent-memory-traces-44142d3ca50d`
Run ID: `norm-preserving-extreme-quantization-for-agent-memory-traces-44142d3ca50d-20260613T164527337666+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b2e9f148a6b9

## What looked useful

At norm_sigma 1.0, recall@10 improved from 0.0184 for sign-only 1-bit storage to 0.5429 for sign plus uint8 log-norm at 31.3x compression versus fp32. At norm_sigma 1.5, recall@10 improved from 0.0099 to 0.5908. Uint8 log-norm matched float16 norm closely, but int8 per-vector quantization remained much stronger at about 0.99 recall@10 with 4x compression.

## Boundaries and scale limits

Only synthetic traces were tested: 20,000 memories, 1,000 queries, 384 dimensions, 96 clusters, three seeds per norm setting. No real agent memory traces, downstream agent tasks, packed-bit retrieval kernels, or long-horizon serving tests were run.

## Claim scope

On synthetic clustered embedding-like memory traces where vector norms encode salience, storing a per-vector norm beside a 1-bit directional sign code substantially improves float32 dot-product retrieval fidelity over sign-only storage at nearly identical storage cost.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy mechanism test, not direct validation on real agent memory traces or packed retrieval kernels.

## Recommended next action

Run the same quantizers on real stored agent/text embedding traces with dot-product retrieval, then compare recall, latency, and memory footprint against packed int8 and binary baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of norm-preserving 1-bit memory retrieval
- Success threshold: Across at least two real-trace datasets, sign plus uint8 norm achieves recall@10 >= 0.40, improves sign-only recall@10 by at least 3x, and preserves >= 25x storage compression versus fp32 without being dominated by a same-budget binary baseline.
- Stop condition: Stop if real-trace recall@10 stays below 0.25 or improves sign-only by less than 2x on both datasets, because the synthetic salience mechanism does not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/norm-preserving-extreme-quantization-for-agent-memory-traces-44142d3ca50d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
