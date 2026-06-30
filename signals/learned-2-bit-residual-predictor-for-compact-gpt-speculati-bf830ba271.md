# Learned 2-bit residual predictor for compact GPT speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-2-bit-residual-predictor-for-compact-gpt-speculati-bf830ba271`
Run ID: `learned-2-bit-residual-predictor-for-compact-gpt-speculati-bf830ba271-20260605T075511909497+0000`

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

- Parent run decision: Transformer Speculative Acceptance for 2-Bit Draft Residual Correction: enoch://control-plane/projects/transformer-speculative-acceptance-for-2-bit-draft-residua-5ffdd705d5/runs/transformer-speculative-acceptance-for-2-bit-draft-residua-5ffdd705d5-20260605T040034388380+0000
- Parent run decision: Tiny 2-Bit Draft with Residual Logit Correction: enoch://control-plane/projects/tiny-2-bit-draft-with-residual-logit-correction-6f3f48822d24/runs/tiny-2-bit-draft-with-residual-logit-correction-6f3f48822d24-20260604T232815214164+0000

## What looked useful

The learned 2-bit residual table raised heldout target-context acceptance from 0.6031 to 0.6796 (+12.7%) and beat shuffled/1-bit controls, but all residual variants underperformed the draft baseline in free-running speculative simulation; the best 2-bit gain reached 2.3521 tokens per target call versus 2.3857 for the draft.

## Boundaries and scale limits

Tested character n-gram target/draft models only, not GPT-2-small-class neural models; one corpus and one deterministic data split with matched stochastic simulation seeds; CPU-only local validation.

## Claim scope

In a compact character autoregressive speculative-decoding proxy on real Tiny Shakespeare text, a learned 2-bit residual predictor improves teacher-forced target-context acceptance versus a 3-gram draft baseline, but it does not improve free-running speculative throughput.

## Why it stopped

Medium local evidence is mixed: mechanism support on teacher-forced acceptance is outweighed by failure to beat the real draft baseline in free-running speculative decoding.

## Recommended next action

Stop paper escalation for this run; a bounded follow-up should test on-policy residual calibration for generated contexts before any neural GPT scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: On-policy calibrated 2-bit residuals for compact speculative decoding
- Success threshold: At least +3% tokens per target call versus the draft baseline in free-running simulation while maintaining positive teacher-forced acceptance lift and beating the shuffled control.
- Stop condition: Stop if all calibrated 2-bit variants remain at or below the draft baseline in tokens per target call, even if teacher-forced acceptance improves.

## Evidence references

- Artifact root: `<local-path>/projects/learned-2-bit-residual-predictor-for-compact-gpt-speculati-bf830ba271`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
