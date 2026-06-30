# Masked Gradient Averaging on Simulated CPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `masked-gradient-averaging-on-simulated-cpu-workers-4f0122779516`
Run ID: `masked-gradient-averaging-on-simulated-cpu-workers-4f0122779516-20260527T124820926570+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5f787d423580

## What looked useful

Masked averaging is not a drop-in unbiased compression method at low mask probabilities: unbiased rescaling raises gradient variance enough to destabilize p=0.125 in this local test. The biased zero-fill variant can act like a conservative learning-rate reduction and preserve final quality on an easy convex problem, suggesting a bounded follow-up with error feedback and tuned schedules.

## Boundaries and scale limits

Synthetic convex regression only; no real network, no GPU training, no non-convex neural model, no optimizer momentum/Adam, no error feedback, and only IID worker shards. Coordinate fraction is a communication proxy, not measured distributed wall-clock bandwidth.

## Claim scope

On synthetic 1024-dimensional linear regression with 8 simulated CPU workers, random coordinate masking reduced transmitted gradient coordinates as intended. Uncorrected zero-fill masking reached dense-like final loss after 350 SGD steps at 12.5%-50% coordinate transmission, while inverse-probability rescaling became unstable at 12.5% transmission with the dense baseline learning rate.

## Why it stopped

Synthetic CPU-worker evidence is informative but not direct enough for a paper; it shows mixed mechanism behavior rather than broad validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up on a small non-convex model with learning-rate tuning and error feedback before considering larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Error-feedback masked averaging on a small non-convex model
- Success threshold: Masked error-feedback variant reaches final validation loss within 2% of dense baseline with at least 4x fewer transmitted gradient bytes and no divergence across 3 seeds.
- Stop condition: Stop if no masked variant meets the 2% validation-loss threshold at 4x byte reduction, or if error-feedback overhead erases the communication/runtime benefit on the local implementation.

## Evidence references

- Artifact root: `<local-path>/projects/masked-gradient-averaging-on-simulated-cpu-workers-4f0122779516`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
