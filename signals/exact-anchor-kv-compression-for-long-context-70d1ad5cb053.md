# Exact-Anchor KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `exact-anchor-kv-compression-for-long-context-70d1ad5cb053`
Run ID: `exact-anchor-kv-compression-for-long-context-70d1ad5cb053-20260607T092325224114+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14562d0f635d

## What looked useful

Exact-anchor preservation did not beat uniform quantization on the primary fidelity metrics. At anchor strength 4.0, exact_anchor beat uniform on MSE in 1/18 settings and KL in 0/18; aggregate exact_anchor MSE was 2.868e-3 versus uniform 2.585e-4. At anchor strength 8.0, exact_anchor again beat uniform on MSE in 1/18 and KL in 0/18. Exact anchors sometimes beat exact-random on anchor-specific metrics, but the cost of exact rows forced lower non-anchor precision and dominated overall fidelity.

## Boundaries and scale limits

Proxy-only evidence: no trained long-context LM, no downstream perplexity/retrieval/generation benchmark, no learned anchor selector, no production KV codec, and no serving latency measurement.

## Claim scope

Synthetic single-layer attention fidelity test for exact-anchor KV preservation versus uniform KV quantization at equal average bit budgets, with sequence lengths up to 32768, anchor fractions 0.5% and 2%, budgets 2/3/4 bits, two anchor salience levels, and exact-random controls.

## Why it stopped

Proxy early falsification, not full validation: the simple exact-anchor allocation lost to uniform compression on attention KL in 36/36 calibrated settings across normal and high-salience regimes, and lost on output MSE in 34/36 settings.

## Recommended next action

Stop this project as a proxy early falsification of the simple exact-anchor bit-allocation claim; only reopen with a bounded pretrained-LM retrieval/perplexity test against uniform, exact-random, and importance-weighted KV compression baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained-LM Exact-Anchor KV Compression Check
- Success threshold: Exact-anchor compression improves downstream retrieval accuracy or perplexity by at least 5% relative over uniform quantization at the same KV memory in at least two context lengths, without worse latency or memory overhead.
- Stop condition: Stop if exact-anchor fails to beat uniform and exact-random on downstream quality at equal KV memory, or if anchor selection overhead erases the memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-context-70d1ad5cb053`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
