# Intent-Driven Memory Routing for Local Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `intent-driven-memory-routing-for-local-agents-585de1c8b54a`
Run ID: `intent-driven-memory-routing-for-local-agents-585de1c8b54a-20260524T201135971299+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5ed284b6fb1

## What looked useful

Rule-based intent routing improved five-seed mean top-1 accuracy from 0.376 to 0.804 and reduced scanned memories from 480 to about 101, while off-intent retrieval fell from 0.565 to 0.133. Ambiguous-query top-1 remained weak at about 0.495, and 10-20% route-error injection reduced accuracy to 0.721 and 0.645.

## Boundaries and scale limits

Synthetic corpus, lexical TF-IDF retrieval, rule/noisy intent classifiers, 480 memories, 1920 queries for the main seed, and five additional robustness seeds; no real local-agent traces, embedding vector store, LLM answer evaluation, or production workload.

## Claim scope

On a controlled synthetic local-agent memory benchmark with six intent namespaces and cross-intent distractors, intent routing improved top-1 retrieval and reduced scanned memories versus global lexical retrieval, but degraded under ambiguous queries and injected routing errors.

## Why it stopped

The evidence is a synthetic mechanism test, not a full validation; it supports intent routing as useful under clean routing but exposes ambiguity and router-error brittleness.

## Recommended next action

Stop this run as no-paper useful signal; next run should test confidence-gated multi-route retrieval on real or high-fidelity local-agent traces against a global vector-store baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Gated Multi-Route Memory Retrieval on Local-Agent Traces
- Success threshold: Compared with global retrieval, confidence-gated routing should reduce scanned memories or retrieval latency by at least 3x while maintaining at least 95% of global top-k recall and reducing off-intent contamination by at least 30% on ambiguous and non-ambiguous subsets.
- Stop condition: Stop if confidence-gated routing cannot maintain 95% of global top-k recall or if ambiguity/error ablations erase the efficiency gain after fallback is enabled.

## Evidence references

- Artifact root: `<local-path>/projects/intent-driven-memory-routing-for-local-agents-585de1c8b54a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
