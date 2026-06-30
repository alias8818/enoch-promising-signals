# Neural tiny-LM quality-threshold sweep on real text shards

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `neural-tiny-lm-quality-threshold-sweep-on-real-text-shards-1a628902f9`
Run ID: `neural-tiny-lm-quality-threshold-sweep-on-real-text-shards-1a628902f9-20260628T084235950949+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Quality classifier threshold sweep on tiny pretraining: enoch://control-plane/projects/quality-classifier-threshold-sweep-on-tiny-pretraining-193d30ec8cd5/runs/quality-classifier-threshold-sweep-on-tiny-pretraining-193d30ec8cd5-20260628T074927637151+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bcfe059b0544

## What looked useful

Across three seeds, the unfiltered baseline was best by mean validation BPC (4.2955). All corrected filtering thresholds worsened mean validation BPC by 0.53% to 1.82%, so the predeclared >=3% improvement rule was not met.

## Boundaries and scale limits

Small CPU-only character LM, short 800-step training runs, clean book-text corpus, heuristic quality scoring, and no GPT-2-small-class or web-noise-scale validation.

## Claim scope

Tier 1 direct test: a NumPy tiny neural character LM trained on three public-domain Gutenberg books did not benefit from filtering real text shards by this heuristic quality score over thresholds 0.95, 0.97, 0.98, 0.99, and 0.995.

## Why it stopped

Corrected Tier 1 direct test falsified the local threshold success rule: filtering real text shards did not improve held-out BPC and consistently underperformed the unfiltered baseline.

## Recommended next action

Stop this follow-up as a no-paper bounded negative; only revisit with a noisier real corpus, a stronger quality estimator, and a parameter-matched neural LM control.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/neural-tiny-lm-quality-threshold-sweep-on-real-text-shards-1a628902f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
