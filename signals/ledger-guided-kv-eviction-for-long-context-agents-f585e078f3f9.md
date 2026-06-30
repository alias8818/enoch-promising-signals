# Ledger-Guided KV Eviction for Long Context Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ledger-guided-kv-eviction-for-long-context-agents-f585e078f3f9`
Run ID: `ledger-guided-kv-eviction-for-long-context-agents-f585e078f3f9-20260525T195311097145+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/abf77b336ae1

## What looked useful

Main run across 6 seeds and 378 queries per seed showed ledger-guided answerability of 7.3%, 25.3%, 43.8%, and 43.8% at cache capacities 128, 256, 512, and 1024, while FIFO/LRU/random were near zero and oracle ranged from 48.5% to 100%. A noisy-ledger control at capacity 512 dropped ledger answerability to 15.3%, showing dependence on ledger recall and precision.

## Boundaries and scale limits

Evidence is CPU-only and synthetic. It does not measure real transformer attention, generated answer quality, ledger extraction quality, latency, memory allocator behavior, or integration overhead in an LLM serving stack.

## Claim scope

In a deterministic synthetic long-context trace where delayed queries require exact retention of earlier fact spans, ledger-guided KV eviction preserves substantially more query-relevant spans than FIFO, LRU, or random eviction under fixed cache budgets.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the retention mechanism only in a synthetic proxy, not in a real long-context agent or model-serving implementation.

## Recommended next action

Run a bounded direct follow-up by integrating ledger-guided eviction into a small transformer KV-cache decoding loop and measuring long-context retrieval QA accuracy, latency, and memory at matched budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Ledger-Guided KV Eviction on Long-Context Retrieval QA
- Success threshold: Ledger-guided eviction improves retrieval QA accuracy by at least 20 percentage points over the best non-oracle eviction baseline at one or more constrained cache budgets, while adding less than 10% median decode latency overhead.
- Stop condition: Stop if ledger-guided eviction improves synthetic retention but fails to improve real model QA accuracy by at least 10 percentage points over the best non-oracle baseline, or if latency overhead exceeds 25% at the tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-guided-kv-eviction-for-long-context-agents-f585e078f3f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
