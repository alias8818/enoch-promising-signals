# Doctrine vs Retrieval in Long-Horizon Agent Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `doctrine-vs-retrieval-in-long-horizon-agent-memory-6bc187b7bd46`
Run ID: `doctrine-vs-retrieval-in-long-horizon-agent-memory-6bc187b7bd46-20260610T191939490211+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58369bbbc25c

## What looked useful

At horizon 8000 with adversarial policy-lookalike distractors, retrieval doctrine-query accuracy was 0.179 +/- 0.028 at top_k=8 while doctrine and hybrid doctrine-query accuracy were 1.0; retrieval episodic accuracy stayed 1.0 while doctrine episodic accuracy was 0.0. In the easy lexical setting retrieval was 1.0 overall through horizon 8000, so the mechanism is conditional rather than a broad retrieval replacement.

## Boundaries and scale limits

Synthetic schema-based event generation only; TF-IDF retrieval only; no LLM agent, learned doctrine writer, embedding retriever, reranker, real user logs, changed-preference drift, or multi-day interactive task validation.

## Claim scope

In a synthetic long-horizon memory benchmark, compressed doctrine rules did not improve over retrieval when relevant memories were lexically easy, but they strongly improved recurring policy-query accuracy under policy-lookalike distractor saturation; retrieval remained necessary for sparse episodic facts, and a query-routed hybrid was best on the mixed workload.

## Why it stopped

Synthetic proxy evidence is sufficient to reject a broad paper-positive claim but useful enough to motivate a bounded direct-evidence follow-up; it is not full validation of long-horizon LLM agent memory.

## Recommended next action

Stop this run as proxy-only useful signal; next run should deepen with an embedding/LLM memory benchmark that compares retrieval, doctrine, and hybrid under realistic doctrine-writing noise and changed-preference cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding/LLM Agent Memory Test for Doctrine-Retrieval Hybrid
- Success threshold: Hybrid improves mixed-workload accuracy by at least 10 percentage points over retrieval-only at long horizon while losing no more than 2 percentage points on episodic queries and exposing stale-doctrine errors below 5 percent.
- Stop condition: Stop if embedding/LLM retrieval-only matches hybrid within 2 percentage points on mixed accuracy across two long-horizon settings or if doctrine writing causes more than 5 percent stale-rule errors.

## Evidence references

- Artifact root: `<local-path>/projects/doctrine-vs-retrieval-in-long-horizon-agent-memory-6bc187b7bd46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
