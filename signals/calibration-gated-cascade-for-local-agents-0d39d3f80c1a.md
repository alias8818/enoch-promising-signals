# Calibration-Gated Cascade for Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `calibration-gated-cascade-for-local-agents-0d39d3f80c1a`
Run ID: `calibration-gated-cascade-for-local-agents-0d39d3f80c1a-20260619T051922104151+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/886dd2a97b95

## What looked useful

Across 10 seeds, the cascade achieved mean accuracy 0.9269 versus 0.9367 for always-large, called the expensive model 44.2% of the time, and reduced modeled cost by 48.9%; hard-region examples were routed to the large model 86.0% of the time versus 29.7% for easy-region examples.

## Boundaries and scale limits

Synthetic binary task only; stand-in classifiers, not real local LLM agents; no tool-use, latency-tail, prompt distribution, or production distribution-shift validation.

## Claim scope

On a synthetic mixed-difficulty classification proxy, a calibration-split confidence gate can route between cheap and expensive local stand-in agents, preserving accuracy within about 1 percentage point of the expensive model while reducing modeled cost by about 49%.

## Why it stopped

Proxy evidence is useful and reproducible, but not direct evidence for real local agents and therefore not paper-ready.

## Recommended next action

Run a bounded deepen follow-up on real local-agent traces with correctness labels, token/latency cost, and calibration/shift diagnostics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibration-gated cascade on real local-agent task traces
- Success threshold: At least 30% reduction in expensive-agent calls or measured cost with task success no more than 2 percentage points below always-strong-agent baseline on held-out traces.
- Stop condition: Stop if calibrated routing cannot beat a raw confidence threshold or if cost savings below 20% are required to stay within 2 percentage points of always-strong accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/calibration-gated-cascade-for-local-agents-0d39d3f80c1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
