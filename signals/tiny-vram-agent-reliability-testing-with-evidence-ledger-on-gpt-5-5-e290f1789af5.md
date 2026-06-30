# Tiny-VRAM agent reliability testing with evidence ledger on gpt-5.5

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-vram-agent-reliability-testing-with-evidence-ledger-on-gpt-5-5-e290f1789af5`
Run ID: `tiny-vram-agent-reliability-testing-with-evidence-ledger-on-gpt-5-5-e290f1789af5-20260607T122819845198+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8f2712a53b46

## What looked useful

Across 300 synthetic episodes, evidence-ledger accuracy exceeded rolling-window accuracy by +0.0014, +0.0067, +0.0275, and +0.1080 at budgets 8, 16, 32, and 64 respectively, with positive 95% bootstrap intervals. At full 112-cell state capacity, the ledger reached 1.0 accuracy while a same-sized rolling window reached 0.6763.

## Boundaries and scale limits

No direct gpt-5.5 calls, no local GPT runtime, no GPU/VRAM telemetry, no generated natural-language answers, and no external judge. The result is a CPU-only memory-policy proxy over synthetic state-tracking episodes.

## Claim scope

In a deterministic synthetic agent-state benchmark with hard retained-memory budgets, a structured evidence ledger with source-step provenance improves exact-answer and audit reliability over a rolling observation window once budget is large enough to preserve a meaningful fraction of durable state.

## Why it stopped

Bounded proxy completed successfully, but direct gpt-5.5/model-backed evidence was unavailable in this CPU worker, so the result is not paper-grade or a full validation.

## Recommended next action

Stop this run as a proxy useful signal; next, run a bounded model-backed agent trial with the same task generator, real context limits, generated answers, and evidence-citation scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-backed tiny-context evidence-ledger reliability trial
- Success threshold: Evidence ledger improves exact-answer accuracy by at least 5 percentage points over rolling transcript and improves citation correctness by at least 10 percentage points with non-overlapping bootstrap 95% confidence intervals.
- Stop condition: Stop if the ledger does not beat rolling transcript by 2 percentage points on the first 30 episodes, or if citation correctness remains below 50% despite exact-answer gains.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-vram-agent-reliability-testing-with-evidence-ledger-on-gpt-5-5-e290f1789af5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
