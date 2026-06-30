# 4-bit Proxy Residual Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-proxy-residual-training-67024687d419`
Run ID: `4-bit-proxy-residual-training-67024687d419-20260604T223601041484+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5938b088e934

## What looked useful

Across three synthetic tasks and five seeds, q4_proxy achieved residual R2 of 0.9971 on smooth, 0.9876 on MLP, and 0.7415 on sharp, with 7.00x effective parameter-bit compression. Raw MSE was still 2.254x fp32 on smooth and 1.594x fp32 on MLP, so this is mechanism evidence rather than paper-ready validation.

## Boundaries and scale limits

No transformer, language-model, GPT-2-small-class, long-schedule, optimizer-state, activation-quantization, or real 4-bit-kernel evidence was produced. Results are limited to synthetic residual correction and parameter-bit accounting.

## Claim scope

Synthetic residual-regression tests with tiny residual MLPs show that 4-bit STE proxy residual weights can learn useful residual corrections with about 7x effective residual-parameter bit reduction, while retaining high residual R2 on smooth and MLP residual functions and closely matching fp32 on an approximation-limited sharp task.

## Why it stopped

The result is a bounded synthetic/proxy mechanism signal, not direct transformer or language-model evidence.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded GPT-2-small-class residual-adapter follow-up with no-residual, fp32 residual, q4, q3, and q2 controls before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class 4-bit proxy residual adapter validation
- Success threshold: q4 proxy residual adapters recover at least 90% of the fp32 residual-adapter validation-loss improvement over no-residual baseline, while q2 is materially worse and the final quantized-weight persistence check changes validation loss by less than 1%.
- Stop condition: Stop if q4 fails to beat the no-residual baseline or recovers less than 75% of the fp32 residual-adapter improvement after a calibrated medium run.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-proxy-residual-training-67024687d419`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
