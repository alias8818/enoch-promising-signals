# Standard-corpus per-head KV quantization validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `standard-corpus-per-head-kv-quantization-validation-f03eefa015`
Run ID: `standard-corpus-per-head-kv-quantization-validation-f03eefa015-20260523T071914512907+0000`

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

- Parent run decision: Per-Head KV Quantization: enoch://control-plane/projects/per-head-kv-quantization-bfca23eac609/runs/per-head-kv-quantization-bfca23eac609-20260523T051744474729+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb1f540afb65

## What looked useful

Across three random WikiText-2 validation seeds, per-head int8 KV cache had mean delta NLL -0.000609 nats/token versus FP, stayed within the 0.01 threshold on every run, and had lower mean KL drift than per-tensor int8 on every run (0.000572 vs 0.000985 mean KL).

## Boundaries and scale limits

One small pretrained GPT-2-family model, one standard corpus validation split, 6,144 scored tokens, 128-token windows, 8-bit fake-quantize/dequantize cache tensors only; no packed int8 kernel, long-context test, larger model family, broad corpus sweep, or latency/memory-bandwidth validation.

## Claim scope

Small direct validation on distilgpt2 autoregressive decoding over WikiText-2 raw validation segments: symmetric int8 per-head KV cache scaling preserved next-token likelihood within 0.01 nats/token of FP cache and reduced KL/logit drift relative to one scale per K/V tensor.

## Why it stopped

Tier 1 controlled direct test completed and produced a useful mechanism signal, but evidence remains too narrow for publication readiness.

## Recommended next action

Run a bounded deepen validation on at least one GPT-2-small or Pythia-class model with longer contexts, 4-bit and 8-bit per-head versus per-tensor controls, and the same NLL/KL thresholds before considering any paper or large-scale serving work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model and bit-width per-head KV quantization validation
- Success threshold: For 8-bit per-head KV, absolute delta NLL <= 0.01 nats/token and lower mean KL than per-tensor in every tested model/context; for 4-bit, either meet the same threshold or clearly characterize the failure boundary.
- Stop condition: Stop if 8-bit per-head exceeds 0.01 nats/token delta NLL or fails to beat per-tensor KL on any bounded direct model/context test.

## Evidence references

- Artifact root: `<local-path>/projects/standard-corpus-per-head-kv-quantization-validation-f03eefa015`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
