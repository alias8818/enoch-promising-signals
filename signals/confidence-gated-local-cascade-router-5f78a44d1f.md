# Confidence-Gated Local Cascade Router

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-local-cascade-router-5f78a44d1f`
Run ID: `confidence-gated-local-cascade-router-5f78a44d1f-20260518T162436553915+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba2a2599325c

## What looked useful

Accepted high-confidence small-model examples were accurate and two of three seeds had nearby oracle thresholds meeting the target, but the preselected validation gate failed the held-out joint threshold in 0/3 seeds.

## Boundaries and scale limits

Single benchmark, shallow local classifiers, three random validation splits, no generative LLM routing, no serving-system latency measurement, no cross-domain robustness.

## Claim scope

On 20 Newsgroups text classification, a local confidence-gated cascade can recover much of the strong classifier's accuracy while avoiding some strong calls, but the validation-selected threshold did not reliably meet the joint target of <=1 percentage point accuracy loss and >=40% strong-call reduction.

## Why it stopped

No-paper closure: the Tier 1 controlled direct test found a useful mechanism signal but failed the stated held-out success threshold for the validation-selected router.

## Recommended next action

Run one bounded deepen test with calibrated or conformal confidence thresholds on 20 Newsgroups plus a second text dataset; stop unless the pre-registered router meets the joint threshold across most seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated confidence gates for stable local cascade routing
- Success threshold: Selected calibrated gate achieves <=1 percentage point accuracy loss versus the strong model and >=40% strong-call reduction on held-out test in at least 2 of 3 seeds on each dataset.
- Stop condition: Stop negative if the pre-registered calibrated gate misses either the accuracy-loss or strong-call-reduction target on more than one seed for any dataset.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-local-cascade-router-5f78a44d1f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
