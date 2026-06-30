# Confidence-Gated Token Acceptance Without Draft Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `confidence-gated-token-acceptance-without-draft-model-a825e16e3737`
Run ID: `confidence-gated-token-acceptance-without-draft-model-a825e16e3737-20260523T082040340414+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c52acf841528

## What looked useful

High-confidence intermediate logits were usually wrong relative to the final model. At threshold 0.995, distilgpt2 accepted 9.43% of positions at 10.00% final agreement, and gpt2 accepted 14.13% at 11.54% final agreement. Tightening confidence reduced coverage without recovering precision.

## Boundaries and scale limits

Small natural-language prompt suite, teacher-forced next-token positions, GPT-2-family models only, projected layer-skip speedup only; no production early-exit kernel, no autoregressive compounding test, and no larger modern decoder validation.

## Claim scope

For distilgpt2 and gpt2 on 898 total short-passage next-token positions, raw max-softmax confidence from intermediate target-model layers is not a viable no-draft token acceptance gate: no tested threshold reached 99% final-top-1 agreement among early accepted tokens.

## Why it stopped

Proxy/early falsification: direct intermediate-logit confidence gates failed on GPT-2-class models, but full production serving and larger-model evidence were not run.

## Recommended next action

Stop this raw-confidence variant as an early/proxy falsification; a bounded follow-up should test a calibrated learned no-draft acceptance classifier rather than max-softmax confidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated No-Draft Early-Exit Acceptance Classifier
- Success threshold: On held-out positions, accepted-token final-top-1 agreement >= 99%, early accept rate >= 10%, and projected layer speedup >= 1.10x.
- Stop condition: Stop if held-out accepted-token final agreement is below 99% at every threshold with early accept rate >= 10%, or if the only passing thresholds give projected speedup below 1.05x.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-token-acceptance-without-draft-model-a825e16e3737`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
