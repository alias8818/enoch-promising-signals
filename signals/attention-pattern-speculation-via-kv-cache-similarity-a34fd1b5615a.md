# Attention-Pattern Speculation via KV-Cache Similarity

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `attention-pattern-speculation-via-kv-cache-similarity-a34fd1b5615a`
Run ID: `attention-pattern-speculation-via-kv-cache-similarity-a34fd1b5615a-20260527T134833299886+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6b0b50c36b43

## What looked useful

KV/query similarity showed short-range correlation with attention patterns but was weaker than trivial previous-token reuse: unrestricted key/query NN recall was 0.5420/0.5634 versus previous-token 0.7333. Excluding the recent 16 tokens dropped key/query NN recall to 0.2200/0.2233, below random-past recall 0.2583.

## Boundaries and scale limits

This run used GPT-2 small, 2,048 validation tokens, top-16 set metrics, and offline attention extraction. It did not test 7B+ models, long-context production traces, custom kernels, latency, or generation quality under actual speculative sparse attention.

## Claim scope

On GPT-2 small over 16 Wikitext validation blocks of 128 tokens, naive per-layer query/key nearest-neighbor copying does not predict top-16 attention destinations as well as previous-token copying, and its nonlocal signal collapses when the most recent 16 source tokens are excluded.

## Why it stopped

Proxy early falsification, not full validation: a direct GPT-2 attention-pattern prediction probe found the proposed naive similarity mechanism weaker than simple temporal baselines and nonlocal similarity worse than random-past recall.

## Recommended next action

Stop this naive KV-cache similarity speculation path unless a follow-up replaces nearest-neighbor key/query copying with a stronger cache feature and directly beats previous-token/local baselines before any kernel or large-model work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-Similarity Attention Speculation With Stronger Features and Hard Baselines
- Success threshold: New cache feature achieves at least +0.05 absolute top-M recall and +0.05 attention-mass over previous-token copying in the unrestricted setting, and remains above random-past by at least +0.10 recall when the most recent 16 source tokens are excluded.
- Stop condition: Stop if the new feature fails to beat previous-token copying on GPT-2 small or if its nonlocal recall remains at or below random-past recall.

## Evidence references

- Artifact root: `<local-path>/projects/attention-pattern-speculation-via-kv-cache-similarity-a34fd1b5615a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
