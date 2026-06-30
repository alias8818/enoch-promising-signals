# Evidence Ledger Compression for Long Agent Runs on Memory-Constrained CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-compression-for-long-agent-runs-on-memory-constrained-cpu-bd136dad7647`
Run ID: `evidence-ledger-compression-for-long-agent-runs-on-memory-constrained-cpu-bd136dad7647-20260525T101421030788+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/74ba39470e6c

## What looked useful

At an 8192-byte budget over 80 traces of 2500 steps and 160 facts each, evidence-ledger recall was 0.956 versus 0.250 for recency summary and 0.006 for tail truncation; old-fact recall was 0.960 versus 0.029 and 0.000. A 2048/4096/8192-byte sweep showed ledger recall scaling from 0.308 to 0.633 to 1.000 while recency stayed at or below 0.250.

## Boundaries and scale limits

Synthetic extractor-friendly traces only; no real agent transcripts, natural-language extraction errors, LLM answer generation, semantic retrieval baseline, contradiction handling, or production memory pressure were tested.

## Claim scope

Synthetic long-agent traces with explicit machine-detectable EVIDENCE records: a compact evidence ledger preserved answer-critical facts under 2-8 KB byte budgets substantially better than tail truncation and recency-biased summary baselines on CPU.

## Why it stopped

Evidence is synthetic/proxy-only and supports the mechanism but not real-agent or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded real-trace replay follow-up with noisy evidence extraction, semantic retrieval baselines, and downstream LLM answer accuracy before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence ledger replay with extractor noise and downstream QA
- Success threshold: At matched token/byte budgets on at least 50 labeled long traces, ledger memory improves downstream answer accuracy by at least 10 percentage points over the best non-ledger baseline while keeping provenance recall at least 0.80 and extractor precision at least 0.90.
- Stop condition: Stop as negative if ledger answer accuracy is within 3 percentage points of semantic retrieval or if extractor precision falls below 0.80 under realistic trace noise.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-compression-for-long-agent-runs-on-memory-constrained-cpu-bd136dad7647`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
