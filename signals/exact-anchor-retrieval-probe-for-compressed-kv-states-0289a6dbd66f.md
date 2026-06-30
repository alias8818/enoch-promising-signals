# Exact-Anchor Retrieval Probe for Compressed KV States

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-retrieval-probe-for-compressed-kv-states-0289a6dbd66f`
Run ID: `exact-anchor-retrieval-probe-for-compressed-kv-states-0289a6dbd66f-20260529T133631049837+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a8589b716432

## What looked useful

Anchor-aware exact KV retention behaved qualitatively differently from generic compression for exact-anchor lookup: full KV and exact-anchor retention both achieved 1.000 top-1 in all sweep conditions; Gaussian rank-16 projection fell to 0.122 worst-case top-1 and random 16-token retention fell to 0.000 worst-case top-1.

## Boundaries and scale limits

No real transformer, no learned anchor detector, no natural-language retrieval task, no generation/perplexity metric, and no comparison to production KV-compression systems beyond simple synthetic controls.

## Claim scope

Synthetic attention-logit retrieval over unit-normalized KV states: exact retention of 16 designated anchor keys preserved top-1 anchor lookup across 512 to 32768 keys, while unanchored same-budget retention and rank-16 projected keys degraded sharply.

## Why it stopped

Synthetic proxy evidence supports the scoped mechanism but is not full validation of compressed KV states in trained LLMs.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded real-model follow-up using a tiny transformer or GPT-2-small-class model with online anchor selection and standard KV-compression baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Exact Anchor KV Retention Probe
- Success threshold: Exact-anchor KV retention improves retrieval accuracy by at least 20 percentage points over same-budget unanchored compression while staying within a fixed KV memory budget and within 5 percentage points of full KV on the retrieval metric.
- Stop condition: Stop if full KV does not solve the task, if anchor detection coverage is below 90% on the synthetic retrieval dataset, or if exact-anchor retention is not better than unanchored same-budget compression in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-retrieval-probe-for-compressed-kv-states-0289a6dbd66f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
