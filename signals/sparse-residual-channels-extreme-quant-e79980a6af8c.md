# Sparse Residual Channels Extreme Quant

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-residual-channels-extreme-quant-e79980a6af8c`
Run ID: `sparse-residual-channels-extreme-quant-e79980a6af8c-20260529T193351051267+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03f6686f4884

## What looked useful

Sparse residual channels selected by weight-error consistently reduced dense-logit MSE, but did not reliably improve task accuracy. On the clean clustered benchmark, top-error selection beat random on logit MSE in 6/6 nonzero-residual comparisons but beat random on accuracy in 0/6 and often underperformed the no-residual baseline.

## Boundaries and scale limits

No transformer, language-model dataset, quantization-aware training, activation-aware selection, inference kernel, or real compression implementation was tested. The teacher-student run had weak dense-model generalization; the clustered run was synthetic and easy for the dense model.

## Claim scope

Bounded NumPy proxy: small MLP post-training 1-bit/2-bit per-output-channel weight quantization on synthetic teacher-student and clustered classification tasks, comparing sparse residual output-channel restoration selected by weight quantization error against random residual-channel controls.

## Why it stopped

Proxy evidence falsified the naive selection rule rather than validating the broader idea: lower approximation error from top-error residual channels did not reliably translate to downstream accuracy.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should replace raw weight-error channel selection with activation-aware or validation-loss-aware residual-channel selection and compare against random controls at matched effective bits per weight.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware sparse residual channel selection for extreme quantization
- Success threshold: Activation-aware selection improves task metric over both no-residual and random residual controls in at least 80% of seed/config comparisons, with no worse than matched effective BPW.
- Stop condition: Stop if activation-aware selection fails to beat random residual controls on task metric in a majority of comparisons or if gains only appear in logit MSE without downstream metric improvement.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-residual-channels-extreme-quant-e79980a6af8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
