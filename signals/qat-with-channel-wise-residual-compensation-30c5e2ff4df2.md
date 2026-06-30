# QAT with Channel-Wise Residual Compensation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `qat-with-channel-wise-residual-compensation-30c5e2ff4df2`
Run ID: `qat-with-channel-wise-residual-compensation-30c5e2ff4df2-20260622T001912015002+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/78415dbfa451

## What looked useful

CWRC appears useful for calibration/output-matching error reduction, especially PTQ, but this run does not support CWRC as a standalone QAT accuracy improvement.

## Boundaries and scale limits

Synthetic teacher-generated classification only; small MLP only; static compensation only; no activation quantization, transformer/CNN model, real dataset, hardware kernel, or full framework QAT stack.

## Claim scope

In a 20-seed NumPy synthetic two-layer MLP int4 probe, static channel-wise residual compensation reduces logit MSE versus FP for PTQ and sometimes QAT, but does not improve QAT task accuracy over matched int4 QAT.

## Why it stopped

Proxy/local evidence is mixed: the mechanism reduced logit error but failed to improve QAT accuracy, so this is an early bounded falsification of the direct QAT-improvement claim rather than full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next test is a bounded real-dataset QAT comparison on a small standard model with identical training schedules and multiple seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data small-model QAT+CWRC confirmation
- Success threshold: QAT+CWRC improves the primary task metric by at least 0.5 percentage points or a predeclared equivalent while reducing logit MSE versus matched int4 QAT in at least 3/3 seeds.
- Stop condition: Stop if QAT+CWRC fails to improve the primary task metric in at least 2 of 3 seeds or if logit-MSE reductions do not transfer beyond the synthetic MLP setting.

## Evidence references

- Artifact root: `<local-path>/projects/qat-with-channel-wise-residual-compensation-30c5e2ff4df2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
