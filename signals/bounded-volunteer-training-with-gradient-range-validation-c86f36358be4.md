# Bounded Volunteer Training with Gradient Range Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-volunteer-training-with-gradient-range-validation-c86f36358be4`
Run ID: `bounded-volunteer-training-with-gradient-range-validation-c86f36358be4-20260613T152059033320+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e9fd98cbd69c

## What looked useful

Gradient range validation is useful as a gross-outlier filter, not as a standalone security mechanism for volunteer training. In the main 25% malicious run it preserved clean accuracy at 0.9832 and rejected all amplified sign flips, but accepted 87.7% of bounded malicious gradients and accuracy fell to 0.8538. In the 40% stress run it accepted 95.7% of bounded malicious gradients and accuracy fell to 0.5266.

## Boundaries and scale limits

Synthetic binary classification only; tiny model; 8-12 seeds; no real volunteer network, privacy layer, Sybil model, real dataset, large model, or adaptive protocol-level attacker beyond bounded sign-flip.

## Claim scope

In a synthetic volunteer-gradient training simulation, historical coordinate range validation preserves clean training and rejects amplified sign-flip outlier gradients, but it does not reliably stop range-conforming malicious gradients.

## Why it stopped

Proxy/local evidence found a clear limitation: bounded malicious gradients can pass coordinate range checks and materially harm training, so standalone gradient range validation is not viable as a paper-ready volunteer-training defense.

## Recommended next action

Stop this run as useful no-paper evidence; a bounded follow-up should test range validation combined with directional robust aggregation against adaptive bounded attackers on a real small dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gradient Range Validation plus Directional Robust Aggregation on Real Small-Model Volunteer Training
- Success threshold: The combined method should stay within 2 percentage points of honest clean accuracy at 25% malicious volunteers while rejecting or neutralizing at least 90% of bounded attack impact relative to unvalidated mean, without rejecting more than 5% of honest updates.
- Stop condition: Stop if the combined method still accepts range-conforming attacks that reduce accuracy by more than 5 percentage points versus clean training at 25% malicious volunteers, or if honest update rejection exceeds 5%.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-volunteer-training-with-gradient-range-validation-c86f36358be4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
