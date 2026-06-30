# Sub-2-bit weights with orthogonal residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-2-bit-weights-with-orthogonal-residual-channels-9e5c9215454b`
Run ID: `sub-2-bit-weights-with-orthogonal-residual-channels-9e5c9215454b-20260621T000642205446+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b672c7910d

## What looked useful

Orthogonal SVD residual channels are better than random orthogonal residuals and recover ternary error, but practical int4 residual factors at 1.968 bits/weight averaged 0.211 relative output MSE versus 0.178 for the 2-bit baseline. Heavy-tail matrices showed a full-precision residual signal that disappeared after int4 factor quantization.

## Boundaries and scale limits

No real transformer checkpoints, GPT-2-small-class training, perplexity evaluation, deployment kernel, or large-model validation was run. Full-precision residual factor results are mechanism probes, not valid sub-2-bit storage claims.

## Claim scope

Bounded proxy on synthetic 128x128 to 512x512 weight matrices: ternary base weights plus low-rank orthogonal residual channels recover error, but quantized int4 residual factors below 2 effective bits per weight did not beat a rowwise 2-bit baseline.

## Why it stopped

Quantized orthogonal residual channels below 2 bits/weight did not beat a simple 2-bit baseline in any tested synthetic distribution; this is proxy evidence, not full-scale model validation.

## Recommended next action

Stop this run as an early proxy falsification; only pursue a bounded follow-up if testing an outlier-aware residual factor quantizer that can preserve the heavy-tail full-precision gain below 2 bits/weight.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Outlier-aware quantized residual factors for heavy-tailed weights
- Success threshold: At less than 2 effective bits per weight, quantized residual channels reduce relative output MSE by at least 10% versus rowwise 2-bit on heavy-tailed or real model-layer weights without worsening Gaussian/structured controls by more than 5%.
- Stop condition: Stop if quantized residual factors still fail to beat the 2-bit baseline on heavy-tail or real-layer matrices, or if the required coding overhead reaches or exceeds 2 bits per weight.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-weights-with-orthogonal-residual-channels-9e5c9215454b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
