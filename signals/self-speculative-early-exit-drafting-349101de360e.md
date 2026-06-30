# Self-speculative early-exit drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-early-exit-drafting-349101de360e`
Run ID: `self-speculative-early-exit-drafting-349101de360e-20260604T060221029809+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c9e6c312f6e1

## What looked useful

Cheap early exits had very low agreement and acceptance, while accurate late exits were too expensive. The best non-control setting was layer 1 draft length 1 with only 9.0% acceptance and a 1.006x idealized speed upper bound, which is not practically meaningful.

## Boundaries and scale limits

Only 32 Wikitext-2 validation texts, 2,838 corpus token positions, and 12 simulated prompts were tested; speed is an idealized compute upper bound rather than production wall-clock speculative decoding.

## Claim scope

GPT-2 small greedy decoding with no-training intermediate exits projected through final layer norm and the tied language-model head.

## Why it stopped

Proxy/early falsification of the simple tied-head early-exit drafting variant: direct greedy acceptance was too low for cheap exits and speed was only estimated, not production-measured.

## Recommended next action

Stop this no-training variant; if continuing locally, train or calibrate a lightweight early-exit head and require a >1.08x idealized speed upper bound before any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated early-exit heads for self-speculative GPT-2 drafting
- Success threshold: At least one layer <=4 and draft length <=2 reaches >1.08x idealized compute speed upper bound with >=20% acceptance on disjoint prompts.
- Stop condition: Stop if trained/calibrated heads remain below 1.03x idealized speed upper bound or require layer >=6 for useful acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-early-exit-drafting-349101de360e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
