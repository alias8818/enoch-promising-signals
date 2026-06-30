# Sub-2-bit Weight Quantization via Offline Orthogonal Residual Channels

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `sub-2-bit-weight-quantization-via-offline-orthogonal-residual-channels-3fc52b69475e`
Run ID: `sub-2-bit-weight-quantization-via-offline-orthogonal-residual-channels-3fc52b69475e-20260619T102714402956+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/69005c8b0bbe

## What looked useful

At 1.723 effective bits, OORC improved 1-bit MSE by 25.1% but had 1.35x the MSE of a 3-level scalar baseline and 1.99x the MSE of a 4-level scalar baseline, beating each on only 2/24 GPT-2 matrices. At 1.935 effective bits it still beat each baseline on only 2/24 matrices.

## Boundaries and scale limits

No downstream perplexity, activation-aware calibration, quantization-aware training, kernel/runtime measurement, larger model family, or full-layer deployment was tested. Evidence is limited to weight reconstruction on selected GPT-2 matrices plus a synthetic smoke test.

## Claim scope

On a bounded reconstruction probe over 24 GPT-2 pretrained weight matrices, a 1-bit scaled-sign base plus fp16 top-SVD orthogonal residual channels improves over pure 1-bit quantization but is not competitive with simple 3-level or 4-level scalar quantization at matched sub-2-bit effective budgets.

## Why it stopped

Proxy/direct reconstruction early falsification: the tested OORC mechanism is useful relative to 1-bit but loses to simpler scalar quantization on most GPT-2 matrices at both 1.75-bit and near-2-bit budgets.

## Recommended next action

Stop this formulation as a paper direction unless a future direct perplexity study can show OORC beats strong scalar quantization baselines with honest storage and runtime accounting.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-weight-quantization-via-offline-orthogonal-residual-channels-3fc52b69475e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
