# Anchored Evidence Ledger for Agent Hallucination Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchored-evidence-ledger-for-agent-hallucination-reduction-76e01384e7ad`
Run ID: `anchored-evidence-ledger-for-agent-hallucination-reduction-76e01384e7ad-20260530T031041005482+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e595c1ffba14

## What looked useful

Ledger provenance and conflict checks are useful against untrusted/stale distractors, but recency should not silently resolve trusted-source conflicts. A conflict-abstaining or corroboration-requiring answer policy is the more promising variant.

## Boundaries and scale limits

Synthetic/proxy-only evidence: 40,000-query main run plus three 10,000-query sensitivity checks. No real LLM agent, natural document extraction, human citation validation, prompt-injection test, latency/cost measurement, or large-scale benchmark was run.

## Claim scope

In a deterministic synthetic retrieval benchmark with exact claim extraction, provenance labels, timestamps, and injected high-overlap distractors, an anchored evidence ledger with trust filtering and conflict-aware abstention reduced unsupported wrong answers versus a first-retrieved baseline; the same benchmark showed recency-based trusted-source override can worsen errors when newer trusted evidence is wrong.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy-only and mixed: it supports the ledger mechanism under distractor pressure but exposes a recency-policy failure mode.

## Recommended next action

Run a bounded real-agent follow-up: wrap a small local or API RAG agent with a conflict-abstaining anchored ledger and measure unsupported answer rate on natural QA tasks with citation validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Conflict-abstaining anchored ledger for real RAG agent citation faithfulness
- Success threshold: Unsupported answer rate falls by >=30% relative to baseline, absolute correctness does not fall by more than 5 percentage points, and abstention increases by <=20 percentage points.
- Stop condition: Stop if unsupported answer reduction is <10% on the first 100 validated questions or if ledger overhead exceeds 2x latency before quality improves.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-evidence-ledger-for-agent-hallucination-reduction-76e01384e7ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
