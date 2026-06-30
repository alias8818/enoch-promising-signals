# Calibrated local cascade router for GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `calibrated-local-cascade-router-for-gb10-4de9b2b9081a`
Run ID: `calibrated-local-cascade-router-for-gb10-4de9b2b9081a-20260610T151131897111+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98409dfd7687

## What looked useful

The cascade mechanism is locally viable: defer only uncertain cheap-model cases to a stronger local model and recover near-strong accuracy at much lower measured inference cost. Calibration reduced ECE from 0.0857 to 0.0180 and Brier score from 0.0381 to 0.0279, making thresholds more interpretable, but an uncalibrated threshold was cheaper in this proxy.

## Boundaries and scale limits

Proxy-only CPU experiment using logistic regression and random forest on sklearn digits; no real LLM serving, no GB10 GPU inference, no token latency, no batching, no UMA/KV-cache pressure, and no production request distribution.

## Claim scope

On a small local sklearn digits proxy, a calibrated confidence router preserved a stronger local model's accuracy within 0.11 percentage points mean while using 7.84% of always-strong measured inference cost; calibration improved confidence reliability but was not the cheapest routing policy.

## Why it stopped

Stopped as a no-paper useful signal because the evidence is a local CPU proxy rather than direct GB10 LLM cascade validation.

## Recommended next action

Run a bounded direct local-LLM follow-up on GB10 with a cheap/strong model pair, public QA or classification tasks, answer correctness, token latency, GPU utilization, and memory telemetry; stop if calibrated routing cannot stay within 0.5 pp of always-strong correctness at at least 30% lower latency/cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GB10 local-LLM calibrated cascade router validation
- Success threshold: Calibrated router is within 0.5 percentage points of always-strong correctness while reducing measured latency or compute cost by at least 30% on both held-out task sets.
- Stop condition: Stop as negative if the calibrated router cannot meet the 0.5 pp correctness gap at any threshold with at least 30% measured latency or cost reduction, or if calibration fails to improve reliability over uncalibrated confidence on held-out requests.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-local-cascade-router-for-gb10-4de9b2b9081a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
