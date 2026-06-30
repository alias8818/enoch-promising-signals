# Compressed Evidence Ledger in KV Cache for Long-Context Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-evidence-ledger-in-kv-cache-for-long-context-agents-12e980549b7c`
Run ID: `compressed-evidence-ledger-in-kv-cache-for-long-context-agents-12e980549b7c-20260531T115820958226+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f587edc8ca0e

## What looked useful

The ledger improved latest-value accuracy by 15.9-19.2 percentage points over recency for frequency-weighted queries on skewed streams and by up to 29.4 points for uniform queries at 128 records. Count accuracy improved because compressed slots amortized repeated evidence, but tiny-budget rare-entity latest recall could underperform recency.

## Boundaries and scale limits

This run did not test a real transformer KV cache, an LLM agent, learned compression, natural-language evidence, noisy entity linking, or multi-hop reasoning. The rare-query and uniform-event ablations show weak or negative latest-value gains at tiny budgets.

## Claim scope

In a synthetic finite-record memory proxy with 10,000 event streams, 256 entities, and oracle retrieval, a fixed-slot per-entity evidence ledger preserves latest-value and count evidence better than raw recency when evidence has repeated entity structure and queries are frequency-weighted or budgets retain enough entities.

## Why it stopped

Closed as a no-paper useful signal because the evidence is a synthetic oracle proxy, not direct validation of compressed evidence ledgers inside actual transformer KV caches.

## Recommended next action

Run a bounded direct transformer follow-up where ledger entries are represented as real prompt or KV tokens in a small controlled retrieval model and compared against recency plus summary-token baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct KV-token ledger test on small transformer retrieval
- Success threshold: At equal token budget, ledger-token runs improve latest-value accuracy by at least 10 percentage points over recency on frequency-weighted and uniform query regimes without more than a 5 point regression on rare-entity queries.
- Stop condition: Stop if ledger tokens are not reliably parsed or attended by the model in a smoke test, or if two budget levels show less than 3 percentage points improvement over recency with no diagnostic path to fix usage.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-evidence-ledger-in-kv-cache-for-long-context-agents-12e980549b7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
