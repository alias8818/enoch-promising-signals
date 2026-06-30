# Commit-Reveal Gradient Integrity for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-integrity-for-volunteer-training-295af6d2bdfd`
Run ID: `commit-reveal-gradient-integrity-for-volunteer-training-295af6d2bdfd-20260523T180034543402+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6bdd29b01892

## What looked useful

Commit-reveal restored equivocation-attack accuracy from 0.1008 without commit-reveal to 0.9562 by rejecting all changed reveals, but accepted all committed poisoned gradients; committed ascent poisoning dropped accuracy from the 0.9566 honest baseline to 0.1008 with zero hash rejections.

## Boundaries and scale limits

Tested only on synthetic binary classification with logistic regression, 25 clients, 60 rounds, 100 seeds, and 28% malicious-client cohort. It does not validate large neural-network training, real volunteer heterogeneity, secure aggregation, identity controls, or adaptive production attackers.

## Claim scope

In a synthetic federated logistic-regression volunteer-training simulation, SHA-256 commit-reveal prevents post-commit gradient byte equivocation but does not verify that accepted gradients were honestly computed.

## Why it stopped

Proxy early falsification of the broad commit-reveal gradient-integrity hypothesis: commit-reveal binds gradient bytes but accepted harmful gradients when attackers committed to them honestly from the protocol's perspective.

## Recommended next action

Stop this run as a no-paper useful signal; any next bounded test should evaluate commit-reveal plus semantic verification such as spot-audited replay or redundant assignment against committed poisoned gradients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Spot-Audited Commit-Reveal Against Committed Gradient Poisoning
- Success threshold: Relative to commit-reveal only, reduce accepted committed-ascent malicious gradients by at least 80% and keep final accuracy within 2 percentage points of the honest baseline with less than 5% false rejection of honest gradients.
- Stop condition: Stop if the verifier cannot distinguish committed poisoned gradients from honest gradients in the synthetic setup, if false rejection exceeds 10%, or if verifier cost exceeds full redundant recomputation for the tested configuration.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-integrity-for-volunteer-training-295af6d2bdfd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
