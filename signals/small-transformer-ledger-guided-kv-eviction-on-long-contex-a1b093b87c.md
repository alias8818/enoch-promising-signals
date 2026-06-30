# Small-Transformer Ledger-Guided KV Eviction on Long-Context Retrieval QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-ledger-guided-kv-eviction-on-long-contex-a1b093b87c`
Run ID: `small-transformer-ledger-guided-kv-eviction-on-long-contex-a1b093b87c-20260526T174321396253+0000`

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

- Parent run decision: Ledger-Guided KV Eviction for Long Context Agents: enoch://control-plane/projects/ledger-guided-kv-eviction-for-long-context-agents-f585e078f3f9/runs/ledger-guided-kv-eviction-for-long-context-agents-f585e078f3f9-20260525T195311097145+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/abf77b336ae1

## What looked useful

Ledger-guided retention can protect old structured fact tokens relative to a recency cache in a controlled small transformer, but the advantage disappears against random eviction and the learned retrieval circuit is too weak for a paper claim.

## Boundaries and scale limits

No natural-language QA, no pretrained LLM, no real serving KV-cache integration, no high-entropy values, and no large-context or multi-model robustness. Full-cache retrieval was weak, and ledger did not outperform random eviction in the high-sample evaluations.

## Claim scope

Controlled synthetic small-transformer retrieval QA only: a 168k-parameter causal transformer on 32 repeated-key key/value facts with low value entropy. Ledger-guided retention improved old-fact accuracy versus pure recency by about 2.9-3.1 percentage points under constrained attention masks.

## Why it stopped

No-paper useful signal: direct small evidence is mixed, supporting ledger over recency for old facts but not over random eviction, and full-cache accuracy is only slightly above chance.

## Recommended next action

Run one bounded deepen test with a stronger learned retrieval circuit and higher value entropy; stop unless ledger beats both recency and random under a real cache-style evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger Small-Transformer Ledger KV Eviction With High-Entropy Retrieval
- Success threshold: Ledger old-fact accuracy exceeds both recency and random by at least 10 percentage points, with 95% confidence intervals excluding zero, while full-cache old-fact accuracy is at least 60%.
- Stop condition: Stop as negative if full-cache accuracy remains below 50% after calibrated training, or if ledger fails to beat random eviction by at least 5 percentage points in a pilot with 2000 or more old-fact examples.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-ledger-guided-kv-eviction-on-long-contex-a1b093b87c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
