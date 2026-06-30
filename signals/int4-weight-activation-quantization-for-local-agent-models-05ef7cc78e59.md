# INT4 Weight+Activation Quantization for Local Agent Models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `int4-weight-activation-quantization-for-local-agent-models-05ef7cc78e59`
Run ID: `int4-weight-activation-quantization-for-local-agent-models-05ef7cc78e59-20260619T225954237237+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7fe93baac7cb

## What looked useful

Corrected benchmark: FP16 loss 4.1600 / ppl 64.07 / 58,755.7 tok/s; INT4 weight-only loss 4.5769 / ppl 97.21 / 37,189.6 tok/s; INT4 weight+activation loss 8.0907 / ppl 3264.11 / 28,457.3 tok/s. The W4A4 activation path increased loss by +3.9308 and ran at 0.484x FP16 throughput.

## Boundaries and scale limits

This is a small GPT-2 proxy with 15,360 timed tokens, seq_len=128, WikiText-2 raw text, and fake-quant wrappers rather than packed INT4 kernels. It does not validate or rule out calibrated W4A4 methods, instruction-tuned 1B-7B local agent models, long-context serving, or tool-use benchmarks.

## Claim scope

Naive per-output-channel INT4 projection weights plus dynamic per-token INT4 activation fake quantization on pretrained GPT-2, evaluated on a short WikiText-2 test slice on GB10, is not viable: it severely degrades language-model loss and is slower than FP16 in this dequantize-to-FP16 implementation.

## Why it stopped

Proxy early falsification: simple dynamic INT4 activation quantization on GPT-2 caused severe quality loss and no speed benefit in the local fake-quant implementation; this is not a full validation of all W4A4 methods.

## Recommended next action

Stop this naive W4A4 path as an early negative; if continuing locally, run a calibrated outlier-aware activation quantization follow-up before any larger agent-model scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated outlier-aware W4A4 activation quantization on GPT-2-class local models
- Success threshold: On the corrected GPT-2 WikiText slice, calibrated W4A4 should keep loss delta <= 0.75 versus FP16 and improve over naive W4A4 by at least 2.0 loss points, while preserving an estimated packed projection-weight storage reduction.
- Stop condition: Stop if calibrated W4A4 still has loss delta > 1.5 versus FP16 or remains slower than weight-only without a credible packed-kernel path.

## Evidence references

- Artifact root: `<local-path>/projects/int4-weight-activation-quantization-for-local-agent-models-05ef7cc78e59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
