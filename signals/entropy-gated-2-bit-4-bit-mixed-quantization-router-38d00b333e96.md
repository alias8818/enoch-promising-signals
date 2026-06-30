# Entropy-gated 2-bit/4-bit mixed quantization router

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `entropy-gated-2-bit-4-bit-mixed-quantization-router-38d00b333e96`
Run ID: `entropy-gated-2-bit-4-bit-mixed-quantization-router-38d00b333e96-20260523T061134556136+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c8b93e0fc7

## What looked useful

Across four bounded runs, entropy/gain correlation was near zero on average (-0.0138), entropy-gated routing recovered less of the 2-bit to 4-bit loss gap than random expectation on average (32.6% vs 35.0%), and the entropy gate beat random in only 2 of 4 seeds. The oracle matched-budget policy was much better, so quantization sensitivity exists but raw context entropy did not capture it.

## Boundaries and scale limits

Synthetic data, tiny transformer, post-training linear-weight quantization, whole-model per-example routing, no production quantized kernels, no pretrained LLM or real corpus validation.

## Claim scope

In a bounded synthetic transformer proxy with per-example whole-model 2-bit/4-bit routing and simple per-row affine linear-weight quantization, raw context entropy did not outperform a matched random 4-bit budget for selecting examples that benefit from 4-bit inference.

## Why it stopped

Proxy early falsification: raw context entropy failed to beat a matched random 4-bit allocation on average in the tested synthetic transformer setting; this is not full LLM validation.

## Recommended next action

Stop this entropy-only router line as no-paper proxy evidence; if continuing locally, test a learned or calibration-derived quantization-sensitivity router against entropy and random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibration-derived sensitivity router for mixed 2-bit/4-bit inference
- Success threshold: At 35% 4-bit budget, the learned or calibrated router recovers at least 45% of the all-2-bit to all-4-bit loss gap and beats random matched expectation by at least 0.005 CE in at least 3 of 4 seeds.
- Stop condition: Stop if the router fails to beat random in at least 3 of 4 seeds or if oracle headroom is below 0.005 CE, indicating the proxy has insufficient selectable quantization sensitivity.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-2-bit-4-bit-mixed-quantization-router-38d00b333e96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
