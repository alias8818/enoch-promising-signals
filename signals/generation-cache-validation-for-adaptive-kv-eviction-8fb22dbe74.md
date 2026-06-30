# Generation-cache validation for adaptive KV eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `generation-cache-validation-for-adaptive-kv-eviction-8fb22dbe74`
Run ID: `generation-cache-validation-for-adaptive-kv-eviction-8fb22dbe74-20260620T001052201127+0000`

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

- Parent run decision: Adaptive KV-Cache Eviction for Long Context on Consumer GPU: enoch://control-plane/projects/adaptive-kv-cache-eviction-for-long-context-on-consumer-gpu-82603adde730/runs/adaptive-kv-cache-eviction-for-long-context-on-consumer-gpu-82603adde730-20260619T231001995973+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7fe93baac7cb

## What looked useful

Adaptive attention-score retention reduced NLL drift versus full cache by 3.25 to 4.68 NLL points relative to recency across all tested budgets and improved top-1 agreement with the full-cache run by 0.21 to 0.24.

## Boundaries and scale limits

Single small pretrained model, one embedded controlled prose corpus, CPU inference, no serving throughput measurement, no broad corpus robustness, no larger-model validation, and no overhead-optimized cache implementation.

## Claim scope

In a controlled 384-token distilgpt2 autoregressive next-token evaluation using real past_key_values pruning, an attention-mass adaptive KV eviction heuristic preserved full-cache behavior better than pure recency eviction at budgets 32, 64, and 128.

## Why it stopped

Tier 1 controlled direct test met the mechanism-support threshold, but the evidence remains small-scope and is not paper-positive.

## Recommended next action

Run a bounded deepen follow-up on a prompt suite and GPT-2-small-class model with recency, random, anchor-only, attention-only, and adaptive policies before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-prompt GPT-2-small validation of attention-score KV eviction
- Success threshold: Adaptive beats recency by at least 20% mean delta-NLL reduction at two or more budgets and beats anchor-only at the median budget, with no more than 25% runtime overhead in the prototype loop.
- Stop condition: Stop if adaptive fails to beat recency on mean delta NLL at the median budget or if anchor-only accounts for essentially all of the improvement.

## Evidence references

- Artifact root: `<local-path>/projects/generation-cache-validation-for-adaptive-kv-eviction-8fb22dbe74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
