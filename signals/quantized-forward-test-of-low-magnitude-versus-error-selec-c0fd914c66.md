# Quantized Forward Test of Low-Magnitude Versus Error-Selected Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `quantized-forward-test-of-low-magnitude-versus-error-selec-c0fd914c66`
Run ID: `quantized-forward-test-of-low-magnitude-versus-error-selec-c0fd914c66-20260520T095206580009+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real Transformer Tensor Test for Error-Selected 2-bit Residual Channels: enoch://control-plane/projects/real-transformer-tensor-test-for-error-selected-2-bit-resi-6943fd3723/runs/real-transformer-tensor-test-for-error-selected-2-bit-resi-6943fd3723-20260520T094106629267+0000
- Parent run decision: Cheap Residual Coding for Error-Selected 2-bit Channels: enoch://control-plane/projects/cheap-residual-coding-for-error-selected-2-bit-channels-8c70450907/runs/cheap-residual-coding-for-error-selected-2-bit-channels-8c70450907-20260520T093559429310+0000

## What looked useful

Error-selected residual channel exemptions are a useful heuristic compared with low-magnitude exemptions in the practical int6 regime, but high-magnitude selection explains much of the effect and is often stronger. The idea should not be written up as a paper-positive result without resolving the high-magnitude control.

## Boundaries and scale limits

Single 124M-parameter GPT-2 model, WikiText-2 validation/test only, residual outputs after transformer blocks only, no production quantization stack, no larger model family replication.

## Claim scope

On GPT-2 small with WikiText-2 forward-only residual-stream activation quantization, calibration-time error-selected channel exemptions outperform low-magnitude exemptions in int6 across tested budgets and in int4 at 12.5% and 25% exemption budgets, but they do not dominate tiny-budget int4 and are usually weaker than a high-magnitude control.

## Why it stopped

Bounded GPT-2-small evidence is mixed: error-selected beats low-magnitude in most relevant settings, but high-magnitude is a stronger control and prevents a clean publication-grade mechanism claim.

## Recommended next action

Stop this run as no-paper useful signal; run one depth-4 bounded deepen study comparing high-magnitude, error-selected, and combined policies on a second model family and dataset if the controller permits one final follow-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-Model High-Magnitude Control for Error-Selected Residual Channel Exemptions
- Success threshold: At int6 or another non-catastrophic activation quantization setting, error-selected or combined selection beats high-magnitude by at least 0.01 NLL at two matched budgets and on both evaluation corpora, while also beating random-control mean by at least two random-control standard deviations.
- Stop condition: Stop as unsupported if high-magnitude matches or beats error-selected/combined on the second model family, or if the effect disappears outside WikiText-2.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-forward-test-of-low-magnitude-versus-error-selec-c0fd914c66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
