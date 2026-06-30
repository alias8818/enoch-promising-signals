# Activation-Weighted Residual Channel Selection for INT1 Backbone

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-weighted-residual-channel-selection-for-int1-backbone-8ac4f57c838a`
Run ID: `activation-weighted-residual-channel-selection-for-int1-backbone-8ac4f57c838a-20260531T224041252132+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fa735c67db63

## What looked useful

Activation-weighted channel scoring produced lower mean logit MSE than weight-error selection at all nonzero budgets tested: 3.0515 vs 3.0739 at 6.25%, 2.6472 vs 2.6999 at 12.5%, 2.0382 vs 2.1156 at 25%, and 1.0361 vs 1.0986 at 50%. It also beat random selection by larger margins and captured more layer-level residual-output MSE. Downstream accuracy differences between informed selectors were small, so the mechanism is useful for fidelity but not yet a robust accuracy result.

## Boundaries and scale limits

Evidence is limited to a small CPU-only synthetic MLP benchmark. It does not validate transformer blocks, language-model perplexity, real INT1 kernels, latency, memory bandwidth, residual storage format, or large-scale training/inference behavior.

## Claim scope

On a reproducible synthetic MLP classifier, activation-weighted residual output-channel selection for an INT1/sign-weight backbone consistently reduced logit MSE, KL divergence, and layer calibration residual-output MSE versus weight-error and random selectors at equal residual-channel budgets.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports the selection mechanism for fidelity but is not direct/full validation of an INT1 transformer backbone.

## Recommended next action

Run a bounded transformer-layer or GPT-2-small-class follow-up using real calibration text, perplexity or task accuracy, and fixed residual metadata budgets before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer calibration test for activation-weighted INT1 residual channel selection
- Success threshold: Activation-weighted selection should reduce perplexity degradation or task accuracy loss by at least 10% relative to weight-error selection at two or more budgets while also improving logit MSE/KL across seeds.
- Stop condition: Stop if activation-weighted selection does not beat weight-error on direct transformer validation metrics at two or more budgets, or if gains appear only in logit MSE without any perplexity or accuracy improvement.

## Evidence references

- Artifact root: `<local-path>/projects/activation-weighted-residual-channel-selection-for-int1-backbone-8ac4f57c838a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
