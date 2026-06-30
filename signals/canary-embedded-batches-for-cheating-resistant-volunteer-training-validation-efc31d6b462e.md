# Canary-Embedded Batches for Cheating-Resistant Volunteer Training Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `canary-embedded-batches-for-cheating-resistant-volunteer-training-validation-efc31d6b462e`
Run ID: `canary-embedded-batches-for-cheating-resistant-volunteer-training-validation-efc31d6b462e-20260621T004722092264+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/871b7fc1a29f

## What looked useful

Canary-embedded batches appear useful only when canaries are unique and balanced; reused/static canary pools are weak against leak-aware colluders, detecting only 5.42% of colluding canary-leak workers in the simulation.

## Boundaries and scale limits

Synthetic only; no real volunteers, no adaptive adversaries, no production training pipeline, no downstream model-quality measurement, and no external/private human evidence.

## Claim scope

In a deterministic synthetic volunteer-validation simulation with 800 trials, 500 workers per trial, and a fixed worker-mix threat model, unique class-balanced hidden canaries improved retained label accuracy from 78.59% without canaries to 84.29% while detecting 69.14% of dishonest workers at 0.71% honest false reject rate.

## Why it stopped

The result is a bounded synthetic/proxy validation that supports the mechanism but is not direct full validation of real volunteer cheating resistance.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement a blinded replay or small human-style annotation harness with adaptive feedback and the same no-canary, reused-canary, and unique-balanced-canary controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded Replay Validation of Unique Balanced Canary Batches
- Success threshold: Unique balanced canaries beat no-canary retained-label accuracy by at least 4 percentage points, detect at least 60% of dishonest/adaptive workers, and keep honest false rejects below 2%.
- Stop condition: Stop if unique balanced canaries fail to beat no-canary retained-label accuracy by 2 percentage points or if honest false rejects exceed 5% under the pre-registered rule.

## Evidence references

- Artifact root: `<local-path>/projects/canary-embedded-batches-for-cheating-resistant-volunteer-training-validation-efc31d6b462e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
