# Volunteer Gradient Puzzle Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-gradient-puzzle-validation-4ac7379bc3fb`
Run ID: `volunteer-gradient-puzzle-validation-4ac7379bc3fb-20260604T220540585096+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5938b088e934

## What looked useful

Hidden probe-gradient cosine and hidden loss-delta checks rejected directionally destructive synthetic gradients while preserving honest gradients; in a 50% honest destructive stress setting they changed mean loss reduction from -0.214969 with accept_all to 0.135339. In a mixed setting, accept_all still had the best downstream loss because some rejected submissions were benign or helpful, so rejection rate alone is not a sufficient success metric.

## Boundaries and scale limits

No real distributed volunteers, no neural-network training, no adaptive probe-inference adversary, and no full validation-overhead/cost model.

## Claim scope

Synthetic least-squares puzzle proxy with hidden probe validation of untrusted volunteer gradients across 20 seeds and two attack profiles.

## Why it stopped

Bounded proxy produced mixed evidence: mechanism supported under destructive synthetic attacks, but not a full volunteer-gradient validation and not universally better than accept_all under the mixed synthetic attack distribution.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded neural-network deepen test with adaptive attackers and validation-overhead accounting before considering publication.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Volunteer Gradient Validation With Adaptive Attackers
- Success threshold: Probe validation must improve final validation loss by at least 10% versus accept_all under destructive/adaptive clients, keep honest rejection below 5%, and keep added coordinator wall-clock overhead below 25%.
- Stop condition: Stop if hidden validation fails to beat accept_all on downstream validation loss in two neural tasks or if overhead exceeds 50% at small scale.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-gradient-puzzle-validation-4ac7379bc3fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
