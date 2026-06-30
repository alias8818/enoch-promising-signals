# Ternary draft + FP16 verifier with residual-aware acceptance

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `ternary-draft-fp16-verifier-with-residual-aware-acceptance-0d8362d13c4c`
Run ID: `ternary-draft-fp16-verifier-with-residual-aware-acceptance-0d8362d13c4c-20260630T095534458049+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b208dfad9bd4

## What looked useful

Baseline ternary draft acceptance overlap on the WikiText-2 confirmation was 0.3152. The residual-aware top-256 corrected proposal fell to 0.1245, a -0.1907 absolute / -60.5% relative change. The 12-point distilgpt2 grid also showed negative residual gains at every point.

## Boundaries and scale limits

Evidence is logit-level and one-step only: distilgpt2, output-head ternarization, 16-prompt grid plus 128 WikiText-2 contexts / 11213 positions. No fused ternary kernel, no trained ternary draft model, no dense draft baseline, and no end-to-end autoregressive throughput benchmark were tested.

## Claim scope

For distilgpt2 output-head ternarization, exact one-step speculative acceptance is low, and correcting only the top-M ternary draft logits with FP16 residuals worsens the proposal distribution across the tested thresholds and shortlist sizes.

## Why it stopped

Bounded direct acceptance evidence falsified the simple ternary output-head draft plus top-M residual-aware correction mechanism; this is an early scoped falsification, not a full validation of all ternary draft designs.

## Recommended next action

Stop this formulation as a paper path; if continuing locally, test an acceptance-preserving residual mixture that explicitly accounts for uncorrected tail mass before doing any fused-kernel or scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-preserving residual mixture for ternary draft logits
- Success threshold: On at least 10000 distilgpt2 WikiText-2 positions, residual mixture acceptance overlap exceeds the uncorrected ternary baseline by at least 0.05 absolute without increasing KL(p||q) or reducing top-1 agreement.
- Stop condition: Stop if no grid point beats the uncorrected ternary acceptance baseline by 0.02 absolute, or if the best method requires correcting most of the vocabulary and is therefore equivalent to the FP16 verifier head.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-draft-fp16-verifier-with-residual-aware-acceptance-0d8362d13c4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
