# Anchor Checkpoint Sliding Window with Dynamic Re-injection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-checkpoint-sliding-window-with-dynamic-re-injection-af316dd198c3`
Run ID: `anchor-checkpoint-sliding-window-with-dynamic-re-injection-af316dd198c3-20260602T141046179758+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a991488e6086

## What looked useful

Default 20-seed run improved overall recall from 0.3338 to 0.5561 (+0.2223) and old-fact recall from 0.0000 to 0.3341 at the same 128-fact context cost. Sensitivity sweeps showed the effect clears threshold around 35% checkpoint retention and up to about 15% retrieval miss rate, but fails at lower retention or higher miss rates.

## Boundaries and scale limits

Proxy-only CPU simulation; no LLM answer accuracy, natural-language paraphrase, lossy summarization, embedding retrieval, production latency, or large-scale serving validation was tested.

## Claim scope

In a deterministic symbolic long-context benchmark with structured facts, fixed 128-fact context budget, 35% checkpoint retention, 5% retrieval miss rate, and 10% distractor retrieval noise, anchor checkpoint dynamic re-injection improved fact availability over a recency-only sliding window.

## Why it stopped

No-paper useful signal: the mechanism is supported only by a symbolic proxy, not by direct LLM or production-context evidence.

## Recommended next action

Run a bounded small-LLM QA follow-up with natural-language conversations, lossy checkpoint summaries, matched retrieval baselines, conflict filtering, answer accuracy, and latency/cost metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM QA Validation of Dynamic Anchor Re-injection
- Success threshold: At matched prompt budget, dynamic anchor re-injection improves long-range QA accuracy by at least 10 percentage points over the best baseline across at least 5 seeds while keeping stale-conflict answer errors under 5% and added latency under 20%.
- Stop condition: Stop if the method fails to beat the best matched baseline by 5 percentage points in a smoke run or if stale-conflict answer errors exceed 10% after conflict filtering.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-checkpoint-sliding-window-with-dynamic-re-injection-af316dd198c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
