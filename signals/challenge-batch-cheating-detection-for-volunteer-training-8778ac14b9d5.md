# Challenge-Batch Cheating Detection for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `challenge-batch-cheating-detection-for-volunteer-training-8778ac14b9d5`
Run ID: `challenge-batch-cheating-detection-for-volunteer-training-8778ac14b9d5-20260529T130113393905+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/277f7d0bf68a

## What looked useful

Static known-answer challenge batches detect ordinary low-effort cheating in the synthetic model, but challenge-error AUC drops from 0.921 to 0.544 when static answers leak. Rotating private challenge items restore the no-leak synthetic performance, with challenge-error AUC 0.921 and combined-detector AUC 0.977.

## Boundaries and scale limits

No real volunteer traces, no real task ambiguity, no human-subject study, no production challenge-bank leakage telemetry, and no operational review-cost measurement. Results support mechanism design only, not deployment-grade performance.

## Claim scope

Synthetic volunteer-training simulation with 20,000 volunteers per scenario, 10 replicated seeds, 60 items per volunteer, 12 challenge items, and modeled honest, random-clicker, leaked-key, and speed-runner behaviors.

## Why it stopped

Evidence is synthetic/proxy-only and not sufficient for a publication-grade claim about real volunteer training systems.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete step is a bounded controlled volunteer or trace-replay study comparing fixed versus rotating private challenge banks with pre-registered thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay Validation of Rotating Private Challenge Banks
- Success threshold: Rotating private challenges improve leaked-answer cheater detection by at least 0.20 AUC or at least 2x TPR at <=5% FPR versus static challenges, without increasing honest-volunteer false positives above the pre-registered budget.
- Stop condition: Stop if trace replay or controlled study shows less than 0.05 AUC improvement and less than 25% relative TPR improvement at <=5% FPR, or if required trace fields are unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/challenge-batch-cheating-detection-for-volunteer-training-8778ac14b9d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
