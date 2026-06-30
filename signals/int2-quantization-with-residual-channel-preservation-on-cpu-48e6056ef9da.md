# INT2 Quantization with Residual Channel Preservation on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-quantization-with-residual-channel-preservation-on-cpu-48e6056ef9da`
Run ID: `int2-quantization-with-residual-channel-preservation-on-cpu-48e6056ef9da-20260605T160603457543+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0bd4b15288b5

## What looked useful

On 1024x1024 synthetic layers with 5% high-energy rows, top-energy residual-channel preservation reduced NMSE from 0.252742 for plain INT2 to 0.058278, versus 0.240436 for random preservation at the same 0.1102x FP32 storage. In no-outlier controls, the improvement was small. The naive CPU path was 1.7x to 2.5x slower than FP32.

## Boundaries and scale limits

No real model perplexity, downstream task, calibration-data selection, or optimized INT2 CPU kernel was tested. The CPU path dequantizes packed INT2 weights to FP32 for matmul and was slower than FP32 NumPy matmul.

## Claim scope

Synthetic CPU linear-layer proxy: preserving the highest-energy 5% of output rows in FP32 can substantially reduce output reconstruction error for packed INT2 weights when the layer contains high-energy outlier rows, at about 11% of FP32 weight storage.

## Why it stopped

Synthetic proxy supports the accuracy/storage mechanism only under outlier-channel structure, while the tested CPU dequantize-on-use implementation is slower than FP32; this is not full validation or a CPU speed result.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is applying the same row-preservation policy to a small pretrained transformer or GPT-2-small-class model with calibration activations and perplexity measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel INT2 on a small real transformer
- Success threshold: At the same storage budget, activation-aware residual-channel INT2 closes at least 50% of the perplexity gap between plain INT2 and FP32/FP16 and beats random preservation across at least three calibration/evaluation seeds.
- Stop condition: Stop if residual-channel preservation fails to beat random preservation by at least 10% relative perplexity-gap closure, or if dequantize-on-use CPU latency remains slower than FP32 with no credible optimized-kernel path.

## Evidence references

- Artifact root: `<local-path>/projects/int2-quantization-with-residual-channel-preservation-on-cpu-48e6056ef9da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
