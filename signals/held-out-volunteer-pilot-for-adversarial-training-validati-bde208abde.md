# Held-out volunteer pilot for adversarial training validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `held-out-volunteer-pilot-for-adversarial-training-validati-bde208abde`
Run ID: `held-out-volunteer-pilot-for-adversarial-training-validati-bde208abde-20260613T230752444884+0000`

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

- Parent run decision: Adversarial Cheating Simulation Harness for Volunteer Training Validation: enoch://control-plane/projects/adversarial-cheating-simulation-harness-for-volunteer-training-validation-0f4c1ff86e5b/runs/adversarial-cheating-simulation-harness-for-volunteer-training-validation-0f4c1ff86e5b-20260613T225729395036+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9ba846459ffd

## What looked useful

Across linear and MLP char-ngram classifiers, adversarial training produced 0/5 threshold successes per model family. Mean held-out accuracy gain was negative for both linear (-2.83 pp) and MLP (-4.08 pp), with MLP also showing an average clean accuracy drop of 8.33 pp.

## Boundaries and scale limits

Surrogate deterministic volunteer styles, generated harmful-vs-benign prompt templates, five seeds per model family, two small char-ngram model families; no recruited human volunteers, no full LLM/RLHF stack, and no real traffic data.

## Claim scope

In a controlled surrogate-volunteer safety-classification pilot, adversarial training on six training attack-style families did not improve held-out attack-style robustness by the required 10 percentage points while preserving clean accuracy.

## Why it stopped

Controlled surrogate-volunteer Tier 1 test failed the operational threshold in 0/10 model-seed combinations across two model families; this is an early bounded falsification, not a full human-volunteer validation.

## Recommended next action

Stop this run as a no-paper useful negative signal; a future human-volunteer pilot should preregister held-out volunteer groups and require both held-out robustness gains and clean-behavior preservation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-held-out volunteer adversarial-training pilot with preregistered clean tradeoff
- Success threshold: Held-out human-volunteer harmful false-negative rate improves by at least 10 percentage points versus clean-only baseline, benign false-positive rate worsens by no more than 3 percentage points, and the effect is positive in at least 2/3 seeds.
- Stop condition: Stop if the first controlled human-volunteer split shows less than 5 percentage points held-out robustness gain or more than 5 percentage points clean/benign degradation, because that would indicate the surrogate negative transfers to the human pilot.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-volunteer-pilot-for-adversarial-training-validati-bde208abde`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
