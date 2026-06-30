# Trace-Based Safety Router for Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-based-safety-router-for-local-agents-a37e00547c4a`
Run ID: `trace-based-safety-router-for-local-agents-a37e00547c4a-20260526T084501014004+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12a892dcebd7

## What looked useful

Trace context carried prior secret access and untrusted-instruction state into later egress/tool decisions, improving recall from 0.50 to 1.00 versus action-only inspection at zero false positives on this benchmark. An initial implementation bug also showed that broad trace-text substring matching can overblock benign temporary cleanup.

## Boundaries and scale limits

Synthetic traces only; no real agent logs, no live model trajectories, no human red-team prompts, and no production workflow false-positive measurement.

## Claim scope

On a deterministic synthetic benchmark of 640 structured local-agent traces, a trace-aware rule router detected context-dependent unsafe actions that an action-only regex router missed.

## Why it stopped

Evidence is synthetic and mechanism-supporting but not a real-world validation; finalizing negative avoids overclaiming a benchmark-shaped result.

## Recommended next action

Stop this run as no-paper useful signal; next, evaluate the same router interface on real local-agent traces with seeded adversarial tasks and blinded labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Evaluation of Trace-Based Local-Agent Safety Routing
- Success threshold: Trace-aware router improves unsafe-action recall by >=25 percentage points over action-only baseline with benign false-positive rate <=5%.
- Stop condition: Stop if real-trace false-positive rate exceeds 10% after one documented normalization pass or if recall gain is below 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-safety-router-for-local-agents-a37e00547c4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
